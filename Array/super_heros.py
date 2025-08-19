heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print("Length of the List :" , len(heros))

# 2. Add element at the end of the list
heros.append("black panther")
print("Updated list :" , heros)

# 3. Remove black panther and add after hulk
heros.remove("black panther")
print(heros)

heros.insert(3, "black panther")
print("Updated list :" , heros)

# 4. Remove and replace
heros[1:3] = ["doctor strange"]
print("Updated list :" , heros)

# 5. sort alphabetically
heros.sort()
print("sorted list :" , heros)