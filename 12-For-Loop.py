print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nFOR LOOPS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# for loops
print("\n")

# ? range(start : end(excluded) : step(optional))

r = range(1, 20, 3)
for i in r:
    print(i)
print("\n")

list = ["hello", "hi", "byebye"]
for i in list:  # // in JS for (let i of list) >> element  # for (let i in list) >> index
    print(i)
print("\n\n")

tup = ("ratan", "tata", "company")
for i in tup:
    print(i)
print("\n\n")

for i in range(
    1, 11
):  # as seen in above indexing is same. last limit is not printed #by default increment factor is taken as 1
    print(i)
print("\n\n")

for i in range(
    0, 11, 2
):  # syntax of for =====> for (vairable) in range (initial_value,final_value,increment_factor_or_decrement_factor):
    print(i)
print("\n\n")

for i in range(0, 51, 5):
    print(i)
print("\n\n")

for i in range(0, -11, -1):
    print(i)
print("\n")

for i in range(1, 11):
    print(i, " ", end="")  # due to end="" this will give output in single line

print("\n")
# nested for-loop which is core topic so just a glimpse
print("\nNested for-loop example")
for i in range(0, 5):
    for j in range(0, 4):
        print(j)
    print("This is particular statement is in i")

print("\n")
print("2Dimension using for loop")
m = 1
for i in range(1, 4):
    for j in range(1, 4):
        print(m, " ", end="")
        m = m + 1
    print("\n")
    m = 1
