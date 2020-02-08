from math import *

def f(x):
    tmp = x - 2.0*exp(-x)
    return tmp

def main():
    err_stop = 1e-5
    xns_old = 1
    rel_err = 1.1 * err_stop
    max_iter = 200
    for i in range(0, max_iter):
        rel_err = abs((xns-xns_old)/xns)
        if rel_err <= err_stop:
            break;
        xns_old=xns
    print(i,xns, rel_err)




if __name__ == '__main__':
    main()

















