#! /usr/bin/env python3
from pyln.client import Plugin, Millisatoshi, RpcError
from collections import defaultdict
from functools import wraps
from os import path
import random
import threading

plugin = Plugin()


# Format hint `simple` makes lightning-cli print it as (-H) human readable
def format_simple(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return {'text': fn(*args, **kwargs), 'format-hint': 'simple'}
    return wrapped


@plugin.method("helpme")
@format_simple
def probe(plugin, command=None, *args):
    """Gives helpful hints about running this node."""

    if (command == "probe"):
        return plugin.rpc.getinfo()
        return "lightning-cli getinfo"
        return "probing probing..."

    print( "test")
    return "howdy there fellas"
    raise ValueError("Unknown command {}".format(command))

# We try to connect to peers ourselves
class ConnectThread(threading.Thread):
    def __init__(self, nodes, peers_wanted):
        super().__init__()
        self.daemon = True
        self.nodes = nodes
        self.peers_wanted = peers_wanted
        self.start()

    def run(self):
        while self.peers_wanted > 0:
            k = random.choice(list(self.nodes.keys()))

            # Try each address.
            for a in self.nodes[k]:
                try:
                    plugin.rpc.connect(k, a['address'], a['port'])
                    del self.nodes[k]
                    self.peers_wanted -= 1
                    break
                except Exception:
                    pass

@plugin.init()
def init(options, configuration, plugin):
    plugin.log("Plugin helpme.py initialized!")


if __name__ == '__main__':
    plugin.run()
