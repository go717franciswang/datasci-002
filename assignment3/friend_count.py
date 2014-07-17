import MapReduce
import sys

"""
Count the number of friends each person has
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    a, b = record
    mr.emit_intermediate(a, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
