import random
while True:   
    print("🎮 Welcome to Number Guessing Game!")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Quit")
    choice = input("choose difficulty: ")

    if choice == "1":
        max_number = 10
        attempts = 10
        secret_number = random.randint(1,max_number)
        while True:
            your_guess = int(input("guess a number between 1 and 10:"))
            if your_guess == secret_number:
                print("🎉 Congratulations! You guessed the number!")
                break
            elif your_guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                print(f"😔 Game Over! The number was {secret_number}.")
                break


    elif choice == "2":
        max_number = 50
        attempts = 5
        secret_number = random.randint(1,max_number)
        while True:
            your_guess = int(input("guess a number between 1 and 50:"))
            if your_guess == secret_number:
                print("🎉 Congratulations! You guessed the number!")
                break
            elif your_guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                print(f"😔 Game Over! The number was {secret_number}.")
                break

    elif choice == "3":
        max_number = 100
        attempts = 3
        secret_number = random.randint(1,max_number)
        while True:
            your_guess  = int(input("guess a number between 1 and 100:"))
            if your_guess == secret_number:
                print("🎉 Congratulations! You guessed the number!")
                break
            elif your_guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                print(f"😔 Game Over! The number was {secret_number}.")
                break 

    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please try again.")