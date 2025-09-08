def enc():
    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Read the encoded file as UTF-8 text
with open("enc", "r", encoding="utf-8") as f:
    data = f.read()

decoded_chars = []

for c in data:
    val = ord(c)
    high = (val >> 8) & 0xFF
    low = val & 0xFF
    decoded_chars.append(chr(high))
    decoded_chars.append(chr(low))

decoded_str = ''.join(decoded_chars)
print(decoded_str)
