# CS361-MicroserviceProject 

Desription: 
This is a Microservice that adjusts the price of a collectible card, whenver its 'rarity' is changed by the user. When a user changes the rarity of current card, a function is called that uses text file to call a python microservice that looks at the change in 'rarity' value and then uses the change to alter the current price. The microservice sends this calculated price back to the user.

How to Request Data:
In the main.py file, there is a function calculateNewPrice(num, cuRarity,newRarity) that takes as its parameters: the current price of the card, the current 'rarity value', and the new  'rarity' value the user wants to change the card to. When the function is called it writes to a text file called send.txt these values, separated by commas and prefixed the character 'S' to indicate that the message is being sent. Meanwhile in the rarity.py file, a while loop is currently running

