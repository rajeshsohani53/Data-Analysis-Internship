#Create a list of 7 colors and replace the first and last colors with new values.

mylist=list()
for i in range(7):
    name = input(f"Enter the color of no {i+1} position: ")
    mylist.append(name)

print(mylist)

print("Enter the color name  of 1th color to edit or update")
mylist[0]=input()
print(mylist)

print("Enter the color name  of last color to edit or update")
mylist[-1]=input()
print(mylist)