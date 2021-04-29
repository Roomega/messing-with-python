#Testing games

print(
"""
("-")
 /|/
_|_|______
""")
movement = ("2")

while True:
    movement3 = input("""
-------------------------------------------------------------
[1] Direita
[2] Esquerda
[3] Saltar
\n""")
    if movement3 == ("1") and movement != ("1") and movement != ("3") and movement != ("5") and movement != ("4"):
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
_____________|_|__________
                          |
                          |
        """)

    elif movement3 == ("2") and movement == ("3"):
         movement = ("1")
         print("""
     ("-")
      /|/
______|_|________________
                         |
                         |
    """)
    elif movement3 == ("1") and movement == ("3"):
        movement = ("4")
        print("""
                     ("-")
                      /|/
______________________|_|_         __________
                          |       |
                          |       |
        """)
    elif movement3 == ("2") and movement == ("4"):
        movement = ("3")
        print("""
            ("-")
             /|/
_____________|_|__________
                          |
                          |
        """)
    elif movement3 == ("1") and movement == ("4"):
        print("""
                            
                      
__________________________         __________
                          | ("-") |
                          |  /|/  |
                          |  | |  |

Você Morreu.
        """)
        break
        

    elif movement3 == ("3") and movement == ("4"):
        movement = ("5")
        print("""
                            ("-")
                             /|/
                             | |
__________________________         __________
                          |       |
                          |       |
                          |       |
        
        """)
        print("""
                                               ___
                                   ("-")      |___|
                                    /|/       |
__________________________         _|_|_______|______
                          |       |
                          |       |
        """)
    elif movement3 == ("2") and movement == ("5"):
        print("""
                            
                      
__________________________         __________
                          | ("-") |
                          |  /|/  |
                          |  | |  |

Você Morreu.
        """)
        break

    elif movement3 == ("1") and movement == ("5"):
        movement = ("6")
        print("""
                                               ___
                                              |___|  ("-")      
                                              |       /|/
__________________________         ___________|_______|_|
                          |       |
                          |       |

        """)
        print("Você Venceu!")
        break

    elif movement3 == ("3") and movement == ("1"):
        print("""
     ("-")
      /|/
      |_|
      
_______________
    """)
        print("""
     ("-")
      /|/
______|_|______
    """)
    elif movement3 == ("3") and movement == ("2"):
        print("""
("-")
 /|/
 |_|
      
_______________
    """)
        print(
"""
("-")
 /|/
_|_|______
""")
    elif movement3 == ("3") and movement == ("3"):
        print("""
            ("-")
             /|/
             |_|
             
__________________________
                          |
                          |
        """)
        print("""
            ("-")
             /|/
_____________|_|__________
                          |
                          |
        """)

    elif movement3 == ("3") and movement == ("5"):
        print("""
                                   ("-")  
                                    /|/        ___
                                    |_|       |___|
                                              |
__________________________         ___________|______
                          |       |
                          |       |
        """)
        print("""
                                               ___
                                   ("-")      |___|
                                    /|/       |
__________________________         _|_|_______|______
                          |       |
                          |       |
        """)

    else: 
        print("Este movimento é impossível.")
