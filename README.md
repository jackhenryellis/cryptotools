# cryptotools
Miscellaneous cryptography tools for performing encryption and decryption on the command line

## Install
> $ git clone https://github.com/jackhenryellis/cryptotools  

**If you want to import cryptotools to use in your own programs**
> $ cd cryptotools  
> $ pip install .

## Usage

### xor
xor is a dynamic XOR utility that takes 2 inputs -m <message> and -k <key> in the form of binary, hexademical, or ascii and returns the XOR result in binary, hexademical, or ascii (default)
> $ cd cryptotools  
> $ python3 cryptotools/xor.py -m <message> -k <key> -o <output [bin, hex, ascii]>  
```
$ python3 cryptotools/xor.py -m 01101010 -k 10101111 -o bin
11000101
$ python3 cryptotools/xor.py -m secret -k a1 -o hex
d2c4c2d3c4d5
$ python3 cryptotools/xor.py -m d2c4c2d3c4d5 -k a1 -o ascii
secret
```
