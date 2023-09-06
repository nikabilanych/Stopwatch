from time import time
from pynput.keyboard import Key, Listener

class StopwatchFunctions:
    """
    Class containing methods for a simple stopwatch app controlled by monitoring user's keyboard
    
    Attributes:
        self.is_running (bool): Indicates whether the stopwatch is currently running.
        start_time (float): will be assigned with the value of time.time()
                            after self.is_running is set to True
        lap_time (float): Equal to start_time, value of this variable is resetted after recording each lap
        laps (list): A list of lap times recorded 
        elapsed_time (float): The total elapsed time of the stopwatch
    """
    def __init__(self):
        self.is_running=False
        self.start_time=0
        self.elapsed_time=0
        self.lap_time=0
        self.laps=[]
    def commands(self,key):
        """
            Monitors user's keyboard and performs stopwatch operations.

        Args:
            key (Key): The key event received from the keyboard.

        Key Bindings:
            - Enter: Toggles the stopwatch on/off.
            - Space: Records a lap time while the stopwatch is running.
            - Esc: Stops the stopwatch if it is not running.

        *key* argument is taken from user's keyboard.
 
        """
        if key == Key.enter:
            self.toggle_stopwatch()
        if key == Key.space and self.is_running:
            self.lap()
    #starting & stopping
    def toggle_stopwatch(self):
        """
        toggles stopwatch on/off
        sets variables start_time && lap_time to time()
        """
        #start the timer
        if not self.is_running:
            self.is_running=True
            self.start_time=time()
            self.lap_time=time()
            print("TIMER STARTED")
            return
        #stop the timer
        self.is_running=False
        self.elapsed_time= time()-self.start_time
        self.print_result()
    def lap(self):
        """
        is triggered when Listener records whitespace was pressed

        
        """
        #if stopwatch is running
        if self.is_running:
            #prints out the number of the lap onto the screen
            print(f"Lap n.:{(len(self.laps)+1)}")
            self.laps.append(time()-self.lap_time)
            #resets the starting time for other lap
            self.lap_time=time()
    def print_result(self):
        """
        Prints the result of the stopwatch.
        together with laps if any
        """
        print("TOTAL TIME ELAPSED: ",self.elapsed_time)
        if self.laps:
            for i,j in enumerate(self.laps,1):
                print(f"LAP n.{i}: {j}")

      
                
    def run(self):
        """
        Starts the stopwatch together with keyboard listening
            ---- starts the multithread ----
        """
        with Listener(on_press=self.commands) as listener:

            listener.join()
