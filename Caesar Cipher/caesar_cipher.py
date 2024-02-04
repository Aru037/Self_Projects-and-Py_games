from caiser_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(start_text, shift_amount, cipher_direction):
    end_text =""
    
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_positon = position + shift_amount
            end_text += alphabet[new_positon]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26 
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")  
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_positon = position + shift_amount
#         new_letter = alphabet[new_positon]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrrypt(cipher_text,shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_positon = position - shift_amount
#         plain_text += alphabet[new_positon]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrrypt(cipher_text = text, shift_amount = shift)
# else:
#     print("Invalid Input")
