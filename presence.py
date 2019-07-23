n,o=map(int,input().split())
n=str(n)
c=0
for i in range(0,o+1):
    if str(i) not in n:
        c=1
        break
if(c==1):
    print("no")
else:
    print("yes")

          
        
    
