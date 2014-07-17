import MapReduce
import sys

"""
Join order and line_item by order_id
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orders = []
    line_items = []
    for v in list_of_values:
        if v[0] == 'order':
            orders.append(v)
        else:
            line_items.append(v)

    for o in orders:
        for l in line_items:
            mr.emit(o + l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
