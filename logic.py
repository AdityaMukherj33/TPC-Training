# name='programming'
# new=''
# for i in name:
#     if i not in new:
#         new+=i
# print(new)

# # # # # # # #List-Stores order-wise data
# # # # # # #     #  -Duplicate values allowed
# # # # # # #     #  -Heterogenous Data
# # # # # # #     #  -Growable
# # # # # # #     #  -Mutable

# mylist=['a','b','g',45,60.5]
# print(type(mylist))
# print(mylist[1:4:2])
# print(mylist[-1:-5:-1])
# mylist[0]='b'
# print(mylist)
# mylist.append('h')
# print(mylist)
# mylist.insert(3,'x')
# print(mylist)
# mylist.remove('h')
# print(mylist)
# new=mylist.copy()
# print(new)

# # # # # # # mine=[[1,2,3],[4,5,6],[7,8,9]]
# # # # # # # print(mine[1][2])
# # # # # # # print(mine[0:1][0:2])

# # # # # # # list2=[1,2,3,4]
# # # # # # # del list2[2]
# # # # # # # print(list2)
# # # # # # # list2.clear()
# # # # # # # print(list2)

# # # # # # n='amdsss'
# # # # # # my=list(n)
# # # # # # print(my)
# # # # # # my.reverse()
# # # # # # print(my)
# # # # # # me=my
# # # # # # print(id(me))
# # # # # # print(id(my))
# # # # # # print(my.count('s'))

# # # # # #palindrome below
# # # # # str=input("enter>")
# # # # # n=list(str)
# # # # # m=n.copy()
# # # # # m.reverse()
# # # # # if n==m:
# # # # #     print("Yes")
# # # # # else:
# # # # #     print("No")

# # # # liss=[1,2,3,2,1,3,4]
# # # # for i in liss:
# # # #     if liss.count(i)==1:
# # # #         print(i)

# # # mylist=[1,2,2,3,2,4]
# # # new=[]
# # # for i in mylist:
# # #     if mylist.count(i)==1:
# # #         new.append(i)
# # # print(new)

# # l1=[1,2,3,4]
# # l2=[3,4,5,6]
# # new=[]
# # for i in l1:
# #     if i in l2:
# #         new.append(i)
# # print(new)

# l1=[1,2,1,1,1,2,2,1,1,1,1]
# l2=[]
# c=0
# for i in l1:
#     if i==1:
#         c+=1
#     else:
#         l2.append(c)
#         c=0
# l2.append(c)
# print(l2)

# def new_func():
#     A=[1,2,3]
#     B=[2,3,4]
#     C=[3,4,5]
#     D=[]
#     for i in A:
#         if i in B and i in C:
#             D.append(i)
#     print(D)

# new_func()

# l1=[0,1,0,13,2]
# for i in l1:
#     if i==0:
#         l1.remove(i)
#         l1.append(i)
# print(l1)

# str1=input("enter>")
# str2=input("enter>")
# a=list(str1)
# b=list(str2)
# a.sort()
# b.sort()
# if a==b:
#     print("y")

l=['a','a','a','b','b']
c=0
l1=[]
str1=''
for i in range(1,len(l)):
    if l.index(i)==l.index(i+1):
        c+=1
    else:
        l1.append(i)
        l1.append(c)
        c=0
l1.append(i)
l1.append(c)
print(l1)