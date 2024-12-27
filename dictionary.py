# mydict={
#     "name":"prashant",
#     "empid":1001
# }
# print(mydict)
# print(type(mydict))

# m={
#     101:"a",
#     103:"b",
#     102:"c",
#     105:'r'
# }
# print(m)

# print(m[102])

# m[102]="z"
# print(m[102])

# for x in m:
#     print(x)

# for x in m.values():
#     print(x)

# for x,y in m.items():
#     print(x,y)

# m[104]="j"
# print(m)

# m.pop(104)
# print(m)
# m[104]="j"
# print(m)

# n=m.copy()
# print(n)

# str1="aaabbbcccc"
# d={}
# for i in range(len(str1)):
#     key=str1[i]
#     count=0
#     for j in range(len(str1)):
#         if key==str1[j]:
#             count+=1
#     d[key]=count
# print(d)
# for i,j in d.items():
#     print(i,j,sep='',end='')


# method 1
# n=int(input(''))
# l=[]
# add=0
# for i in range(0,n):
#     m=int(input())
#     l.append(m)
# for j in range(len(l)):
#     diff=0    
#     if j+1 in range(len(l)):
#         if l[j]>l[j+1]:
#             diff=l[j]-l[j+1]
#             add+=diff
#         elif l[j+1]>l[j]:
#             diff=l[j+1]-l[j]
#             add+=diff
# print(add)


# method 2
# n=int(input(''))
# l=[]
# add=0
# for i in range(0,n):
#     m=int(input())
#     l.append(m)
# for j in range(len(l)):
#     diff=0    
#     if j+1 in range(len(l)):
#         add+=abs(l[j]-l[j+1])
# print(add)


# dict={}
# for i in range(1,3):
#     name=input("Enter name>")
#     marks=int(input("Enter marks>"))
#     dict[name]=marks
# while True:
#     name=input("Get marks>")
#     marks=dict.get(name,-1)
#     if marks==-1:
#         print('N.A.')
#     else:
#         print('The student',name,'has got',marks)
#     option=input("Want to find more>")
#     if option=='No':
#         break


# dict={}
# key=0
# for i in range(0,2):
#     k=input()
#     v=int(input())
#     dict[k]=v
# print(dict)
# for i in dict:
#     if i in range(len(dict)):
#         if dict[i]<dict[i+1]:
#             print(i)


# dict={
#     'a':'',
#     'b':'2',
#     'c':'2'
# }
# count=0
# for i in dict:
#     if dict[i] != '':
#         count+=1
# print(count)

# s="abbbabbbbabababaaaaaba"
# s1=s.replace('a','b')
# print(s1)


#remove keyvalue pairs from a dictionary
#merge two dictionary
#chek if key exist in a dictionary
#reverse dictionary
#median value of dictionary

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# b={'a':1,'b':2}
# print(b['a','b'])

# ar={}
# ar[1]=1
# ar['1']=2
# ar[1]+=1
# sum=0
# for k in ar:
#     sum+=ar[k]
# print(sum)

# b={}
# c={}
# j={}
# b['bi']=1
# b['ci']=3
# j['jj']=4
# c['b']=b
# c['j']=j
# print(len(c[b]))

a={'b':3,'a':4,'c':5}
for _ in sorted(a):
    print(a[_])
b=a.copy()
print(id(b)==id(a))