def lead(rt,name):
    ind=0
    try:
        tx=open('reit.txt','r')
    except FileNotFoundError:
        tx=open('reit.txt','w')
        tx.write(str(rt)+" "+name+"\n")
        ind=1
    tx.close()
    tx=open('reit.txt','r')
    A=[]
    S=[]
    SR=[]
    for line in tx:
        nb=0
        s=""
        num=""
        while s!=" ":
            s=line[nb]
            if s!=" ":
                num=num+s
                nb=nb+1
        A.append(int(num))
        S.append(line)
    print(A)
    ttt=0
    B=[]
    j=0
    for i in A:
        if rt<i and ind==0:
            B.append(i)
            SR.append(S[j])
            j=j+1
        else:
            if ttt==0 and ind==0:
                B.append(rt)
                SR.append(str(rt)+" "+name+"\n")
                ttt=1
                B.append(i)
                SR.append(S[j])
                j=j+1
            else:
                B.append(i)
                SR.append(S[j])
                j=j+1
    if ttt==0 and ind==0:
        B.append(rt)
        SR.append(str(rt)+" "+name+"\n")
    print(B)
    print(S)
    print(SR)
    tx.close()
    tx=open('reit.txt','w')
    for i in SR:
        tx.write(i)