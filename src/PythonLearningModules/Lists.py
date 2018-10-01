'''
- Lists stores any values like int, str. similar to array.
- syntax is varname = ['val1','val2'] 
'''

names = ["pankaj","sandip","anil","kishor","ram","ajay","bhupesh","sneha","julia","robert","dany"]
#print(names)
''''''
i=0
newnames = []
for i in range (0,11):
    x = names[i]
    newnames.append(x)
    print (newnames[i])
    
''''''
names.extend(newnames)
print(names)

''''''
print(len(names))
print(len(newnames))

''''''
#slices
print(names[1:-17])
