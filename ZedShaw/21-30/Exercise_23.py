#ZedShaw Python Exercise #23
# Encoding A string into UTF-16 BYTES
#Each chunk corresponds to one byte in the UTF-16 encoded representation of the string "Hello, World!"
# With the last chunk being the null terminator

import encodings

# Check if ASCII is available in the standard encodings
if 'utf-16' in encodings.aliases.aliases.values():
    print("utf-16 encoding is available in Python.")
else:
    print("utf-16 encoding is not available in Python.")


print("------------------------------------------------")

# Define a string variable
text = "Hello, World!"

# Encode the string to utf-16
# The encode() method converts the string to bytes using the specified encoding (utf-16)
encoded_data = text.encode("utf-16")

# Print the encoded bytes
print("Encoded bytes:", encoded_data)


# UTF-16 ENCODING
# "Hello, World!"
# ==
# b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'