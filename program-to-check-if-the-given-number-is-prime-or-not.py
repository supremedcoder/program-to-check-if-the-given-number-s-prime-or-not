# num=61
# flag=0
# for i in range(2,num):
#      if num%i==0:
#         flag=1
#         break
# if flag==1:
#     print("not a Prime number")
# else:
#     print("Prime number")

# for num in range(20000,):
#     def checkPrime(num,iter=2):
#         if num == iter:
#             return True
#         if num%iter==0:
#             return False
#         if num<2:
#             return False
#         return checkPrime(num,iter+1)
#     if checkPrime(num)==True:
#         print(num ," :-  Prime")
#     else:
#         print(num ," :- Not prime")
b=[]
c=[]
for i in range(999999000,10000000000):
    for j in range(2,10000000000):
        if i%j==0:

            if i==j:
                if i>2:
                    c.append(i)
                    break
            b.append(i)
            break
        elif i==j:
            if i%2!=0:
                c.append(i)
                break 
# print(b)
print(c)
