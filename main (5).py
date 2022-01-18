cnt=0
num = int(input()) 
check = num
 
while True:
    ten=num//10      
    one=num%10      
    sum=ten+one     
    a=one*10         
    b=sum%10           
    result=a+b        
    cnt+=1 
    num = result
    if result==check:
        break
print(cnt)