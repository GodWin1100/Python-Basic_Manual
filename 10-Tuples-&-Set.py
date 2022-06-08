print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nTUPLES\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Tuples  #you cant change content of tuples nor u can delete but u can add tuples
print("\n")
tup = ("happy", "sad", "angry", "mild")
print(tup)
print(tup[0])

print("\n")
# * tup[0]='lol'  #this cannot be compiled it will show error
print(tup)

print("\n")
tup2 = ("laugh", "cry", "sob")
tup3 = tup2 + tup
print(tup3)

print("\n")
del tup3  # tuple can be deleted as a whole
print(tup)
print(len(tup))
print(tup2[0:4])  # printing of elements is same as list
print("\n")

# List to Tuple
lst = ["hello", "this", 15, "list"]
tple = tuple(lst)
print(lst, type(lst))
print(tple, type(tple))


print("\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nSET\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# There is no indexing in sets, repeated elements are treated as single only insert and delete can be perform
s = {4, 5, "sdf", "heelo", 54, 54, 4, 5, "sdf"}
print(s, type(s))
s.update([88, 99])
print(s)
s.remove("heelo")
print(s)
print("\n")

# FrozenSet no operation can be done
f = frozenset(s)
print(f, type(f))

# List to set
lst = [5, 6, 8, 324, 45]  #'hello','bye']
print("Given List : ", lst)
st = set(lst)
print("set : ", st, " and its type is ", type(st))
print(sorted(st))
