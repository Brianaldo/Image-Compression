import numpy as np
from PIL import Image
import os
import math
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

ERR_TOL = 10**(-6)

def svd(A):
    s = np.linalg.matrix_rank(A)
    n, m = np.shape(A)
    V = np.random.rand(m, s)
    err = 1 # inisialisasi error
    while (err > ERR_TOL):
        Q, R = np.linalg.qr(np.dot(A, V))
        U = Q[:,:s]
        Q, R = np.linalg.qr(np.dot(np.transpose(A), U))
        V = Q[:,:s]
        sigma = R[:s, :s]
        err = np.linalg.norm(np.dot(A, V) - np.dot(U, sigma))
    return s, U, np.diag(np.diag(sigma)), V

def kompresiSVD(matrix, percent):
    rank, U, S, V = svd(matrix)
    rank = int(round(rank * percent / 100))
    if (rank <= 0):
        rank = 0

    return np.dot(np.dot(U[0:, 0:rank], S[0:rank, 0:rank]), np.transpose(V[0:, 0:rank]))

def compress(percent):
    x = imageToThreeArray(r"img.jpg")
    R = x[0]
    G = x[1]
    B = x[2]
    NR = kompresiSVD(R, percent)
    NG = kompresiSVD(G, percent)
    NB = kompresiSVD(B, percent)
    arrayToImg( np.uint8( threeArrayToOneArray ([NR, NG, NB]) ) )
    return

def main():
    os.chdir(os.path.join("Algeo02-20112", "src", "backend", "imageProcessing"))
    
    x = imageToThreeArray(r"img.jpg")
    UR, sigmaR, VR = svd(x[0])
    UG, sigmaG, VG = svd(x[1])
    UB, sigmaB, VB = svd(x[2])

    rank = 70
    R = np.dot(np.dot(UR[0:, 0:rank], sigmaR[0:rank, 0:rank]), np.transpose(VR[0:, 0:rank]))
    G = np.dot(np.dot(UG[0:, 0:rank], sigmaG[0:rank, 0:rank]), np.transpose(VG[0:, 0:rank]))
    B = np.dot(np.dot(UB[0:, 0:rank], sigmaB[0:rank, 0:rank]), np.transpose(VB[0:, 0:rank]))
    Image.fromarray(np.uint8(threeArrayToOneArray([R, G, B]))).save(r"1.jpg")

if __name__ == "__main__":
    main()