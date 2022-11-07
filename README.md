# CS361-MicroserviceProject

Desription: This is a Microservice that adjusts the price of a collectible card, whenver its 'rarity' is changed by the user. When a user changes the rarity of current card, a function is called that uses text file to call a python microservice that looks at the change in 'rarity' value and then uses the change to alter the current price. The microservice sends this calculated price back to the user.
