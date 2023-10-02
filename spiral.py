def translate(n):
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for letters in n:
        if letters in consonant:
            return (letters+"O"+letters)
        else:
            return(Vowel)

n = str(input())
print(Vo)