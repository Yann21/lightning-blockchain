#! /usr/bin/env python3
from pyln.client import Plugin, Millisatoshi, RpcError
import pyln.client

plugin = Plugin()
print(plugin.rpc)
print("test test")

# %%
@plugin.method("helpme")
def probe(plugin, command=None, *args):
    """Gives helpful hints about running this node."""

    if (command == "probe"):
        return plugin.rpc.getinfo()
        return "lightning-cli getinfo"
        return "probing probing..."

    print( "test")
    return "howdy there fellas"
    raise ValueError("Unknown command {}".format(command))

def invoiced():
    plugin.rpc.invoice(100, "label101", "testpayment")

# %%
@plugin.init()
def init(options, configuration, plugin):
    plugin.log("Plugin helpme.py initialized!")


if __name__ == '__main__':
    plugin.run()
