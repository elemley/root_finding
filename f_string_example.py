from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    fn_string = "pow(x,3)-x-exp(x)-1+y"
    #fn_string = "-0.3*x**3"
    return fn_string

def f(x,y):
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    x = 1.0
    y = -0.5
    print(f(x,y))
    print("x=", x)
    print("y=", y)
    print("f(x,y)=", f_string(),"=",f(x,y))

if __name__ == '__main__':
    main()















