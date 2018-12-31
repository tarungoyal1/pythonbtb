from itertools import islice, count
nums  = [x for x in islice(count(), 100)]
print(nums)
