import sys

a,b = map(int, sys.stdin.readline().split())
lenA=len(str(a))  #첫번째 수 자릿수
lenB=len(str(b))  #두번째 수 자릿수
aList=[]
bList=[]
n=1
hap=0
for i in range(0,lenA):
  aDigit1=int(pow(10,n))
  aDigit2=int(pow(10,n-1))
  aList.append((a%aDigit1-a%aDigit2)//pow(10,n-1))     
  n+=1

n=1

for j in range(0,lenB):
  bDigit1=int(pow(10,n))
  bDigit2=int(pow(10,n-1))
  bList.append((b%bDigit1-b%bDigit2)//pow(10,n-1))     
  n+=1

for i in range(lenA):
  for j in range(lenB):
    
    hap+=aList[i]*bList[j]
    
   
print(hap)  



#   a1=lenA-(lenA-1)
#   for j in lenB:
#     b1=lenB-1
#     a%pow(10,a1)

