def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

def main():
    print("_____________________________________________")
    print("_____________________________________________")
    print(" ____     ___    ___   ____     ___     ____ ")
    print("|  _ \   / _ \  |_ _| |  _ \   / _ \   / ___|")
    print("| |_) | | | | |  | |  | | | | | | | | | |  _ ")
    print("|  __/  | |_| |  | |  | |_| | | |_| | | |_| |")
    print("|_|      \___/  |___| |____/   \___/   \____|")
    print("_____________________________________________")
    print("_____________________________________________")
    print("\n")
    print("Ceaser Cipher")
    print("/"*90)
    print("**Note:**This program will encrypt your text using Ceaser Cipher method and provide you with encrypted text. \nAnd this a very simple program to encrypt your text using Ceaser Cipher method.\nDon't use this program for real encryption of text in real life situations.")
    print("/"*90)
    print("\n")
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()
