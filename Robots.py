import sys
sys.path.append(r'C:\Users\przyz\Documents\GitHub\Robot_Tracking_Sim\Libs\python')
import sim
import math




class RobotBase:
    def __init__(self, client_id, motor_names):
        self.client_id = client_id
        self.initialize_motors(motor_names)

    def initialize_motors(self, motor_names):
        self.motor_handles = []
        for name in motor_names:
            _, handle = sim.simxGetObjectHandle(self.client_id, name, sim.simx_opmode_blocking)
            self.motor_handles.append(handle)

    def move(self, speed):
        # Set the same speed to all motors
        for handle in self.motor_handles:
            sim.simxSetJointTargetVelocity(self.client_id, handle, speed, sim.simx_opmode_streaming)

    def stop(self):
        # Set speed to 0 to stop the robot
        for handle in self.motor_handles:
            sim.simxSetJointTargetVelocity(self.client_id, handle, 0, sim.simx_opmode_streaming)


class PioneerP3DX(RobotBase):
    def __init__(self, client_id, motor_names):
        super().__init__(client_id, motor_names)

    def turn(self, left_speed, right_speed):
        # Ustawienie różnych prędkości dla lewego i prawego silnika
        if len(self.motor_handles) >= 2:  # Upewniamy się, że mamy dwa silniki
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[0], left_speed, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[1], right_speed, sim.simx_opmode_streaming)

    
        
class KukaYouBot(RobotBase):
    def __init__(self, client_id, motor_names):
        super().__init__(client_id, motor_names)
        self.initialize_omni_wheels()

    def initialize_omni_wheels(self):
        omni_wheel_joints = ['slippingJoint_fl', 'slippingJoint_fr', 'slippingJoint_rl', 'slippingJoint_rr']
        self.slipping_joints = []
        for name in omni_wheel_joints:
            _, handle = sim.simxGetObjectHandle(self.client_id, name, sim.simx_opmode_blocking)
            self.slipping_joints.append(handle)

    def set_omni_wheel_orientation(self):
        # Ustawienie orientacji stawów omni-kół
        sim.simxSetObjectOrientation(self.client_id, self.slipping_joints[0], -1, [-math.pi/4, 0, 0], sim.simx_opmode_streaming)
        sim.simxSetObjectOrientation(self.client_id, self.slipping_joints[1], -1, [math.pi/4, 0, math.pi], sim.simx_opmode_streaming)
        sim.simxSetObjectOrientation(self.client_id, self.slipping_joints[2], -1, [math.pi/4, 0, math.pi], sim.simx_opmode_streaming)
        sim.simxSetObjectOrientation(self.client_id, self.slipping_joints[3], -1, [-math.pi/4, 0, 0], sim.simx_opmode_streaming)
        
    def setMovement(self, speed, speed2, speed3, speed4):
        # Zakładamy, że motor_handles[0] to lewe przednie koło, 
        # motor_handles[1] to lewe tylne koło, itd.
        if len(self.motor_handles) >= 4:
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[0], speed, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[1], speed2, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[2], speed3, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[3], speed4, sim.simx_opmode_streaming)

    def synchronized_movement(self, speed, speed2, speed3, speed4):
        # Najpierw ustaw orientację stawów
        self.set_omni_wheel_orientation()
        # Następnie ustaw prędkości kół
        self.setMovement(speed, speed2, speed3, speed4)


"""
    def setMovement(self, forwBackVel, leftRightVel, rotVel):
        # Zakładamy, że motor_handles[0] to lewe przednie koło, 
        # motor_handles[1] to lewe tylne koło, itd.
        if len(self.motor_handles) >= 4:
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[0], -forwBackVel - leftRightVel - rotVel, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[1], -forwBackVel + leftRightVel - rotVel, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[2], -forwBackVel - leftRightVel + rotVel, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(self.client_id, self.motor_handles[3], -forwBackVel + leftRightVel + rotVel, sim.simx_opmode_streaming)

"""