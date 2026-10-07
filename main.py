secret_number = 17

print("THIS IS THE NUMBER GUESSER")
print("You have to choose a number between 1 and 50")
print("You have 5 attempts")


attempts = 0




while attempts <= 5:
    guess = int(input(f"Please enter guess NO.{attempts} -   "))
    hearts = 5 - attempts

    if guess == 17:
        print("CONGRATULATIONS YOU HAVE WON")
        break

    elif guess>=1 and guess<=15:
        print("Wrong")
        print("You are WARM")
        print(f"YOU HAVE {hearts} hearts left")

    elif guess>=15 and guess<=20:
        print("Wrong")
        print("You are HOT")
        print(f"YOU HAVE {hearts} hearts left")

    elif guess>=20 and guess<=35:
        print("Wrong")
        print("You are COLD")
        print(f"YOU HAVE {hearts} hearts left")

    elif guess>=35 and guess<=50:
        print("Wrong")
        print("You are ICE COLD")
        print(f"YOU HAVE {hearts} hearts left")

    
    attempts = attempts + 1




    

