#3角形上のランダムウォーク
import sympy as sym
import matplotlib.pyplot as plt
from sympy import*
import numpy as np
from matplotlib.animation import FuncAnimation

#animationのやり方が自分のteratailにある。

#定数の定義（1stepのとき）
N = 1
P = 0
Q = sym.Rational(1, 6)
R = 0
#自分で持ってきた変数の定義
p,q,r,Pn,Qn,Rn=symbols("p,q,r,Pn,Qn,Rn")
#n回目のそれぞれの確率
Pn = sym.Rational(3, 2)*q
Qn = p/6 + q/2 + r/2
Rn = q/2

while N<15:
    N +=1
    Pstep = Pn.subs([(q, Q)]) #qにQを代入
    Qstep = Qn.subs([(p,P),(q,Q),(r,R)])
    Rstep = Rn.subs([(q, Q)])
    P=Pstep
    Q=Qstep
    R=Rstep

    plt.plot(N,P,"-ro",label="P")
    plt.plot(N,Q,"-o", label="Q")
    plt.plot(N,R,"-*", label="R")
    plt.xlabel("step")
    plt.ylabel("probability")
    #plt.pause(1) #1秒ずつ、リアルタイムプロット
plt.title('random-walk on  a triangle(15step)')
plt.show()
