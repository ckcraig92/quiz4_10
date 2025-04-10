# title
print("Rock, Paper, Scissors Game")

#Ask user to input
selection = int(input("Make your selection: 0=Rock 1=Paper 2=Scissors 4=Exit  "))

import random
computerchoose = random.randint(0,2)


#loop process for user selection
if selection == 0:
    print ("you chose: rock")
   
    
elif selection == 1:    
    print ("you chose paper")
  
    
elif selection == 2:
    print ("you chose sissors")  
   
    
else:
    print ("exit") 


#loop process for computer selection
if computerchoose == 0:
  
    print (f"computer chose:rock")
    
elif computerchoose == 1:    
 
    print (f"computer chose: paper")
    
elif computerchoose == 2:

    print (f"computer chose: scissors")  
    

    
       
#determine winner
if selection == computerchoose:
    print('you tie')
elif selection == 0 and computerchoose == 2:
    print('you win') 
elif selection == 1 and computerchoose == 0:
    print('you win')
elif selection == 2 and computerchoose == 1:
        print('you win')    
else:
    print('you loose')        

##or array
#import random
#rps=["rock, "paper", "scissors"]
#while true
#guess = int(input('input 0 for rock etc.))
#if guess==4:
#print('bye')
#break
#print('you chose: '+rsp[guess])
#comm = random.randint(0,2)
#print('computer choice' +rsp[com])
#if(guess==com)
#print("tie")
#elif(guess==0 and com==2) or (guess==1 and com==0) or (guess==2 and comm==1);
#print("you win")
#else:
#print("you lose")

##or
#wincombination = [[0,2] , [1,0] , [2,1]]