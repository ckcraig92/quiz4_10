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


#loop process for user selection
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

