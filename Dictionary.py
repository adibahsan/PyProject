words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print(words["Hello"])
print(words["No"])


dict = {}
dict['Ford'] = "Car"
dict['Python'] = "The Python Programming Language"
dict[2] = "This sentence is stored here."

print(dict['Ford'])
print(dict['Python'])
print(dict[2])


words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print(words)           # print key-pairs.
del words["Yes"]       # delete a key-pair.
print(words)           # print key-pairs.
words["Yes"] = "Oui!"  # add new key-pair.
print(words)           # print key-pairs.