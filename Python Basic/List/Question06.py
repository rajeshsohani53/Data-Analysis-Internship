#Create a list of 12 cities and display the last 4 elements.

mylist=list()
for i in range(12):
    name = input(f"Enter the name  of city {i+1} : ")
    mylist.append(name)

print("the last 4 cities are")
for i in range(9, 5, -1):
    print(mylist[i])

