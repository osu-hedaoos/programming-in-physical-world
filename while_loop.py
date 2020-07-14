from finch import Finch
#Here we start using the robot
robot = Finch()

length = 1.2 #let's use a default length of the note
stop_playing = False

while stop_playing is False:

    robot.buzzer_with_delay(length, 588)
    #pause for a minute
    stop = input("Do you want to stop? Enter Y to stop playing. Enter anything else to continue playing")
    if stop == 'Y':
        stop_playing = True

    if stop_playing is True:
        robot.buzzer_with_delay(length, 670)
        # Question: What happens if I *remove* the indentation for the next two lines?
        robot.buzzer_with_delay(length, 670)
        robot.buzzer_with_delay(length, 670)


