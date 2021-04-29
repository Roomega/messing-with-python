#Testing games

print(
"""
("-")
 /|/
_|_|______
""")
movement = ("0")

while True:
    movement3 = input("""
-------------------------------------------------------------

[1] Direita
[2] Esquerda
\n""")
    if movement3 == ("1") and movement != ("1") and movement != ("3"):
        movement = ("1")
        print("""
     ("-")
      /|/
______|_|______
    """)

    elif movement3 == ("2") and movement == ("1"):
        movement = ("2")
        print(
"""
("-")
 /|/
_|_|______
""")
    elif movement3 == ("2") and movement == ("2") :
        movement = ("2")
        print("Este movimento é impossível.")

    elif movement3 == ("1") and movement == ("1"):
        movement = ("3")
        print("""
            ("-")
             /|/
_____________|_|______
        """)

    elif movement3 == ("2") and movement == ("3"):
         movement = ("1")
         print("""
     ("-")
      /|/
______|_|______
    """)
    elif movement3 == ("1") and movement == ("3"):
        print("Este movimento é impossível.")

    else: 
        print("Este movimento é impossível.")

