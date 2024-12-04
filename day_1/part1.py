l1 = []
l2 = []

with open('input_day1.txt', 'r') as file:
    for line in file:
        nums = line.split()
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))

l1.sort()
l2.sort()

distance = 0

for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])

print(distance)