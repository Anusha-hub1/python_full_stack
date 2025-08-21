##Squares of even nums


num = []
#for i in range(1,11):
  # if i%2==0:
  #    num.append(i*i)
        
#print(num)
num = list(range(1,11))
num = [i*i for i in num if i%2==0]
print(num)