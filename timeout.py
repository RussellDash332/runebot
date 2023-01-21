import sys
import trace
import threading
import time
import signal

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, target=kwargs['target'], args=(self, *kwargs['args']))
        self.killed = False
        self.ex_handler = kwargs['handler']

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True
        raise self.ex_handler

class fluid:
    def __init__(self,signum,frame):
        self.signum = signum
        self.frame = frame
        # do whatever according to signal id

    def __call__(self):
        pass

signal.signal(signal.SIGALRM, lambda x,y: fluid(x,y)())

class timeout:
    def __init__(self, thread=lambda: None, terminatefun=lambda: None, seconds=10):
        self.seconds = seconds
        self.thisthread = thread
        self.terminatefun = terminatefun

    def handle_timeout(self):
        try:
            self.thisthread.kill()
        except Exception as e:
            self.terminatefun()

    def __enter__(self):
        fluid.__call__ = self.handle_timeout
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)
