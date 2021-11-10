import numpy as np
from PIL import Image
import os
from svd import *

def imageToThreeArray(address):
    img = Image.open(address)
    arr = np.array(img)
    return [arr[0:, 0:, 0], arr[0:, 0:, 1], arr[0:, 0:, 2]]

def threeArrayToOneArray(array):
    newArr = np.zeros((len(array[0]), len(array[0][0]), 3), dtype=np.uint8)
    newArr[0:, 0:, 0] = array[0]
    newArr[0:, 0:, 1] = array[1]
    newArr[0:, 0:, 2] = array[2]
    return newArr

def arrayToImg(array):
    img = Image.fromarray(array)
    img.save(r"new.jpg")
    return

def main():
    os.chdir(os.path.join("Algeo02-20112", "src", "backend", "imageProcessing"))
    
    x = imageToThreeArray(r"img.jpg")
    Image.fromarray(threeArrayToOneArray([x[0], x[0], x[0]])).save(r"test.jpg")
    y = np.round_(kompresiSVD(x[0], 100))
    y = np.uint8(y)
    Image.fromarray(threeArrayToOneArray([y, y, y])).save(r"new.jpg")

if __name__ == "__main__":
    main()