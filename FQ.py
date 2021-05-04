#Programa sobre o Cálcio

from time import sleep
pontos = 0
while True:
    introduction = input("""
 _______________________________________________________
|    Bem Vindo à nossa introdução ao elemento cálcio.   |
|    Introduze:                                         |
|                                                       |
|    [1] Começar                                        |
|    [2] Quiz                                           |
|    [3] Sair                                           |
|_______________________________________________________|
    \n""")

    if introduction == ("1"):
        print("O morango, leite e natas todos contém cálcio.\n")
        
        input("Carrege no Enter para continuar\n")

        print("O cálcio é um elemento beneficial para a saúde. Alguns de estes benefícios são,")
        sleep(3)
        print("1. Fortalece os Ossos\n")
        sleep(2)
        print("2. Previne a obesidade\n")
        sleep(2)
        print("3. Protege os múscolos cardíacos\n")
        sleep(2)
        print("4. Atua no transporte de nutrientes\n")
        sleep(2)
        print("5. Controla a pressão arterial\n")
        sleep(2)
        print("6. Ajuda a evitar o cancro no cólon\n")
        sleep(2)
        print("7. Protege os dentes e as gengivas\n")

        input("Carrege no Enter para continuar\n")

#pesquisa sobre esse elemento químico: símbolo químico, número atómico, número de massa, distribuição eletrónica, localização na TP, benefícios para a saúde.
        print("""O símbolo químico do cálcio é
Ca\n""")
        sleep(2)
        print("O número atómico do cálcio é 20\n")
        sleep(2)
        print("O número de massa do cálcio é 40.078\n")
        sleep(2)
        print("A distribuição eletrónica é 2-8-8-2\n")
        sleep(2)
        print("E por fim, o Cálcio está localizado no grupo 2 e periódo 4 da tabela periódica.\n")

        sleep(3)

        print("Este é o fim da nossa pequena introdução ao cálcio.\n")

        input("Carrege no Enter para continuar")

    elif introduction == ("2"):
        print("Agora vamos iniciar um pequeno quiz sobre a informação dada na nossa introdução.")

        sleep(2)

        print("O cálcio é um elemento beneficial para a saúde, dos benefícios apresentados, indique verdadeiro(V) ou falso(F),\n")
        q1 = input("""
O cálcio previne pressões altas no sangue.
        """)
        if q1 == ("V"):
            print("Errado,")
            sleep(1)
            print("O cálcio previne a Obesidade.")
        
        elif q1 == ("F"):
            print("Certo!\n")
            pontos += 1
        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q2 = input("O cálcio fortalece os ossos.\n")

        if q2 == ("V"):
            print("Certo!\n")
            pontos += 1
        
        elif q2 == ("F"):
            print("Errado,")
            print("Esta afirmação é verdadeira.\n")
            sleep(1)

        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q3 = input("O cálcio controla a pressão arterial.\n")

        if q3 == ("V"):
            print("Certo!\n")
            pontos += 1
        
        elif q3 == ("F"):
            print("Errado,")
            print("Esta afirmação é verdadeira.\n")
            sleep(1)

        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q4 = input("O cálcio atua no transporte de oxigénio.\n")

        if q4 == ("V"):
            print("Errado,")
            sleep(1)
            print("O cálcio atua no transporte de nutrientes.\n")
        
        elif q4 == ("F"):
            print("Certo!\n")
            pontos += 1
        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q5 = input("A distribuição eletrónica do cálcio é 2-8-8-2\n")

        if q5 == ("V"):
            print("Certo!\n")
            pontos += 1
        
        elif q5 == ("F"):
            print("Errado,")
            print("Esta afirmação é verdadeira.\n")
            sleep(1)

        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q6 = input("O número atómico do cálcio é 21\n")

        if q6 == ("V"):
            print("Errado,")
            sleep(1)
            print("O número atómico do cálcio é 20.\n")
        
        elif q6 == ("F"):
            print("Certo!\n")
            pontos += 1
        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        q7 = input("O Cálcio está localizado no grupo 1 e periódo 4 da tabela periódica.\n")

        if q7 == ("V"):
            print("Errado,")
            sleep(1)
            print("O Cálcio está localizado no grupo 2 e periódo 4 da tabela periódica.\n")
        
        elif q7 == ("F"):
            print("Certo!\n")
            pontos += 1
        else:
            print("A resposta é inválida.")
            
        sleep(5)

#------------------------------------------------------------

        print(f"Você conseguiu acertar {pontos} de 7 perguntas!\n")
        sleep(2)
        print("Este é o fim da nossa apresentação.\n")

        input()

    elif introduction == ("3"):
        print("Até á próxima!")
        sleep(2)
        exit()


