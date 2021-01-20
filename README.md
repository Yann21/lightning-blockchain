# lightning-blockchain

## Table of contents
* [General info](#general-info)
* [Get started](#get-started)
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
