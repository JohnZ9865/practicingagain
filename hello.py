def pns(a, b): #prime numer searcher
  primeNumbers = []
  for i in range(a, b + 1):
    isPrimeFlag = True
    for loop in range(2, i):
      if i % loop == 0:
        isPrimeFlag = False
        break
    if isPrimeFlag == True:
      primeNumbers.append(i)
  print(primeNumbers)

i0 = int(input('Please enter the first integer: '))
i1 = int(input('Please enter the second integer: '))
pns(i0, i1)
    