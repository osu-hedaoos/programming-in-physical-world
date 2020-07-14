from finch import Finch
#Here we start using the robot
robot = Finch()

#what happens if I change stop_playing to True?
stop_playing = False

notes = [880, 988, 523, 587, 659, 698]
length = 1.2 #let's use a default length of the note


while stop_playing is False:
    for note in notes:
        print("Note is", note)
        #Question: What happens if I *remove* the indentation for the next line?
        robot.buzzer_with_delay(length, note)
    #pause for a minute
    stop = input("Do you want to stop? Enter Y to stop playing. Enter anything else to continue playing")
    if stop == 'Y':
        stop_playing = True


