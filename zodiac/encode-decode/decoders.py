import base64
import re
import base45 as base45


def decode_base64(string):
    decoded_string = ""
    try:
        pattern = re.compile("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$")
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as base64
        decoded_string = base64.b64decode(string)
    except Exception as e:
        print(e)
    return decoded_string


def decode_base32(string):
    decoded_string = ""
    try:
        pattern = re.compile("^[A-Z2-7]+$")
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as base32
        decoded_string = base64.b32decode(string)
    except:
        pass
    return decoded_string


def decode_base16(string):
    decoded_string = ""
    try:
        pattern = re.compile("^[0-9A-Fa-f]+$")
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as base16 (hex)
        decoded_string = base64.b16decode(string)
    except:
        pass
    return decoded_string


def decode_a85(string):
    decoded_string = ""
    try:
        pattern = re.compile(r'^<~[!-u]+~>$')
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as a85 (hex)
        decoded_string = base64.a85decode(string)
    except:
        pass
    return decoded_string


def decode_b32hex(string):
    decoded_string = ""
    try:
        pattern = re.compile(r'^[0-9A-V]{8}(?:[0-9A-V]{8})*$')
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as b32hex (hex)
        decoded_string = base64.b32hexdecode(string)
    except:
        pass
    return decoded_string


def decode_b85(string):
    decoded_string = ""
    try:
        pattern = re.compile(r'^[!-u]+$')
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as b85
        decoded_string = base64.b85decode(string)
    except:
        pass
    return decoded_string


def decode_base45(string):
    decoded_string = ""
    try:
        pattern = re.compile(r'^[0-9A-Z\$%\*\+\-\./:]+$')
        if not pattern.match(string.decode()):
            return decoded_string
        # Attempt to decode string as base32
        decoded_string = base45.b45decode(string)
    except:
        pass
    return decoded_string


def decode_hex_encoding(string):
    decoded_string = ""
    try:
        # Decode hex encoded string
        decoded_string = bytes.fromhex(string).decode('utf-8')
    except:
        pass
    return decoded_string


def decode_octal_encoding(string):
    decoded_string = ""
    try:
        # Decode hex encoded string
        decoded_string = bytes([int(x, 8) for x in string.split("\\")]).decode('utf-8')
    except:
        pass
    return decoded_string


def decode_charcode_encoding(input_string):
    decoded_string = ""
    chars=""
    string = input_string.decode()
    try:
        for splitting_char in find_splitting_character(string):
            if str(string).startswith(splitting_char):
                chars = string.split(splitting_char)[1:]
            else:
                chars = string.split(splitting_char)[0:]
        decoded_string = ""
        if len(chars) > 0:
            # TODO fix the below code
            for char in chars:
                decoded_char = chr(int(char.split(";")[0]))
                decoded_string += decoded_char
    except Exception as e:
        print(e)
        pass
    return decoded_string

def find_splitting_character(string):
    found_characters = []
    for splitting_character in ["&#", "\\x", "\\u", ";", ","," ", ":", "\\n"]:
        if splitting_character in string:
            found_characters.append(splitting_character)
    if not found_characters:
        print("No known splitting character found")
    return found_characters