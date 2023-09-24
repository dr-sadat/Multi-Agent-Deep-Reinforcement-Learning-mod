import math

with open('snr.txt') as f:
    data = [float(line.rstrip()) for line in f]

print('Average SNR =', sum(data)/len(data))
