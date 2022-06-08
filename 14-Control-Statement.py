print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nCONTROL STATEMENTS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# * 1.BREAK  2.CONTINUE  3.PASS
# BREAK & CONTINUE can be used with if statement if any condition is to be satisfied for break and continue to execute
print("\n")
# BREAK will terminate the loop and will pass the execute control outside the loop
print("Break example")
c = 0
while c < 6:
    c = c + 1
    if c == 4:
        break  # when c became 4 break got executed and it passed te execute control outside the loop
    print(c)
print("Yippee!!! I am outside the loop and 4 5 6 didn't got printed")

# CONTINUE will pass the execute control to starting of the loop without letting control to execute further for given condition
print("\nContinue example")
c = 0
while c < 10:
    c = c + 1
    if c % 2 == 0:
        continue  # as condition is satisfied continue is executed and execution control was directly passed to starting of the loop without further execution
    print(c)

# PASS it is nothing but simply null function which just occupies space
print("\nPass example")
c = 0
while c < 6:
    c = c + 1
    pass
    print(c)
