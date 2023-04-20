import pywt
import matplotlib.pyplot as plt
import numpy as np

ts = [1,2,3,4,5,6,7,8,9]

(ca, cd) = pywt.dwt(ts,'haar')

cat = pywt.threshold(ca, np.std(ca)/2, mode='soft')
cdt = pywt.threshold(cd, np.std(cd)/2, mode='soft')

ts_rec = pywt.idwt(cat, cdt, 'haar')

plt.close('all')

plt.subplot(211)
# Original coefficients
plt.plot(ca, '--*b')
plt.plot(cd, '--*r')
# Thresholded coefficients
plt.plot(cat, '--*c')
plt.plot(cdt, '--*m')
plt.legend(['ca','cd','ca_thresh', 'cd_thresh'], loc=0)
plt.grid('on')

plt.subplot(212)
plt.plot(ts)
# plt.hold('on')
plt.plot(ts_rec, 'r')
plt.legend(['original signal', 'reconstructed signal'])
plt.grid('on')
plt.show()