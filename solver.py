import hashlib
import fileinput
file=[]
hashes={}
def loadfile():
    with open("12bits_salts_and_salted_passwords_file.txt","r") as f:
        for i in f:
            i=i.strip()
            file.append((i[:12],i[12:len(i)]))
def solver():
    out=open("out.txt","w")
    loadfile()
    hashes={i[1] for i in file}
    with open("10-million-password-list-top-1000000 (1).txt","r",errors="ignore") as f:
        for i in f:
            for j in file:
                a=j[0]
                b=i
                val=hashlib.sha256((a+b).encode("utf-8")).hexdigest()
                if val in hashes:
                    print(i)
                    with open("out.txt","a")as f:
                        out.write(i)
                    break
if __name__=="__main__":
    solver()

