##Dict Comprehension — Pass/Fail Map
names = ['Rita','Sita','Mita','Vita']
scores = [45,56,23,67,16]
result = {}
for name,score in zip(names,scores):
    if score>=35:
        result[name] = "Pass"
    else:
        result[name] = 'Fail'
print(result)


result = {names[i]:('Pass' if scores[i] >=35 else 'fail') for i in range(len(names))}
print(result)