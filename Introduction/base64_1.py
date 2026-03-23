import base64

hex_text = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')

print(hex_text)

encoded_text = base64.b64encode(hex_text)
print(encoded_text)