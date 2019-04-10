dic = {'a':'...-', 'b':'--..', 'c':'/', 'd':'-.--', 'e':'.-.', 'f':'...', 'g':'.-..', 'h':'--', 'i':'---', 'j':'-', 'k':'-..-', 'l':'-..', 'm':'..', 'n':'.--', 'o':'-.-.', 'p':'--.-', 'q':'-.-', 'r':'.-', 's':'-...', 't':'..', 'u':'....', 'v':'--.', 'w':'.---', 'y':'..-.', 'x':'..-', 'z':'.--.', '{':'-.', '}':'.'}
encrypted = '.. - / .. ... -. - / -- --- .-. ... / -.-. --- -.. .'

dic_reversed = dict()
for k in dic:
    dic_reversed[dic[k]] = k

flag = ''
for s in encrypted.split(' '):
    flag += dic_reversed[s]
    
print(flag)