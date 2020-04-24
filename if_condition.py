from finch import Finch

#Here we start using the robot
robot = Finch()

#Ask user for a note
note = input("Enter a note in lowercase")

#if the note entered is uppercase, it will be long, else short
if (note.isupper()):
    length = 1.2  # uppercase letters mean long notes
else:
    length = 0.6  # lowercase are short

#convert note to lowercase so that we can compare easily
note = note.lower() 

if (note == 'a'):
    frequency = 880  
elif (note == 'b'):
    frequency = 988
elif (note == 'c'):
    frequency = 523
elif (note == 'd'):
    frequency = 587
elif (note == 'e'):
    frequency = 659
elif (note == 'f'):
    frequency = 698
else:
    #no valid note, nothing to play
    frequency = 0
    
if frequency > 0:
    print("Playing note: ", note)
    #this is how we play the note on the robot
    robot.buzzer(length, frequency)  # play the note!
else:
    print("Please enter a valid note!")
