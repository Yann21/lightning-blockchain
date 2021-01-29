# Lightning Network Vulnerabilities

## Table of contents
* [General info](#the-root-of-all-evil)
* [Get started](#how-to-get-started)
* [Requirements](#requirements)

## The root of all evil
```
--- a/trunk/main.h
+++ b/trunk/main.h
@@ -15,6 +15,7 @@
 class CKeyItem;
 
 static const unsigned int MAX_SIZE = 0x02000000;
+static const unsigned int MAX_BLOCK_SIZE = 1000000;
 static const int64 COIN = 100000000;
 static const int64 CENT = 1000000;
 static const int COINBASE_MATURITY = 100;
 ```


## How to get started?
```
# Start the bitcoin daemon
$ bitcoind [--testnet]

# Start the c-lightning daemon
$ lightningd --plugin=$PWD/src/probe.py

# Wait for synchronization

# Install python libraries
$ pip install -r requirements.txt

# Run the plugin
$ lightning-cli probe <node_id> <max_capacity> <epsilon_precision>
```

## Requirements
* bitcoin-core
* c-lightning
* python 3.6+
    * pyln-client

## ABSTRACT
As digital currencies enjoy renewed attention, Bitcoin takes once
again center stage as the leading technological breakthrough of
the last decade. Lightning Network draws its popularity from Bit-
coin and holds the promise of increasing the speed and capacity
of Bitcoin, and sustainably decreasing transaction fees. Lightning
Network has succeeded in establishing itself as a reliable off-chain
scaling solution for Bitcoin, allowing it to achieve commercial adop-
tion and breadth. However, Lightning is not impervious to exploits,
some of which can have dire consequences. We study a wide range
of known vulnerabilities from time dilation to lockdown attacks
and try to better understand how to guard against these weaknesses.
Moreover, we implement a probing attack on Lightning channel
and grapple with its consequences in the latter part of the paper.
