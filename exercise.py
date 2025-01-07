heights = input("Enter height separated by space: ")
H=heights.split()
print(H)#This list is still string
count=0
for i in H: # to count the number of heights entered
   count+=1
print("the number of height = ",count)

for i in range(count):
   H[i]=int(H[i])#To typecast the string list to integer
print(H)

SUM=0
for i in H:
   SUM+=i
print("The sum is : ",SUM)
Average= SUM/count
print("Average height : ",round(Average))