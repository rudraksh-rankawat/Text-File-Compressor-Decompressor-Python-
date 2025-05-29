# Text File Compressor/Decompressor (Python)
built a simple desktop application built with Tkinter for compressing and decompressing text files using zlib and base64. I learnt about so many things while building this. Particulary read about Unicode, how encoding works, how file compression works (lossless and lossy), DEFLATE Algorithm (which uses combination of LZ 77 and Huffman coding, which zlib uses internally too), filedialog in Tkinter. I loved this one. The code could be rudimentary, specially the methods to set text file names. Error handling is not done properly either. But I enjoyed making the prototype.



https://github.com/user-attachments/assets/40d1fad3-34d5-4f12-b816-adf6c139a72f



## 🚀 How It Works

This application uses the following Python modules:
* `tkinter`: For creating the graphical user interface.
* `zlib`: A standard library for data compression (using the DEFLATE algorithm).
* `base64`: For encoding the compressed binary data into a text format, making it suitable for saving in a `.txt` file.

When you compress a file:
1.  The content of the selected `.txt` file is read.
2.  `zlib` compresses the text data.
3.  The compressed binary data is then Base64 encoded to convert it into a string of ASCII characters.
4.  This Base64 string is saved to a new file with `_compressed.txt` suffix.

When you decompress a file:
1.  The content of the selected `_compressed.txt` file (which contains Base64 encoded data) is read.
2.  The Base64 string is decoded back into the original compressed binary data.
3.  `zlib` decompresses this binary data back into the original text.
4.  The restored text is saved to a new file with `_decompressed.txt` suffix.

## 📦 Installation

1.  **Clone this repository:**
2.  **No special dependencies are required** beyond Python's standard library. Ensure you have Python 3.x installed.

## 🏃‍♀️ How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the `main.py` script:
    ```bash
    python main.py
    ```
    This will open the application window.





---
