# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Ravi Chhawal"
__date__ = "$Mar 20, 2015 2:29:40 PM$"

from CDR_Result import *

def idea():
    file_r = 'F:\\Ravi Work\\Raid Case\\idea\\idea.csv'
    read_f = open(file_r, 'r')
    out_w = open('F:\\Ravi Work\\Raid Case\\idea\\out.txt', 'w')
    line = read_f.readline()
    count = 0
    out_w.write('IDEA_NO|' + line)
    line = read_f.readline()
    while line:
        count += 1
        data = line.split('|')
        #print (line.strip('\n'))
        if len(data) > 8:
            if data[6] == 'MO':
                temp = data[0]
                out_w.write(temp + '|' + line)
            if data[6] == 'MT':
                temp = data[1]
                out_w.write(temp + '|' + line)                        
        line = read_f.readline()
        
        if count % 100000 == 0:
            print (count)        

def BSNL():
    file_r = 'F:\\Ravi Work\\Raid Case\\BSNL\\BSNL.txt'
    read_f = open(file_r, 'r')
    out_w = open('F:\\Ravi Work\\Raid Case\\BSNL\\out.txt', 'w')
    line = read_f.readline()
    count = 0
    out_w.write('BSNL_NO|' + line)
    line = read_f.readline()
    while line:
        count += 1
        data = line.split('|')
        #print (line.strip('\n'))
        if len(data) > 8:
            if data[7] == 'MOC':
                temp = data[0]
                out_w.write(temp + '|' + line)
            if data[7] == 'MTC':
                temp = data[1]
                out_w.write(temp + '|' + line)                        
        line = read_f.readline()
        
        if count % 100000 == 0:
            print (count)       
            
def see_sample(file_name):
    reader = open(file_name, 'r')
    line = reader.readline()
    count = 0
    data = line.split('|')
    for i in range(0, len(data)):
        print (i, data[i])
    while line:
        count += 1
        print (line.strip('\n'))                
        line = reader.readline() 
        if count > 10:
            break 

def search_key(k):
    key = k.split('|')
    print ('hhhh')
    file_r = 'F:\\Ravi Work\\Raid Case\\TTSL\\search.txt'
    file_w = 'F:\\Ravi Work\\Raid Case\\TTSL\\record_v2.txt'
    reader = open(file_r, 'r')
    writer = open(file_w, 'w')
    line = reader.readline()
    writer.write(line)
    count = 0
    while line:
        count += 1
        data = line.split('|')
        for s in key:
            if s == data[0]:
                writer.write(line)
                print ('Found', count)
        line = reader.readline()
        if count % 100000 == 0:
            print (count)

if __name__ == "__main__":
    print ("Hello World")
    #see_sample('F:\\Ravi Work\\Raid Case\\TTSL\\ravi.txt')
    #bsnl_result()
    key = '9214434210|9214434215|9214434217'
    search_key(key)
    #BSNL()
