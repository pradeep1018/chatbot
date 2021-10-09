from itertools import permutations

Entities_list=["kolkata", "delhi","mumbai"]
utterance_list=["How far is <> from <>", "How is the weather in <>"]
output = []

x = len(Entities_list)
l = [*range(1, x+1, 1)]

for utterance in utterance_list:
    n = utterance.count("<>")
    p = list(permutations(l,n))
    print(p)
    for entity in Entities_list:
        s = utterance.replace("<>",entity)
        output.append(s)
    
print(output)