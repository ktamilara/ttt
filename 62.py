v1=int(input())
h1=0
for i in range(1,v1+1):
    if v1%i==0 and (v1/i)%2!=0:
        print(i)
        break
