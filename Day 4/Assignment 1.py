test_str = "what we think we become; we are Python programmer"
test_sub = "we"
print("The original string is : " + test_str)  
print("The substring to find : " + test_sub) 
 
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
 
print("The start indices of the substrings are : " + str(res)) 
