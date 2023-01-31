import base64
# from detect_and_decode import write_to_dict
from detect_and_decode import DetectDecodeMain as dm


def decode_base64(string):
    decoded_string = ""
    try:
        # Attempt to decode string as base64
        decoded_string = base64.b64decode(string)
    except Exception as e:
        print(e)
    return decoded_string


def decode_base32(string):
    decoded_string = ""
    try:
        # Attempt to decode string as base32
        decoded_string = base64.b32decode(string)
    except:
        pass
    return decoded_string


def decode_base16(string):
    try:
        # Attempt to decode string as base16 (hex)
        decoded_string = base64.b16decode(string)
        dm.write_to_dict(string, decoded_string, "base16")
    except:
        pass


def decode_a85(string):
    try:
        # Attempt to decode string as a85 (hex)
        decoded_string = base64.a85decode(string)
        dm.write_to_dict(string, decoded_string, "a85")
    except:
        pass


def decode_b32hex(string):
    try:
        # Attempt to decode string as b32hex (hex)
        decoded_string = base64.b32hexdecode(string)
        dm.write_to_dict(string, decoded_string, "b32hex")
    except:
        pass


def decode_b85(string):
    try:
        # Attempt to decode string as b85
        decoded_string = base64.b85decode(string)
        dm.write_to_dict(string, decoded_string, "b85")
    except:
        pass
