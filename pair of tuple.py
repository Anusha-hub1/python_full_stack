##Creating a dictionary from two lists (keys and values):
keys = ['a', 'b', 'c']
values = [10, 20, 30]
dic = {}
#for i in range (len(keys)):
      #  dic[keys[i]] = values[i]
        
#print(dic)
        
dic = {k:v for k,v in range zip(keys,values)}  ##zip → pairs items together:
print(dic)