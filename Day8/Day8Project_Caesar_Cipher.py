# importing the logo
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# rerun the program again by asking the user
game = True
while game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Creating function caesar
    def caesar(original_text,shift_amount,direction_of_text):
        cipher = ""
        if direction_of_text == 'decode':
            shift_amount *= -1
        for letter in original_text:
            # if user type other character other than alphabet
            if letter not in alphabet:
                cipher += letter
            else:
                new_index = alphabet.index(letter) + shift_amount
                new_index %= len(alphabet)
                cipher+= alphabet[new_index]
        print(f'Here is your {direction_of_text}d with result {cipher}')

    caesar(text,shift,direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no' . \n" ).lower()
    if user_input == 'no':
        game = False
