# 🖼️ AVIF to PNG Converter

Convert AVIF images to PNG using Python. Lightweight, fast, and simple to use via the command line. Powered by Pillow and the `pillow-avif-plugin`.

---

## 🚀 Features

- ✅ AVIF → PNG conversion
- ✅ Easy to use
- ✅ Compatible with Windows, macOS, Linux
- ✅ Output folder support

---

## 🧰 Requirements

Install the necessary packages:

```bash
pip install pillow pillow-avif-plugin
```

---

## 💡 Usage

### 1. Place your `.avif` image in the same folder or provide a full path.

### 2. Run the script

```bash
python avif_to_png.py
```

By default, it will convert `ibi1.avif` to `ibi1.png` in the same folder.

---

## 🧾 Example Script

```python
import pillow_avif  # Enables AVIF support
from PIL import Image
import os

def avif_to_png(input_path, output_dir=None):
    base_filename = os.path.splitext(os.path.basename(input_path))[0]

    if output_dir is None:
        output_path = os.path.join(os.path.dirname(input_path), base_filename + ".png")
    else:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, base_filename + ".png")

    with Image.open(input_path) as img:
        img.save(output_path, "PNG")
        print(f"{input_path} converted → {output_path}")

if __name__ == "__main__":
    avif_to_png("ibi1.avif")
```

---

## 📂 Output Folder Option

You can specify a custom folder like this:

```python
avif_to_png("ibi1.avif", output_dir="converted_images")
```

---

## 🛠️ To-Do

- [ ] Batch conversion support
- [ ] GUI support
- [ ] Web interface (Flask/FastAPI)

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---

## 📄 License

This project is licensed under the MIT License.
