List1 = [1,2,3,4,5,7,8]
List2 = ["a","b","c","d","e"]
print({List1[item] : index for item, index in enumerate(List2)})


