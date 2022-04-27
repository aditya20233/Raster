# function for data change
# filename , key , value 
#LAT_TTIME

from os import listdir
from os.path import isfile, join

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def edit_hru(factor,fileName,key,value):
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
                pok=p
                ival=""
                while aa[pok]!=' ':
                    ival+=aa[pok]
                    pok-=1
                ival=ival[::-1]
                if(factor=='R'):
                    value=(1+float(value))*(float(ival))
                elif(factor=='V'):
                    value=float(value)+float(ival)
                value=str(value)  
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
    value = input()
    factor=input()
    mypath="./"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for x in onlyfiles:
        if x.find('.py') == -1 :
            edit_hru(factor,x,key,value)
get()
