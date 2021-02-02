print('follow me on instagram \n >> @omarmazin_ <<')
def encrypting(string,shift):
    crazy = ''
    for char in string:
        if crazy ==' ':
            crazy = crazy + 1
        elif char.isupper():
            crazy=crazy+chr((ord(char)+shift-65)%26+65)
        else:
            crazy=crazy+chr((ord(char)+shift-97)%26+97)
    return crazy
def tryy():
    YOOU = input('Enter text >> :')
    s = int(input('enter (number)shift >> :'))
    print('Before encrypt >> : ', YOOU)
    print('after encrypt >> : ', encrypting(YOOU, s))
    return tryy()
tryy()
