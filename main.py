from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
import os
from pathlib import Path

path_input = 'input_pdf'
path_output = 'output_img'

def pdf2img(file):
    images = convert_from_path(
        str(path_input + '/' + file),
        poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin',
        userpw='Transmission28369'
    )
    filename, file_extension = os.path.splitext(file)

    for img in images:
        img.save(str(path_output + '/' + filename + '.jpeg'), 'JPEG')


def main():
    for file in os.listdir(path_input):
        if file.endswith(".pdf"):
            pdf2img(file)


if __name__ == '__main__':
    main()
