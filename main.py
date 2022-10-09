input_text = input().split()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code_text = []

for word in input_text:
    text = list(word)
    shift = 0
    for i in word:
        if i.isalpha():
            shift += 1
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                text[i] = abc[(abc.index(text[i]) + shift) % 26]
            else:
                text[i] = (abc[(abc.index((text[i]).upper()) + shift) % 26]).lower()
                
        else:
            continue
        
    text = ''.join(text)
    code_text.append(text)

print(' '.join(code_text))
