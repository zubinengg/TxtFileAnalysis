# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "R.N. Saini"
__date__ = "$Mar 23, 2015 10:27:41 AM$"

def bsnl_result():
    file_r = 'F:\\Ravi Work\\Raid Case\\BSNL\\ravi.txt'
    out_w = 'F:\\Ravi Work\\Raid Case\\BSNL\\Details.txt'
    reader = open(file_r, 'r')
    writer = open(out_w, 'w')
    line = reader.readline()
    count = 0
    moc = 0
    mtc = 0
    og_call_count = 0
    in_call_count = 0
    old = line.split(',')[0]
    value = 'Mobile_No|OG_call_count|IC_Call_count|Total_OG_duration|Total_IC_Duration|OG_Percent|D_CELL_ID|DISTINCT_OG_Mob_No\n'
    writer.write(value)
    cell_id = []
    mob_no = []
    while line:
        data = line.split('|')
        new = data[0]
        if old == new:
            if len(data) > 8:
                if data[6] in cell_id:
                    pass
                else:
                    cell_id.append(data[6])
                if data[8] == 'MOC':
                    og_call_count += 1
                    moc += int(data[5])
                    if data[2] in mob_no:
                        pass
                    else:
                        mob_no.append(data[2])
                if data[8] == 'MTc':
                    in_call_count += 1
                    mtc += int(data[5])
        else:
            if moc > 0 or mtc > 0:
                value = old + '|' + str(og_call_count) + '|' + str(in_call_count) + '|' + str(moc) + '|' + str(
                    mtc) + '|' + str(
                    (moc * 100) / (moc + mtc)) + '|' + str(
                    len(cell_id)) + '|' + str(len(mob_no)) + '\n'
                writer.write(value)
            else:
                pass
            moc = 0
            mtc = 0
            og_call_count = 0
            in_call_count = 0
            cell_id = []
            mob_no = []
            old = new
        count += 1
        if count % 100000 == 0:
            # break
            print (count)
            '''
            for i in range(0, len(data)):
                print i,data[i]'''
        line = reader.readline()

def ttsl_result():
    file_r = 'F:\\Ravi Work\\Raid Case\\TTSL\\ravi.txt'
    out_w = 'F:\\Ravi Work\\Raid Case\\TTSL\\Details.txt'
    reader = open(file_r, 'r')
    writer = open(out_w, 'w')
    line = reader.readline()
    count = 0
    moc = 0
    mtc = 0
    og_call_count = 0
    in_call_count = 0
    old = line.split(',')[0]
    value = 'Mobile_No|OG_call_count|IC_Call_count|Total_OG_duration|Total_IC_Duration|OG_Percent|D_CELL_ID|DISTINCT_OG_Mob_No\n'
    writer.write(value)
    cell_id = []
    mob_no = []
    while line:
        data = line.split('|')
        new = data[0]
        if old == new:
            if len(data) > 8:
                if data[6] in cell_id:
                    pass
                else:
                    cell_id.append(data[6])
                if data[8] == 'MOC':
                    og_call_count += 1
                    moc += int(data[5])
                    if data[2] in mob_no:
                        pass
                    else:
                        mob_no.append(data[2])
                if data[8] == 'MTc':
                    in_call_count += 1
                    mtc += int(data[5])
        else:
            if moc > 0 or mtc > 0:
                value = old + '|' + str(og_call_count) + '|' + str(in_call_count) + '|' + str(moc) + '|' + str(
                    mtc) + '|' + str(
                    (moc * 100) / (moc + mtc)) + '|' + str(
                    len(cell_id)) + '|' + str(len(mob_no)) + '\n'
                writer.write(value)
            else:
                pass
            moc = 0
            mtc = 0
            og_call_count = 0
            in_call_count = 0
            cell_id = []
            mob_no = []
            old = new
        count += 1
        if count % 100000 == 0:
            # break
            print (count)
            '''
            for i in range(0, len(data)):
                print i,data[i]'''
        line = reader.readline()