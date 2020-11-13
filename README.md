# lightning-blockchain

## The source of all evil
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
