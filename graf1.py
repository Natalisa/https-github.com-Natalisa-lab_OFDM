import matplotlib.pyplot as plt
import lab1
N=512
BER=[]
# QPSK,tmp=lab1.fun(512,15)
# x=[]
# y=[]
# for i in range(0, len(QPSK)):
#     if QPSK[i].imag < 0:
#         y.append(QPSK[i].imag)
#     else:
#         y.append(QPSK[i].imag)
#     if QPSK[i].real < 0:
#         x.append(QPSK[i].real)
#     else:
#         x.append(QPSK[i].real)
# #print (x,y)
# plt.plot(x,y,color='white',marker='.',markerfacecolor ='blue')
# plt.axis([-1,1,-1,1])
# plt.grid(True)
# plt.show()
x=[]
y=[]
for i in range(-5,26):
    x.append(i)
    QPSK2,tmp=lab1.fun(N,i)
    BER.append(tmp)
    y.append(tmp/N)
plt.plot(x, y)
plt.ylim([0,1])
plt.grid(True)
print (BER)
plt.show()
