import csv
from collections import Counter

with open('i:/vscode/adventofcode2024/src/day1/input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
    left_list = []
    right_list = []
    for item in data:
        left_list.append(item[0])
        right_list.append(item[1])
        
        
    # left list organize least to greatest
    left_list.sort()
    # right list organize least to greatest
    right_list.sort()
    # get difference between each pair
    diff = [abs(int(left) - int(right)) for left, right in zip(left_list, right_list)]
    # print(len(diff))
    # add differences in running sum
    difference_total = sum(diff)
    # print total sum of differences
    print(difference_total)

    # print(diff)
    
    
    # ANS: 1873376
    
    right_count = Counter(right_list)
    similarity_score = sum(int(num) * int(right_count[num]) for num in left_list)
    print(similarity_score)
    
    # ANS: 18997088