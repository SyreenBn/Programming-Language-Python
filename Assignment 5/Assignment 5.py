import random
#my_list = [44, 90, 30, 87, 93, 49, 74, 7, 3, 82]

my_list = []
i = 0
for i in range(0,10):
    x = random.randint(1,100)
    my_list.append(x)
    
copy_list = my_list[:]
copy_list.sort()
while (my_list != copy_list):
    print ("Current list of numbers: ", my_list)
    rev_num = int(input("How many numbers would you like to reverse?"))-1
    counter = 0
    s = 0
    temp = ""
    for s in range (0,rev_num):
        if (counter < rev_num):
            temp = my_list[s]
            my_list[s] = my_list[rev_num]
            my_list[rev_num] = temp
            rev_num = rev_num - 1
            counter = counter +1
print ("Final sorted list: ", my_list)
