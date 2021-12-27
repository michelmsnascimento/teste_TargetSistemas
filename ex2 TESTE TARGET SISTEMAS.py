numA=0
numB=1
result=0
entrada=int(input("Digite um numero inteiro :"))

while result < entrada:
    result = numA + numB
    print(result)
    numA = numB
    numB = result

if entrada == result:  
    print("O numero",entrada,", pertence a sequência Fibonacci.")

else:
    print("O numero",entrada,", não pertence a sequência Fibonacci.")
