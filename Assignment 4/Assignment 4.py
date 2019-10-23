count = 1
first_file = open("in1.txt", "r")
word1 = first_file.readline()
second_file = open("in2.txt", "r")
word2 = second_file.readline()
output_file = open("out.txt","w")
while (count <= 100):
    if word1 < word2 and word1 !="":
        min_value = word1
        output_file.write(min_value)
        word1 = first_file.readline()
    elif word2 < word1 and word1 !="": 
        min_value = word2
        output_file.write(min_value)
        word2 = second_file.readline()
    else:
        output_file.write(word1)
        output_file.write(word2)
        word1 = first_file.readline()
        word2 = second_file.readline()
    count = count + 1
