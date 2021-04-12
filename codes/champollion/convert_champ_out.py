import sys
cp_file = sys.argv[1]
eng_file=sys.argv[2]
hin_file=sys.argv[3]
out_file=sys.argv[4]
cp = open(cp_file).read().split('\n')
eng = open(eng_file).read().split('\n')
hin = open(hin_file).read().split('\n')
# print(cp)
print(len(cp))

print(len(eng))
print(len(hin))

#Creating English sentence and hindi sentence dictionary with ids
edict={};hdict={}
for i, eline in enumerate(eng,1):
    edict[i]=eline
for i, hline in enumerate(hin,1):
    hdict[i]=hline
# print(edict)
# print(hdict)
print("edict and hdict created.....")


#creating champollion output file in sentence format
allealignlist = []
allhalignlist = []
eal = []
hal = []
for entry in cp:
    if("<=>" in entry):
        eids = entry.split(" <=> ")[0].strip()
        hids = entry.split(" <=> ")[1].strip()
        if "omitted" in eids  :
            eal.append(eids)
            hal.append(int(hids))
        elif "omitted" in hids  :
            eal.append(int(eids))
            hal.append(hids)
        
        elif ',' in eids and ',' not in hids:
            eal.append([int(i) for i in eids.split(',')])
            hal.append(int(hids))
        elif ',' in hids and ',' not in eids:
            eal.append(int(eids))
            hal.append([int(i) for i in hids.split(',')])
        elif ',' in eids and ',' in hids:
            eal.append([int(i) for i in eids.split(',')])
            hal.append([int(i) for i in hids.split(',')])
        elif ',' not in eids and ',' not in hids:
            eal.append(int(eids))
            hal.append(int(hids))


import itertools
# for eids, hids, org in itertools.zip_longest(eal , hal, cp):
#     print(eids,"<=>",hids,"\t\t", org)


with open(out_file,'w') as f:
    i=1
    for eids, hids, org in itertools.zip_longest(eal , hal, cp):
        if eids == "omitted":
#             print(i,eids," <=> ",hdict[hids])
            f.write(str(eids)+" <=> "+str(hids) +"] "+hdict[hids]+ "\n")
            
        elif hids == "omitted":
#             print(i,edict[eids],' <=> ',hids)
            f.write(edict[eids]+' <=> '+str(hids)+ "\n")

        elif type(eids) is list and type(hids) is int:
#             print(i," ## ".join([edict[i] for i in eids])," <=> ", hdict[hids])
            f.write(" ## ".join([str(i)+") "+edict[i] for i in eids])+" <=> "+ str(hids) +"] "+hdict[hids]+ "\n")
            
        elif type(hids) is list and type(eids) is int:
#             print(i,edict[eids],' <=> '," ## ".join([hdict[i] for i in hids]))
            f.write( str(eids) +") "+edict[eids]+' <=> '+" ## ".join([str(i)+"] "+hdict[i] for i in hids])+"\n")
        elif type(eids) is list and type(hids) is list:
            f.write(" ## ".join([str(i)+") "+edict[i] for i in eids])+" <=> "+" ## ".join([str(i)+"] "+hdict[i] for i in hids])+ "\n")
        elif type(eids) is int and type(hids) is int:
            f.write(str(eids) +") "+ edict[eids]+' <=> '+ str(hids) +"] "+hdict[hids]+ "\n")
        i+=1     

'''    for eids, hids, org in itertools.zip_longest(eal , hal, cp):
        if eids == "omitted":
#             print(i,eids," <=> ",hdict[hids])
            f.write(str(eids)+" <=> "+str(hids) +"] "+hdict[hids]+ "\n")
            
        elif hids == "omitted":
#             print(i,edict[eids],' <=> ',hids)
            f.write(edict[eids]+' <=> '+str(hids)+ "\n")

        elif type(eids) is list and type(hids) is int:
#             print(i," ## ".join([edict[i] for i in eids])," <=> ", hdict[hids])
            f.write(" ## ".join([str(i)+") "+edict[i] for i in eids])+" <=> "+ str(hids) +"] "+hdict[hids]+ "\n")
            
        elif type(hids) is list and type(eids) is int:
#             print(i,edict[eids],' <=> '," ## ".join([hdict[i] for i in hids]))
            f.write( str(eids) +") "+edict[eids]+' <=> '+" ## ".join([str(i)+"] "+hdict[i] for i in hids])+"\n")
        elif type(eids) is list and type(hids) is list:
#             print(i," ## ".join([edict[i] for i in eids])," <=> ", " ## ".join([hdict[i] for i in hids]))
            f.write(" ## ".join([str(i)+") "+edict[i] for i in eids])+" <=> "+" ## ".join([str(i)+"] "+hdict[i] for i in hids])+"\n")
#####" ## ".join(str(i)+"] "+[hdict[i] for i in hids])+ "\n")
        elif type(eids) is int and type(hids) is int:
#             print(i,edict[eids],' <=> ',hdict[hids])
            f.write(str(eids) +") "+ edict[eids]+' <=> '+ str(hids) +"] "+hdict[hids]+ "\n")
        i+=1     

print("E1_champollion_out EE <=> HH created...")
'''
