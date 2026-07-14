#Create a list of 10 subjects and display the elements from index 2 to index 7.

mylist=list()
for i in range(10):
    name = input(f"Enter the number {i+1} subject name: ")
    mylist.append(name)

for i in range(1,6,1):
    print(mylist[i])