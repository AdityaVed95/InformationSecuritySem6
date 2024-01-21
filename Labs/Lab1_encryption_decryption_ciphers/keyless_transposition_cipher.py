# no_of_rows and no_of_columns are secretly shared between the sender and reciver.

def  generate_empty_matrix(no_of_rows,no_of_columns):
    return [["#" for i in range(no_of_columns)] for i in range(no_of_rows)]


def sender_side():
    
    print("\n\nAt the sender side : \nEnter Plain Text (Note : The plain text cannot be more than 16 characters long):")
    plain_text = input()
    # plain_text = "meetmeatthepark"

    if len(plain_text) > 16:
        print("The message is too long !!!")
        exit

    no_of_rows = 4
    no_of_columns = 4
    counter = 0

    matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    # filling the plain text into the matrix row by row 
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            if(counter >= len(plain_text)):
                break
            matrix[i][j] = plain_text[counter]
            counter += 1

    print("The matrix formed at the sender side is : ",matrix)

    cipher_text = ""

    # create cipher text from the matrix by reading the matrix column by column
    for i in range(no_of_columns):
        for j in range(no_of_rows):
            cipher_text += matrix[j][i]
            
    print("The cipher text enciphered at sender side is : ",cipher_text)
    return cipher_text  


def reciever_side(cipher_text : str):
    print("\n\nAt the reciever side : ")
    print("The cipher text obtained is : ",cipher_text)
    no_of_rows = 4
    no_of_columns = 4
    counter = 0

    matrix = generate_empty_matrix(no_of_rows,no_of_columns)
    
    # fill the matrix column by column
    for i in range(no_of_columns):
        for j in range(no_of_rows):
            matrix[j][i] = cipher_text[counter]
            counter += 1
    
    print("The matrix formed at the reciever side : ",matrix)
    
    deciphered_plain_text = ""       
    
    # make the plain text by reading the matrix row by row
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            deciphered_plain_text += matrix[i][j]
    
    print("Deciphered Plain Text with bogus characters : ")
    print(deciphered_plain_text)
    
    deciphered_plain_text = deciphered_plain_text.replace("#","")
    
    print("Deciphered Plain Text : ")
    print(deciphered_plain_text)

def main():
    cipher_text = sender_side()
    reciever_side(cipher_text)

if __name__ == "__main__":
    main()



