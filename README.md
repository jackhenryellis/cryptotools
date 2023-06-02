# cryptotools
Miscellaneous cryptography functions to assist with encryption and decryption

## Install
> $ git clone https://github.com/jackhenryellis/cryptotools  
> $ cd cryptotools  
> $ pip install . (optional)

## Usage

### XOR
xor is a dynamic XOR utility that takes 2 inputs -m <message> and -k <key> in the form of binary, hexademical, or ascii and returns the XOR result in binary, hexademical, or ascii (default)
> $ cd cryptotools  
> $ python3 cryptotools/xor.py -m <message> -k <key> -o <output [bin, hex, ascii]>  
```
$ python3 cryptotools/xor.py --m secret -k a1 -o hex
d2c4c2d3c4d5
$ python3 cryptotools/xor.py --m d2c4c2d3c4d5 -k a1 -o ascii
secret
```
