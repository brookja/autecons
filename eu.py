# Import the pulsar library
from pulsar import Pulse

# Create a pulse with some initial values
pulse1 = Pulse()
pulse1.set_values([1, 2, 3, 4, 5])

# Initialize a new pulse based on the values of pulse1
pulse2 = Pulse()
pulse2.initialize_from_pulse(pulse1)

# Print the values of pulse2
print(pulse2.get_values())
