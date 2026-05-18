#pracitcing and revising dictionaries in python

PERSON={
    "Name":"John",
    "Age":30,
    "City":"New York"
}
#print(PERSON["department"]) #this will give an error because there is no key called department in the dictionary

PERSON["department"]="IT"#as dictionaries are mutable we can add new key value pairs to the dictionary
print(PERSON)
#same syntax can be used to update the value of an existing key
#for example 
PERSON["Age"]=31
print(PERSON)
d = {
    "x": 1,
    "x": 2,
    "x": 3,
    "y": 4
}

print(d)
#In the above code we have defined a dictionary with three key value pairs but all the keys are the same "x". In a dictionary, keys must be unique. When we define a dictionary with duplicate keys, only the last key-value pair will be retained. Therefore, in this case, the dictionary will only contain one key "x" with the value 3. The output of the above code will be {'x': 3}.
#there also exist a del function
del PERSON["City"] #this will delete the key value pair with key "City" from the dictionary
print(PERSON)
#ummm.or we can clear the entire dictionary using the clear method
PERSON.clear() #this will clear all the key value pairs from the dictionary
print(PERSON)

#well
x=d.pop("x") #this will remove the key "x" from the dictionary and return its value
print(x) # this will print the value of "x" which is 3
print(d) # this will print the dictionary after removing the key "x" which is {'y': 4}  