from finch import Finch
#Here we start using the robot
robot = Finch()

notes = ['A','a','B','b','C','c','D','d','E','e','F','f','A','a']

for note in notes:
    print("Note is", note)
    if (note.isupper()):
        length = 1.2  # uppercase letters mean long notes
    else:
        length = 0.6  # lowercase are short

    #convert note to lowercase so that we can compare easily
    current_note = note.lower() 

    if (current_note == 'a'):
        frequency = 880  
    elif (current_note == 'b'):
        frequency = 988
    elif (current_note == 'c'):
        frequency = 523
    elif (current_note == 'd'):
        frequency = 587
    elif (current_note == 'e'):
        frequency = 659
    elif (current_note == 'f'):
        frequency = 698
   
    print("Frequency is", frequency)
    #Question: What happens if I *remove* the indentation for the next line?
    robot.buzzer_with_delay(length, frequency)

