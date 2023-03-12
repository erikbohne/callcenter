import simpy
import random

from callcenter import CallCenter
from parameters import *

callsHandled = 0

def main():
    
    env = simpy.Environment()
    env.process(setup(env))
    env.run(until=SIMULATIONTIME)
    
    print(f"Customers handled: {callsHandled}")

def setup(env):
    call_center = CallCenter(env, EMPLOYES, CALLTIME)

    for incoming in range(1, 4):
        env.process(customer(env, incoming, call_center))

    while True:
        yield env.timeout(random.randint(NEWCALLRATE - 1, NEWCALLRATE + 1))
        incoming += 1
        env.process(customer(env, incoming, call_center))
        
def customer(env, name, call_center):
    global callsHandled
    print(f"Customer {name} enters waiting queue at {env.now:.2f}")
    yield env.process(call_center.support(name))
    print(f"Customer {name} left call at {env.now:.2f}")
    callsHandled += 1

if __name__ == "__main__":
    main()