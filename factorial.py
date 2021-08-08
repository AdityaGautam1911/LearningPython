# a=eval(input('enter number'))
# fact=1
# while a>=1:
#   fact*=a
#   a-=1
# print(fact)
a=eval(input("enter number here--->"))
fact=1
for i in range(1,a+1):
    fact*=i
print("factorial of",a," is--->",fact)