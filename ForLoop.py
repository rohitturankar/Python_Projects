for letter in "Rohit Turankar":
     print(letter)

## second example

friends = ["Ramneek", "Anuj", "Rimi"]
for friend in friends :
    print(friend)
#number

for i in range(3,10):
    print(i)
#####exponential function

def raise_to_power(base_num, pow_num):
    result = 1
    if base_num > 0 and pow_num > 0 :
        for i in range(pow_num):
            result = result * base_num
            i += 1
        return result
    elif base_num == 0 and pow_num > 0 :
        result = 0
    else:
        result = 1
    return result

print(raise_to_power(12, 3))



