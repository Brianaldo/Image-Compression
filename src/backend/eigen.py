import math
import numpy as np
from scipy.linalg import hessenberg

def nbar (m):
# Mengembalikan jumlah baris matrix
# Algoritma
    return len(m)

def nkol (m):
# Mengembalikan jumlah kolom matrix
# Algoritma
    return len(m[0])

def magnitude (v):
# Mengembalikan magnitude v
# Kamus Lokal
    # i, soq : int
    # length : real
# Algoritma
    soq = 0
    for i in range(len(v)):
        soq += (v[i])**2
    length = math.sqrt(soq)
    return length

def sumOfRow (m, row):
# Mengembalikan jumlah dari setiap element m
# Kamus Lokal
    # i, j : int
    # sum = real
# Algoritma
    sum = 0
    for i in range(nkol(m)):
        sum += m[row][i] 
    return sum

def sumOfCol (m, col):
# Mengembalikan jumlah dari setiap element m
# Kamus Lokal
    # i, j : int
    # sum = real
# Algoritma
    sum = 0
    for i in range(nbar(m)):
        sum += m[i][col] 
    return sum

def min (m):
# Mengembalikan nilai minimum dari matrix
# Kamus Lokal
    # i, j, min : int
# Algoritma
    min = m[0][0]
    for i in range(nbar(m)):
        for j in range(nkol(m)):
            if m[i][j]<min:
                min = m[i][j]
    return min

def copyMatrix (m):
# Mengembalikan matrix yang berelemen sama seperti m
# Kamus lokal
    # mh : matrix
    # i, j : int
# Algoritma
    mh = [[0 for j in range (nkol(m))] for i in range (nbar(m))]
    for i in range (nbar(m)):
        for j in range (nkol(m)):
            mh[i][j] = m[i][j]
    return mh

def getCol (A, col):
# Mengembalikan elemen A pada kolom col sebagai sebuah array
# Kamus Lokal
    # v: array
    # i: int
# Algoritma
    v = [0 for i in range (nbar(A))]
    for i in range (nbar(A)):
        v[i] = A[i][col]
    return v

def UkurangV (u,v):
# Mengembalikan hasil u-v
# Kamus Lokal
    # i: int
    # w : matrix
# Algoritma
    w = [0 for i in range(len(u))]
    for i in range(len(u)):
        w[i] = u[i]-v[i]
    return w

def matKaliX (m, X):
# Mengembalikan matrix m dengan setiap elemen m telah dikalikan X
# Kamus Lokal
    # i, j : int
# Algoritma
    n = copyMatrix(m)
    for i in range(nbar(n)):
        for j in range(nkol(n)):
            n[i][j] *= X
    return n

def vKaliX (v, X):
# Mengembalikan v dengan setiap elemen v telah dikalikan X
# Kamus Lokal
    # i, j : int
# Algoritma
    w = [0 for i in range (len(v))]
    for i in range(len(v)):
        w[i] = v[i]
    for i in range(len(v)):
        w[i] *= X
    return w

def isInvalid (A, bar):
# Mengembalikan true jika seluruh elemen dalam baris bar adalah -9999
# Kamus Lokal
    # i: int
# Algoritma
    found = False
    i = 0
    while (i<nkol(A) and not(found)):
        if (A[bar][i]!=-9999):
            found = True
        else:
            i += 1
    return not(found)
        

def isInV (v, x):
# Mengembalikan apakah X ada dalam v
# Kamus Lokal
    # i : int
    # found : boolean
# Algoritma
    found = False
    i = 0
    while (i<len(v) and not(found)):
        if (round(v[i],3)==round(x,3)):
            found = True
        else :
            i += 1
    return found

def makeIdentity(n):
# Mengembalikan matriks identitas nxn
# Kamus Lokal
    # m : matrix
    # i, j : int
# Algoritma
    m = [[0 for j in range (n)] for i in range (n)]
    for i in range (n):
        m[i][i] = 1
    return m

def sort (v):
# Mengembalikan v yang sudah disort mengecil nilai absolutnya
# Kamus Lokal
    # pas, imax, i, temp : int
# Algoritma
    if (len(v)>1):
        for pas in range(0, len(v)-1):
            imax = pas
            for i in range(pas+1, len(v)):
                if (abs(v[i])>abs(v[imax])):
                    imax = i
            temp = v[imax]
            v[imax] = v[pas]
            v[pas] = temp
    return v

# def normalize (v):
# # Melakukan normalisasi vektor
# # Kamus Lokal
#     # i, soq: int
#     # length: real
# # Algoritma
#     soq = 0
#     for i in range(len(v)):
#         soq += (v[i][0])**2
#     length = math.sqrt(soq)
#     for i in range(len(v)):
#         v[i][0] /= length
#     return v

def normalize (v):
# Melakukan normalisasi vektor
# Kamus Lokal
    # i, soq: int
    # length: real
# Algoritma
    soq = 0
    for i in range(len(v)):
        soq += (v[i])**2
    length = math.sqrt(soq)
    for i in range(len(v)):
        v[i] /= length
    return v

def isUpperTriangular (m):
    upper = True
    i = 0
    while (i<nbar(m) and upper):
        j = 0
        while (j<=i-1 and upper):
            if (round(m[i][j],3)!=0):
                upper = False
            else:
                j += 1
        i += 1
    return upper

def dotProduct (u,v):
# Mengembalikan hasil perkalian dot antara u dan v
# Kamus Lokal
    # result, i: int
# Algoritma
    result = 0
    for i in range(len(u)):
        result += u[i]*v[i]
    return result

def mulmat (a,b):
# Melakukan perkalian matrix a kali b
# Kamus Lokal
    # i, j, k : int
    # c : matrix
# Algoritma
    # c = [[0 for j in range(nkol(b))] for i in range(nbar(a))]
    # for i in range(nbar(a)):
    #     for j in range(nkol(b)):
    #         c[i][j] = 0
    #         for k in range(nkol(a)):
    #             c[i][j] += a[i][k] * b[k][j]
    # return (c)
    return np.dot(a, b)

def transpose (m):
# Melakukan transpose matrix m
# Kamus Lokal
    # i, j : int
    # m1 : matrix
# Algoritma
    m1 = [[0 for j in range (nbar(m))] for i in range(nkol(m))]
    for i in range (nbar(m)):
        for j in range (nkol(m)):
            m1[j][i] = m[i][j]
    return m1

def powerMethod (A):
# Mengembalikan nilai eigen terbesar
# Kamus Lokal
    # i, f : int
    # v : matrix
# Algoritma
    v = [[0 for j in range (1)] for i in range (nkol(A))]
    v[0][0] = 1
    for i in range(50):
        v = mulmat(A,v)
    w = mulmat(A, v)
    k = mulmat(transpose(v), w)[0][0]
    l = mulmat(transpose(v), v)[0][0]
    f = min(v)
    if f<1:
        f = 1
    return ((k/l), matKaliX(v, 1/f))              # (eigenValue, eigenBase)
    # Problem : No eigenValue / Defective matrix
    # f = [[-2, -1], [5,2]] -> no eigenvalue
    # b = [[2,1,0], [0,2,0], [0,0,3]] # 2/3 -> defective
    # g = [[3,1], [0,3]] -> defective

def projection (u,v):
# Mengembalikan vektor proyeksi u pada v
# Algoritma
    if (abs(magnitude(v)) < 0.001):
        k = 9999
    else:
        k = dotProduct(u,v) / magnitude(v)**2
    return vKaliX(v, k)

'''def Q (m):
# Mengembalikan matrix Q sebagai faktor m berdasarkan QR factorization
# Metode yang digunakan adalah Gram-Schmidt process
# Kamus Lokal
    # ma, mh: matrix
# Algoritma
    ma = transpose(m)
    mh = copyMatrix(ma)
    for i in range (nbar(mh)):
        for j in range (i):
            mh[i] = UkurangV(mh[i], projection(ma[i], mh[j]))
    for i in range (nbar(mh)):    
        x = magnitude(mh[i])
        if round(x,3)!=0:
            mh[i] = vKaliX(mh[i], 1/x)
    return transpose(mh)'''

'''def R (m):
# Mengembalikan matrix R sebagai faktor m berdasarkan QR factorization
# Algoritma
    return mulmat(transpose(Q(m)), m)'''

def getEigenValues(matrix):
    length = len(matrix)
    retMat = np.array([])
    i = 0
    while(not isUpperTriangular(matrix) and i < 25):
        Q, R = QR(matrix)
        matrix = np.dot(R, Q)
        i += 1
    for j in range(length):
        retMat = np.append(retMat, matrix[j][j])
    return retMat

def QR(matrix):
    matrix1 = matrix
    # matrix1 = hessenberg(matrix)
    length = len(matrix1)
    Q = np.empty((length, length))
    R = np.zeros((length, length))
    for i in range(length):
        col = matrix1[0:, i]
        # print(col)
        for j in range(1, i + 1):
            R[j - 1][i] = np.dot(col, Q[0:, j - 1])
            col = col - (np.dot(col, Q[0:, j - 1]) * Q[0:, j - 1])
        magn = np.linalg.norm(col)
        R[i][i] = magn
        # print(magn)
        
        if (magn == 0):
            col = 0
        else:
            col = col / magn
        Q[0:, i] = col
    return (Q, R)

'''def QR (A):
 # Mengembalikan nilai eigen dari matrix m
 # Kamus Lokal
     # i, j: int
     # eigen : array
     # tempA : matrix
 # Algoritma
    for i in range(1000):
        A = mulmat(R(A),Q(A))
    for i in range(nbar(A)):
        for j in range(nkol(A)):
            A[i][i] = round(A[i][i], 20)
    length = nbar(A)
    eigen = []
    for i in range(length):
        tempA = copyMatrix(A)
        tempA[i][i] = 0
        if round(np.linalg.det(tempA))==0 and not(isInV(eigen, A[i][i])):
            eigen.append(A[i][i]) 
    return sort(eigen)'''

def tukarBaris (A, baris1, baris2):
# Menukar baris baris1 dan baris2 pada matriks A
# Kamus Lokal
    # m, n, temp: int
    # B : matrix
# Algoritma
    m = nkol(A)
    n = nbar(A)
    B = copyMatrix(A)
    for i in range(0,m):
        temp = B[baris1][i]
        B[baris1][i] = B[baris2][i]
        B[baris2][i] = temp
    return B

def tambahBaris (A, baris1, baris2, x):
# Menambahkan baris1 dengan baris2 yang telah dikalikan x
# Kamus Lokal
    # m, n: int
    # B : matrix
# Algoritma
    m = nkol(A)
    n = nbar(A)
    B = copyMatrix(A)
    for i in range(0, m):
        B[baris1][i] += B[baris2][i] * x
    return B

def kaliX (A, baris, x):
# Mengalikan setiap elemen pada baris baris dengan x
# Kamus Lokal
    # m, n: int
    # B : matrix
# Algoritma
    m = nkol(A)
    n = nbar(A)
    B = copyMatrix(A)
    for i in range(0, m):
        B[baris][i] *= x
    return B

def notZero(A, baris, kolom):
# Menemukan posisi terdekat dari baris dan kolom yang elemennya di A bukan 0
# Kamus Lokal
    # m, n, i, j: int
    # found : boolean
    # arrIDX : array
# Algoritma
    i = baris
    j = kolom
    found = False
    m = nkol(A)
    n = nbar(A)
    while (j<=m-1 and not(found)):
        while (i<=n-1 and not(found)):
            if (round(A[i][j],3)!=0):
                found = True
            else:
                i += 1
        if (not(found)):
            i = baris
        j += 1
    if (not(found)):
        i = -1
        j = 0
    arrIDX = [i, j-1]
    return arrIDX

def gauss (A):
# Melakukan metode Gauss pada matrix A
# Kamus Lokal
    # m, n, bar, kol: int
    # idxNotZero : array
    # B : matrix
# Algoritma

    bar = 0
    kol = 0
    idxNotZero = [-1,-1]
    B = copyMatrix(A)
    m = nkol(B)
    n = nbar(B)
    

    while (bar<=n-1 and kol<=m-1):
        idxNotZero = notZero(B, bar, kol)
        if idxNotZero[0] == -1:
            bar = n
        else:
            B = tukarBaris(B, bar, idxNotZero[0])
            kol = idxNotZero[1]
            for i in range(bar+1, n):
                if (B[i][kol] != 0):
                    B = tambahBaris(B, i, bar, (-1*B[i][kol]/B[bar][kol]))
            bar += 1
    
    bar = 0
    kol = 0
    
    while (bar<=n-1):
        done = False
        while (kol<=m-1 and not(done)):
            if (round(B[bar][kol],3)!=0):
                B = kaliX(B, bar, 1/B[bar][kol])
                done = True
            else :
                kol += 1
        bar += 1

    for i in range (0, n):
        for j in range (0, m):
            if (round(B[i][j],3)==0):
                B[i][j] = 0

    return B
            
def gaussJordan (A):
# Melakukan metode Gauss-Jordan pada matrix A
# Kamus Lokal
    # m, n, bar, kol, tempBar: int
    # idxNotZero : array
    # B : matrix
    # done: boolean
# Algoritma

    bar = 0
    kol = 0
    B = copyMatrix(A)
    B = gauss(B)
    m = nkol(B)
    n = nbar(B)

    while (bar<=n-1):
        done = False
        tempBar = 0
        while (kol<=m-1 and not(done)):
            if (round(B[bar][kol],3)==1):
                while (tempBar <= n-1):
                    if (round(B[tempBar][kol],3)!=0 and tempBar!=bar):
                        B = tambahBaris(B, tempBar, bar, (-1*B[tempBar][kol]/B[bar][kol]))
                    tempBar += 1
                if tempBar == n:
                    done = True
            kol += 1
        bar += 1

    return B

def isAllZero (A, bar, kol):
# Menentukan apakah elemen - elemen sebelah kanan A[bar][kol+1] nol semua
# Kamus Lokal
    # i: int
    # found : boolean
# Algoritma
    found = False
    i = kol + 1
    while (i<=nkol(A)-1 and not(found)):
        if (round(A[bar][i],3)!=0):
            found = True
        else:
            i += 1
    return not(found)

def getEigenVector(matrix, eigen):
# Inverse Power Method
    length = len(matrix)
    v = np.arange(length)
    np.random.shuffle(v)
    for i in range(15):
        vx = (matrix - np.identity(length) * eigen)
        if (np.linalg.det(vx) == 0):
            vx = (matrix - np.identity(length) * 0.000000001)
        v = np.dot(np.linalg.inv(vx), v)
        magn = np.linalg.norm(v)
        v = v / magn
    return v

def eigenVector (A, val):
# Mengembalikan eigen vector dari A dengan eigenvalue val
# Kamus Lokal
    # B: matrix
    # i, j, p: int
    # em : matrix
    # done: boolean
    # eV : array
# Algoritma
    B = matKaliX(A, -1)
    for i in range (nbar(B)):
        B[i][i] += val
    B = gaussJordan(B)
    
    i = 0

    em = [[-9999 for j in range (nkol(B))] for i in range (nbar(B))]
    
    while (i<=nbar(B)-1):
        j = 0
        done = False
        while (j<=nkol(B)-1 and not(done)):
            
            if (round(B[i][j],3)==1):
                if (isAllZero(B, i, j)):
                    for p in range (nkol(B)):
                        em[i][p] = 0
                    em[i][j] = 1
                else:
                    for p in range (0, j):
                        em[i][p] = 0
                    em[i][j] = 1
                    for p in range(j+1, nkol(B)):
                        em[i][p] = -1*B[i][p]
                done = True
            else:
                j += 1
        i += 1

    i = 0
    while (i<=nbar(B)-1):
        j = 0
        done = False
        while (j<=nkol(B)-1 and not(done)):
            if (round(em[i][j],3)==1 and i!=j):
                em = tukarBaris(em, i, j)
                done = True
            else:
                j += 1
        if not(done):
            i += 1

    eV = []

    i = 0
    while (i<=nbar(em)-1):
        if (isInvalid(em, i)):
            em[i][i] = 1
            eV.append(getCol(em, i))
        i += 1

    for i in range (nbar(eV)):
        for j in range(nkol(eV)):
            if (eV[i][j]==-9999):
                eV[i][j] = 0

    return eV


def filterZero(x):
# Mencegah 0 dan negatif (kalau negatif pasti mendekati 0)
# Mencegah akar negatif pada perhitungan nilai singular
    if x < 0.000001:
        return False
    return True

def eigen (A):
# Mengembalikan eigenvalue dan linearly independent eigenvector dari A
# Kamus Lokal
    # eigval : array
    # temp, eigvector : matrix
    # i: int
# Algoritma
    A = np.array(A)
    # eigVal = QR(A)
    eigVal = getEigenValues(A)
    eigVal = sorted(eigVal, reverse=True)
    for i in range(len(eigVal)):
        eigVal[i] = round(eigVal[i],3)
    eigVector = []
    for i in range (len(eigVal)):
        temp = eigenVector(A, eigVal[i])
        for j in range (len(temp)):
            eigVector.append(temp[j])
    return (eigVal, eigVector)

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

'''

Pemanggilan

tes = eigen(e)
tes[0] berisi eigen value terurut mengecil
tes[1] berisi basis eigen

'''
