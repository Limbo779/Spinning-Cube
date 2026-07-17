import pickle

vtx=[]

connectors=[]

num = 0

with open('cat.txt', 'r') as file:
    for line in file:
        l=line.strip()

        raw = l.split(" ")
        if raw[0]=='v':
            vtx.append([float(raw[1]),float(raw[2]),float(raw[3])])
            
            print(f"vertex {num} is done \n")
            num += 1

        elif raw[0]=='f':
            raw_1=raw[1].split('/')
            raw_1=int(raw_1[0])

            raw_2=raw[2].split('/')
            raw_2=int(raw_2[0])

            raw_3=raw[3].split('/')
            raw_3=int(raw_3[0])

            connectors.append([raw_1,raw_2,raw_3])
            

            print(f"connector {num} is done \n")
            num += 1

        else:
            continue


print(vtx)
print('\n\n\n\n')
print(connectors)

with open("vtx.pkl","wb") as file:
    pickle.dump(vtx,file)

with open("connectors.pkl","wb") as file:
    pickle.dump(connectors,file)