##WAP to apply 10% discount on each item
iteams = {'papers': 50, 'book':45, 'pens':30,'sketches':60, 'board':120}
discount = {}
for iteam,price in iteams.items():
    discount[iteam] = price * 0.9
    
print(discount)

discount = {iteam: price * 0.9 for iteam , price in iteams.items()}
print(discount)