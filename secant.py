from math import *
import numpy as np
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    #fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    #fn_string = "pow(x,3)-x-exp(x)-2"
    fn_string = "x-2*exp(-x)"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    x1 = 0.0     #left side of bracketing values for root
    x2 = 1.0     #right side of bracketing values for root
    x_start = 0.0
    x_end = 10.0
    root_approx = [x1,x2]

    rel_err_stop = 1e-5     #adjust as needed...
    rel_err = 1.1*rel_err_stop  #set value large enough to start process
    count = 0
    max_iter = 1000

    while rel_err > rel_err_stop and count < max_iter:
        count+=1
        x3 = x2-(f(x2)*(x1-x2)/(f(x1)-f(x2)))
        root_approx.append(x3)
        if count > 1:
            rel_err = abs((x3-x2)/x3)

        x1=x2
        x2=x3
    print(count)
    print(rel_err)
    print(root_approx)
    print(x3)


if __name__ == '__main__':
    main()

