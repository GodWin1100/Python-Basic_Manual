print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nLIST\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# List and array are same difference is array is mostly called list containing only number dataset (comma separated values or CSV)
# indexing starts from 0 in list too
print("\n")
list = ["hello", "how", "are", "you", "world"]  # syntax for declaring list list_name=['list_elements','more_elements']
print("this is list>>>", list)
print(list[0], "<<<this is first element of list but index start from 0")
print(list[2])
print(list[4 - 3])
print(list[0 + 1])
print(list[2 * 2])  # for such operation it should be integer and not float
print(list[0:2])  # indexing is same as indexing for strings
print(list[:4])
print(list[2:])
print(list[-1])
print(list[1:-2])

print("\nOperation starts")
# list operations
list.append("global")  # this will append(add) item to this string at last index
print(list)
print(list[5])
list[0] = "hi"  # to change list content at a particular index just call it and assign the new content
print(list)
list[3] = "we"
print(list)
del list[3]  # this will delete the particular element of list at the said index
print(list)
print(len(list))  # len will show the length of list NOTE it is not indexing it is number of elements in the list
length = len(list)
print(length)
list2 = ["bravo", "ronaldo", "awesome", "anime"]
print(list2)
list3 = list + list2  # this will add 2 list
print(list3)
print(list * 2)  # this will print list for 2 times as it is multiplied by 2
# * list.clear()  #will clear the list
print("\n")

# NEW OPERATORS OR SYNTAX
print("\nExclusive syntax starts")
print(max(list))  # for string it will print highest value ascii number
print(min(list))
list.append("Are")
print(min(list))  # will print lowest value ascii number
list.append("Ara")
print(
    min(list)
)  # if elements are same it will go to next alphabet of word till the difference is found and will print accordingly
num = [5, 78, 52, 45, 74, 20]
print(max(num))  # will print biggest number in the list
print(min(num))  # will print smallest number in the list
print(list.count("hello"))  # count will count how many times the said element is present in list
print("\n")

# LIST ELEMENT OPERATION
list.append("hello")
list.append("Hello")
print(list)
print(list.count("hello"))
list.append("hello")
print(list.count("hello"))
list.insert(8, "added")  # this will insert the element at desired index position which is 8 in this case
print(list)
list.pop()  # .pop will delete the last element of list
print(list)
list.remove(
    "hi"
)  # this will remove specific element of the list it will remove only once when it is occurred for first time
print(list)
list.clear()  # this will delete every element in the string
print(len(list))
print(list2)
print(list3)
list2.append(list3)  # whole list can be append too
print(list2)
list3.extend(
    list3
)  # the difference is that it will append each element to the  list unlike .append which append whole as one # ? (like spread operator in JS)
print(list3)
list3.remove("hi")  # example of remove # // only one hi is removed
print(list3)
# * print(random.choice(list3)) #will print random element of list 3  for this we need to import random
print("\n")

# SORTING (ARRANGING)
list3.sort()  # this will sort(arrange) element in ascending order in case of character value of ascii value will be taken in consideration
print(list3)
num.sort(reverse=True)  # this will sort in descending order
print(num)
print("\n")

# SEARCHING ELEMENT
print(list3.index("world"))  # this will print index of given data to be searched in the list
print("hi" in list3)  # this will print True if given data exist in list or False if given data is not in the list
print("lol" in list3)
