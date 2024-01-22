'''
numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

if numero_1.isdigit() and numero_2.isdigit():
    int_numero_1 = int(numero_1)
    int_numero_2 = int(numero_2)
    
    soma = int_numero_1 + int_numero_2
    
    print(f"A soma de {int_numero_1} e {int_numero_2} é: {soma}")
else:
    print("Erro: Ambas as entradas devem conter apenas números.")
'''