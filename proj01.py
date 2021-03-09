#Computer Project #1
#Neil Kim
#CSE 231
#Input the rods and convert it into the desired unit such as furlong, mile, feet, and walking speed. Using each of those
# units we used one another to find the conversions for the other units. Then finding each of those conversions we
# display it.
rod = 5.0292 #meters
furlong = 40 #rods
mile = 1609.34 #meters
foot = 0.3048 #meters
walking_speed = 3.1 #mph

inp_rods = input("Input rods: ")
flt_rods = float(inp_rods)
print( "You Input:", flt_rods, "rods.")

print("Conversions")

meters_conv = (flt_rods * rod)
flt_meters = float(meters_conv)
print_meters = print("Meters:", round(flt_meters, 3))

feet_conv = (flt_meters / foot)
flt_feet = float(feet_conv)
print_meters = print("Feet:", round(flt_feet, 3))

miles_conv = (flt_meters / mile)
flt_miles = float(miles_conv)
print_miles = print("Miles:", round(flt_miles, 3))

furlongs_conv = (flt_rods / furlong)
flt_furlongs = float(furlongs_conv)
print_furlongs = print("Furlongs:", round(flt_furlongs, 3))

minwalk_conv = flt_rods / ((walking_speed * mile) / (60 * rod))
flt_minwalk = float(minwalk_conv)
print_minwalk = print("Minutes to walk", flt_rods, "rods:", round(flt_minwalk, 3))



