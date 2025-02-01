#### solar energy production ####

# Initialize variables
is_sunny = True
wind_speed = 5.4
temperature = 23
solar_panel_output = 9
is_cloudy = False

# The complete logical expression
result = is_sunny == True and \
    wind_speed < 10 \
        and solar_panel_output < 15 \
            and is_cloudy == False \
    and temperature > 20 \
        or is_cloudy == False


# Print result
print("Checking conditions for solar energy production...")
print("1. Is it sunny?", is_sunny)
print("2. Is wind speed safe?", wind_speed < 10)
print("3. Can panels produce more?", solar_panel_output < 15)
print("4. Is temperature good OR no clouds?", (temperature > 20 or not is_cloudy))
print("\nFinal result - Good day for solar energy production:", result)

#### Pet allowance ####
# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = has_license or has_experience and has_space
can_sell_exotic_pet = has_license and has_experience and has_space
cannot_sell_any_pet = (not has_license and has_space) and (not has_experience)

# Print result
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)


#### Calculations ####
# Use the // operator for integer division. For example: 7 // 2 equals 3 (not 3.5)
# Type your code below
x = 15
y = 4
z = 23

w = x // y
v = z // x
u = z // y

# Don't change the line below
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"w = {w}")
print(f"v = {v}")
print(f"u = {u}")

# Type your code below
score = 100
score /= 2
score += 10
score *= 3

# Don't change the line below
print(f"score = {score}")


#### Is hiking possible ####
# initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculate conditions
# Can go hiking if it's sunny, temperature is above 15°C, and wind speed is below 20 km/h
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20

# Can go swimming if it's sunny, temperature is above 20°C, and water temperature is above 18°C
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18

# Cannot go outside if it's not sunny, temperature is below 10°C, or wind speed is above 30 km/h
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)