# def outer(n):
#     def inner(x):
#         return x * n
#     return inner
# multi = outer(2)
# print(multi(5))

ls = [1,2,3,4,5,6,7]

ev = [x for x in ls if x % 2 ==0]

od = [x for x in ls if x % 2 !=0]

print("evens are",ev)
print("odds are", od)