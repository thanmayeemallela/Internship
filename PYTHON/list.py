l1=[10,20,30,5]
print(l1)
l2=[x for x in l1 if x%2==0]
print("even numbers=",l2)
l2=[x for x in l1 if x%2!=0]
print("odd numbers=",l2)
l1.append(15)
l1.extend([20,25])
l3=l1.copy()
l3=l2+[100]
print(l3)
l1.sort()
print("minimum=",l1[0]) 
l1.reverse()
print("maximum=",l1[0])
print("list=",l1)
print("popped value=",l1.pop())
l1.remove(20)
print("list after removing the 20",l1)
l1.clear()
print("list1 is cleared=",l1)

