from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    fn_string = "pow(x,3)-x-exp(x)-1"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

#Below is a function definition
def main():
    print(f(1.0))
    print(f_string())








if __name__ == '__main__':
    main()















