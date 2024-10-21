
from functools import reduce

my_list = [10, 21, 30, 43, 50, 60, 70]
even_index_elements = reduce(lambda i,sum:i%2==0,filter(lambda x: my_list.index(x) % 2 == 0, my_list))
print(even_index_elements)
