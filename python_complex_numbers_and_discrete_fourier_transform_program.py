import math

class Complex():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def magnitude(self):
        magnitude = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return magnitude

    def orientation(self):
        orientation = math.atan(self.imaginary / self.real)
        return orientation

x = Complex(3, 4)
print(x.magnitude())
print(x.orientation())

x = [2, 2, 2, 2, 2, 2, 2, 2, 2]
dft = []
N = 8
for k in range(9):
    a = 0
    b = 0
    for n in range(9):
        a = a + x[n] * math.cos((2 * 3.14 * n * k) / N)

        b = b + (-x[n] * math.sin((2 * 3.14 * n * k) / N))

    dft.append((a, b))

dft
dft_ = []

for i in range(9):
    c = Complex(dft[i][0], dft[i][1])
    dft_magn = c.magnitude()
    dft_spectra = c.orientation()
    dft_.append((dft_magn, dft_spectra))

dft_

