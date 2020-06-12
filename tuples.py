
#working with tuples - immutable

coordinates = (4, 5)

print(coordinates)
#coordinates[1] = 10
# we cant change the values of tuples are these are immutable
# we can make list of tuples like below

list1 = [(3, 4), (5, 4), (7, 6)]
print(list1)

#working with functions
#indentation is must while defining functions

def sayhello():
    print("Hello Rohit Turankar")
print("Top")
sayhello()
print("Bottom")
#calling a function

# functions wiht parameters

def say_hi(name, age):
    print(name + age)

say_hi("Rohit", "27")


