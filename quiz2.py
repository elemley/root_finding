from math import *

def main():
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    y = [0.1, 0.08023, 0.02016, -0.08351, -0.23408, -0.43125, -0.66752, -0.92459, -1.16976, -1.35233, -1.4]

    #Note x and y are known to be the same length
    sumx = 0.0
    for i in range(0,len(x)):
        sumx+=x[i]
    xmean = sumx / len(x)

    summ = 0.0

    for i in range(0,len(x)):
        #What code goes here

    rms = sqrt(summ)


if __name__ == '__main__':
    main()











