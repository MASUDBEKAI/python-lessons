sabzavotlar = ["sabzi", "bodring" , "baqlajon" , "kartoshka ", "pomidor"]
with open("sabzavotlar.txt", "w" , encoding= "utf-8") as f:
    for sabzav in sabzavotlar:
        f.write(sabzav + "\n")
with open("sabzavotlar.txt", "r", encoding= "utf-8") as f:
    qator = f.readlines()
    raqam = 1
    for q in qator:
        print(f"{raqam}. {q.strip()}")
        raqam += 1