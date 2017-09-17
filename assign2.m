#Scalar variables

a=10
b=b=2.5*10^23
c=2+3i
d=exp(j*2*pi/3)

#Vector variables

aVec=[3.14 15 9 26]
bVec=[2.71;8;28;182]
cVec=[5:-0.5:-5]
dVec=logspace(10^0,10^1,100)
eVec="Hello"

#Matrix Variables

aMat=2*ones(9,9)
v=[1 2 3 4 5 4 3 2 1];
bMat=diag(v)
l=[1:100];
cMat=reshape(l,10,10)
dMat=nan(3,4)
eMat=[13 -1 5; -22 10 -87]
fMat=floor(-3+rand(5,3)*(6))
fMat=ceil(-3+rand(5,3)*(6))

#Scalar Equations

x=1/(1+exp(-1*(a-15)/16))
y=(sqrt(a)+b^(1/21))^pi
z=log(real((c+d)*(c-d))*sin(a*pi/3))/(c*conj(c))

#Vector Equations

xVec=1/(sqrt(2*pi*2.5*2.5))*exp(-cVec.*cVec/(2*2.5*2.5))
yVec=sqrt(transpose(aVec).*transpose(aVec)+bVec.*bVec)
zVec=log10(1./dVec)



#Matrix Equations

yMat=bVec*aVec
zMat=det(cMat)*transpose(aMat*bMat)
Csum=sum(cMat,1)
eMean=mean(eMat,1)
eMat(1,:)=[1 1 1]
cSub=cMat(2:9,2:9)
lin=[1:20];
lin(2:2:end)=-1*lin(2:2:end)
r=rand(1,5);
find(r<0.5)
