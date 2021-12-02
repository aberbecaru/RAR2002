f = open("date.out", "r")
g = open("decrypt.out", "w")
key=input()
lungime_key = len(key)
final=""
sir = f.read()
lungime= len(sir)
c=0
for i in range(0,lungime,8):
    sirnou= sir[i:i+8]
    sirnou= int(sirnou,2)
    caracter_key = key[c % lungime_key]
    bin_carac_key = ord(caracter_key)
    c=c+1
    numar = int(sirnou ^ bin_carac_key)
    numar= chr(numar)
    final=final + numar
g.write(final)