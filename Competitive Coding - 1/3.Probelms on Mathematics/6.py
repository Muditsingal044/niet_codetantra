import sys

d1 = int(sys.argv[1])
d2 = int(sys.argv[2])
c = int(sys.argv[3])
L = int(sys.argv[4])

def isDivisibleBy41(d1, d2, c, L):
  d = [d1,d2]+[0]*(L-2)
  for i in range(2,L):
    d[i] = (d[i-1]*c + d[i-2])%10
  
  num = 0
  for i in range(L):
    num+=d[i]*10**(L-i-1)
  
  return num%41==0
  
print("true" if isDivisibleBy41(d1, d2, c, L) else "false")
