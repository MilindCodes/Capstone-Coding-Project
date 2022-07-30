
temp_dict = {"ONE" : 1, "TWO" : 2, "THREE" : 3, "FOUR" : 4}
key_values = temp_dict.keys()

list_key_values = list(key_values)

'''
print(type(key_values))
print(key_values)

print(type(list_key_values))
print(list_key_values)
'''

'''
PLAYING AROUND WITH THE ENUMERATE FUNCTION
'''

#l1 = ["ZERO", "ONE", "TWO", "THREE", "FOUR"]

d1 = {"ONE" : 1, "TWO" : 2, "THREE" : 3, "FOUR" : 4, "FIVE" : 5}



for i,j in enumerate(d1):
    print(i,j)