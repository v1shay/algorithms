# a=[1, 2, 4, 3, 5, 7, 6, 8, 9, 10]
# for b in range(len(a)):
#     if a[b]==7:
#         print(b)
# import random 
# import time
# b=[5]
# for a in range(0, 10):
#     c=random.randint(0, 20)
#     b.append(c)
# b.sort()
# print(b)
# x=5
# min_index=0
# max_index=9
# while True:
#     mid_index=(min_index+max_index)//2
#     time.sleep(1)
#     print(mid_index)
#     if b[mid_index]==5:
#         print("5 was found in", mid_index)
#         break
#     if b[mid_index]>5:
#         max_index=mid_index-1
#     if b[mid_index]<5:
#         min_index=mid_index+1

# import random
# a=[]
# for b in range(0, 10):
#     c=random.randint(0, 40)
#     a.append(c)

# for e in range(0, 9):
#     for d in range(len(a)-1):
#         if a[d]>a[d+1]:
#             a[d], a[d+1] = a[d+1], a[d]
#         print(a)

# import random
# c=[]
# min_index=0

# for b in range(0, 5):
#     a=random.randint(0,10)
#     c.append(a)
# print(c)
# for d in range(len(c)):
#     smallest=d
#     for i in range(d, len(c)):
#         if c[i]< c[smallest]:
#             smallest=i
#     c[d], c[smallest]=c[smallest], c[d]
# print(c)
    
# import random
# a=[]
# for b in range(0, 5):
#     c=random.randint(0, 100)
#     a.append(c)
# print(a)
# for d in range(1, len(a)):
#     for e in range(d-1, -1, -1):
#         if a[d]>=a[e]:
#             insert_at=e+1
#             break
#         else:
#             insert_at=0
#     f=a.pop(d)
#     a.insert(insert_at, f)
#     print(a)

import time
