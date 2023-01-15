import base64

string_to_encode = "test"
string_bytes =string_to_encode.encode("ascii")

base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Encoding")
print(f"Text to encode: {string_to_encode}")
print(f"Text encoded in base64: {base64_string}")


base64_bytes_decode = base64_string.encode("ascii")
  
string_bytes_decode = base64.b64decode(base64_bytes_decode)
string_decoded = string_bytes_decode.decode("ascii")

print("--------------")
print(f"Decoding:")
print(f"Now I will decode: {base64_string}")
print(f"Decoded text: {string_decoded}")