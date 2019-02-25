from math import *
from psm_plot import *

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    tmp = x - 2.0*exp(-x)

    return tmp

def main():
    a = 0.0         #define and a and b (bracketing values)
    b = 1.0
    if f(a)*f(b)<0:
        err_stop = 1e-5
        xns_old = 1
        rel_err=1.1*err_stop
        max_iter = 200
        for i in range(0,max_iter):
            xns = (a+b)/2
            if f(a)*f(xns) < 0:
                b = xns
            else:
                a = xns

            if i > 0:
                rel_err = abs((xns-xns_old)/xns)
                if rel_err <= err_stop:
                    break;
                xns_old=xns
            print("%3d %5.5f %.2e" % (i+1,xns,rel_err))

        print("%3d %5.5f %.2e" % (i + 1, xns, rel_err))

    else:
        print("Oops, your a and b values do not bracket the root")


if __name__ == '__main__':
    main()











