
   
print("welcome to the GCDS postoffice")

data = input ("enter your length, height ,thickness, the zip code your shipping from, to the zip code you are shipping too seperated by commas")
dimensions = data.split(",")
length = dimensions[0]
length = float(length)
height = dimensions [1]
height = float(height)
thickness = dimensions [2]
thickness = float(thickness)

print (length)
print (height) 
print (thickness) 
while true:
    if height >= 3.25 and height <= 4.25: 
        print ("yes")
