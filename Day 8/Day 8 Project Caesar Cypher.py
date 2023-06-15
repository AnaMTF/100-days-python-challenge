alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt (plain_text, shift):
    cypher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            cypher_text += letter
        else:
            old_position = alphabet.index(letter)
            new_position = old_position + shift
            while new_position > 25:
                new_position -= 26
            new_letter = alphabet[new_position]
            cypher_text += new_letter
    print(f"The encrypted text is: {cypher_text}.")
    
def decrypt (crypted_text, shift):
    decrypted_text = ""
    for letter in crypted_text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            old_position = alphabet.index(letter)
            new_position = old_position - shift
            if new_position < 0:
                new_position += 26
            new_letter = alphabet[new_position]
            decrypted_text += new_letter
    print(f"The decrypted text is: {decrypted_text}.")

if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Please chose one of the two options.")