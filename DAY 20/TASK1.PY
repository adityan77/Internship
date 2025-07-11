# Simple Reflex Agent – Vacuum Cleaner
# 🔹Objective:
# Simulate a simple reflex agent for a 1D or 2D vacuum cleaner world.

# 🔹Instructions:
# Create an environment as a list of rooms: e.g. ['Dirty', 'Clean', 'Dirty']

# Agent starts at position 0.

# If the current position is 'Dirty' → clean it.

# Move to the next room and repeat.

# Stop when all rooms are clean.



class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0

    def clean(self):
        while 'Dirty' in self.environment:
            if self.environment[self.position] == 'Dirty':
                print(f"Cleaning room {self.position}...")
                self.environment[self.position] = 'Clean'
                print(f"Room {self.position} is now clean.")
            
            self.move_to_next_room()

        print("All rooms are clean!")

    def move_to_next_room(self):
        self.position = (self.position + 1) % len(self.environment)
        print(f"Moved to room {self.position}.")

# Create an environment
environment = ['Dirty', 'Clean', 'Dirty', 'Dirty', 'Clean']

# Initialize and run the vacuum cleaner
vacuum = VacuumCleaner(environment)
print("Initial environment:", environment)
vacuum.clean()
print("Final environment:", environment)


