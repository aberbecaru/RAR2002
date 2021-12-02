f = open("date.in", "r")
g = open("date.out", "w")
key = input()
sir = f.read()
lungime_key = len(key)
lungime_sir = len(sir)
sir_bin = ""
for i in range(lungime_sir):
    caracter_sir = sir[i]
    caracter_key = key[i%lungime_key]
    bin_carac_sir = ord(caracter_sir)
    bin_carac_key = ord(caracter_key)
    numar= str(bin(bin_carac_sir^bin_carac_key))
    numar=numar[2:]
    lungime= len(numar)
    zerouri= "0"*(8-lungime)
    final= zerouri + numar
    sir_bin = sir_bin + final

g.write(sir_bin)
g.close()
