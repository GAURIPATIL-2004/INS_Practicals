P=int(input("Enter value of P ="))
Q=int(input("Enter value of Q ="))
e=int(input("Enter value of e ="))
n=P*Q

print("n= ",n)

i=1
M=int(input("Enter value of M ="))
de=0
d=0
phi_n=(P-1)*(Q-1)
print("Phi of n =",phi_n)
while True :
     if ((phi_n*i)+1)%e==0:
         print("True",i,"d*e=",((phi_n*i)+1),"d=",(phi_n*i+1)/e)
         de=((phi_n*i)+1)
         d=(phi_n*i+1)/e
         break
     else:
         i+=1
         print("False")

if de%phi_n==1:
    C=(M**e)%n
    print("Cipher Text =",C)
    M=(C**int(d))%n
    print("M = ",M)
