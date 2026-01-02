# QR Code Generator 🖼️

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

This Python project generates QR codes from text, URLs, or Wi-Fi credentials using the `qrcode` library.  
It demonstrates file handling, image generation, and QR code creation.

---

## ✨ Features

- Generate QR codes for text, URLs, and Wi-Fi credentials
- Save QR codes as PNG images
- Simple and beginner-friendly Python script
- Easily customizable input data


---

## 📂 Project Structure

```

qr_code_generator/
├── qr_code_generator.py
├── qr_codes/
│ ├── youtube_qr.png
│ ├── hello_qr.png
│ └── wifi_qr.png
├── README.md
└── requirements.txt

```

---

## 💻 Requirements

- Python 3.x  
- `qrcode` library (with Pillow support)

Install dependencies:

```bash
pip install -r requirements.txt

```

---

## ⚡ How to Run

1.Open terminal in the project folder.

2.Run the script:

```

python qr_code_generator.py

```

3.QR code images will be saved in the qr_codes/ folder:

-youtube_qr.png → URL QR code
-hello_qr.png → Text QR code
-wifi_qr.png → Wi-Fi QR code

---

## 🔧 Customization

-Change the data in generate_qr() function:

```
generate_qr('Your Data Here','output_filename.png')

```

-Supports URLs, text, or Wi-Fi credentials:

```
wifi_data = 'WIFI:T:WPA;S:MyWiFi;P:password123;;'
generate_qr(wifi_data,'wifi_qr.png')


```

---

## 🖼️ Example Output

![QR Code Example](qr_codes/hello_qr.png)

---

## 📌 Use Cases

- Sharing URLs quickly
- Generating Wi-Fi QR codes for guests
- Encoding short messages
- Learning basic image generation in Python

---

## 🚀 Future Improvements

- Add GUI support
- Allow color customization for QR codes
- Accept user input from terminal
- Batch QR code generation




