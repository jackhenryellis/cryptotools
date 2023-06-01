def atbash(message:str) -> str:
    """
    Encrypts/ decrypts a message string using the atbash cipher
    Returns the encrypted/ decrypted string
    """
    # lookup table for the atbash cipher
    ATBASH = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

    message = message.upper()
    result = ""
    for char in message:
        if not char.isalpha():
            result += char
            continue
        result += ATBASH[char]
    return result
