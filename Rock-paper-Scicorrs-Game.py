import random

print("lets play ROCK-PAPER-SCICCORS"
      "\n"
      "\n")

user_name = input("ENTER YOUR NAME  ")
i=1
count = 0
count_computer = 0
while i < 10:

    i=i+1

    Computer_value = ["1","2","3"]
    computer_play = random.choice(Computer_value)
    your_value = input("INPUT THE NUMBER RESPECTIVELY \n"
                       "1. ROCK \n"
                       "2. PAPER \n"
                       "3. SCICCORS \n")

    #print(your_value)

    if( computer_play== "1" and your_value == "1"):
        print( i, "match draw")

    elif (computer_play == "1" and your_value == "3"):
        print(i,"computer won")
        count_computer=  count_computer+1

    elif (computer_play == "1" and your_value == "2"):
        print(i,"you won")
        count= count + 1

    elif (computer_play == "2" and your_value == "3"):
        print(i,"you won")
        count= count + 1

    elif (computer_play== "2" and your_value == "2"):
        print(i,"match draw")

    elif (computer_play == "2" and your_value == "1"):
        print(i,"computer won")
        count_computer = count_computer + 1

    elif (computer_play == "3" and your_value == "2"):
        print(i,"computer won")
        count_computer = count_computer + 1

    elif (computer_play== "3" and your_value == "1"):
        print(i," you won")
        count = count + 1

    elif (computer_play == "3" and your_value == "3"):
        print(i,"match draw")

    else:
        print(i,"invalid choice")
        continue


print("COMPUTER WIN STREAKS", count_computer, "\n")
print(f" {user_name} WIN STREAKS", count,
      "\n")

if(count_computer == count):
    print("tie")

elif(count > count_computer):
    print(f" {user_name} WON THE WHOLE GAME")

else:
    print(F" BAD LUCK! {user_name}, YOU LOST THE GAME")