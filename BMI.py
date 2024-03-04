# BMI CALCULATOR

# Asking input to Users
Height=int(input("Enter your Height in Cm:\n"))
Weight=float(input("Enter Your Weight in Kg:\n"))

BMI=Weight/(Height/100)**2 # BMI Calculate Formula

print(f'YOUR Body Mass index RESULT IS :{BMI}') # Print BMI Result

if BMI <=18.5: # use if-elif conditions
     print(" Oops!You Are Underweight")
elif BMI <= 24.9:
     print("Congrats!You Are Healthy !!!!")
elif BMI <=29.9:
     print(" You Are overweight")
elif BMI <=35:
     print("obesity level 1")     
else:
    print("you are Obese")
                
            
              
