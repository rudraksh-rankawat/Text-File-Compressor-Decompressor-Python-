# Text File Compressor/Decompressor (Python)

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) A simple desktop application built with Tkinter for compressing and decompressing text files using `zlib` and `base64`.





https://github.com/user-attachments/assets/40d1fad3-34d5-4f12-b816-adf6c139a72f





## ✨ Features

* **Compress Text Files:** Reduces the size of `.txt` files.
* **Decompress Compressed Files:** Restores compressed files back to their original text.
* **User-Friendly GUI:** Simple interface powered by Tkinter.

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

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **No special dependencies are required** beyond Python's standard library. Ensure you have Python 3.x installed.

## 🏃‍♀️ How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the `main.py` script:
    ```bash
    python main.py
    ```
    This will open the application window.

## 🛠️ Usage

1.  Click the "Select File to Compress" button to choose a `.txt` file you want to compress.
2.  A new file with `_compressed.txt` will be created in the same directory, containing the compressed data.
3.  Click the "Select File to Decompress" button to choose a `_compressed.txt` file.
4.  A new file with `_decompressed.txt` will be created, containing the original text.

## 📸 Screenshots (Optional but Recommended)

*(Add screenshots of your application here. This greatly helps users understand what to expect.)*

## 💡 Future Enhancements (Optional)

* Add options to specify output directory.
* Implement progress bar for large files.
* Support for more file types (e.g., binary files, though this would require changing how files are read/written).
* Add a clear button to reset selected file.
* Improve UI aesthetics.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or want to improve the code, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Your Name - [Your Email/GitHub Profile Link]

---
