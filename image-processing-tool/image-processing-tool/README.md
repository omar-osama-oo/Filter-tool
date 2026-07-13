# Image Processing Tool 🖼️

A simple command-line tool for applying basic image processing filters,
built with **OpenCV** and **NumPy** as a learning project.

## Features

- Display image info (dimensions, size)
- Convert to grayscale
- Flip image (horizontal / vertical)
- Resize image
- Adjust brightness
- Adjust contrast
- Negative (invert colors) effect
- Blur (box blur)
- Threshold (black & white)
- Swap color channels
- Save the processed image

## Demo

```
Image processing tool
=====================
0) exit
1) show the original image
2) show image info
3) convert to grayscale
4) flip horizontal
5) flip vertical
6) resize image
7) edit the brightness
8) edit the contrast
9) negative effect
10) blur image
11) threshold (black & white)
12) swap colors
13) save image
=====================
```

## Installation

```bash
git clone https://github.com/<your-username>/image-processing-tool.git
cd image-processing-tool
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Enter the path to an image when prompted, then choose an option from the menu.

## Tech Stack

- Python 3
- OpenCV (`cv2`)
- NumPy

## What I learned

This project was built to practice:
- Reading images as NumPy arrays and understanding their shape `(H, W, C)`
- Manual pixel-level operations (brightness, contrast, negative) using array math
- Basic OpenCV functions (`cvtColor`, `flip`, `resize`, `blur`, `threshold`)
- Building an interactive CLI menu in Python

## License

This project is open source and available under the [MIT License](LICENSE).
