print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nINDEXING OF STRING\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# indexing of string
state1 = "Shivam is my name."
print(state1[0])  # indexing of string starts with 0
print(state1[4])  # this will print a single character
print(state1[0:6])  # this will print character from index 0 to 5 both included ans last 6 is excluded
print(state1[0:5])  # last limit is not included while printing
print(state1[:6])  # by default it consider starting limit as 0
print(state1[2:])  # by default it will print till last index
print(state1[-1])  # can take negative value it will start indexing from last character from end indexing start from -1
print(state1[-8:-1])  # lowest number should be start and greatest should be last
print(state1[0:-4])  # this limit also works it will print till last limit character in case last limit is negative
print(
    state1[0::2]
)  # string_variable[starting_index : ending_index : step_increment/decrement] in this case it will print element with difference of 2
print(state1[::-1])  # this will reverse the string as start index is last index of string and step_decrement of -1
print(state1[18::-1])
