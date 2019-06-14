# Simple_timer
Python based simple timer, just for debug usage, print the time using timeit


# Install
```
pip install git+https://github.com/cftang0827/simple_timer.git
```

# Example
```Python
import simple_timer.timer as t
import time

with t.Timer("Foo"):
    time.sleep(3) # Will return all time usage within the with block
```

and you will get
```
The overall time of Foo: 3.002550 secs
```
