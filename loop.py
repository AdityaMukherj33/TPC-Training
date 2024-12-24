# n=int(input('enter>'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(65+j-1),end=' ')
#     print('')
# if(i>n-1):
#     for k in range(1,n+1):
#             for m in range(1,n+1-k):
#                print(chr(65+m-1),end=' ')
#             print('')

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50
# print(a)

def f(i,v=[]):
    v.append(i)
    print(v)
f(1)
f(2)
f(3)