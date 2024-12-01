# dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121,12: 144, 13: 169, 14: 196, 15: 225}
# total_sum = 0
# for value in dict1.values():
#     total_sum += value
# print("The sum of all the items in the dictionary is:", total_sum)

# list1 = [2, 3, 4, 1, 32, 4]
# list1.append(15)
# print(list1)
# a=list1.count(3)
# print(a)
# list2=[3,4]
# list1.extend(list2)
# print(list1)
# b=list1.index(2)
# list1.insert(1,4)
# print(list1)

# list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
# list1.pop(5)
# print(list1)
# list1.remove(3)
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)

# items = "Jane John Peter Susan".split()
# print(items)

# item = "09/20/2012".split("/")
# print(item)



# lst = [30, 1, 2, 1, 0]
# a=(lst.append(40))
# print(a)
# b=(lst.extend([1, 43]))
# print(b)
# c=(lst.remove(1))
# print(c)
# d=(lst.pop(1))
# print(d)
# e=(lst.pop())
# print(e)
# f=(lst.sort())
# print(f)
# g=(lst.reverse())
# print(g)
# import random
# h=(random.shuffle(lst))
# print(h)

# list1 = [30, 1, 2, 1, 0]
# list2 = [1, 21, 13]
# print(list1 + list2)
# print(2 * list2)
# print(list2 * 2)
# print(list1[1 : 3])
# print(list1[3])

# list1 = [30, 1, 2, 1, 0]
# a=[x for x in list1 if x > 1]
# print(a)
# b=[x for x in range(0, 10, 2)]
# print(b)
# c=[x for x in range(10, 0, -2)]
# print(c)

list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]
print(list1 < list2)
print(list1 <= list2)
print(list1 == list2)
print(list1 != list2)
print(list1 > list2)
print(list1 >= list2)