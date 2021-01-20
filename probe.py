#!/usr/bin/env python3
"""Plugin that solemnly swears it is up to no good.

Failcode -1 and 16399 are special:

 - -1 indicates that we were unable to find a route to the destination. This
    usually indicates that this is a leaf node that is currently offline.

 - 16399 is the code for unknown payment details and indicates a successful
   probe. The destination received the incoming payment but could not find a
   matching `payment_key`, which is expected since we generated the
   `payment_hash` at random :-)

"""
from datetime import datetime
from pyln.client import Plugin, RpcError
import random
import string

plugin = Plugin()


@plugin.method("probe")
def bin_search(plugin, node_id, capacity, epsilon, **kwargs):
    def loop(lower, upper, i):
        i += 1
        middle = (lower + upper) // 2
        error_code = failcode(node_id, middle)

        if (upper - lower) < epsilon:
            return middle, i

        elif error_code == 16399:
            return loop(middle, upper, i)

        elif error_code == 4103:
            return loop(lower, middle, i)

        else:
            raise Exception("UnknownErrorCode")

    return loop(0, capacity, 0)


def failcode(node_id, amount, **kwargs):
    probe = {
        'destination': node_id,
        'started_at': str(datetime.now()),
        'probes': [],
        'payment_hash': ''.join(random.choice(string.hexdigits) for _ in range(64)),
    }
    try:
        probe['route'] = plugin.rpc.getroute(
            probe['destination'],
            msatoshi=amount,
            riskfactor=1,
        )['route']
        probe['payment_hash'] = ''.join(random.choice(string.hexdigits) for _ in range(64))
    except RpcError:
        probe['failcode'] = -1
        return probe

    plugin.rpc.sendpay(probe['route'], probe['payment_hash'])

    try:
        plugin.rpc.waitsendpay(probe['payment_hash'], timeout=30)
        raise ValueError("The recipient guessed the preimage and cryptography is broken.")
    except RpcError as e:
        probe['finished_at'] = str(datetime.now())
        if e.error['code'] == 200:
            probe['error'] = "Timeout"
        else:
            probe['error'] = e.error['data']
            probe['failcode'] = e.error['data']['failcode']

    return probe["failcode"]
