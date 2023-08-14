import time


class Timer:
    """ Context manager Timer with __enter__ and __exit__ """
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        self.time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time = time.perf_counter() - self.time
        self.readout = f"Block '{self.msg}' executed in {self.time:.3f} seconds"
        print(self.readout)


with Timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
