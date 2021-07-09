"""The distance between two cities (in km) is input through keyboard.
   Write a program to convert and print the distance in meters, feet, inches and centimetres."""

Dist_KM = int(input("Give me your Distance Between Two Cities "))

#Distance in M , F , inch , cm

Dist_M = Dist_KM*1000
Dist_feet = Dist_KM*3280.84
Dist_inch = Dist_KM*39370.1
Dist__CM = Dist_KM*100000
print("Your Distance in Meter, feet , inches and centimeters is respectively : ",
      (Dist_M), ",", (Dist_feet), ",", (Dist_inch), ",", (Dist__CM))
