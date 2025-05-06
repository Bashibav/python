#program to read txt file and find if if contains  specific word or not
st=( '''
    They talk all day
and when it starts to get dark
they lower their voices
to converse with their own shadows
and with the silence.

They are like everybody
—the parakeets—
all day chatter,
and at night bad dreams.

With their gold rings
on their clever faces,
brilliant feathers
and the heart restless
with speech...

They are like everybody,
—the parakeets—
the ones that talk best
have separate cages.
    ''')
with open("poem.txt","w") as p:
    p.write(st)
with open("poem.txt") as p:
    print(p.read())
word=input("Enter word to find: ")
with open("poem.txt") as p:
    poem=p.read()
    if (word in poem):
         print(f"The word {word} is  present in poem.")
    else:
         print(f"The word {word} is not  present in poem.")