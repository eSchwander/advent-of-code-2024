from collections import defaultdict

l1 = []
l2 = defaultdict(int)

with open('input_day1.txt', 'r') as file:
    for line in file:
        nums = line.split()
        l1.append(int(nums[0]))
        l2[int(nums[1])] = l2[int(nums[1])] + 1

similarity_score = 0

for num in l1:
    similarity_score += num * l2[num]

print(similarity_score)