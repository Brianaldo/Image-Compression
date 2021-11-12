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

def householder (m):
    n = len(m)
    for k in range(n-2):
        total = 0
        for i in range(k+1,n):
            total += (m[i,k])**2
        total = math.sqrt(total)
        if m[k+1,k]>=0:
            total *= -1
        r = math.sqrt((0.5)*(total)**2 - (0.5)*total*m[k+1,k])
        w = []
        for j in range(k+1):
            w.append(0)
        w.append((m[k+1,k] - total)/(2*r))
        for j in range(k+2, n):
            w.append(m[j,k]/(2*r))
        w = np.matrix(w)
        wwt = np.dot(np.transpose(w), w)
        id = np.identity(n)
        wwt = wwt * 2
        h = np.subtract(id,wwt)
        temp = np.dot(h, m)
        m = np.dot(temp,h)
    return m

def main():
    os.chdir(os.path.join("Algeo02-20112", "src", "backend", "imageProcessing"))
    
    x = imageToThreeArray(r"img.jpg")
    print(len(np.dot(np.transpose(x[1]), x[1])))
    print(householder(np.array(np.dot(np.transpose(x[1]), x[1]))))
    # Image.fromarray(threeArrayToOneArray([x[0], x[0], x[0]])).save(r"test.jpg")
    # # y = np.round_(kompresiSVD(x[0], 100))
    # # y = np.uint8(y)
    # Image.fromarray(threeArrayToOneArray([x[0], x[0], x[0]])).save(r"new.jpg")
    # Image.fromarray(threeArrayToOneArray([y, y, y])).save(r"new.jpg")

if __name__ == "__main__":
    main()