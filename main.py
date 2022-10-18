# The task is this: the program will ask for the user's name and then it will say


secretNumber = randint(1,101)
name = input("What is your name?")
print(name)

print("Well, " + name + " I've thought of a number between 1 and 100")
print("You have only eight tries to guess it.")
guess = input("What number do you think it is?")
print(guess)


# 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.
count = 0
for guess in secretNumber(count):
  if guess != secretNumber:
    count = count + 1
  elif count == 8:
    print("You lose! Better luck next time.")
    
          
    
  
  





if guess >= secretNumber():
  print("Your guess is higher than the number I've thought of")
else:
  print("Your guess is smaller than the number I've thought of")
  
  
  


# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.

    
if guess >= secretNumber:
  print("Your guess is higher than the number I've thought of")

  
# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.

  
if guess >= secretNumber:
  print("Your guess is higher than the number I've thought of")

  
# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.

  
if guess == secretNumber:
  print("You got it right! Congradulations")



# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.
