def cube(num):
    num1 = num*num*num
    return(num1)

print(cube(3))

#using IF statements in Python

is_male = False
is_taller = False

if is_male and is_taller:
    print(" You are a male")
elif is_male and not(is_taller):
    print("You are male and short")
else:
    print("You are taller")

#if statements and comparisons
def max_num(num1, num2, num3) :
    if num1 >= num2 and num2 >= num3 :
       return num1
    elif num2 >= num1 and num1 >= num3 :
        return num2
    else:
        return num3

print(max_num(400, 76, 1123))

#month conversions

monConversions = {
    "Jan": "January",
    "Dec": "December",
}
print(monConversions["Dec"])
print(monConversions.get("Jun"))



