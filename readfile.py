# data = []
count = 0
with open('reviews.txt', 'r') as f:
    # for line in f:
    #     if line != '\n':
    #             if len(line) <= 50:
    #                     data.append(line)
    d = [line for line in f if len(line) <= 50 and line != '\n' and 'love' in line]
print(len(d)) 
for x in d:
    print(x)
# print(data)
