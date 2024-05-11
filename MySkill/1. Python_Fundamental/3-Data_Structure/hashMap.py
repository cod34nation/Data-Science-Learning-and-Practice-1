def printdic (d) :
    for key in d :
        print (key, " -> ", d[key])

hashmap = {1: 'first', 2: 'second'}
printdic (hashmap)
print()

hashmap[4] = 'fifth'
printdic(hashmap)
print()


hashmap.popitem()
printdic(hashmap)