#string slicing (+ve)
name="toyaraj"
namesplit=name[0:5] #print from 0 to 4 excluding 5th character
print(namesplit)
character=name[6] # print 7 th charracter count start from 0
print(character)

#stirng slicing (-ve)

name="toyaraj bhatt"
print(name[-5:]) #is same as [-5:-1]
print(name[:8]) #is same as [0:8]

# string slicing skip

word="9809470966"
print(word[2:6:9])