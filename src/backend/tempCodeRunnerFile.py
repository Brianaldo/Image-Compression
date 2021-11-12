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