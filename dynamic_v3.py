import math as m
import numpy as np
import matplotlib.pyplot as plt
#位移
x_1=[]
x_2=[]
x_3=[]
#速度:u_1,u_2,u_3
#加速度:a_1,a_2,a_3
#物块受力，向右为正:f_1,f_2,f_3
#弹簧力，拉伸为正:F_k1,F_k2

start=float(input("开始时间:"))
stop=float(input("结束时间:"))
dt = 0.01
num = int((stop-start) / dt + 1)
tx = np.linspace(start,stop,num)
dt = (stop-start) / (num - 1)

for t in tx:
    if t == 0:
        u1 = 3
        u2 = 0
        u3 = 0
        x1 = 0
        x2 = 5
        x3 = 10
        x_1.append(x1)
        x_2.append(x2)
        x_3.append(x3)
    elif t != 0:
        Fk1 = (x2 - x1 - 5) * 10
        Fk2 = (x3 - x2 - 5) * 10
        f1 = Fk1
        f2 = -Fk1 + Fk2
        f3 = -Fk2
        a1 = f1 / 1
        a2 = f2 / 2
        a3 = f3 / 3
        u1 = a1 * dt + u1
        u2 = a2 * dt + u2
        u3 = a3 * dt + u3
        x1 = x1 + u1 * dt
        x2 = x2 + u2 * dt
        x3 = x3 + u3 * dt
        x_1.append(x1)
        x_2.append(x2)
        x_3.append(x3)

plt.plot(tx,x_1,color="green")
plt.plot(tx,x_2,color="red")
plt.plot(tx,x_3,color="blue")

plt.title("dynamic")
plt.xlabel("time")
plt.ylabel("displacement")
plt.show()