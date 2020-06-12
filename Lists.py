friends = ["A","B","C","D"]
num_ex = [1, 2, 3, 4]
#join 2 lists using extend
friends.extend(num_ex)
print(friends)
#insert one more value in list

friends.insert(4,"E")
print(friends)

#remove one value from lists

friends.remove(1)
print(friends)
print(friends.index("A"))

#sorting the list using sort function

num_ex.sort()
num_ex.reverse()
print(num_ex)

friends2 = friends.copy()
print(friends2)