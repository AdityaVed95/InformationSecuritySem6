class PlayFairCipherProcessor:
    def are_letters_in_same_row(self,secret_key_matrix,letter1,letter2):
        pos1 = None
        pos2 = None
        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    pos1 = i
                elif(secret_key_matrix[i][j] == letter2):
                    pos2 = i
                    
                    
        if pos1 == pos2:
            return 1
        
        return 0


    def are_letters_in_same_column(self,secret_key_matrix,letter1,letter2):
        pos1 = None
        pos2 = None
        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    pos1 = j
                elif(secret_key_matrix[i][j] == letter2):
                    pos2 = j
                    
                    
        if pos1 == pos2:
            return 1
        
        return 0


    def get_encrypted_or_decrypted_letters_same_row(self,secret_key_matrix,letter1,letter2,encrypt):
        if encrypt == 1: # if we want to perform encryption at the sender side
            encrypted_letter1 = None
            encrypted_letter2 = None
        
        elif encrypt == 2: # if we want to perform decryption at the reciever side
            decrypted_letter1 = None
            decrypted_letter2 = None
        
        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    if encrypt == 1:
                        encrypted_letter1 = secret_key_matrix[i][(j+1)%5]
                    elif encrypt == 0:
                        decrypted_letter1 = secret_key_matrix[i][(j-1)%5]
                
                elif(secret_key_matrix[i][j] == letter2):
                    if encrypt == 1:
                        encrypted_letter2 = secret_key_matrix[i][(j+1)%5]
                    elif encrypt == 0:
                        decrypted_letter2 = secret_key_matrix[i][(j-1)%5]
                
        if encrypt == 1:
            return encrypted_letter1,encrypted_letter2
        elif encrypt == 0:
            return decrypted_letter1,decrypted_letter2


    def get_encrypted_or_decrypted_letters_same_column(self,secret_key_matrix,letter1,letter2,encrypt):
        if encrypt == 1: # if we want to perform encryption at the sender side
            encrypted_letter1 = None
            encrypted_letter2 = None
        
        elif encrypt == 2: # if we want to perform decryption at the reciever side
            decrypted_letter1 = None
            decrypted_letter2 = None
        
        else:
            return None, None
        
        
        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    if encrypt == 1:
                        encrypted_letter1 = secret_key_matrix[(i+1)%5][j]
                    elif encrypt == 0:
                        decrypted_letter1 = secret_key_matrix[(i-1)%5][j]
                
                elif(secret_key_matrix[i][j] == letter2):
                    if encrypt == 1:
                        encrypted_letter2 = secret_key_matrix[(i+1)%5][j]
                    elif encrypt == 0:
                        decrypted_letter2 = secret_key_matrix[(i-1)%5][j]

        if encrypt == 1:
            return encrypted_letter1,encrypted_letter2
        elif encrypt == 0:
            return decrypted_letter1,decrypted_letter2


    # this fxn can be used for both encryption and decryption , thus can be used at both sender side and reciever side : 
    def get_encrypted_or_decrypted_letters_neither_same_row_nor_column(self,secret_key_matrix,letter1,letter2):
        encrypted_letter1 = None
        encrypted_letter2 = None
        column_of_letter1 = None
        column_of_letter2 = None
        
        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    column_of_letter1 = j
                
                elif(secret_key_matrix[i][j] == letter2):
                    column_of_letter2 = j

        for i in range(5):
            for j in range(5):
                if(secret_key_matrix[i][j] == letter1):
                    encrypted_letter1 = secret_key_matrix[i][column_of_letter2]
                
                elif(secret_key_matrix[i][j] == letter2):
                    encrypted_letter2 = secret_key_matrix[i][column_of_letter1]
        
        return encrypted_letter1,encrypted_letter2


    def remove_repeating_characters(self,my_string):
        temp_my_string = ""
        for i in range(len(my_string)):
            if my_string[i] not in temp_my_string:
                temp_my_string = temp_my_string + my_string[i]
        
        return temp_my_string


    def get_letters_string(self,key):
        
        letters_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(len(key)):
            if key[i] in letters_string:
                letters_string = letters_string.replace(key[i],'')

        return letters_string


    def generate_secret_key_matrix(self,key,letters_string):
        no_of_rows = 5
        no_of_columns = 5

        secret_key_matrix = [ ["#" for i in range(5)] for j in range(5)]

        key_counter = 0
        letters_counter = 0


        for i in range(no_of_rows):
            j = 0
            while(j < no_of_columns):
                if key_counter < len(key):
                    secret_key_matrix[i][j] = key[key_counter]
                    key_counter += 1
                    
                else:
                    if(letters_string[letters_counter] == "J"):
                        letters_counter += 1
                        j = j - 1
                        
                    else:
                        secret_key_matrix[i][j] = letters_string[letters_counter]
                        letters_counter += 1
                
                j += 1
        
        return secret_key_matrix


    def add_bogus_character_between_same_letters(self,plain_text):
        for i in range(len(plain_text)):
            if(i == 0):
                continue
            
            if(plain_text[i] == plain_text[i-1]):
                plain_text = plain_text[:i] + "Z" + plain_text[i:]
        
        return plain_text


    def generate_cipher_text(self,plain_text,secret_key_matrix):
        ciphertext = ""
        # here we encipher plain text to generate cipher text
        encrypted_letter1 , encrypted_letter2 = None,None
        
        for i in range(0,len(plain_text),2):
            if self.are_letters_in_same_row(secret_key_matrix,plain_text[i],plain_text[i+1]):
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_same_row(secret_key_matrix,plain_text[i],plain_text[i+1],1)

            elif self.are_letters_in_same_column(secret_key_matrix,plain_text[i],plain_text[i+1]):
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_same_column(secret_key_matrix,plain_text[i],plain_text[i+1],1)
                
            else:
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_neither_same_row_nor_column(secret_key_matrix,plain_text[i],plain_text[i+1])
                
        
            ciphertext += encrypted_letter1 + encrypted_letter2
        
        return ciphertext


    def generate_plain_text(self,ciphertext,secret_key_matrix):
        reciever_plain_text = ""
        
        for i in range(0,len(ciphertext),2):
            if self.are_letters_in_same_row(secret_key_matrix,ciphertext[i],ciphertext[i+1]):
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_same_row(secret_key_matrix,ciphertext[i],ciphertext[i+1],0)

            elif self.are_letters_in_same_column(secret_key_matrix,ciphertext[i],ciphertext[i+1]):
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_same_column(secret_key_matrix,ciphertext[i],ciphertext[i+1],0)
                
            else:
                encrypted_letter1 , encrypted_letter2 = self.get_encrypted_or_decrypted_letters_neither_same_row_nor_column(secret_key_matrix,ciphertext[i],ciphertext[i+1])
                
            reciever_plain_text += encrypted_letter1 + encrypted_letter2
        
        return reciever_plain_text


    def input_and_preprocess_key_and_generate_secrect_key_matrix(self):
        print("Enter Key (Note : The key cannot contain the letter j and it should be of length less than or equal to 25)")
        key = input()
        # key = "secure"
        key = key.upper()
        print("Entered key is : ",key)

        # removing repeating characters from the key : 
        # E.g : converting SECURE to SECUR
        key = self.remove_repeating_characters(key)
        print("Key after removing duplicates is : ",key)

        # get string of all letters except the ones in the key
        letters_string = self.get_letters_string(key)


        # generating Secret key matrix : 
        secret_key_matrix = self.generate_secret_key_matrix(key,letters_string)
        print("Secret Key Matrix is : ")
        for row in secret_key_matrix:
            print(row)
            
        return secret_key_matrix


    def input_plain_text_and_preprocess_it(self):
        print("Enter the plain text (Note : the plain text should not contain Z as it is treated as a bogus character): ")
        plain_text = input()
        # plain_text = "adityaav"
        plain_text = plain_text.upper()

        print("At the Sender side : ")
        print("Plain Text : ",plain_text)


        plain_text = self.add_bogus_character_between_same_letters(plain_text)
        print("Plain text after inserting bogus character between any two similar letters: ",plain_text)

        if(len(plain_text) %2 != 0):
            plain_text += "Z"

        print("Plain text after inserting bogus character to make plain text of even no of characters: ",plain_text)
        
        return plain_text


    def decipher_plain_text_and_display_it(self,ciphertext,secret_key_matrix):
        print("Cipher Text recieved  : ",ciphertext)

        reciever_plain_text = self.generate_plain_text(ciphertext,secret_key_matrix)   

        print("Plain Text calculated : ",reciever_plain_text)

        # remove the bogus characters : 
        reciever_plain_text = reciever_plain_text.replace('Z','')
        print("After Removing the bogus characters, the final plain text is : ",reciever_plain_text)

    # def process_playfair_cipher_sender_side(self,): 
        
    
    # def process_playfair_cipher_reciever_side(self,):
        
        
if __name__ == "__main__":  
    playFairCipherObject = PlayFairCipherProcessor()

    # sender side : 
    print("\n\nAt the sender side : ")
    secret_key_matrix = playFairCipherObject.input_and_preprocess_key_and_generate_secrect_key_matrix()
    plain_text = playFairCipherObject.input_plain_text_and_preprocess_it()
    ciphertext = playFairCipherObject.generate_cipher_text(plain_text,secret_key_matrix)    
    print("Cipher text : ",ciphertext)


    # reciever side : 
    print("\n\nAt the reciever side : ")
    playFairCipherObject.decipher_plain_text_and_display_it(ciphertext,secret_key_matrix)
