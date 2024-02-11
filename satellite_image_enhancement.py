import numpy as np
from PIL import Image as img
import matplotlib.pyplot as plt
import pywt
import pywt.data
# Load image
original = img.open('./2.jpg')
# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail', 'Combined']
coeffs2 = pywt.dwt2(original, 'bior3.1')
LL, (LH, HL, HH) = coeffs2
comb = []
for i in range(0, len(LL)):
    comb.append([])
    for j in range(0, len(LL[0])):
        ll = LL[i][j]
        lh = LH[i][j]
        hl = HL[i][j]
        hh = HH[i][j]
        comb[i].append((lh + hl + hh) / 4)
fig = plt.figure(figsize=(12, 2))
for i, a in enumerate([LL, LH, HL, HH, comb]):
    ax = fig.add_subplot(1, 5, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
plt.show()