import math


# define functions to calculate

print("\t===========WELCOME TO THE BETA VERSION OF RESULTANT FINDER=======\nBy KAVINDU CHAMODH NETHSARA")

def calculateResultant(first_vector,second_vector,angle):

    # calculate the size of resultant

    resultant = math.sqrt(first_vector**2+second_vector**2+2*first_vector*
                          (second_vector*math.cos(angle)))
    return resultant

def  calculateSecondAngle(first_vector,second_vector,angle):

    # calculate of the direction of the resultant
    tangent = (second_vector*math.sin(angle)/(first_vector+
                             first_vector*math.cos(angle)))
    
    secondAngle  = math.degrees(math.atan(tangent))
    secondAngle1 = int(math.degrees(math.atan(tangent)))
    floatings = secondAngle - secondAngle1
    minutes = int(floatings*60)
    

    return [secondAngle1,minutes]

# Get the Inputs
while True:
    first_vector  = int(input("Enter the first vector: "))
    second_vector = int(input("Enter the second vector: "))
    angle = int(input("Enter Your Angle: "))
    angle = math.radians(angle)
    # call the functions

    Resultant = calculateResultant(first_vector,second_vector,angle)
    second_degree = calculateSecondAngle(first_vector,second_vector,angle)[0]
    second_minutes =calculateSecondAngle(first_vector,second_vector,angle)[1]

    # print the output

    print("Resultant Vector Is : "+str(Resultant))
    print("Angle of the Resultant is : "+ str(second_degree)+" degrees "+
          str(second_minutes)+" minutes")

    if input("enter 'c' to continue: ") == 'c':
        continue
    else:
        break




                            



