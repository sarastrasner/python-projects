# TODO: Given the above information, complete the code exercise by printing out the speed it takes to run the
#  fast_function() vs the slow_function(). You will need to complete the speed_calc_decorator() function.

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i * i


fast_function()
slow_function()
