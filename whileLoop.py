i = 10
while i < 1 :
    print(i)
    i = i - 1

print("done with loop")

###3 while loop with guess code

secret_code = "Rohit"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_code and not(out_of_guess) :
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess == True:
    print("you loose")
else:
    print("You win the game")