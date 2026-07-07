import pickle
import numpy as np

vtx={}
mess=[
    #[arr1,arr2,arr3,normal],
    ]

num = 1

with open('cat.txt','r') as file:
    for line in file:
        l=line.strip()

        raw = l.split(" ")
        if raw[0]=='v':
            vtx[num]=np.array([float(raw[1]),float(raw[2]),float(raw[3])])
            num += 1
        elif raw[0]=='f':
            raw_1=raw[1].split('/')
            raw_1=int(raw_1[0])

            raw_2=raw[2].split('/')
            raw_2=int(raw_2[0])

            raw_3=raw[3].split('/')
            raw_3=int(raw_3[0])

            mess.append([raw_1,raw_2,raw_3])
        else : 
            continue


def get_normal(l):
    one = l[0]
    two = l[1]
    three = l[2]

    return np.cross(vtx[two]-vtx[one],vtx[three]-vtx[one])


for i in range(len(mess)):
    normal = get_normal(mess[i])
    mess[i].append(normal)


with open("vtx.pkl","wb") as file:
    pickle.dump(vtx,file)

with open("mess.pkl","wb") as file:
    pickle.dump(mess,file)

#with open('penger.txt', 'r') as file:
#    for line in file:
#        l=line.strip()
#
#        raw = l.split(" ")
#        if raw[0]=='v':
#            vtx["x"].append(float(raw[1]))
#            vtx["y"].append(float(raw[2]))
#            vtx["z"].append(float(raw[3]))
#
#            print(f"vertex {num} is done \n")
#            num += 1
#
#        elif raw[0]=='f':
#            raw_1=raw[1].split('/')
#            raw_1=int(raw_1[0])
#
#            raw_2=raw[2].split('/')
#            raw_2=int(raw_2[0])
#
#            raw_3=raw[3].split('/')
#            raw_3=int(raw_3[0])
#
#            connectors.append([raw_1,raw_2])
#            connectors.append([raw_1,raw_3])
#            connectors.append([raw_2,raw_3])
#
#            print(f"connector {num} is done \n")
#            num += 1
#
#        else:
#            continue

