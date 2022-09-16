import sys

sys.path.insert(1, 'F:/Python/__My Python Programs/AudioPlayer')
from AudioPlayer import AudioPlayer
sys.path.insert(1, 'F:/Python/__My Python Programs/GetCurrentTime')
from GetCurrentTime import GetCurrentTime

class ErrorLogger:
    def __init__(self):
        self.AP = AudioPlayer()
        self.GCT = GetCurrentTime()
        self.error_log = []


# This function displays a message in case there is an error, and saves the information about the error to a CSV log
    def inCaseOfError(self, error=None, description=None, pause_time=0, program=None, line_number=None, number_of_attempts=1, alert=True):
        print(program + ' : !!! ERROR occurred on line ' + str(line_number) + ' while ' + description)
        print(program + ' : Error: ' + str(error))
        pause_for_error = True
        starting_second = int(self.GCT.getTimeStamp())
        starting_datetime = self.GCT.getDateTimeString()
        error_dict = {'Time': starting_datetime, \
                      'Error': error, \
                      'Description': description, \
                      'Program': program, \
                      'Line #': line_number, \
                      'Pause Time': pause_time, \
                      '# of Attempts': number_of_attempts}
        self.error_log.append(error_dict)
        if alert:
            self.AP.playSound('Navi Hey')
        if pause_time > 0:
            print('Pausing for ' + str(pause_time) + ' seconds')
            while pause_for_error:
                current_second = int(self.GCT.getTimeStamp())
                if current_second - starting_second > pause_time:
                    pause_for_error = False
            print('Pause over! Returning to ' + description)
        return(error_dict)
