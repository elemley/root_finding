from math import *

def g(x):
    #f(x) = x**3-x-exp(x)-2
    tmp = ??              #ENGR 3703 fill in this line with the correct g(x) function
    return tmp

def main():
    xold = 2.0     #initial guess of x

    rel_err_stop = 1e-5     #adjust as needed...
    rel_err = 1.1*rel_err_stop  #set value large enough to start process
    max_iter = 50

    for i in range(0,max_iter):
        tmp = g(xold)
        xnew = tmp
        if i > 0:
            rel_err = abs((xnew - xold) / xnew)
            if rel_err < rel_err_stop:
                break
        xold = xnew
        print(i, xold, xnew, rel_err)


if __name__ == '__main__':
    main()



