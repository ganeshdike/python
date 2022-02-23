#LIST operation
list1=[1,2,3,4,5]
list2=["om","sai","ram","sham"]
list3=['a',1,2,3,"omkar"]
print(list1)
print(list2)
print(list3)

#Nesting List
list4=["ganesh",8,list1,list2]
print(list4)

#Length
print('List1 length:',len(list1))

#Concatnation
print(list1+list2)

#Slicing

print('slicing list1[0:2]=',list1[0:2]) #=> slicing list1[0:2]= [1, 2]
print('slicing list2[1:3]=',list2[1:3]) #=> slicing list2[1:3]= ['sai', 'ram']
print('slicing list4[:2]=',list4[:2]) #=> slicing list4[:2]= ['ganesh', 8]
print('slicing list4[2:]=',list4[2:]) #=> slicing list4[2:]= [[1, 2, 3, 4, 5], ['om', 'sai', 'ram', 'sham']]
print('slicing list1[2]=',list1[2]) #=> slicing list1[2]= 3

#membership
print('om' in list2) #True
print(list1 in list4) #True
print(7 in list1) #False

#Iterating
for i in list2:
	print(i)

#method:append,extend,delete
list1.append(6)
print(list1) # =>[1, 2, 3, 4, 5, 6]

list1.extend("noode")
print(list1)# =>[1, 2, 3, 4, 5, 6, 'n', 'o', 'o', 'd', 'e']

del list1[2:6]
print(list1) # =>[1, 2, 'n', 'o', 'o', 'd', 'e']
