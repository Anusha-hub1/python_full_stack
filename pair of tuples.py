##Creating Tuples of Pairs.
alps = ['a', 'b', 'c']
let = [1,2]
pair = []
#for a in alps:
    #for l in let:
    # pair.append((a,l))
#print(pair)

pair = [(a,l) for a in alps for l in let ]
print(pair)
    