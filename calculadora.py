def subtracao (a, b):
  return a-b

a = int(input("Digite o primeiro valor para a: "))
b = int(input ("Digite o segundo valor para b: "))

operacao = input("-: Subtração\n*: Multiplicação: ")

if operacao == '-':
  resultado = (a - b)
else:
  operacao == '*'
  resultado = (a * b)

print (resultado)