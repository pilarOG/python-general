# line profiler: library to check how much time it takes for each of a function

# sudo pip install line_profiler

import line_profiler

@profile
def slow():
    x = range(0, 3000)

@profile
def faster():
    x = xrange(0, 3000)

# run on terminal: kernprof -v -l code_profiler.py
slow()
faster()

 # memory profiler: same but for memory use, not time

 # sudo pip install memory_profiler

from memory_profiler import profile

@profile
def heavier():
    x = range(0, 30000000)

@profile
def lighter():
    x = range(0, 3000)

# run on terminal: python -m memory_profiler code_profiler.py
heavier()
lighter()
