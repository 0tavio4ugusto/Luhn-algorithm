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
firstPacing= 1
firstSum = 0

secondCounter = cardNumberLen-1
secondPacing = 2
secondSum = 0
termSum = 0


while firstPacing <= cardNumberLen:
    currentNumber = (cardNumberInt // (10**(cardNumberLen-firstCounter)) % 10)
    firstPacing += 2
    firstCounter -= 2
    firstSum = firstSum + currentNumber
   

while secondPacing <= cardNumberLen:
    currentNumberTwo = (cardNumberInt // (10**(cardNumberLen-secondCounter)) % 10)
    doubledCurrentNumberTwo = currentNumberTwo * 2
    
    if ((doubledCurrentNumberTwo) / 10) >= 1:
        firstTerm = (doubledCurrentNumberTwo // 1) % 10
        secondTerm = (doubledCurrentNumberTwo // 10) % 10
        
        secondPacing += 2
        secondCounter -= 2
        

        secondSum =  secondSum + (firstTerm + secondTerm)
        
    else:         
        
        secondPacing += 2
        secondCounter -= 2
        secondSum = secondSum + doubledCurrentNumberTwo
        
finalSecondSum = termSum + secondSum
    
        

if (finalSecondSum + firstSum) % 10  == 0:
    print('=== VALID CARD NUMBER ===')
    if cardNumberStr[0] == ('4'):
        print('=== VISA ===')
    elif cardNumberStr[0] == ('3'):
        print('=== AMERICAN EXPRESS ===')
    elif cardNumberStr[0] == ('5'):
        print('=== MASTERCARD ===')
else:
    print('=== INVALID CARD NUMBER ===')

    