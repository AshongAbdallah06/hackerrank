def cipher(og_alphabets, s, k):
    for letter_index in range(0, len(s)):
        letter = s[letter_index]

        for alpha_index in range(0, len(og_alphabets)):
            alphabet = og_alphabets[alpha_index]
            if letter != "-" and letter.lower() == alphabet.lower():
                ciphered_index = (alpha_index + k) % 26

                ciphered_letter = ""
                ciphered_letter = og_alphabets[ciphered_index]

                if letter.isupper():
                    ciphered_letter = ciphered_letter.upper()
                s[letter_index] = ciphered_letter


def caesarCipher(s, k):
    og_alphabets = list("abcdefghijklmnopqrstuvwxyz")
    s = list(s)

    cipher(og_alphabets, s, k)

    result = ""
    for li in s:
        result += li
    return result


if __name__ == "__main__":
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

# 1
# middle-Outz
# 2
