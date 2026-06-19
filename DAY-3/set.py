# Simple Set Operations Program
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("set1:", set1)
print("set2:", set2)    
# Add
set1.add(10)
print(set1)
# Update
set1.update({11, 12})
print(set1)
# Union
print("Union:", set1 | set2)
# Intersection
print("Intersection:", set1 & set2)
# Difference
print("Difference:", set1 - set2)
# Symmetric Difference
print(set1.symmetric_difference(set2))
# Remove
s = {1, 2, 3, 4}
s.remove(3)
print(s)
# Discard
s.discard(5)
print(s)
# Pop
s2 = {1, 2, 3}
popped = s2.pop()
print(s2)
# Clear
s3 = {1, 2, 3}
s3.clear()
print(s3)
# Check subset
print({1, 2}.issubset({1, 2, 3, 4}))
# Check superset
print({1, 2, 3, 4}.issuperset({1, 2}))
# Check membership
print(2 in {1, 2, 3})