#Create a list of 10 employee names and display the list in reverse order.
mylist = []

for i in range(10):
    name = input(f"Enter the employee no {i+1} name: ")
    mylist.append(name)

print("The names in reverse order are:")

for i in range(9, -1, -1):
    print(mylist[i])