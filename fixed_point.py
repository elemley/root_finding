from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    #fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    fn_string = "5/(exp(0.5*x)+1.2)"
    return fn_string

def g(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    xold = 2.0     #initial guess of x
    root_approx = [xold]

    rel_err_stop = 1e-5     #adjust as needed...
    rel_err = 1.1*rel_err_stop  #set value large enough to start process
    count = 0
    max_iter = 5

    while rel_err > rel_err_stop and count < max_iter:
        count+=1
        tmp = g(xold)
        xnew = tmp
        root_approx.append(xnew)
        if count > 1:
            rel_err = abs((xnew-xold)/xnew)
        xold=xnew
        print(count, xold, xnew,rel_err)
    #print(rel_err)
    #print(root_approx)
    #print(xnew)


if __name__ == '__main__':
    main()



