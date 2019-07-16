H1,K1=map(int,input().split())
v1=list(map(int,input().split()))
for i in range(0,H1-1):
    for j in range(i+1,H1):
        if (v1[i]+v1[j])==K1:
            print("yes")
            sys.exit()
print("no")
