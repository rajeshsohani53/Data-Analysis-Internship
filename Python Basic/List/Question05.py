#Create a list of 10 programming languages and display the first 5 elements.
mylist=list()
for i in range(10):
    name = input(f"Enter the  {i+1} programming language name: ")
    mylist.append(name)

print(mylist[4])

