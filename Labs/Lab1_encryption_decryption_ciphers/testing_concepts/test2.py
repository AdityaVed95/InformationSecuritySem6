secret_key_matrix = [ ["#"] * 5 ] * 5

for row in (secret_key_matrix):
    print(id(row))
    print(row)

    
    
secret_key_matrix[0][0] = "s"

print("Transform :\n")

for row in (secret_key_matrix):
    print(id(row))
    print(row)