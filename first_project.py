nome = input("qual seu nome?\n")
print("Bem vindo",nome)
idade = input(f"qual seria sua idade {nome}?\n")
trabalho1 = input(f"""vc trabalha {nome}?
[1] Sim
[2] Não
\n""")
if trabalho1 == ("1"):
   trabalho2 = input("Com o quê?\n")

moradia = input(f"Onde vc vive {nome}?\n")
if trabalho1 == ("1"):
    print(nome, idade, trabalho2, moradia)
else:
    trabalho1 = ("Não tem trabalho.")
    print(nome, idade, trabalho1, moradia)
