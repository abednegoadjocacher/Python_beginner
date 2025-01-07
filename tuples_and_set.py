#Operations on sets
set1={1,2,3,4,6,8}
set2={45,4,6,7,8,89}
set3={3,5,67,78,5}
print(set1.union(set2)) 
print("The intersect:",set1.intersection(set2))
print("The difference:",set1.difference(set2))
print(set2-set1)
print("Symmetric:",set1.symmetric_difference(set2))
print("Disjoint:",set1.isdisjoint(set2))
print("subset:",set1.issubset(set2))
print("superset:",set1.issuperset(set2))
#set3.clear()
del set3
print("Set3 cleared",set3)



#mark_tuples=(12,3,4,5,6,75,44,32,8)
#print(mark_tuples)
#print(type(mark_tuples))
#
#
##Set
#
#set_mark={34,3,342,12,3,4,532,1,3,45}
#set_mark.add(100)
#print("The set: ",set_mark)


