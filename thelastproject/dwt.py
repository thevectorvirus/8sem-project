import pywt
cA, cD = pywt.dwt([1, 0, 0, 1], 'db1')
print (cA)
print (cD)