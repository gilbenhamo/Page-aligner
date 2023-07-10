# Page Aligner
This repository contains a program that aligns and crops a photo of a paper page. The program allows the user to choose the output path for the resulting aligned image. It utilizes image processing techniques to detect the rectangular shape of the object (page), find the corners, and align the page properly.
<br/>**This project was developed as part of an image processing course.**

## Environment

- Operating System: Windows/macOS
- Development Environment: PyCharm
- Language: Python
- Required Packages: cv2, numpy

Please make sure you have the following packages installed before running the program.

## How to Run
To run the program, follow the steps below:
1. Format to run on the command line:
   ```shell
   python Scanner.py <path of the input image> <path of the output image>
   ```
   Example:
   ```shell
   python Scanner.py input_image.jpg output_image.jpg
   ```

2. The program will process the input image, detect the page's rectangular shape, find the corners, and align the page properly.

3. The aligned image will be saved at the specified output path.

### Example
**Input image:**
<img src="/images/input.jpg" alt="Input img" width="200" >
**Output image:**
<img src="/images/out.jpg" alt="Input img" width="200" >

## Authors
- [Gil Ben Hamo](https://github.com/gilbenhamo)
- Yovel Aloni

If you have any questions or suggestions regarding the page aligner program, feel free to reach out to the authors.
Enjoy using the page aligner to straighten and crop your paper page images effortlessly!
