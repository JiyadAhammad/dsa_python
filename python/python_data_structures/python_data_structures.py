"""
1. List Learn: Indexing Slicing Insert Append Extend Remove Pop Sort
Reverse List copying
2. Tuple Immutable collections Tuple unpacking Nested tuples
3. Set Union Intersection Difference Symmetric difference Membership testing
4.Dictionary Master: keys() values() items() get() pop() update() setdefault()
5.Comprehensions list comprehension set comprehension dict comprehension
Important Understand:
List → ordered,
mutable Tuple → ordered,
immutable Set → unique values Dictionary → key-value mapping Practice
"""

same_data = ["list", ("tuple",), {"set"}, {"k": "dict"}]

for c in same_data:
    print(type(c).__name__)

print("same job — hold many values — four different rules")


## =========================================================
# 1. List
sample_list = [0, 1, 2, 3, 4, 5, 6]
n = len(sample_list)

sample_list[0]  # first element
sample_list[-1]  # last element

for i in range(0, n):  # Forward iteration from 0 -> n
    pass

for i in range(n - 1, -1, -1):  # Backward iteration from n -> 0
    pass

# 2. Slicing
print(sample_list[1:4])  #  items from 1 –> 3, # subset
print(sample_list[int(n / 2) : n])  # (n//2)  items from mid –> end, # subset
print(sample_list[::2])  # every second item
print(sample_list[::-1])  # reversed.
print(sample_list[::-2])  # every second item reversed

# 3. insert()
sample_list.insert(1, 0.5)  # puts 99 at index 1, shifting the rest right.
print(sample_list)

# 4. append()
sample_list.append(7)  # adds one item to the end.
print(sample_list)

# 5. extend() -> (addAll)
sample_list.extend([8, 9])  # appends each item of another iterable individually.
print(sample_list)

# 6. remove()
sample_list.remove(0.5)  # deletes the first item that equals 3, by value.
print(sample_list)

# 7. pop()
sample_list.pop()  # removes & returns the last item;
print(sample_list)

sample_list.pop(0)  # removes & returns by index.
print(sample_list)

# 8. sort() / reverse()
sample_list.sort()  # orders in place;
print(sample_list)

new_list = sorted(sample_list)  # Creates a new sorted list:


sample_list.reverse()  # flips order in place.
print(sample_list)

# 9. List copying
b = sample_list  # copies the reference.
b.append(10)
print(f"copy reference {b}")
# copies the data.
b = sample_list.copy()
b.append(11)
print(b)
b = sample_list[:]
print(b)
