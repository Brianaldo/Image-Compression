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

def power_iteration(A, num_simulations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])
    # b_k = np.array([1, 1])
    # print('Start')
    # print(b_k)
    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = max(b_k1.min(), b_k1.max(), key=abs)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
        # print(b_k1)
        # print(b_k1_norm)
        # print(b_k)
    return b_k, b_k1_norm

def getU(m):
    A = np.dot(m, np.transpose(m))
    # print(A)
    return power_iteration(A, 1000)

def getV(m):
    A = np.dot(np.transpose(m), m)
    # print(A)
    return power_iteration(A, 1000)

def svda(m):
    U, e1 = getU(m)
    V, e2 = getV(m)
    U = U/np.linalg.norm(U)
    V = V/np.linalg.norm(V)
    print(U)
    print(V)
    if (e1 < e2):
        sigma = math.sqrt(e2)
    else:
        sigma = math.sqrt(e1)
    print(sigma)
    return np.dot(np.dot(np.matrix(U).T, np.matrix(sigma)), np.matrix(V))

ERR_TOL = 10**(-10)

def blockPowerMethod(A):
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
        # print(err)
    return U, np.diag(np.diag(sigma)), V

def main():
    os.chdir(os.path.join("Algeo02-20112", "src", "backend", "imageProcessing"))
    
    x = imageToThreeArray(r"img.jpg")
    U, sigma, V = blockPowerMethod(x[0])
    y = np.round(np.dot(np.dot(U, sigma), np.transpose(V)))
    Image.fromarray(np.uint8(y)).save(r"1.jpg")
    # M, N = np.shape(x[0])
    # y = np.round(svda(A))
    # y = np.uint8(y)
    # print(y)
    # Image.fromarray(y).save(r"1.jpg")
    # print(QR(np.array(householder(np.dot(x[0], np.transpose(x[0]))))))
    # print(getEigensVector(np.dot(x[0], np.transpose(x[0])), QR(np.array(householder(np.dot(x[0], np.transpose(x[0])))))))
    # print(len(np.dot(np.transpose(x[1]), x[1])))
    # print(householder(np.array(np.dot(np.transpose(x[1]), x[1]))))
    # Image.fromarray(threeArrayToOneArray([x[0], x[1], x[2]])).save(r"test.jpg")
    # print(np.reshape(svd(x[0]).ravel(), (M, N)))
    # y = np.round_(np.reshape(svd(x[0]).ravel(), (M, N)))
    # y = np.uint8(y)
    # Image.fromarray(y).save(r"1.jpg")
    # Image.fromarray(threeArrayToOneArray([x[0], x[0], x[0]])).save(r"new.jpg")
    # Image.fromarray(threeArrayToOneArray([y, y, y])).save(r"new.jpg")

if __name__ == "__main__":
    main()