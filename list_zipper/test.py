import zippers
from pprint import pprint

cities = ['Salvador','Ubatuba','Belo Horizonte']
states = ['BA','SP','MG','RJ','PE']

pprint(zippers.zip_smallest(cities,states))
print()
pprint(zippers.zip_longest(cities,states))