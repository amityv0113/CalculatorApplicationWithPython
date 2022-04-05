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
