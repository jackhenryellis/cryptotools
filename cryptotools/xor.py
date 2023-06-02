import argparse
import convert

def xor(message:str, key:str, output='ascii') -> str:
    """
    Receives a message (ascii, bin, or hex) and key (ascii, bin, or hex)
    Returns the XOR result with an optional output of 'ascii', 'hex', or 'bin'
    """
    HEX_BYTE = 2
    HEX_BASE = 16
    BIN_BYTE = 8
    BIN_BASE = 2

    # perform input sanitation
    if message is None:
        return("Message is missing. -m <message_to_XOR>")
    if key is None:
        return("Key is missing. -k <XOR_key>")
    if type(message) is not str:
        return("Invalid message format (must be ascii, bin, or hex)")
    if type(key) is not str:
        return("Invalid key format (must be ascii, bin, or hex)")
    message_is_bin = True
    message_is_hex = True
    key_is_bin = True
    key_is_hex = True
    # CHECK MESSAGE TYPE
    try:
        # check if message is binary
        int(message, BIN_BASE)
        message = message.lstrip('0b')
        while len(message) % BIN_BYTE != 0: # append leading 0s
            message = '0' + message
        message_is_hex = False
    except:
        message_is_bin = False
    if not message_is_bin:
        # check if message is hex
        try:
            int(message, HEX_BASE)
            message = message.lstrip('0x')
        except:
            message_is_hex = False
    if not message_is_bin and not message_is_hex:
        # message must be ascii
        try:
            message.encode('ascii')
        except:
            return("Invalid message format (must be ascii, bin, or hex)")
    # CHECK KEY TYPE
    try:
        # check if key is binary
        int(key, BIN_BASE)
        key = key.lstrip('0b')
        while len(key) % BIN_BYTE != 0: # append leading 0s
            key = '0' + key
        key_is_hex = False
    except:
        key_is_bin = False
    if not key_is_bin:
        # check if key is hex
        try:
            int(key, HEX_BASE)
            key = key.lstrip('0x')
        except:
            key_is_hex=False
    if not key_is_bin and not key_is_hex:
        # key must be ascii
        try:
            key.encode('ascii')
        except:
            return("Invalid key format (must be ascii, bin, or hex)")

    # convert message to hex
    if message_is_bin:
        message = convert.bin_to_hex(message)
    elif not message_is_hex: # message is ascii
        message = convert.ascii_to_hex(message)
        
    # convert key to hex
    if key_is_bin:
        key = convert.bin_to_hex(key)
    elif not key_is_hex: # key is ascii
        key = convert.ascii_to_hex(key)
    
    # make message and key the same length
    if len(message) != len(key):
        if len(message) > len(key):
            # pack key to length of message
            key *= len(message)//len(key) # first to nearest whole length
            key += key[:(len(message) % len(key))] # then adding the remainder
        # strip key
        key = key[:len(message)]

    # split message and key into bytes
    message_bytes = [message[start:start+HEX_BYTE] for start in range(0, len(message), HEX_BYTE)]            
    key_bytes = [key[start:start+HEX_BYTE] for start in range(0, len(key), HEX_BYTE)]

    # create list of (message, key) tuples for each byte
    bytes_to_xor = zip(message_bytes, key_bytes)
    xor = []
    # xor message bytes with key bytes
    for byte in bytes_to_xor:
        result = int(byte[0], HEX_BASE) ^ int(byte[1], HEX_BASE)
        if output == 'ascii':
            ascii_result = chr(result)
            xor.append(ascii_result)
        elif output == 'hex':
            hex_result = hex(result).lstrip('0x')
            if hex_result == "": # result was 0
                hex_result = 00
            xor.append(hex_result)
        else: # output is binary
            bin_result = bin(result).lstrip('0b')
            if bin_result == "":  # result was 0
                bin_result = '00000000'
            while len(bin_result) % BIN_BYTE != 0: # append leading 0s
                bin_result = '0' + bin_result
            xor.append(bin_result)
    # output as 1 bitstream
    xor = ''.join(map(str, xor))
    return xor


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    xor is a dynamic XOR utility
    that takes 2 inputs [message, key] in the form of binary, hexademical, or ascii
    and returns the XOR result in either binary, hexademical, or ascii (default)

    example usage:
        xor.py -m 01101010 -k 10101111 -o bin
        11000101

        xor.py --message secret --key a1 --output hex
        d2c4c2d3c4d5

        xor.py -m d2c4c2d3c4d5 -k a1 -o ascii
        secret
        """)

    parser.add_argument("-m", "--message", help="The message to XOR. -m <message> -k <key> -o <output type>")
    parser.add_argument("-k", "--key", help="The XOR key (may be in binary, hexademical, or ascii)")
    parser.add_argument("-o", "--output", help="The output type [bin, hex, ascii(default)]")

    args = parser.parse_args()
    
    if args.output:
        print(xor(args.message, args.key, args.output))
    else:
        print(xor(args.message, args.key))
