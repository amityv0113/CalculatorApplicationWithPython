from calculatorClass import calculator 
from check import checkNum



if __name__ == '__main__':
    print("Starting Calculator Application")
    num1 = str(input("Enter first number: ")) #taking 1st input from user
    count1=0
    count2=0
    #loop for valid input 1
    while(checkNum.check_num(num1,count1)==False):
        num1=str(input("You have entered wrong input! number Please enter first number again : "))

    num2 = str(input("Enter second number: ")) #taking 2nd input from user
    #loop for valid input 2
    while(checkNum.check_num(num2,count2)==False):
        num2=str(input("You have entered wrong input! number Please enter first number again : " ))
    #object of calculator
    obj =calculator.SampleCalculator(float(num1),float(num2))
    # starting calculator 
    obj.run()

    print("end")
