import timeit


class Timer:

    def __init__(self, task_name):
        self.task_name = task_name

    def __enter__(self):
        self.t1 = timeit.default_timer()

    def __exit__(self, type, value, trace):
        print("The overall time of {}: {:3f} secs".format(self.task_name, timeit.default_timer() - self.t1))
