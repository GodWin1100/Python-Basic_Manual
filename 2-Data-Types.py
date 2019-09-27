print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nData-Types\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#type(variable or data) is a syntax which is used to print which type of data is it
int=5
str='five'
point=8.5
bool=True
com=3+6j  #for complex we use j for iota
bin=0B01011  #for writing in binary we use 0B before Binary number
hex=0XF15A  #for writing in binary we use 0X before Hexadecimal number
oct=0O73210  #for writing in binary we use 0O before Octadecimal number

print('\n',int,' is a type of ',type(int),'\n')

print(str,' is a type of ',type(str),'\n')

print(point,' is a type of ',type(point),'\n')

print(bool,' is a type of ',type(bool),'\n')  #boolean is a two option dataset which is only True and False

print(com,' is a type of ',type(com),'\n')

print(bin,' is a type of ',type(bin),'\n')

print(oct,' is a type of ',type(oct),'\n')

print(hex,' is a type of ',type(hex),'\n')
list=['tsk','hmm','asap']  #this is a list, will be cover up later on
print(list,' is a type of ',type(list),'\n')

tuple=('lol','wud','n8',5)  #this is a tuple, will be cover up later on
print(tuple,' is a type of ',type(tuple),'\n')

dictionary={'one':1,2:'two','n8':'night'}  #this is a dictionary, will be cover up later on
print(dictionary,' is a type of ',type(dictionary),'\n')

def function():  #this is a function, will be cover up later on
    print('This is a function')
print('Below Function is Called...')
function()
print('above is a data type of ',type(function),'\n')
