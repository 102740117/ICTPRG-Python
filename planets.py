planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

count = 0
numberint = 0

while (numberint < 1 or numberint > 9):
    print("Try Again")
    number = input ("Pick a number between 1 and 9: ")
    numberint = int(number)
    print(planets[numberint-1])
   










