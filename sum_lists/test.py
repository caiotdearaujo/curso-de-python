from pprint import pprint
from sum_lists import sum_lists

list1 = [i+1 for i in range(7)]
list2 = [i+1 for i in range(4)]

pprint(sum_lists(list1,list2,mode="s"))