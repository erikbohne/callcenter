import simpy
import random
import numpy as np

from parameters import *

class CallCenter:
    def __init__(self, env, employees, callTime):
        self.env = env
        self.csrs = simpy.Resource(env, capacity=employees)
        self.callTime = callTime
        self.callsHandled = 0

    def support(self, customer):
        randomTime = max(1, np.random.normal(self.callTime, 4))
        yield self.env.timeout(randomTime)
        print(f"Support finished for {customer} at {self.env.now:.2f}")
        
        
    def generate_calls(self):
        while True:
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            call = self.process_call(call)


def customer(env, name, call_center):
    global callsHandled
    print(f"Customer {name} enters waiting queue at {env.now:.2f}")
    yield env.process(call_center.support(name))
    print(f"Customer {name} left call at {env.now:.2f}")
    callsHandled += 1

    