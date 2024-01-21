# name = "adityanow"

# character = "a"

# if character in name:
#     name = name[:5] + name[6:]

# print(name)








# key = "secureisamyth"

# temp_key = ""

# for i in range(len(key)):
#     if key[i] not in temp_key:
#         temp_key = temp_key + key[i]

# key = temp_key

# print(key)



secret_key_matrix = [ ["#" for i in range(5)] for j in range(5)]

for row in (secret_key_matrix):
    print(id(row))
    print(row)
    
    
secret_key_matrix[0][0] = "s"

print("Transform :\n")

for row in (secret_key_matrix):
    print(id(row))    
    print(row)
        
   