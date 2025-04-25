#methods of dictionary
#item method(used to show paired values)
marks={
    "ram":45,
    "hari":56,
    "krishna":55,
    "rohan":67
}
print(marks.items(),"\n")

#values method prints values of index in dictionary
print(marks.values(),"\n")
#keys method prints index keys in dictionary
print(marks.keys(),"\n")
#update method used to change keyvalues in dictionary
marks.update({"ram":67,"raju":70})
print(marks,"\n")

#get method is used to return keys value
print(marks.get("raju"))

