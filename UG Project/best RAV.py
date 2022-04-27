from os import listdir
from os.path import isfile, join
from traceback import print_tb

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
     with open('best_par.txt','r+') as f:
         a = f.readline()
         while(a):
             if a.find(':')!=-1:
                 c=a.find(':')
                 c+=1
                 p=c
                 c+=3
                 key=""
                 while a[c]!='.' and a[c]!='(':
                     key+=a[c]
                     c+=1
                #  print(key)
                 fitted_val = ""
                 while(a[c]<'0' or a[c]>'9') :
                     c+=1
                 while(a[c]!=' '):
                     fitted_val += a[c]
                     c+=1
                #  print(fitted_val)
                #  if(a[p]=='V'):
                 get(key,fitted_val,a[p])
             a=f.readline()

input()
