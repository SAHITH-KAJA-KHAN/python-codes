from collections import Counter

t = (1, 3, 2, 3, 4, 3, 5)
counter = Counter(t)

print(counter.most_common(1))  # [(3, 3)] top fequent
print(counter.most_common(2))  # [(3, 3), (1, 1)]  (Top 2 frequent elements)
