for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
                                                          #{0} , {1},   {2}


for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))    #formated display
                                                                 #{0} , {1},   {2}

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))    #formated display, indent to left

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:<12f}".format(22 / 7))
print("Pi is approximately {0:<12.50}".format(22 / 7))
print("Pi is approximately {0:<52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))


name="Sipho"
age=22
print("My name is {0} and i am {1} years old".format(name,age))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))    #formated display
                                                                 #{0} , {1},   {2}