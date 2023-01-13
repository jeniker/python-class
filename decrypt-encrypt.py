# Program 4
# Jennifer King
# October 2, 2017
# This program is a Caesar Cypher- encryption and decryption mode.
# The user provides the text to encrypt or decrypt, and the key
# that either defines the encryption result or successfully
# decrypts the text to the original message. 


def encrypt():2
    # the function to encrypt a phrase using a Caesar cipher.
    # it takes the phrase and adds the chosen key to the
    # ascii value of each letter, changing the text.
plainText = input("Enter a phrase with no spaces, letters only:")
plainText = plainText.upper()
print(plainText)
    # user input of the phrase to encrypt
key = int(input("Enter the key value to encrypt phrase- 1 to 26: "))
    # user input of the key which is the amount to move the ascii value
code = "" # placeholder for the encrypted code
for ch in plainText: # this starts an iteration through the string
        ordValue = ord(ch)  # obtains the ascii value of each letter
        cipherValue = ordValue + key  # adds the key value to the ascii value
        if cipherValue > ord('Z'): # tests for result outside of alphabet
                   cipherValue = ord('A') + key - \
                   (ord('Z') - ordValue +1) # if the resulting value is past letter z
                                            # this returns the value back to a
        code += chr(cipherValue)  # places the encryption of each letter in the code placeholder
print(code)  # prints the resulting encrypted code 


def decrypt():
    # the function to decrypt a phrase that used a Caesar cipher
    # it takes the coded text and subtracts the needed key to the
    # ascii value ot each letter, changing the text back to original
    codeText = input("Enter the coded text to decipher: ")
    codeText = codeText.upper()
    print(codeText)
    # user input of the coded text to decipher
    key = int(input("Enter the key to decipher the coded text, 1 to 26: "))
    # user input of the key needed to decipher the code
    code = "" # placeholder for the decrypted text
    for ch in codeText: # this starts an iteration through the string
        ordValue = ord(ch)  # obtains teh ascii value of each letter
        cipherValue = ordValue - key # subtracts the key from each ascii value
        if cipherValue < ord('A'):
          # tests for the result outside of the alphabet
            cipherValue = (ord('Z') - (key - ord('A') - (cipherValue + 1)))
                                    # if the resulting value is less than the letter a
                                    # this returns the value to the letter z
        code += chr(cipherValue)  # places the decrypted text of each letter in the code placeholder
    print(code) # prints the resulting decrypted code


def main():
    # the main function to select encryption or decryption
    userSelect = int(input("Enter 1 for encryption and 2 for decryption: "))
    result = ""  # placeholder for the result
    if userSelect == 1:
        result = encrypt() # sends the program to the encryption function
    if userSelect == 2:
        result = decrypt() # sends the program to the decryption function
main()

                     
                
                   
        
