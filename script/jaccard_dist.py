def compute(a,b):
  intersection_count = len(a.intersection(b))
  union_count = len(a.union(b))
  similarity = (intersection_count/union_count)
  distance = (1-similarity)
  return distance
