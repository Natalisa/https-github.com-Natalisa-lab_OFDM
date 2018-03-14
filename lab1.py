import random
import cmath
def OFDM(t,N,QPSK):
    sum=0
    for k in range(0,int(N/2)):
        sum+=QPSK[k]*cmath.exp(-1j*t*((2*cmath.pi*k)/(N/2)))
    return sum

#генерация шумов в радиоканале
def Signal_Plus_Noise(t,N,QPSK,sigma):
    part1=OFDM(t,N,QPSK)
    rnd = 0
    while(rnd==0):
        rnd=random.random()
    part2=sigma*cmath.cos(2*cmath.pi*random.randint(0,1)*cmath.sqrt(-2*cmath.log(rnd)))
    rnd = 0
    while (rnd == 0):
        rnd = random.random()
    part3=1j*sigma*cmath.cos(2*cmath.pi*random.randint(0,1)*cmath.sqrt(-2*cmath.log(rnd)))
    return part1+part2+part3

#подсчет количества ошибок(исходный массив, полученный массив)
def BER(mas,mas2):
    count=0
    for i in range(0,len(mas)):
        if(mas[i]!=mas2[i]):
            count=count+1
    return count

def demodulation(QPSK):
    tmp=[]
    for i in range(0,int(len(QPSK))):
        if QPSK[i].imag<0:
            tmp.append(1)
        else:
            tmp.append(0)
        if QPSK[i].real<0:
            tmp.append(1)
        else:
            tmp.append(0)
    return tmp

#основная функция(число битов данных, отнощение сигнала к шуму)
def fun(N,SNR):
    print(SNR)
    mas=[]
    #масив нулей и едениц
    for i in range(0,N):
        mas.append(random.randint(0,1))
    #print(mas)

    #Формирование QPSK-символов
    QPSK=[]
    for i in range(0,int(N),2):
        if mas[i]==0 and mas[i+1]==0:
            QPSK.append(complex(1,1))
        if mas[i]==0 and mas[i+1]==1:
            QPSK.append(complex(-1,1))
        if mas[i]==1 and mas[i+1]==1:
            QPSK.append(complex(-1,-1))
        if mas[i]==1 and mas[i+1]==0:
            QPSK.append(complex(1,-1))

    sigma=(cmath.sqrt(1/(cmath.log(4,2)*2*pow(10,0.1*SNR)))).real

   # print(sigma)
    #Формирование QPSK символов с шумом
    QPSK_Noisy=[]
    for i in range(0,int(N/2)):
        sum=0
        for k in range(0,int(N/2)):
            sum+=Signal_Plus_Noise(i,N,QPSK,sigma)*cmath.exp(1j*i*((2*cmath.pi*k)/(N/2)))
        QPSK_Noisy.append((1/(N/2))*sum)
    #демодуляция QPSK-сигнала
    mas2=[]
    mas2=demodulation(QPSK_Noisy)

    #print(mas2)
    return (QPSK_Noisy,BER(mas,mas2))

