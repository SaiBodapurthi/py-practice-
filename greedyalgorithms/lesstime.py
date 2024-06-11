s_t=list(map(int,input().split()))
e_t=list(map(int,input().split()))
seq1=[]
seq2=[]
for i in range(0,len(s_t)):
    seq1.append(i)
for i in range(0,len(s_t)):
    for j in range(0,len(s_t)-1):
        if e_t[j]>e_t[j+1]:
            temp=seq1[j]
            seq1[j]=seq1[j+1]
            seq1[j+1]=temp
seq2.append(seq1[0])
x=seq2[0]
y=seq1[1]
for i in range(1,len(s_t)):
    if s_t[y]>=e_t[x]:
        seq2.append(seq1[i])
        x+=1
    y+=1
print(seq2)