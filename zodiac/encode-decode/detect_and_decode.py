import sys
import chardet
import decoders
from zodiac.utility.utility_tools import update_csv
from utils import Utils

separator = "#!||!#"


class DetectDecodeMain:
    output = []
    update_flag = False

    def __int__(self):
        output = []
        update_flag = False

    def update_csv_data(self):
        update_csv("data.csv", self.output, Utils.setup_column_names_for_csv())

    @staticmethod
    def write_to_dict(encoded_string, decoded_string, encoding):
        if decoded_string != encoded_string.decode('utf-8'):
            result = {}
            print("Decoded string:", decoded_string)
            result["encoded_string"] = encoded_string.decode()
            result["decoded_string"] = decoded_string.decode()
            result["encoding_type"] = encoding
            dm.output.append(result)
            dm.update_flag = True

    def detect_base_encoding(self, string):
        try:
            self.write_to_dict(string, decoders.decode_base64(string), "base64")
            if not self.update_flag:
                self.write_to_dict(string, decoders.decode_base32(string), "base32")

        except Exception:
            print("No base encoding detected")

    def detect_and_decode(self, string):
        # Detect the encoding of the string
        encodings = chardet.detect_all(string)
        decoded_string = ""
        for encoding in encodings:
            # Decode the string using the detected encoding
            try:
                decoded_string = string.decode(encoding['encoding'])
                self.write_to_dict(string, decoded_string, encoding['encoding'])
                if not self.update_flag:
                    self.detect_base_encoding(string)
                else:
                    check = input("Do you have the decode string? (y/n)")
                    if "y" in check:
                        decoded_string = input("Please input the decoded string?")
                        encoding_algo = input("Please input the encoding algorithm used?")
                        self.write_to_dict(string, bytes(decoded_string), encoding_algo)
                    else:
                        print("Exiting")

            except Exception:
                print("Unable to decode with this encoding")
        else:
            if decoded_string is None:
                print("Unable to decode with any encoding")


if __name__ == "__main__":

    if sys.argv is not None and sys.argv[1] is not None and len(str(sys.argv[1]).strip()) > 0:
        dm = DetectDecodeMain()
        dm.detect_and_decode(str(sys.argv[1]).strip().encode())
        for opt in dm.output:
            print(str(opt["encoded_string"]) + " -> " + str(opt["decoded_string"]) + " :: enc used : " + str(
                opt["encoding_type"]))
        outputCheck = input("Is it usable? (y/n)")
        if "y" in outputCheck:
            dm.update_csv_data()
