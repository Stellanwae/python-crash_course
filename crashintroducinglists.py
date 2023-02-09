#python lists
shopping_list = ["avocado", "grapes", "cooking oil", "salt", "wheat flour"]
print(shopping_list)
print(shopping_list[:])
print(shopping_list[3].upper())

#friends
friends = ["Lizmary", "Holida","Rebecca", "Priscah", "Lilian", "Caroline"]
print(friends)
for f in friends:
    print("{} ".format(f) , end="")
print("\n", len(friends))
for i in range(6):
    print(friends[i])
print(friends.sort())
friends.append("Maureen")
print(friends)
print("Maureen" in friends)
new_friends = []
new_friends.append("Nancy")
new_friends.append("Cynthia")
print(new_friends)
#insert on a specific index
new_friends.insert(0, "Shanteel")
print(new_friends)
#deleting an item from a list
del new_friends[1]
print(new_friends)
for item in range(len(new_friends)-1):
    del new_friends[item]
print(new_friends)
print(new_friends)
#removing using the pop() method
new_friends.pop()
print(new_friends)
if []:
    print("True")
else:
    print("False")

#remove item from a list
'''remove() only removes the first occurence of the item on a list
To ensure all the items are removed, 
you might need to used a loop'''
print(friends)
friends.remove('Caroline')
print(friends)
#exercise
'''make a list that includes three people you'd like to inivite
to dinner. Use that list to invite them to come to dinner'''

def invitation(list=[]):
    for i in list:
        print("Hi {} please come to this dinner invite".format(i))

finvitation = ["Lizmary", "Chela", "Priscah"]
print(invitation(finvitation))
print("Chela will not be coming anymore, she'll be having crucial exams")
print(finvitation.index("Chela"))
finvitation[1] = "Rebecca"
print(invitation(finvitation))
print("A bigger number will now be coming")
finvitation.insert(0, "Cynthia")
print(len(finvitation))
finvitation.insert(3, "Natalie")
finvitation.append("Lilian")
print(invitation(finvitation))
print("I'm really sorry ladies, I can only invite two people")
finvitation.pop()
finvitation.pop()
finvitation.pop()
print(len(finvitation))
finvitation.pop()
print(len(finvitation))
del finvitation[1]
print(finvitation)
del finvitation[0]
print(finvitation)

#organising a list
#sorting
print(friends)
print(friends.sort())#it does not sort within the print function
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(len(friends))
#exercise
'''think of at least five places in the 
world you'd like to visit'''
prospects = ["Hawai","Zanzibar", "Mombasa", "Tsavo", "Rwanda", "Scotland"]
print(prospects)
#sort in alphabetical order
prospects.sort()
print(prospects)
print(sorted(prospects))
print(prospects)
print(prospects)
prospect = []
for i in range(len(prospects)):
    prospect.append(prospects[i])
print(prospect)
print(prospect*2)
print("we are going to be {:d} people in the dinner invite".format(len(friends)))

print(prospect[-1])
'''How to sort lists temporarily(should Google this)'''
