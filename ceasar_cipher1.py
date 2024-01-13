alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  
  #shift each letter of the 'text' forwards in the alphabet by the shift amount and print the   encrypted text.
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

# create a function the decrypts the text and returns the result
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  
  # shift each letter of the 'text' backwards in the alphabet by the shift amount.
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


#if direction == "encode":
  #encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
  #decrypt(cipher_text=text, shift_amount=shift)
#else:
  #print("You have entered an invalid input.")

def ceaser(start_text, shift_amount, cipher_direction):
  end_text = ""
  
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for letter in start_text:
    position = alphabet.index(letter)  
    new_position = position + shift_amount
    end_text += alphabet[new_position]

  print(f"The {cipher_direction}d text is {end_text}")

ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
