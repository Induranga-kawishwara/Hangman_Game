# 20200688 Induranga

# Importing packages and modules
import sub.player_data, sub.game_code, datetime

#Initializing the variables
play=""
chance=1
word_save_list=[]
turn_save_list=[]
status_list=[]
time_list=[]

# Displaying the menu and getting menu input
print("\n""""        !!!***Welcome to HANGMAN***!!!

PLAY----enter 1              EXIT----enter 2""")


# Getting and validating the input
while play != '1' or play!='2':
    play=str(input("\n""    (Type 1 to play / Type 2 to exit) : "))
    if play=='1' or play=='2':
        break
    else:
        print("       PLEASE ENTER A VALID INPUT !!!")
        continue

              
while play=='1':
    if play=='1':
        play='0'
        print()
        print("==============================================================================\n")
        name=str(input("Enter your name : ")).lower()
        print()
    
        print("-----------------------------------------------------------------------------")

        print("Hi",name)
        print("\n""""        An word with empty spaces will be given.
        You need to guess and type the letters according to the hint.
        You have a limited number of chances.
        If you complete the word within the given number of chances, YOU WIN!!!
        Else, YOU LOSE

        GOOD LUCK!!! \n""")

        

        # Getting and validating user input
        while play !='1':
            play=str(input("Enter 1 to proceed to the game : "))
            if play=='1':
                break
            else:
                print("PLEASE ENTER A VALID INPUT")
                print()
                continue

            
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        while (play=='1'):
            play='0'

            # Runs the game loop while the chances are not equal to zero
            while(chance!=0):
                print("-----------------------------------------------------------------------------")
                print('\n')
                chance, word= sub.game_code.game()
                word_save_list.append(word)
                turn_save_list.append(chance)
                

                # Getting the current time and appending to a list
                now=datetime.datetime.now()
                current_time=now.strftime("%H:%M:%S")
                time_list.append(current_time)
                
                
                if chance==0:
                    status_list.append("LOST")
                    break
                status_list.append("WON")

                
                # Getting and validating user input
                while play!= '1' or play!= '2':
                    play=str(input("\nEnter 1 to play again / Enter 2 to exit : "))
                    if play=='1' or play=='2':
                        break
                    else:
                        print("PLEASE ENTER A VALID INPUT")
                        continue
                    
                if play=='1':
                    play='0'
                    continue
                else:
                    break

                
            # If the player runs out the chanses
            if chance==0:
                print("-----------------------------------------------------------------------------\n")
                print("Ooops!!!, You are out of luck!, The word is",word,"\n")

                
                # Calling player data function
                sub.player_data.curr_session(name, time_list, word_save_list, turn_save_list, status_list)
                print()
                play=str(input("Enter 1 to try again / Enter 2 to exit : "))
                if play=='1':
                    chance=1

                    # Clearing all the elements from the lists
                    time_list.clear()
                    word_save_list.clear()
                    turn_save_list.clear()
                    status_list.clear()
                    continue
                else:
                    break
                                
    else:
        break

#If chances are greater than 0 after exiting
if chance>0 and (len(word_save_list))>0:
   sub.player_data.curr_session(name, time_list, word_save_list, turn_save_list, status_list) 
    
print("\nThank you for playing HANGMAN!!!, Hope you will be back soon!!!")



















            
             
