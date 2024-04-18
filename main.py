# FORK this starter file and save it to your own Repl.it account.


# Declare and initialize the 12 variables here:

date = "Monday 2019-03-18"
time = "10:05:34 AM"
astronautCount = input("Please Enter The Number Of Astronauts: ")
astronautStatus = "ready"
averageAstronautMassKg = 80.7
crewMassKg = int(astronautCount) * averageAstronautMassKg
fuelMassKg = 760000
shuttleMassKg = 74842.31
totalMassKg = crewMassKg + fuelMassKg + shuttleMassKg
fuelTempCelsius = -225
fuelLevel = "100%"
weatherStatus = "clear"

# Write code to generate the LC04 report here:

print("-------------------------------------")
print("> LC04 - LAUNCH CHECKLIST")
print("Date: " + date)
print("Time: " + time)
print("\n-------------------------------------")
print(">" + " ASTRONAUT INFO")
print("-------------------------------------")
print("* count: " + str(astronautCount))
print("* status: " + astronautStatus)
print("\n-------------------------------------")
print(">" + " FUEL DATA")
print("-------------------------------------")
print("* Fuel temp celsius: " + str(fuelTempCelsius) + " C")
print("* Fuel level: " + fuelLevel)
print("\n-------------------------------------")
print(">" + " MASS DATA")
print("-------------------------------------")
print("* Crew mass: " + str(crewMassKg) + " kg")
print("* Fuel mass: " + str(fuelMassKg) + " kg")
print("* Shuttle mass: " + str(shuttleMassKg) + " kg")
print("* Total mass: " + str(totalMassKg) + " kg")
print("\n-------------------------------------")
print(">" + " FLIGHT PLAN")
print("-------------------------------------")
print("* weather: " + weatherStatus)
print("\n-------------------------------------")
print(">" + " OVERALL STATUS")
print("-------------------------------------")
print("* Clear for takeoff: YES")

# When done, have your TA check your code.

# BONUS: Use input to prompt the user to enter the number of astronauts going on the mission.