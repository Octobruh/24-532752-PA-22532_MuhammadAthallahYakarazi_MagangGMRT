# M Athallah Y

import math as mt
import numpy as np
import matplotlib.pyplot as plt

def tMatMult (Mat1, Mat2):
    return np.dot(Mat1, Mat2)

def make_A(th, l):
    #3x3 homogeneous transform A = R(th) * T(l), calculation in the pdf
    return np.array([
        [mt.cos(th), -mt.sin(th), l * mt.cos(th)],
        [mt.sin(th),  mt.cos(th), l * mt.sin(th)],
        [0, 0, 1]
    ])

def make_plot(A_res):
    fig = plt.figure()
    ax = fig.add_subplot(111)
   
    xPoints = np.array([0, A_res[0][2]])
    yPoints = np.array([0, A_res[1][2]])

    plt.plot(xPoints, yPoints)
    ax.plot(xPoints, yPoints)
    
    for xy in zip(xPoints, yPoints):                                      
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

    plt.title("Position vector of final coordinate")
    plt.show()
    
# ------------- main() --------------
DOF = int(input("DOF: "))

l = list(map(float, input("l: ").split()))
th_deg = list(map(float, input("th (deg): ").split()))
th_rad = [mt.radians(th) for th in th_deg]

# Build list of matrices 
A = []

for th, l in zip(th_rad, l):
    A.append(make_A(th, l))
    
A_res = A[0]
for i in range(1, len(A)):
    A_res = tMatMult(A_res, A[i])

print("Final Mat =")
print(A_res)
make_plot(A_res)