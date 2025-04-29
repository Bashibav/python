#program to check given word(name) mentioned on post or not
post=input("Enter the post: ")
name=input("Enter word: ")
if(name.lower()in post.lower()):
    print("\nThe given word mentioned in the given post.")
else:
    print(" \nthe given word is not found.")