
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale") 
guess4 = input("What is the largest desert in the world ")
check_guess(guess4, "The Sahara Desert") 
guess5 = input("Which country has the longest coastline in the world? ")
check_guess(guess5, "Canada?") 
guess6 = input("What is the largest planet in our solar system? ")
check_guess(guess6, "Jupiter")
guess7 = input("What is the capital of France? ")
check_guess(guess7, "Paris") 

print("Your Score is "+ str(score)) 
