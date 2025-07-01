
repetir=0

while repetir==0:

    print("o que deseja fazer:")
    print("1- somar.\n2-multiplicar\n3-dividir\ndigite 0 para sair.\n")
    escolha=int(input("digite sua escolha:\n"))
    if escolha==1:
        valor1=int(input("digite o primeiro valor"))
        valor2=int(input("digite o segundo valor"))
        resultado=valor1+valor2
        resultado=int(resultado)
        print("o resultado é",resultado)
    elif escolha==2:
        valor1=int(input("digite o primeiro valor"))
        valor2=int(input("digite o segundo valor"))
        resultado=valor1*valor2
        resultado=int(resultado)
        print("o resultado é",resultado)
    elif escolha==0:
        repetir=1
        print("sistema fechando...")
    else:
        valor1=int(input("digite o primeiro valor"))
        valor2=int(input("digite o segundo valor"))
        resultado=valor1/valor2
        resultado=int(resultado)
        print("o resultado é",resultado)
    
    
    