from math import *
from psm_plot import *

#Note this is specified def f_string():
##You can choose not to use this... Just delete it in that case

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    tmp = x - 2.0*exp(-x)
    return tmp

def main():
    a = 0.0         #define and a and b (bracketing values)
    b = 1.0
    err_stop = 1e-5
    if f(a)*f(b)< 0:
        rel_err = 1.1*err_stop
        max_iter = 200
        xns_old = (a+b)/2
        for i in range(0,max_iter):
            xns = (a+b)/2
            #put code here to decide if f(a)*f(xns) is < 0
                #if < 0 what do you do (look at notes)

            #if NOT < 0 do what is in the notes here

            if i >0:
                #calc rel_err here and compare to err_stop
                #if rel_err is less than rel_err stop the loop now

                #if it's not put find a new xns (don't forget to store the old value in'
                #xns_old










    else:
        print("Your a and b values do not bracket the root")





if __name__ == '__main__':
    main()











