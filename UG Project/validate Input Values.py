dict={}

with open('parameters.txt','r+') as f:
    a=f.readline()
    while(a):
        a=list(a)
        if(a[0]>='A' and a[0]<='Z'):
            para = ""
            ul = ""
            ll = ""
            i = 0
            while((a[i]>='A' and a[i]<='Z') or a[i]=='_' or (a[i]>='0' and a[i]<='9')):    #Baaki ki hru files me ye bali condition daalni he
                para += a[i]
                i+=1

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
            dict[para]=[ll,ul]
        a=f.readline()

#####################################################################

from os import listdir
from os.path import isfile, join

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def edit_hru(fileName,key,value):
    # fileName='000010000.sub'
    # key='WGNFILE'
    # value='12345678'
    # print(fileName,key,value)
    c=0
    with open(fileName,'r+') as f:
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
                print(prev)
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

def get():
    key = input()
    value = float(input())
    flag=0
    for x, y in dict.items():
        if(x==key):
            flag=1
            ll=dict[x][0]
            ul=dict[x][1]
            if(value<ll or value>ul):
                print("Enter Valid value")
                return
    if flag==0:
        print("Enter valid Key")
        return
    mypath="./"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for x in onlyfiles:
        if x.find('.py') == -1 :
            edit_hru(x,key,value)

get()