# Addition
#add = lambda x, y: x + y
#print(add(5, 3))  

# Multiplication
#multiply = lambda x, y: x * y
#print(multiply(4, 6))  

# Squaring a number
#square = lambda x: x ** 2
#print(square(7)) 


# Conditional statements (if-else)
#is_odd_even = lambda num: 'even' if num%2==0 else 'odd'
#print(is_odd_even(98))

##With higher-order functions map() and filter()
#map()Applies a function to every item in an iterable.
##filter() Creates a new iterable with elements that satisfy a given condition


### Square each number in the list
inputs = [1,2,3,4,5,6]
#squ_input= list(map(lambda x:x*2, inputs))
#print(squ_input)

##Creates a new iterable with elements that satisfy a given condition
even_num = list(filter(lambda x:x%2==0, inputs))
print(even_num)

data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
# Sort by the second element (the fruit name)
sorted_by_name = sorted(data, key=lambda x: x[1])
print(sorted_by_name) 