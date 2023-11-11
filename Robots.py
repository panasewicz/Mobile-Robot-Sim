import sys
sys.path.append(r'C:\Users\przyz\Documents\GitHub\Robot_Tracking_Sim\Libs\python')
import sim



class RobotBase:
    def __init__(self, client_id):
        self.client_id = client_id
"""
    def move(self, speed):
        # General method for movement, can be overridden in derived classes
        raise NotImplementedError("The move method must be implemented in the derived class.")

    def stop(self):
        # General method for stopping, can be overridden
        raise NotImplementedError("The stop method must be implemented in the derived class.")
"""   
class PioneerP3DX(RobotBase):
    def __init__(self, client_id):
        super().__init__(client_id)
        _, self.left_motor_handle = sim.simxGetObjectHandle(client_id, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_blocking)
        _, self.right_motor_handle = sim.simxGetObjectHandle(client_id, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_blocking)

    def move_forward(self, speed):
        # Set speed to both motors to move forward
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle, speed, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle, speed, sim.simx_opmode_streaming)
        
    def stop(self):
        # Set speed to 0 to stop the robot
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle,0, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle,0, sim.simx_opmode_streaming)
    
        
class KukaYouBot(RobotBase):
     def __init__(self, client_id):
        super().__init__(client_id)
        _, self.left_motor_handle = sim.simxGetObjectHandle(client_id, 'rollingJoint_fl', sim.simx_opmode_blocking)
        _, self.right_motor_handle = sim.simxGetObjectHandle(client_id, 'rollingJoint_fr', sim.simx_opmode_blocking)
        _, self.left_motor_handle_2 = sim.simxGetObjectHandle(client_id, 'rollingJoint_rl', sim.simx_opmode_blocking)
        _, self.right_motor_handle_2 = sim.simxGetObjectHandle(client_id, 'rollingJoint_rr', sim.simx_opmode_blocking)

     def move_forward(self, speed):
        # Set speed to both motors to move forward
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle, speed, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle, speed, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle_2, speed, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle_2, speed, sim.simx_opmode_streaming)

     def stop(self):
        # Set speed to 0 to stop the robot
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle,0, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle,0, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.left_motor_handle_2,0, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, self.right_motor_handle_2,0, sim.simx_opmode_streaming)