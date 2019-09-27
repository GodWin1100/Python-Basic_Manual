print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nFUNCTIONS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#syntax ====> def function_name (parameters or can be empty or variable):
#we dont have to define data-type for variable in function in python
#function work as a call function it means it will only be executed when it is call for calling synta ====> function_name ()
print('\n')
def welcome():  #function is defined
    print('Hello World!!!')
welcome()  #function is called for execution
print('\n')

def greeting(name):  #variable is passed in the function parameter
    print('Hola '+name+'!!!')
greeting('Shivam')  #while calling the function you should also define the content of element for execution or else it will note be executed
print('\n')

#Passing function as a parameter
def seeoff(name2):
    return "Sayonara "+name2

def Identity():
    return 'GodWin'
print(seeoff(Identity()))
print('\n')


def addition(a,b):
    print('addition of ',a,'+',b,' is',a+b)
addition(5,10)
print('\n')

#RETURN
def returnsub (a,b):
    return(a-b)  #return is used for associating the value with some variable and once return is encounter further execution of code is stopped
    print('hello')  #this will not be executed
sub=returnsub(10,5)  #value or return will be stored in the variable where function is called
print(sub)

#variable or content of the function can not be called directly without calling the function
