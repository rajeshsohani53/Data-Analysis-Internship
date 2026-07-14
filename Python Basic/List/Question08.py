#Create a list of 15 integers and display every second element.
mylist=list()
for i in range(15):
    name = input(f"Enter the number {i+1} postion number: ")
    mylist.append(name)



for i in range(1,15,2):
    print(mylist[i])