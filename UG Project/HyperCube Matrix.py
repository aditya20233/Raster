arr=[]
key=[]

def hypercube(rows,cols):
    from scipy.stats import qmc
    sampler=qmc.LatinHypercube(d=cols)
    sample=sampler.random(n=rows)
    for x in sample:
        arr.append(x)
    

def getparams(aa,coln,rows) :
    a=list(aa)
    para = ""
    ul = ""
    ll = ""
    i = 0
    while(a[i]>='A' and a[i]<='Z') :
        para += a[i]
        i+=1

    key.append(para)
    while(a[i]<'0' or a[i]>'9') :
        i+=1

    while((a[i]>='0' and a[i]<='9') or a[i]=='.' or a[i]=='-') :
        ll += a[i]
        i+=1

    while(a[i]<'0' or a[i]>'9') :
        i+=1

    while((a[i]>='0' and a[i]<='9') or a[i]=='.') :
        ul += a[i]
        i+=1
    ll=float(ll)
    ul=float(ul)
    for r in range(0,rows):
        arr[r][coln]=ll+(ul-ll)*arr[r][coln]

def read():
    cnt = 0
    with open('parameters.txt','r+') as f:
        a=f.readline()
        while(a):
            if(a[0]>='A' and a[0]<='Z'):
                cnt+=1
            a=f.readline()

    #declareing 2d sample array
    rows = int(input())
    hypercube(rows,cnt)

    coln = 0
    with open('parameters.txt','r+') as f:
        a=f.readline()
        while(a):
            if(a[0]>='A' and a[0]<='Z'):
                getparams(a,coln,rows)
                coln+=1
            a=f.readline()

read()
# for i in range(0,10):
#     for j in range(0,10):
#         print(arr[i][j],end=" ")
#     print()