#Create a list of 8 fruits and replace the last fruit with "Kiwi".


mylist=list()
for i in range(8):
    name = input(f"Enter the number {i+1} fruit name: ")
    mylist.append(name)

print(mylist)

print("Enter the name of last fruit to edit or update")
mylist[-1]=input()
print(mylist)