print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

totalPrice=0

def cal_pepperoni(statement):
     while True:
            pepperoni=input("Do you want pepperoni? Y or N")
            pepperoni=pepperoni.upper()
            print(pepperoni)
            if (pepperoni == "Y"):
                global totalPrice
                totalPrice=totalPrice+statement
                break;
            elif(pepperoni == "N"):
                break;
            else:
                 print("Please input only Y or N")
                 continue

def cal_cheese():
      while True:
            cheese=input("Do you want extra cheese? Y or N")
            cheese=cheese.upper()
            print(cheese)
            if (cheese == "Y"):
                global totalPrice
                totalPrice=totalPrice+1
                break;
            elif(cheese == "N"):
                break;
            else:
                 print("Please input only Y or N")
                 continue

while True:
        p_size=input(" What size pizza do you want? S, M, or L")
        p_size=p_size.upper()
        print(p_size)
        if (p_size == "S"):
            totalPrice+=15
            cal_pepperoni(2)
            cal_cheese()
            break;
        elif(p_size == "M"):
            totalPrice+=20
            cal_pepperoni(3)
            cal_cheese()
            break;
        elif((p_size == "L")):
            totalPrice+=25
            cal_pepperoni(3)
            cal_cheese()
            break;
        else:
            print("you give wrong input, please type S , M or L")

print(f"Your final bill is: ${totalPrice}")