from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, functionA, functionB, functionC, functionD, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.functionA   = functionA
        self.functionB   = functionB
        self.functionC   = functionC
        self.functionD   = functionD
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.functionA(*self.args, **self.kwargs)
        self.functionB(*self.args, **self.kwargs)
        self.functionC(*self.args, **self.kwargs)
        self.functionD(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False