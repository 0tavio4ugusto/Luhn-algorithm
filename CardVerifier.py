# 1 from the last digit we skip every other number and then sum them up
# 2 from the last digit +1 we double them and then we sum them up
# 3 sum up both results, if the final result == 0, then the card is valid


# american express cards start with 34 or 37 and have 15 digits
# mastercard cards start with 51-55 and have 16 digits
# visa cards start with 4 and have 13 or 16 digits



cardNumberStr = str(input('Card Number: '))
cardNumberInt = int(cardNumberStr)
cardNumberLen = len(cardNumberStr)


firstCounter = cardNumberLen
firstJubilu = 1
firstSum = 0

secondCounter = cardNumberLen-1
secondJubilu = 2
secondSum = 0
termSum = 0


while firstJubilu <= cardNumberLen:
    currentNumber = (cardNumberInt // (10**(cardNumberLen-firstCounter)) % 10)
    print((cardNumberInt // (10**(cardNumberLen-firstCounter)) % 10))
    firstJubilu += 2
    firstCounter -= 2
    firstSum = firstSum + currentNumber
   
print (firstSum)

while secondJubilu <= cardNumberLen:
    currentNumberTwo = (cardNumberInt // (10**(cardNumberLen-secondCounter)) % 10)
    doubledCurrentNumberTwo = currentNumberTwo * 2
    
    if ((doubledCurrentNumberTwo) / 10) > 1:
        firstTerm = ((doubledCurrentNumberTwo) // 1) % 10
        secondTerm = ((doubledCurrentNumberTwo) // 10) % 10
        
        finalTerm = firstTerm + secondTerm
        termSum = termSum + finalTerm
        
    else:
         
        print((cardNumberInt // (10**(cardNumberLen-secondCounter)) % 10))
        secondJubilu += 2
        secondCounter -= 2
        secondSum = secondSum + doubledCurrentNumberTwo

finalSecondSum = termSum + secondSum
        
print (finalSecondSum)
#for len(cardNumberStr):
# 5502090966601067 
    