f = open("date.out", "rb")
d = f.read()
sir=""
g=open("date.in","r")
b=g.read()
for i in range(len(d)):
  sir=sir + chr(d[i]^ord(b[i]))
print(sir)
