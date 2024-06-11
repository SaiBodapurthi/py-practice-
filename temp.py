rooms = [[2],[],[1]]
keys = []
keys.extend(rooms[0])
count=0
for i in range(1,len(rooms)):
    if i in keys:
        count+=1
        keys.extend(rooms[i])
    else:
        break
if count==len(rooms)-1:
    print("True")
else:
    print("False")
