import pywt
coef = pywt.wavedec([1, 2, 3, 4], 'db1', level=2)
cA, cD, cE = coef
print (cA)
print (cD)
print (cE)