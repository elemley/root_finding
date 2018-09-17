from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    fn_string = "pow(x,3)-x-exp(x)-2"
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

    x_list = [] #initialize lists with no elements
    f_list = []
    #write a loop to fill the lists
    a = 1.0
    b = 4.0
    dx = 0.25
    N = (int)((b-a)/dx)+1
    for i in range(0,N):
        x = i*dx + a
        x_list.append(x)
        f_list.append(f(x))

    x_list.insert(0,3.0)
    x_list.pop(0)
    x_list.reverse()

    print(x_list)
    print(f_list)












if __name__ == '__main__':
    main()















