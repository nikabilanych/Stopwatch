###either w countdown or by entering enter
from StopFunct import StopwatchFunctions 



class StopwatchApp:
    """

    Simple stopwatch application that uses the StopwatchFunctions class.

    Usage:
    - Press Enter to start/stop the timer.
    - Press Space to record a lap while the timer is running.
    - Press Esc to stop the timer.

    Example:
    stopwatch_app = StopwatchApp()
    stopwatch_app.run()

    """

    @staticmethod
    def run():
        """"""
        print("Welcome to Stopwatch")
        print("TO START/STOP THE TIMER PRESS: # enter #")
        print("TO MAKE A LAP WHILE THE TIME IS RUNNING PRESS: # space # ")
        # print("TO STOP THE TIMER PRESS:  # esc #")
        stopwatch=StopwatchFunctions()
        stopwatch.run()
if __name__=='__main__':
    StopwatchApp.run()



