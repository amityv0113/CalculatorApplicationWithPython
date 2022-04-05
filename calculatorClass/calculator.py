from databaseClass import dbconnection

#Abstract class of calculator operation
class OperationAbstract:
    def __add():
        pass
    def __sub():
        pass
    def __mul():
        pass
    def __div():
        pass

# calculator class inherit operationAbstract class 
# containing private member num1,num2
class SampleCalculator(OperationAbstract):
    def __init__(self ,_num1 , _num2):
        self.__num1=_num1
        self.__num2=_num2
        dbconnection.createTable() #create table for db

    # function defination 
    def __add(self):
        return self.__num1+self.__num2
    def __sub(self):
        return self.__num1-self.__num2
    def __mul(self):
        return self.__num1*self.__num2
    def __div(self):
        result=0
        try:  
            a = self.__num1/self.__num2
        except ZeroDivisionError:  
            print ("Zero Division Exception Raised." )
        else:  
            result=self.__num1/self.__num2
        return result

    #doing operation and saving operation to db
    def __operation(self ,val):
        if (val==1):
            res=self.__add()
            dbconnection.insertData(self.__num1,self.__num2,'+',res)
            return res
        elif(val==2):
            res=self.__sub()
            dbconnection.insertData(self.__num1,self.__num2,'-',res)
            return res
        elif(val==3):
            res=self.__mul()
            dbconnection.insertData(self.__num1,self.__num2,'*',res)
            return res
        elif(val==4):
            res=self.__div()
            dbconnection.insertData(self.__num1,self.__num2,'/',res)
            return res
        elif(val==5):
            temp_list =dbconnection.showAllData()
            for temp_val in temp_list:
                print("id : ",temp_val[0])
                print("num1 : ",temp_val[1])
                print("num2 : ",temp_val[2])
                print("operator : ",temp_val[3])
                print("Result : ",temp_val[4])
                print("----------------------")
            return -1
        
        else:
            return -1
    

    def __operationToPerform(self):
        print("enter 1 for addition")
        print("enter 2 for subtraction")
        print("enter 3 for multiplication")
        print("enter 4 for divsion")
        print("enter 5 to look all operation")
    # to start calculator application 
    def run(self):
        
        flag=True
        while flag:
            self.__operationToPerform()
            val=int(input())
            while val not in [1,2,3,4,5,-1]:
                val=int(input("please enter valid input ! :"))
            if val!=-1:
                result =self.__operation(val)
                print("result : ",result)
                print("enter -1 for exit !")
            
            
            else:
                flag=False
                break

    
    def setNum1(self,num1):
        self.__num1=num1
    def setNum2(self,num2):
        self.__num2=num2
    def setNum(self,num1,num2):
        self.__num1=num1
        self.__num2=num2
