from math import *

def f(x):
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
            #Find which quarter the root is in
            deltax = b - a
            x1 = a + 0.25*deltax
            x2 = a + 0.5*deltax
            x3 = a + 0.75*deltax
            if f(a)*f(x1)<0:
                x_left = a
                x_right = x1
            elif f(x1)*f(x2)<0:
                x_left = x1
                x_right = x2
            elif f(x2)*f(x3)<0:
                x_left = x2
                x_right = x3
            else:
                x_left = x3
                x_right = b
            xns = (x_left+x_right)/2
            #ENGR 3703 Choose the correct line of code for this line
                a = xns
                b = x_right
            else:
                b = xns
                a = x_left
            if i > 0:
                rel_err = abs((xns-xns_old)/xns)
                if rel_err <= err_stop:
                    break;
                xns_old=xns
        print(i,xns, rel_err)

    else:
        print("Oops, your a and b values do not bracket the root")


if __name__ == '__main__':
    main()

















