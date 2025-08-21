# Without list comprehension
li = []
for i in range(10):
    li.append(i**3)

print(li)  

# With list comprehension
li2 = [x**3 for x in range(10)]
print(li2)



# 10 times 5 in a list
li3 = [5] * 10


li4 = [(i,j) for i in range(5) for j in range(4)]
print(li4)


# [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
li5 = [[i for i in range(4) if i!=j]for j in range(3)]
print(li5)