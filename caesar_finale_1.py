alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, direction):
    encrypted_message = []
    if direction == "encrypt":
        for i in message:
            try:
                encrypted_message += alphabet[alphabet.index(i)+shift]
            except:
                try:
                    if (alphabet.index(i) + shift) > 25:
                        encrypted_message += alphabet[shift-(26-alphabet.index(i))]
                except:
                    if i == " " or i == "," or i == "!" or i == "?" or i == "'":
                        encrypted_message += i
        print(''.join(encrypted_message))
        return encrypted_message
    elif direction == "decrypt":
        for i in message:
            try:
                encrypted_message += alphabet[alphabet.index(i)-shift]
            except:
                if i == " " or i == "," or i == "!" or i == "?" or i == "'":
                    encrypted_message += i
        print(''.join(encrypted_message))
        return encrypted_message
    else:
        print("You better learn to follow the instructions! THAT was not an option to choose!")
    
    

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)