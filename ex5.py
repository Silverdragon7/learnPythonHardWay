name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches to cm
wieght = 180 * 0.4535 # lbs to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {wieght} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + wieght
print(f"If I add {age}, {height}, and {wieght} I get {round(total)}")