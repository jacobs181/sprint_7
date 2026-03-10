print("hola mundo")
print (2+2)

## Texto e imagen de un cuaderno 
- - -
![imagen ejemplo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

En jupyter Notebook puedes mezclar:
* Código
* Texto
* Imágenes
import os
cpu_num = os.cpu_count()
print(f"Este equipo tiene {cpu_num} núcleos de CPU")

import numpy as np
from matpotlib import pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)

import sys 
sys.version

from PIL import Image
im = imagen.open("tripleten_logo.jpeg")
print(im.size)
rotated = im.rotate(90)
rotated.save('rotated-png')


python3 image_rotator.py


from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')

im = Image.open(args.input_file)
im.close()

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')




product price = 12.0 
product qty = 5 

def total price():
    product price = 11.0
    product qty = 4
    print("Total price inner:", product price * product qty)

total price() 
    
