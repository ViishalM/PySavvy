def Swap(mList, pos1, pos2):
    pos1 = pos1-1
    pos2 = pos2-1
    temp = mList[pos1]
    mList[pos1] = mList[pos2]
    mList[pos2] = temp
    return mList


my_list = []
length = int(input("Enter the Size: "))
for i in range(length):
    x = input(f"Enter the {i+1} element: ")
    my_list.append(x)
print(my_list)
Pos1 = int(input("Enter the initial position: "))
Pos2 = int(input("Enter the final position: "))
if Pos1 > length or Pos2 > length:
    print("Enter a valid position")
print(Swap(my_list, Pos1, Pos2))
