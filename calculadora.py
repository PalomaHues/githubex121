def subtracao (a, b):
  return a-b

a = int(input("Digite o primeiro valor para a: "))
b = int(input ("Digite o segundo valor para b: "))

operacao = input("-: Subtração\n*: Multiplicação\n/: Divisão\n**: Exponenciação:\n  ")

if operacao == '-':
  resultado = (a - b)
elif   operacao == '*':
  resultado = (a * b)
elif   operacao == '/':
  resultado = a // b
else:
  operacao == '**'
  resultado = (a**b)
print (resultado)