Use of sets and keeps the chain of friends
main sets contains the domain of friends
loop does required iterating identifying relation
make_sets the person in reference not same as value held in sets,
if not the case then reassgins correct value of j. This is because of how the dataset
is you dont need to itearte all
final loop makes a set of arrays(chains of friends) and adds it and return the len


def friendCircles(friends):
    sets = []//students in domain
    for i in range(0, len(friends)):// len of all friends so 5 in this case
        sets.append(i)

    for i in range(1, len(friends)):
        for j in range(0, i)://iterative loop to iterate row and for all cols
            if (friends[i][j]) == "Y":
                sets[make_sets(i, sets)] = make_sets(j, sets)

    res = set([])
    for i in range(0, len(friends))://adds the friends circle sets, direct/indirect
        res.add(make_sets(i, sets))
    return len(res)

takes the user as a node and checks it with the students in the sets->[0,1,2] 
def make_sets(node, sets):
    while sets[node] != node:
        sets[node] = sets[sets[node]]
        node = sets[node]
    return node

//approach for java

take in the array


