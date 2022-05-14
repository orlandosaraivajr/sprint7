import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')
cProfile.run('sum((i * 2 for i in range(10000)))')
cProfile.run('sum([i * 2 for i in range(10000000)])')
cProfile.run('sum((i * 2 for i in range(10000000)))')
