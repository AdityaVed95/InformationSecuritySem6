# key_dictionary and group_size are secretly shared between the sender and reciever
# the key_dictionary of sender and reciver are opposite of each other

def sender_side():
    print("\n\nAt the sender side :")
    print("Enter Plain Text :")
    plain_text = input()
    # plain_text = "enemyattackstonight"
    key_dictionary = {3:1,1:2,4:3,5:4,2:5}
    # size of the group of characters in which the plain text is divided into
    group_size  = 5
    
    if len(plain_text) % 5 != 0:
        no_of_bogus_characters_to_add = 5 - len(plain_text) % 5
        plain_text = plain_text + ("#" * no_of_bogus_characters_to_add)
        print("Plain text with bogus characters : ")
        print(plain_text)
    
    
    group_of_char_list = []
    
    for i in range(0,len(plain_text),group_size):
        temp_string = ""
        for j in range(i,i+5,1):
            temp_string += plain_text[j]
        
        group_of_char_list.append(temp_string)
    
    print("Group of characters list : ")
    print(group_of_char_list)
    
    encrypted_group_char_list = []
    
    for group_string in group_of_char_list:
        temp_encrypted_string = "#" * group_size
        
        for key,value in key_dictionary.items():
            # replace a character in a string at a paritcular position with another character :
            temp_encrypted_string = temp_encrypted_string[:value-1] + group_string[key-1] + temp_encrypted_string[value:] # since the key defined is 1 based and not zero based (index is 1 based)
    
        encrypted_group_char_list.append(temp_encrypted_string)
    
    print("Encrypted group of characters list : ")
    print(encrypted_group_char_list)    
    
    cipher_text = ""
    
    for encrypted_group_string in encrypted_group_char_list:
        cipher_text += encrypted_group_string
    
    print("Cipher Text to be sent to reciever is : ")
    print(cipher_text)
    
    return cipher_text

def reciever_side(cipher_text):
    group_size = 5
    print("\n\nAt reciver side : ")
    key_dictionary = {1:3,2:1,3:4,4:5,5:2} # this key value pair is the opposite of what we have at the sender side
    
    print("Cipher text recieved :")
    print(cipher_text)
    
    encrypted_group_of_char_list = []
    for i in range(0,len(cipher_text),group_size):
        temp_encrypted_string = ""
        for j in range(i,i+5,1):
            temp_encrypted_string += cipher_text[j]
        
        encrypted_group_of_char_list.append(temp_encrypted_string)
    
    print("Encrypted group of characters list : ")
    print(encrypted_group_of_char_list)
    
    decrypted_group_of_char_list = []
    
    for encrypted_group_string in encrypted_group_of_char_list:
        temp_decrypted_string = "#" * group_size
        
        for key,value in key_dictionary.items():
            # replace a character in a string at a paritcular position with another character :
            temp_decrypted_string = temp_decrypted_string[:value-1] + encrypted_group_string[key-1] + temp_decrypted_string[value:] # since the key defined is 1 based and not zero based (index is 1 based)
        
        decrypted_group_of_char_list.append(temp_decrypted_string)
        
    print("Decrypted group of characters list : ")   
    print(decrypted_group_of_char_list)
    
    deciphered_plain_text = ""
    for decrypted_group_string in decrypted_group_of_char_list:
        deciphered_plain_text += decrypted_group_string
    
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
