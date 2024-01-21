# keyed_columnar_transposition_cipher aka columnar_transposition_cipher

# no_of_rows , no_of_columns, key_dictionary are secretly shared between the sender and reciever

def  generate_empty_matrix(no_of_rows,no_of_columns):
    return [["#" for i in range(no_of_columns)] for i in range(no_of_rows)]

def sender_side():
    print("\n\nAt the sender side : ")
    key_dictionary = {3:1,1:2,4:3,5:4,2:5}
    print("Enter Plain Text (Note : The plain text cannot be more than 20 characters long):")
    plain_text = input()
    # plain_text = "enemyattackstonight"

    if len(plain_text) > 20:
        print("The message is too long !!!")
        exit

    no_of_rows = 4
    no_of_columns = 5
    counter = 0

    matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    # filling the plain text into the matrix row by row 
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            if(counter >= len(plain_text)):
                break
            matrix[i][j] = plain_text[counter]
            counter += 1

    print("The matrix formed at the sender side is : ")
    print(matrix)

    cipher_text = ""
    
    # reordering the columns of "matrix" as per key_dictionary to get "reordered_matrix"
    reordered_matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    for column_of_matrix,column_of_reordered_matrix in key_dictionary.items():
        for j in range(no_of_rows):
            reordered_matrix[j][column_of_reordered_matrix-1] = matrix[j][column_of_matrix-1]
    
    print("Reordered matrix is : ")
    print(reordered_matrix)
    
    # create cipher text from the reordered_matrix by reading the matrix column by column
    for i in range(no_of_columns):
        for j in range(no_of_rows):
            cipher_text += reordered_matrix[j][i]
            
    print("The cipher text enciphered at sender side is : ",cipher_text)
    
    return cipher_text

def reciever_side(cipher_text):
    print("\n\n\nAt the reciever side : ")
    key_dictionary = {1:3,2:1,3:4,4:5,5:2} # this key value pair is the opposite of what we have at the sender side
    no_of_rows = 4
    no_of_columns = 5
    counter = 0
    
    reordered_matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    # fill the matrix column by column
    for i in range(no_of_columns):
        for j in range(no_of_rows):
            reordered_matrix[j][i] = cipher_text[counter]
            counter += 1
    
    print("The reordered_matrix formed at the reciever side : ")
    print(reordered_matrix)
    
    # reordering the columns of "reordered_matrix" as per key_dictionary to get "matrix"
    matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    for column_of_reordered_matrix,column_of_matrix in key_dictionary.items():
        for j in range(no_of_rows):
            matrix[j][column_of_matrix-1] = reordered_matrix[j][column_of_reordered_matrix-1] 
    
    print("The matrix on decrypting the reordered matrix is : ")
    print(matrix)
    
           
    
    # make the plain text by reading the matrix row by row
    deciphered_plain_text = ""
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            deciphered_plain_text += matrix[i][j]
    
    print("\nDeciphered Plain Text with bogus characters : ")
    print(deciphered_plain_text)
    
    deciphered_plain_text = deciphered_plain_text.replace("#","")
    
    print("\nDeciphered Plain Text : ")
    print(deciphered_plain_text)

def main():
    cipher_text = sender_side()
    reciever_side(cipher_text)
    

if __name__ == "__main__":
    main()