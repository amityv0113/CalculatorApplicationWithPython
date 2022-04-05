from calculatorClass import calculator 

#function to check num is valid or not 
def check_num(num1,count):
    if len(num1)>18: 
        return False
    for i in range(len(num1)):
        if num1[0]=='-': #check for negative number 
            continue
        if ord(num1[i])==46:
            count=count+1
            if count>1:  #check for number of decimal points
                return False
        elif ord(num1[i])<48 or ord(num1[i])>57: #check for invalid char
            return False
    return True



if __name__ == '__main__':
    print("Starting Calculator Application")
    num1 = str(input("Enter first number: ")) #taking 1st input from user
    count1=0
    count2=0
    #loop for valid input 1
    while(check_num(num1,count1)==False):
        num1=str(input("You have entered wrong input! number Please enter first number again : "))

    num2 = str(input("Enter second number: ")) #taking 2nd input from user
    #loop for valid input 2
    while(check_num(num2,count2)==False):
        num2=str(input("You have entered wrong input! number Please enter first number again : " ))
    #object of calculator
    obj =calculator.SampleCalculator(float(num1),float(num2))
    # starting calculator 
    obj.run()

    print("end")
