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
    if type(message) is not str:
        raise TypeError("Invalid message format (must be ascii, bin, or hex)")
    if type(key) is not str:
        raise TypeError("Invalid key format (must be ascii, bin, or hex)")
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
            raise TypeError("Invalid message format (must be ascii, bin, or hex)")
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
            raise TypeError("Invalid key format (must be ascii, bin, or hex)")

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

    """XOR binary + binary"""
    bin_bin_result = xor('01101010', '10101111', output='bin')
    print(bin_bin_result)
    # 01101010
    # 10101111
    # --------
    # 11000101
    
    """XOR binary + hex"""
    bin_hex_result = xor('10101010', '2f', output='bin') # 2f = 00101111
    print(bin_hex_result)
    # 10101010
    # 00101111
    # --------
    # 10000101
    
    """XOR binary + ascii"""
    bin_asc_result = xor('01010101', 'G', output='bin') # G = 01000111
    print(bin_asc_result)
    # 01010101
    # 01000111
    # --------
    # 00010010
    
    """XOR hex + binary"""
    hex_bin_result = xor('3e', '01101001', output='bin') # 3e = 00111110
    print(hex_bin_result)
    # 00111110
    # 01101001
    # --------
    # 01010111

    """XOR hex + hex"""
    hex_hex_result = xor('1bf2', '213c', output='bin') # 1bf2 = 0001101111110010
    print(hex_hex_result)                              # 213c = 0010000100111100
    # 0001101111110010
    # 0010000100111100
    # ----------------
    # 0011101011001110

    """XOR hex + ascii"""
    hex_asc_result = xor('776f77', 'hey', output='bin') # 776f77 = 011101110110111101110111
    print(hex_asc_result)                               # hey    = 011010000110010101111001
    # 011010000110010101111001
    # 011101110110111101110111
    # ------------------------
    # 000111110000101000001110

    """XOR ascii + bin"""
    asc_bin_result = xor('guess', '1000', output='bin') # guess = 0110011101110101011001010111001101110011
    print(asc_bin_result)
    # 0110011101110101011001010111001101110011
    # 1000100010001000100010001000100010001000
    # ----------------------------------------
    # 1110111111111101111011011111101111111011

    """XOR ascii + hex"""
    asc_hex_result = xor('this', 'fe', output='bin') # this = 01110100011010000110100101110011
    print(asc_hex_result)                            # fe   = 11111110111111101111111011111110
    # 01110100011010000110100101110011
    # 11111110111111101111111011111110
    # --------------------------------
    # 10001010100101101001011110001101

    """XOR ascii + ascii"""
    asc_asc_result = xor('bite', 'me', output='bin') # bite = 01100010011010010111010001100101
    print(asc_asc_result)                            # me   = 01101101011001010110110101100101
    # 01100010011010010111010001100101
    # 01101101011001010110110101100101
    # --------------------------------
    # 00001111000011000001100100000000