def encrypter(text, key):
    return_string = ""
    for x in text:
        if(x == " "):
            return_string += " "
            continue
        char_val = ord(x)
        new_val = char_val + key
        if((new_val > 90 and x.isupper()) or new_val > 122):
            new_val -= 26
        return_string += chr(new_val)
    return return_string

def decrypter(text,key):
    return_string = ""
    for x in text:
        if (x == " "):
            return_string += " "
            continue
        char_val = ord(x)
        new_val = char_val - key
        if ((new_val < 65 and x.isupper()) or new_val < 97):
            new_val += 26
        return_string += chr(new_val)
    return return_string

KEY = int(input("ENTER ENCRYPTION KEY VALUE (integer): "))
input_text = input("Enter text: ")

choice = int(input("ENTER CHOICE: \n1. ENCRYPT\n2. DECRYPT\n"))

if(choice == 1):
    print(encrypter(input_text,KEY))
elif(choice == 2):
    print(decrypter(input_text,KEY))
else:
    print("ENTER VALID CHOICE!!!")