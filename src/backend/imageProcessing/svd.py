from math import sqrt
from eigen import *

def min3(x, y, z):
    if (x <= y and x <= z):
        return x
    elif (y <= x and y <= z):
        return y
    else:
        return z

def getU(matrix, matrixT, length):
    MMT = np.dot(matrix, matrixT)
    eigenMMT = sorted(getEigenValues(MMT), reverse=True)
    rank = len(list(filter(filterZero, eigenMMT)))
    retMat = np.empty((length, length))
    for i in range(len(eigenMMT)):
        vector = getEigenVector(MMT, eigenMMT[i])
        retMat[i] = vector
    return [rank, np.transpose(retMat)]

def getSigma(eigenMMT, l, l2):
    m = l
    n = l2
    sigma = np.zeros((m, n))
    eigenMMT= list(filter(filterZero, eigenMMT))
    singular = np.sqrt(eigenMMT)

    length = min3(m, n, len(singular))
    for i in range(length):
        sigma[i][i] = singular[i]
    return sigma


def getV(MMT, eigenMMT, length):
    retMat = np.empty((length, length))
    for i in range(len(eigenMMT)):
        vector = getEigenVector(MMT, eigenMMT[i])
        retMat[i] = vector
    return np.transpose(retMat)


# def svd(matrix):
# # Return rank, U, Sigma, and V Transpose
#     length = len(matrix)
#     length0 = len(matrix[0])
#     matrixT = np.transpose(matrix)
#     lengthT = len(matrixT)
#     MMT = np.dot(matrixT, matrix)
#     eigenMMT = sorted(getEigenValues(MMT), reverse=True)
#     U = getU(matrix, matrixT, length)
#     S = getSigma(eigenMMT, length, length0)
#     VT = np.transpose(getV(MMT, eigenMMT, lengthT))
#     return [U[0], U[1], S, VT]

def kompresiSVD(matrix, percent):
    rank, U, S, VT = svd(matrix)
    rank = int(round(rank * percent / 100))
    if (rank <= 0):
        rank = 0

    return np.dot(np.dot(U[0:, 0:rank], S[0:rank, 0:rank]), VT[0:rank, 0:])

def main():
    m = [[1, 1, 1, 0, 0],
     [3, 3, 3, 0, 0],
     [4, 4, 4, 0, 0],
     [5, 5, 5, 0, 0],
     [0, 2, 0, 4, 4],
     [0, 0, 0, 5, 5],
     [0, 1, 0, 2, 2]] 
    # m = [[3, 1, 1],
    #      [-1, 3, 1]]
    print(kompresiSVD(m, 100))

if __name__ == "__main__":
    main()