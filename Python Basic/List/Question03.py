#Create a list of 10 numbers and change the 5th element to 100.


mylist=list()
for i in range(10):
    name = input(f"Enter the number {i+1} postion number: ")
    mylist.append(name)

print(mylist)

print("Enter the update no of 5th number to edit or update")
mylist[4]=input()
print(mylist)