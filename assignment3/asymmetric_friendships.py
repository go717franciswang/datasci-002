import MapReduce
import sys

"""
Get (A, B) if B is not friend of A but A is friend of B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    a, b = record
    mr.emit_intermediate(tuple(record), 1)
    mr.emit_intermediate((b, a), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) == 1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
