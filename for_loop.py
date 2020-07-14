from finch import Finch
#Here we start using the robot
robot = Finch()

notes = [880, 988, 523, 587, 659, 698]
length = 1.2 #let's use a default length of the note

for note in notes:
    print("Note is", note)
       
    #Question: What happens if I *remove* the indentation for the next line?
    robot.buzzer_with_delay(length, note)

print("The last note was ", note)
print("All notes played!")