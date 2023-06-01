def list_to_string(in_list, sep=' '):
    """
    Returns a string containing all elements in a list
    with 'sep' separating each value
    """
    string = sep.join(map(str, in_list))
    return string


def string_to_list(string, n):
    """
    Splits a string into a list of strings that are n long
    """
    out_list = [string[start:start+n]\
                for start in range(0, len(string), n)]
    return out_list


def ascii_to_bin(text, space=False):
    """
    Converts a string of text to a binary string
    with the optional parameter to remove the space
    between each byte
    """
    byte_list = []
    # iterate through each character
    # determine its ascii binary value
    # and append it to the list
    for char in text:
        char_byte = bin(ord(char)).replace('b', '')
        # pad with 0's until char_byte is 8 digits long
        while len(char_byte) < 8:
            char_byte = '0' + char_byte
        byte_list.append(char_byte)
    if space:
        return list_to_string(byte_list)
    else:
        return list_to_string(byte_list, '')


def ascii_to_hex(text, space=False):
    """
    Converts a string of text to hex
    with an optional parameter to remove the space
    between each byte
    """
    hex_list = []
    # iterate through each character
    # determine its ascii hex value
    # and append it to the list
    for char in text:
        char_hex = hex(ord(char)).lstrip('0x').upper()
        hex_list.append(char_hex)
    if space:
        return list_to_string(hex_list)
    else:
        return list_to_string(hex_list, '')


def bin_to_ascii(binary):
    """
    Converts a binary string to a string of UTF-8 encoded text
    """
    # if input is a list, convert it to a string
    if isinstance(binary, list):
        binary = list_to_string(binary, '')
    # remove all whitespace
    binary = binary.replace(" ", "")
    # divide binary string into a list of bytes
    byte_list = string_to_list(binary, n=8)
    # initialise empty text string
    text = ""
    try:
        for byte in byte_list:
            # convert byte to its respective character
            char = chr(int(byte, base=2))
            # concatenate character to existing text string
            text += char
    except:
        return None
    return text


def bin_to_hex(binary):
    """
    Converts a binary bitstream to a hex string
    """
    binary = binary.lstrip('0b') 
    # append leading 0s to nearest byte
    while len(binary) % 8 != 0:
            binary = '0' + binary
    return hex(int(binary, 2)).lstrip('0x').upper()


def hex_to_ascii(hexadecimal):
    """
    Converts a hex string to a string of UTF-8 encoded text
    """
    # if input is a list, convert it to a string
    if isinstance(hexadecimal, list):
        hexadecimal = list_to_string(hexadecimal, '')
    # remove all whitespace
    hexadecimal = hexadecimal.replace(" ", "")
    # divide hex string up into bytes
    hex_list = string_to_list(hexadecimal, n=2)
    # initialise empty text string
    text = ""
    try:
        for byte in hex_list:
            # convert byte to its respective character
            char = chr(int(byte, base=16))
            # concatenate character to existing text string
            text += char
    except:
        return None
    return text


def hex_to_bin(hexadecimal):
    """
    Converts a hex string to a binary bitstream
    """    
    hexadecimal = hexadecimal.lstrip('0x')
    binary = bin(int(hexadecimal, 16)).lstrip('0b')
    # append leading 0s to nearest byte
    while len(binary) % 8 != 0:
            binary = '0' + binary
    return binary



if __name__ == '__main__':
    MSG = "Test #79: This is a test message."
    print(MSG)

    # convert message to hex
    hex_msg = ascii_to_hex(MSG)
    print(hex_msg)
    # and back
    reverse_hex = hex_to_ascii(hex_msg)
    print(reverse_hex)

    # convert message to binary
    bin_msg = ascii_to_bin(MSG)
    print(bin_msg)
    # and back
    reverse_bin = bin_to_ascii(bin_msg)
    print(reverse_bin)