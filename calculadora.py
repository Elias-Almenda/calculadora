import modulo_matematico

print("Bem-vindo(a) Calculadora")

while True:
  opcoes_validas = ['1','2','3','4','5','6','7']
  print("\n[1] somar\n[2] multiplicar\n[3] subtrair\n[4] divisão\n[5] potencia \n[6] raiz\n[7] juros\n[8] sair")
  
  choice = input("Escolha: ")
  
  if choice == '8':
        print("Saindo.")
        break

  elif choice == '6':
        print("\nTipos de raiz(coloque no segundo número):")
        print("2 - Raiz quadrada")
        print("3 - Raiz cúbica")
        print("4 - Raiz quarta")
        
  if choice not in opcoes_validas:
    print("Opção inválida! Tente novamente.")
    continue

  if choice == '7':
    n3 = float(input('digite o tempo do seu juros: '))

  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: "))  
  
  if choice == '1':
      print(f'Resultado da soma de {n1} e {n2} é: ',modulo_matematico.somar(n1,n2))
  elif choice == '2':
      print(f'Resultado da multiplicação de {n1} e {n2} é: ',modulo_matematico.multiplicar(n1,n2))
  elif choice == '3':
      print(f'Resultado da subtração de {n1} e {n2} é: ',modulo_matematico.subtrair(n1,n2))
  elif choice == '4':
      print(f'Resultado da divisão de {n1} e {n2} é: ',modulo_matematico.divisao(n1,n2))
  elif choice == '5':
      print(f'Resultado da potencia/raiz de {n1} e {n2} é: ',modulo_matematico.potencial(n1,n2))
  elif choice == '6':
      print(f'Resultado da raiz de {n1} e {n2} é:', modulo_matematico.raiz(n1,n2))
  elif choice == '7':
      print(f'Resultado do juros simples é:', modulo_matematico.juros_simples(n1,n2,n3))
