import numpy as np
from matplotlib import pyplot as plt
from math import floor


def multiplicative_method(x0):
    a = 22695477
    b = 1
    m = pow(2, 32)
    x = (a * x0 + b) % m
    u = x / m
    return u, x


def generate_sequence(A, B, N, x0):
    vector = []
    for i in range(1, N):
        rnd, x0 = multiplicative_method(x0)
        vector.append((B - A) * rnd + A)
    return vector


def get_period(sequence):
    for i in range(0, len(sequence)):
        tmp = sequence[i]
        for j in range(i + 1, len(sequence)):
            if tmp == sequence[j]:
                return j - i
            else:
                return -1


def get_frequencies(sequence, a, b, m):
    s = (b - a) / m
    frequencies = [0] * m
    criterion_pearson = 0
    nj = 1 / m
    for j in range(0, len(sequence)):
        index = floor(sequence[j] / s)
        frequencies[index] += 1
    for i in range(0, len(frequencies)):
        frequencies[i] = frequencies[i] / (len(sequence) * s)
    for j in range(0, len(frequencies)):
        npj = frequencies[j]
        criterion_pearson += pow((nj - npj), 2) / npj
    return frequencies, criterion_pearson


if __name__ == '__main__':
    exp_nmb = [10 ** n for n in range(2, 6)]

    for exp in exp_nmb:
        seria = generate_sequence(0, 10, exp, 1)
        seria_no = exp_nmb.index(exp) + 1
        print(f'---SERIA_{seria_no}---')

        seria = np.array(seria)

        Mx = np.mean(seria)
        print(f'Mx{seria_no}: {Mx}')

        Dx = np.var(seria)
        print(f'Dx{seria_no}: {Dx}')

        period = get_period(seria)
        print(f'Period {seria_no}: {period}')

        frequency, pearson = get_frequencies(seria, 0, 10, 10)
        print(f'Frequency {seria_no}: {frequency}')
        print(f'Pearson criterion {seria_no}: {pearson}')

        parts = np.arange(0, 10, 1)
        plt.figure(figsize=(8, 8))

        plt.subplot(2, 2, seria_no)
        plt.bar(parts, frequency, color='blue', edgecolor='black')
        plt.title(f"frequency{seria_no}")

        plt.show()
