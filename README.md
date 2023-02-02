# Auto Decoder

Auto Decoder is a free and open source command line based encoded text decoder(still in making though). It is your swiss-army knife for decoding flags 
specifically used in CTFs.

# Functionalities
Currently can decode only till single layer encodings like:
1. Base64
2. Base32
3. Base16
4. Base45
5. Hex
6. Octal
7. Charcoded
8. ASCII85
9. Base85
10. Base32hex

As it decodes, it asks the user if the decoding is correct, and if it is correct, it stores it to a csv file, which will be used later on to train a RNN model.

# Usage
1. git clone 
2. pip install -r requirements.txt
3. python3 detect_and_decode.py <encoded_string>

# Future Tasks
1. Adding the RNN model
2. Adding multi-layer decoding
3. Adding partial decoding
4. Adding more decoders
5. If it will be possible will add more for encryption and decryption
