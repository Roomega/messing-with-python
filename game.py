
#Testing games
print("Bem Vindo ao jogo mais simples do mundo.\n")
start2 = 1
while start2 == 0 or start2 == 1:
    start = input("""\n
----------------------------------------------------------------\n
[A] Start
[B] Exit\n
----------------------------------------------------------------
\n""")
    if start == ("A") or start == ("a"):
        movement = ("2")
        print(
        """
        ("-")
         /|/
_________|_|______
        """)

        while True:
            movement3 = input("""
 ----------------------------------------------------------------
|    [1] Direita                                                 |
|    [2] Esquerda                                                |
|    [3] Saltar                                                  |
 ----------------------------------------------------------------
        \n""")
            if movement3 == ("1") and movement != ("1") and movement != ("3") and movement != ("5") and movement != ("4"):
                movement = ("1")
                print("""
             ("-")
              /|/
______________|_|______
            """)

            elif movement3 == ("2") and movement == ("1"):
                movement = ("2")
                print(
        """
        ("-")
         /|/
_________|_|______
        """)
            elif movement3 == ("2") and movement == ("2") :
                movement = ("2")
                print("Este movimento é impossível.")

            elif movement3 == ("1") and movement == ("1"):
                movement = ("3")
                print("""
                    ("-")
                     /|/
_____________________|_|__________
                                  |
                                  |
                """)

            elif movement3 == ("2") and movement == ("3"):
                 movement = ("1")
                 print("""
             ("-")
              /|/
______________|_|________________
                                 |
                                 |
            """)
            elif movement3 == ("1") and movement == ("3"):
                movement = ("4")
                print("""
                             ("-")
                              /|/
______________________________|_|_         __________
                                  |       |
                                  |       |
                """)
            elif movement3 == ("2") and movement == ("4"):
                movement = ("3")
                print("""
                    ("-")
                     /|/
_____________________|_|__________
                                  |
                                  |
                """)
            elif movement3 == ("1") and movement == ("4"):
                print("""
                            
                      
__________________________________         __________
                                  | ("-") |
                                  |  /|/  |
                                  |  | |  |
                                  |/\_/\_/|
        Você Morreu.
                """)
                break
        

            elif movement3 == ("3") and movement == ("4"):
                movement = ("5")
                print("""
                                    ("-")
                                     /|/
                                     | |
__________________________________         __________
                                  |       |
                                  |       |
                                  |       |
        
                """)
                print("""
                                                       ___
                                           ("-")      |___|
                                            /|/       |
__________________________________         _|_|_______|______
                                  |       |
                                  |       |
                """)
            elif movement3 == ("2") and movement == ("5"):
                print("""
                            
                      
__________________________________         __________
                                  | ("-") |
                                  |  /|/  |
                                  |  | |  |
                                  |/\_/\_/|
        Você Morreu.
                """)
                break

            elif movement3 == ("1") and movement == ("5"):
                movement = ("6")
                print("""
                                                       ___
                                                      |___|  ("-")      
                                                      |       /|/
__________________________________         ___________|_______|_|
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
      
______________________
            """)
                print("""
             ("-")
              /|/
______________|_|______
            """)
            elif movement3 == ("3") and movement == ("2"):
                print("""
        ("-")
         /|/
         | |
      
______________________
            """)
                print(
        """
        ("-")
         /|/
_________|_|______
        """)
            elif movement3 == ("3") and movement == ("3"):
                print("""
                    ("-")
                     /|/
                     |_|
             
__________________________________
                                  |
                                  |
                """)
                print("""
                    ("-")
                     /|/
_____________________|_|__________
                                  |
                                  |
                """)

            elif movement3 == ("3") and movement == ("5"):
                print("""
                                           ("-")  
                                            /|/        ___
                                            |_|       |___|
                                                      |
__________________________________         ___________|______
                                  |       |
                                  |       |
                """)
                print("""
                                                       ___
                                           ("-")      |___|
                                            /|/       |
__________________________________         _|_|_______|______
                                  |       |
                                  |       |
                """)

            else: 
                print("Este movimento é impossível.")
    elif start == ("B") or start == ("b"):
        exit()
    else:
        start2 = 0
        print("Esta escolha é inválida.")