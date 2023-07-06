b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "This is a string"
print(s)

# Bytes and strings need to be properly encoded and decoded
# before you can work with them together
print(s + b.decode("utf-8"))

b2 = s.encode("utf-8");
print(b+b2)

# Encoding the string as UTF-32
b3 = s.encode("utf-32")
print(b3)
