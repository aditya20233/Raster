from os import listdir
from os.path import isfile, join
from traceback import print_tb

arr=[]
key=[]
rows = int(1)
best_val = int(0) #todo
flag = int(0) #got better best value

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

#############################################################################################################
all_set={".pnd",".rte",".sub",".swq",".wgn",".wus",".chm",".gw",".hru",".mgt",".sdr",".sep",".sol"}


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def edit_hru(fileName,key,value,factor):
    # fileName='000010000.sub'
    # key='WGNFILE'
    # value='12345678'
    # print(fileName,key,value)
    c=0
    with open(fileName,'r+') as f:
        # print(fileName)
        a = f.readline()
        while(a) :
            c+=1
            p=a.split('|')
            if(len(p)==1) :
                a = f.readline()
                continue
            idx = a.find('|')
            # p = idx - 5
            # num=""
            title = ""
            # while(a[p]!=' ') :
            #     num += a[p]
            #     p = p-1
            # num = num[::-1]
            p = idx + 1
            while(a[p]==' ') :
                p = p + 1
            while(a[p]!=' ' and a[p]!=':') :
                title += a[p]
                p = p+1
            if title == key :
                aa=list(a)
                p = idx - 5
                de=p
                prev=""
                while(aa[de]!=' '):
                    prev+=aa[de]
                    de-=1
                prev=prev[::-1]
                final_val=float(value)
                prev_val= float(prev)
                if(factor=='R'):
                    final_val=(1+final_val)*prev_val
                elif(factor=='A'):
                    final_val=final_val+prev_val
                final_val=round(final_val,6)
                value=str(final_val)
                value = value[::-1]       
                i = 0
                while(i != len(value)) :
                    aa[p] = value[i]
                    p = p-1   
                    i = i+1       
                while(aa[p]!=' ') :
                    aa[p] = ' '
                    p = p - 1  
                pp=''.join(aa)
                replace_line(fileName,c-1,pp)
            # print(f"key - {title} | value - {num}")
            a = f.readline()

def get(key,value,factor):
    # print(key,value,factor)
    mypath="./"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for x in onlyfiles:
        flag = 0
        for ext in all_set :
            if(x.find(ext)!=-1) :
                flag = 1
                break
        if flag :
            edit_hru(x,key,value,factor)

def input():
    for i in range (rows) :
         best_iter = 0
         for j in range(len(key)):
             get(key[j],arr[i][j],'V')
        #  if flag :
        #      best_iter = i
        #      flag = 0

input()
