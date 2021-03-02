
nums = []
with open("data.txt", "r") as file:
    for line in file:
        nums.append(int(line.rstrip("\n")))

print(nums)

