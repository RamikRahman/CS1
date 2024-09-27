def getSize(length, height, thickness):

    if length > 3.5 and length <= 4.25 and height > 3.5 and height < 6 and thickness > .007 and thickness <= 0.16:
        Package_type = "Postcard"

    elif length > 4.25 and length < 6  and height > 6 and height < 11.5 and thickness > .007 and thickness <= .015:
        Package_type = "Large_Post_Card"

    elif length > 3.5 and length <= 6.125 and height > 5 and height <= 11.5 and thickness > 0.16 and thickness < .25:
       Package_type = "Envelope" 

    elif length > 6.125 and length < 24. and height > 11 and height <= 18. and thickness > .25 and thickness <= .5:
      Package_type = "Large_Envelope"  

    elif 42.5 <= length + height *2 + thickness*2 <= 84.0: 
       Package_type = "Package"

    elif 84 < length + height*2 + thickness*2 <= 130.0:
        Package_type = "Large_Package"
    else: 
        return "Package unmailable"
    
    return Package_type
 

def getZipZone(zip1):
   
    if zip1 >= 1 and zip1 <= 6999:
        zip = 1
    
    elif zip1 >= 7000 and zip1 <= 19999: 
        zip = 2
    
    elif zip1 >= 20000 and zip1 <= 35999:
        zip = 3
        
    elif zip1 >= 36000 and zip1 <= 62999: 
        zip = 4
    
    elif zip1 >= 63000 and zip1 <= 84999:
        zip = 5

    elif zip1 >= 85000 and zip1 <= 99999: 
       zip = 6
    return zip
    
 


def getCost(type, zip1, zip2):
    if type == "Postcard":
        print (.20 + .03* abs(getZipZone(zip1) - getZipZone(zip2)))
    elif type  == "Large_Post_Card":
        print (.37 + .03* abs(getZipZone(zip1) - getZipZone(zip2)))
    elif type == "Envelope":
        print (.37 + .04* abs(getZipZone(zip1) - getZipZone(zip2)))
    elif type == "Large_Envelope":
        print (.60 + .05* abs(getZipZone(zip1) - getZipZone(zip2)))
    elif type == "Package":
        print (2.95 + .25* abs(getZipZone(zip1) - getZipZone(zip2)))
    elif type == "Large_Package":
        print (3.95 + .35* abs(getZipZone(zip1) - getZipZone(zip2)))

        


def main():

    print("welcome to the GCDS postoffice")
while True:
    try:
        data = input("enter your length, height ,thickness, the zip code your shipping from, to the zip code you are shipping too seperated by commas ").split(",")

        mail_type = getSize(float(data[0]),float(data[1]),float(data[2]))
        print(mail_type)

        cost = getCost(mail_type, int(data[3]), int(data[4]))
        (cost)
    except IndexError:
        print("Please put in 3")
    except ValueError:
        print (" ONLY put in a number")
                                   
        main()