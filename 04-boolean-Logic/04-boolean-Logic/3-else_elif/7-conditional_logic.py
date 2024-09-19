a = 16
b = 25
c = 27
if a > b:		# se "a" for maior que "b" o código abaixo será executado
    if b > c:		# se "b" for maior que "c"  o programa imprimirá "a is greater than b and b is greater than c")
        print ("a is greater than b and b is greater than c")
    else: 		# se a condição b > c não for verdadeira, então o código abaixo será eexecutado
        print ("a is greater than b and less than c")
elif a == b:		# Se a condição a > b não for verdadeira, essa instrução será executada
    print ("a is equal to b")
else:			# Se nenhuma das condições anteriores for verdadeira, este bloco de código será executado, indicando que "a" é menor que "b"
    print ("a is less than b")