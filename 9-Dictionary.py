print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nDICTIONARY\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

print('\n')
#Dictionaries
student={'john':15,'naruto':17,'luffy':19} #syntax for declaring dictionary dictionary_name={'keyvalue_pair_of_dictionary'}
print(student)
print(student['john']) #to print certain element value
student['naruto']=19 #to edit element value
print(student)

print('\n')
del student['john'] #will delete element pair
print(student)
print(len(student))
print(student.keys()) #keys will be printed only
print(student.values())  #values will be printed only
student.clear()  #this will clear every key value pair in dictionary and will make it empty
print(len(student))
print(student)

print('\n')
updated={'one':1,'two':2,'three':3}
student.update(updated)  #this will simply append 1 dictionary with other dictionary
print(student)

print('\n')
geeks={'idiots':5,'dumbs':2,'scholar':1,'multitalented':0}
updated.update(geeks)
print(updated)

print('\n')
print('final dictionary values')
print(geeks)
print(student)
print(updated)


print('\nAppending or adding a key-value pair in dictionary')
new_key='newly'
new_value='added'
updated[new_key]=new_value  #this syntax is used for appending a dictionary. syntax==> dictionary_name[keys_name]=values_name
print(updated)
updated['Over']=100
print(updated)