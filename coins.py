# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # vraagt hoeveel je moet betalen en zet het om in centen
paid = int(float(input('Paid amount: ')) * 100) # vraagt hoeveel je betaalt hebt en maakt dat naar centen
change = paid - toPay # berekent wat je moet terug geven

if change > 0: # als er wisselgeld moet zijn is 500 het beginaantal
  coinValue = 500 # begin aantal
  
  while change > 0 and coinValue > 0: # zorgt ervoor dat als het niet in 1 keer word terug betaalt dat het dan naar de volgende gaat
    nrCoins = change // coinValue # de deelsom om het resultaat te berekenen

    if nrCoins > 0: # als je wisselgeld terug moet krijgen 
      print('return maximal '+ str(nrCoins) + " coins of " + str(coinValue) + ' cents!' ) # laat het aantal zien dat je maximaal moet terug gevenß
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue # de rekensom om het teruggegeven geld te berekenen

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    
    else:
      coinValue = 0

if change > 0: #als het groter is dan 0 en niet genoeg  terug gegeven word er pinrt(Change not returned) 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('je hebt in totaal ' + str(nrCoinsReturned) +  " coins terug gegeven") 