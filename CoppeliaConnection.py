import sys
sys.path.append(r'***')
import sim

class CoppeliaConnection:
    def __init__(self):
        self.client_id = -1

    def connect(self, address='127.0.0.1', port=19999):
        """
        Establishes a connection with the CoppeliaSim server.
        """
        sim.simxFinish(-1)  # Close all existing connections
        self.client_id = sim.simxStart(address, port, True, True, 5000, 5)

        if self.client_id != -1:
            print("Connected to CoppeliaSim")
        else:
            raise ConnectionError("Failed to connect to CoppeliaSim")

    def disconnect(self):
        """
        Closes the connection with the CoppeliaSim server.
        """
        if self.client_id != -1:
            sim.simxFinish(self.client_id)
            print("Disconnected from CoppeliaSim")

    def is_connected(self):
        """
        Checks if there is an active connection with the CoppeliaSim server.
        """
        return self.client_id != -1

