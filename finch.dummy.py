#Dummy Finch class to make sure the sample code can run without the robot

class Finch:
    def __init__(self):
        print("initializing dummy finch robot object")

    def buzzer_with_delay(self, length, note):
        print("****")
        print("ROBOT: Playing a note of frequency '%s' for '%s' seconds" % (note, length))
        print("****")
