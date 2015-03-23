# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Ravi Chhawal"
__date__ = "$Mar 20, 2015 2:29:40 PM$"

def idea():
    file_r = 'F:\\Ravi Work\\Raid Case\\idea\\idea.csv'
    read_f = open(file_r, 'r')
    out_w=open('F:\\Ravi Work\\Raid Case\\idea\\out.txt','w')
    line=read_f.readline()
    count=0
    out_w.write('IDEA_NO|'+line)
    line=read_f.readline()
    while line :
        count+=1
        data=line.split('|')
        #print (line.strip('\n'))
        if len(data)>8 :
            if data[6]=='MO':
                temp=data[0]
                out_w.write(temp+'|'+line)
            if data[6]=='MT':
                temp=data[1]
                out_w.write(temp+'|'+line)                        
        line=read_f.readline()
        
        if count%100000==0 :
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
            
if __name__ == "__main__":
    print ("Hello World")
    
