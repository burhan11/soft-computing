import copy

def heuristic(l,g):
   h=0
   for i in range(len(l)):
     for j in range(len(l[i])):
       if(l[i][j]!=g[i][j]):
         h+=1
   return h-1
def least(open,go,g):
  min=999999999999
  s=[]
  for i in open:
    if((heuristic(i,g)+go[repr(i)])<min):
        min=heuristic(i,g)+go[repr(i)]
        s=i
  return s
def zero(l):
   for m in range(len(l)):
      for n in range(len(l[m])):
       
       if(k[m][n]==0):
         return m,n
def dist(a,b):
 count=0
 for i in range(len(a)):
   for j in range(len(a[i])):
     if(a[i][j]!=b[i][j]):
       count+=1
 return count-1
def traverse(l,k,parent):
   p=parent[repr(k)]
   while(parent[p]!='0'):
        
        print(p)
        p=parent[repr(p)]

def check(k,succ,g,go,closed):
  flag1=0
  flag2=0
  if(heuristic(k,g)+go[repr(k)]>heuristic(succ,g)+go[repr(succ)]):
    flag1=1
  for i in closed:
    if(heuristic(i,g)+go[repr(i)]<heuristic(succ,g)+go[repr(succ)]):
       flag2=1
       break
  if(flag1==1 and flag2!=1):
    return True
  else:
    return False
l=[[8,1,3],[4,0,7],[2,6,5]]
g=[[8,1,3],[4,7,5],[2,6,0]]

open=[]
closed=[]
open.append(l)
parent={}
parent[repr(l)]='0'
go={}
go[repr(l)]=0
while(len(open)!=0):
     for i in closed:
       if(i in open):

        open.remove(i)
     k=least(open,go,g)
     print(k)
     
     if(k==g):
        traverse(closed,k,parent)
        break   
  
          
           
         
     #closed.append(k)
     #open.remove(k)
     
     m,n=zero(k)
     succ=copy.deepcopy(k)
     
     
     if((m==0 and n==0)):
          temp=succ[m][n]
          succ[m][n]=succ[1][0]
          succ[1][0]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
         
          

          
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[0][1]
          succ[0][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
        
     elif(m==0 and n==2):
          
          temp=succ[m][n]
          succ[m][n]=succ[0][1]
          succ[0][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
          
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[1][2]
          succ[1][2]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
           
     elif(m==2 and n==0):
          temp=succ[m][n]
          succ[m][n]=succ[1][0]
          succ[1][0]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[2][1]
          succ[2][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          
     elif(m==2 and n==2):
          temp=succ[m][n]
          succ[m][n]=succ[1][2]
          succ[1][2]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[2][1]
          succ[2][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
         
     elif(m==0 and n==1 ):
          temp=succ[m][n]
          succ[m][n]=succ[1][1]
          succ[1][1]=temp
          temp=0
          open.append(succ)
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[0][0]
          succ[0][0]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[0][2]
          succ[0][2]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          
     elif(m==1 and n==0):
          
          temp=succ[m][n]
          succ[m][n]=succ[0][0]
          succ[0][0]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[1][1]
          succ[1][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[2][0]
          succ[2][0]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          
     elif(m==2 and n==1):
          
          temp=succ[m][n]
          succ[m][n]=succ[1][1]
          succ[1][1]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[2][2]
          succ[2][2]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[2][0]
          succ[2][0]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
     elif(m==1 and n==2 ):
          temp=succ[m][n]
          succ[m][n]=succ[2][2]
          succ[2][2]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[1][1]
          succ[1][1]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)        
          succ=copy.deepcopy(k)
          temp=succ[m][n]
          succ[m][n]=succ[0][2]
          succ[0][2]=temp
          temp=0
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
        
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)          
     else:
          
          temp=succ[m][n]
          
          succ[m][n]=succ[0][1]
         
          succ[0][1]=temp
          
          
          
          
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
          succ=copy.deepcopy(k)
          
          temp=succ[m][n]
          succ[m][n]=succ[2][1]
          succ[2][1]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
          succ=copy.deepcopy(k)
          
          temp=succ[m][n]
          succ[m][n]=succ[1][0]
          succ[1][0]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
          
          succ=copy.deepcopy(k)
          
          temp=succ[m][n]
          succ[m][n]=succ[1][2]
          succ[1][2]=temp
          temp=0
          go[repr(succ)]=go[repr(k)]+dist(k,succ)
          parent[repr(succ)]=repr(k)
          if(check(k,succ,g,go,closed)==True):
            open.append(succ)
        
          open.remove(k)
          closed.append(k)



        
        
         
           
