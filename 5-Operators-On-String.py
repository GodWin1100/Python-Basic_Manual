print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nOPERATORS ON STRING\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# operators on string
# if you need to use quotation mark in string then use \ before using it as it will command python that it is an statement and not string quotation
print(
    "\nit's a beautiful day"
)  # for not making python confuse which quotation is a statement we use back slash before it
print('he said"shut up"\n')

state1 = "hello"
state2 = "world"
print(state1 + state2)  # + will not concatenate the two statements but will print it without any spaces
print("state1=" + state1 + " state2=" + state2)
print(state1 + " " + state2)  # to insert spaces u need to add space manually
print(state1, state2)  # this doesn't add or concatenate the variable it just prints
print(state1 * 5, "\n")  # this means state1 will be printed for 5times

state = "MagiC CoMmeNceS"
print(state.upper())  # this will convert all alphabet to upper case i.e. CAPITAL LETTERS
print(state.lower())  # this will convert all alphabet to lower case i.e. small letters
print(state.title())  # every first alphabet of word will be in uppercase
print(state.count("a"))  # this will count number of times alphabet appeared in the string
print(state.count("m"))  # it is case sensitive
print(state.count("M"))
print(state.count("s"))  # if it is not in string it will print 0
print(state.find("m"))  # will print the index of the given
print(
    state.find("M")
)  # if letter are repeated in string then it will print the index number where it occurred for the first time
print(state.find("s"), "\n")  # if character is not in string then it will return -1 (print)

restate = state.replace(
    "MagiC", "Dark Magic will"
)  # it replaces the particular character at index with some other string
print(help(state.replace))  # syntax===> variable_name=variable_name.replace('string_need_to_replace','replace_content')
print(restate, "\n")

again = restate.replace("CoMmeNces", "end soon")
print(
    again, "\n"
)  # nothing will change as replace() is case sensitive take a look at CoMmeNces(in replace) but CoMmeNceS(in string)

restate = restate.replace("CoMmeNceS", "end soon")
print(restate, "\n")

print("again=", again, "\nrestate=", restate)
again = again.replace("Dark Magic", restate)  # you can replace it with variable containing string too
print(again, "\n")
