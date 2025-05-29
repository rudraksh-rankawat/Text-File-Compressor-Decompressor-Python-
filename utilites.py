import zlib, base64
def compress(txt_file):
    
    with open(txt_file, mode="r", encoding="UTF-8") as f:
        text_data = f.read()
    compressed_data = zlib.compress(text_data.encode())
    name = ""
    # need to learn regex
    for c in txt_file:
        if c == ".":
            break
        name += c
    with open(f"{name}_compressed.txt", mode="w", encoding="UTF-8") as f:
        compressed_text = base64.b64encode(compressed_data)
        f.write(compressed_text.decode())
        


def decompress(c_txt_file):
    with open(c_txt_file, mode="r", encoding="UTF-8") as f:
        data = f.read()  
    decompressed_bytes = zlib.decompress(base64.b64decode(data))
    name = c_txt_file[0:len(c_txt_file)-15] + "_decompressed.txt"
    print(name)
    with open(name, mode="w", encoding="UTF-8") as f:
        f.write(decompressed_bytes.decode())

