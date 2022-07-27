# 1 from the last digit we skip every other number and then sum them up
# 2 from the last digit +1 we double them and then we sum them up
# 3 sum up both results, if the final result == 0, then the card is valid


# american express cards start with 34 or 37 and have 15 digits
# mastercard cards start with 51-55 and have 16 digits
# visa cards start with 4 and have 13 or 16 digits


cardNumberStr = str(input('Card Number: '))
cardNumberInt = int(cardNumberStr)
cardNumberLen = len(cardNumberStr)

while cardNumberInt <= 0:
    print(cardNumberInt)
   
  
       

#for len(cardNumberStr):
# 5502090966601067 5
     11