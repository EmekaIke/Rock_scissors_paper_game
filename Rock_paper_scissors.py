from xml.dom import InvalidCharacterErr


print("Welcome to our Rock, Paper, Scissors game.")
print("This game is between the CPU and a Player")
print('In this game, "R" stands for Rock, "P" stands for Paper, "S" stands for Scissors')
print("If the two players choose the same 'character' it is a tie, and the game repeats. Rock beats Scissors, Paper beats Rock, Scissors beats Paper")
# create a list that has r, p and s.
# create a loop that will keep the process repeating.
# import random module and use choice method to choose one at a time from a list of p, r,& s.
# Ask the user to make his choice. Use Try and Exempt to catch the errors.
# print the output of the module and the user_input
# compare the two choices of the user and the module
# print the winner.
# Ask if the user will like to continue playing and then repeat the process

def start_game():
    import random
    CPU_choice=random.choice(game_list)
  
    user_choice=input("Please pick one from the list ['R', 'P', 'S']: ")  
    game()
  
game_list=['R', 'P', 'S']

def game(): 
   
  while True:
    import random
    CPU_choice=random.choice(game_list)
    user_choice=input("Please pick one from the list ['R', 'P', 'S']: ") 
    cased_text=user_choice.upper()   
  
    if user_choice in ['R', 'P', 'S']:
          
      print("Player chose " + user_choice + ": CPU chose " + CPU_choice) 
      
      if user_choice == CPU_choice:
        print("It's a tie, we will restart the game")
        start_game()
        
      if user_choice == "R" and CPU_choice == "S" :
        print("The player Wins")
            
      if user_choice == "S" and CPU_choice == "R" :
        print("The CPU Wins")
        
      if user_choice == "P" and CPU_choice == "R" :
        print("The Player Wins")
      
      if user_choice == "R" and CPU_choice == "P" :
        print("The CPU Wins")
            
      if user_choice == "S" and CPU_choice == "P" :
        print("The Player Wins")
        
      if user_choice == "P" and CPU_choice == "S" :
        print("The CPU Wins")
        
      play_again =input("Do you wish to play again? [y/n]")
      if play_again=='y':
            pass
      if play_again == "n":
        print("Thank you for playing this game. Catch you next time.")
        break

    
    else:
      print('Invalid choice, pick between "R", "P" and "S" ')

game()   




