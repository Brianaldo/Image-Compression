from math import sqrt
from eigen import *

def svd (m, k):
# KAMUS LOKAL
   # res : matrix
   # e : array
# ALGORITMA
    U = getU(m)
    Vt = getVt(m)
    sigma = getSigma(U, Vt, k, len(m), len(m[0]))
    print(sigma)
    M = mulmat(U[1], sigma)
    M = mulmat(M, Vt[1])

    return M

def getU (m):
# Mengembalikan U
# KAMUS LOKAL
    # U : matrix
    # i : int
    # e : tuple of eigenVal and eigenVec
# ALGORITMA
    e = eigen(mulmat(m, transpose(m)))
    # print(e)
    U = [e[0], []]
    for i in range (len(e[1])):
        U[1].append(normalize(e[1][i]))
    U[1] = transpose(U[1])
    
    return U

def getVt(m):
# Mengembalikan Vt
# KAMUS LOKAL

# ALGORITMA
    e = eigen(mulmat(transpose(m), m))

    Vt = [e[0], []]
    for i in range (len(e[1])):
        Vt[1].append(normalize(e[1][i]))
    
    return Vt

def getSigma(U, Vt, k, m, n):
# KAMUS LOKAL

# ALGORITMA
    eigen = []
    
    for i in range (len(U[0]) - 1, -1, -1):
        if (abs(sqrt(U[0][i])) > 0.000001):
            eigen.append(sqrt(U[0][i]))

    for i in range (len(Vt[0])):
        val = sqrt(Vt[0][i])
        if (abs(val) > 0.000001):
            if (len(eigen) == 0):
                eigen.append(val)
            else:
                j = 0
                while ((j < len(eigen)) and (eigen[j] < val)):
                    j = j + 1
                
                if (len(eigen) == 1):
                    if (abs(eigen[j] - val) > 0.000001):
                        eigen.insert(j, val)
                elif (j == len(eigen)):
                    if (abs(eigen[j - 1] - val) > 0.000001):
                        eigen.append(val)
                else:
                    if ((abs(eigen[j - 1] - val) > 0.000001) and (abs(eigen[j] - val) > 0.00001)):
                        eigen.insert(j, val)

    sigma = [[0 for j in range (n)] for i in range (m)]

    for i in range (k):
        sigma[i][i] = eigen.pop()

    return sigma

def main():
    m = [[3, 1, 1],
         [-1, 3, 1]]
    k = 2
    print(svd (m, k))

if __name__ == "__main__":
    main()