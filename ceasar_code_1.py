alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift):
    encrypted_message = []
    
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
    return encrypted_message

def decrypt(message, shift):
    encrypted_message = []
    for i in message:
        try:
            encrypted_message += alphabet[alphabet.index(i)-shift]
        except:
            if i == " " or i == "," or i == "!" or i == "?" or i == "'":
                encrypted_message += i
    return encrypted_message

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

message = encrypt(text, shift)
print(''.join(message))
print("Now decrypted:")
message = decrypt(''.join(message), shift)
print(''.join(message))
