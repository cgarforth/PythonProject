close = False

while close == False:
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Close")
    option = int(input("Select an option: "))

    if option == 5:
        close = True
    else:
        close = False

    if option <= 5 and option>=1:
        valid = True
    else:
        valid = False
        print("Error: enter a number from the list")


    if close == False and valid == True:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))

      if option == 1:
        total = int(num1+num2)
        print("{0} + {1} = {2}".format(num1, num2, total))
      elif option == 2:
        total = int(num1-num2)
        print("{0} - {1} = {2}".format(num1, num2, total))
      elif option == 3:
        total = int(num1*num2)
        print("{0} * {1} = {2}".format(num1, num2, total))
      elif option == 4:
        total = float(num1/num2)
        remainder = num1 % num2
        intTotal = int(num1/num2)
        print("{0} / {1} = {2}".format(num1, num2, total))
        print("{0} / {1} = {2} remainder {3}".format(num1, num2, intTotal, remainder))



    
   
    

