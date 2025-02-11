# 1.
name = input("Your name: ")
out_file = open("data.txt", "w")
out_file.write(name)
out_file.close()

# # 2.
in_file = open("data.txt", "r")
name = in_file.read()
print(f"Hi {name}!")
in_file.close()

# 3.
sum = 0
with open("numbers.txt", "r") as in_file:
    for i in range(2):
        sum += int(in_file.readline())
print(sum)

# 4.
sum = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        sum += int(line)
print(sum)
