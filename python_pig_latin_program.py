def pig_latin(text):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if text[0] in vowel:
        text = text + text[0] + 'ay'
        text1 = list(text)
        del (text1[0])
    else:
        text1 = text + 'hay'
    str1 = ''.join(text1)
    return str1


pig_latin('hello')
