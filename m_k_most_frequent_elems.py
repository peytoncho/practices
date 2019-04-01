import collections

def k_most_frequent_elem(nums, k):
    return [a[0] for a in collections.Counter(nums).most_common(k)]

nums = [2,2,2,5,5,3,3,3,3]
k = 3
print(k_most_frequent_elem(nums, k))