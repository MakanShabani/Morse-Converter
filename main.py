WELCOME_MSG = """                                             _..._       .-'''-.                                         
                                 .---.    .-'_..._''.   '   _    \                                       
                   __.....__     |   |  .' .'      '.\/   /` '.   \  __  __   ___         __.....__      
       _     _ .-''         '.   |   | / .'          .   |     \  ' |  |/  `.'   `.   .-''         '.    
 /\    \\   ///     .-''"'-.  `. |   |. '            |   '      |  '|   .-.  .-.   ' /     .-''"'-.  `.  
 `\\  //\\ ///     /________\   \|   || |            \    \     / / |  |  |  |  |  |/     /________\   \ 
   \`//  \'/ |                  ||   || |             `.   ` ..' /  |  |  |  |  |  ||                  | 
    \|   |/  \    .-------------'|   |. '                '-...-'`   |  |  |  |  |  |\    .-------------' 
     '        \    '-.____...---.|   | \ '.          .              |  |  |  |  |  | \    '-.____...---. 
               `.             .' |   |  '. `._____.-'/              |__|  |__|  |__|  `.             .'  
                 `''-...... -'   '---'    `-.______ /                                   `''-...... -'    
                                                   `"""


# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def encrypt(text: str) -> str:
    result = ""
    # Search for morse code char of each char in the text
    # If original char is " " then we add it to the result as it is ( space between words )
    # Also, we add " " to the end of each morse char (space between morse chars)
    for char in text:
        try:
            if char != " ":
                result += MORSE_CODE_DICT.get(char) + " "
            else:
                result += " "
        except:
            # If we could find a char in the morse code, raise an exception
            print(f"Invalid character : {char}")
    return result


def decrypt(morse_code: str) -> str:
    result = ""
    codes = morse_code.split(" ")

    # Search for original character of each morse code in the coded text
    for code in codes:
        if code != " ":
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    result += key
                    break
        else:
            result += " "
    return result.title()


print(WELCOME_MSG)
print("\n\n")


# morse_text = encrypt(input("Enter the text to encrypt: ").upper())
original_text = decrypt(input("Enter the Morse Code to decrypt: "))

print(f"Equivalent Morse Code : {original_text}")

input("Press enter to exit")
