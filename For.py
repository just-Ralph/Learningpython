import os
os.system('clear')

#for loop


names = ["john", "sussan", "ralph" ]

for name in names:
	print(name)

fav_pizza = {
	"John": "Pepperoni",
	"Tim": "Mushroom",
	"Mary": "Cheese"
}

for key,value in fav_pizza.items():
	print(key + " likes " + value + " pizza!")
	