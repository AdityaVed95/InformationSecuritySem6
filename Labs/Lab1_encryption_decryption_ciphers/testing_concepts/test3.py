secret_key_matrix = ["#"] * 5


for item in secret_key_matrix:
    print(item)
    print(id(item))

print("Now after changing 0th element : ")
        
secret_key_matrix[0] = "$"

for item in secret_key_matrix:
    print(item)
    print(id(item))