import sys
sys.path.append(r'C:\Users\przyz\Documents\GitHub\Robot_Tracking_Sim\Libs\python')
import sim
import math




class RobotBase:
    def __init__(self, client_id, motor_names):
        self.client_id = client_id
        self._initialize_motors(motor_names)

    def _initialize_motors(self, motor_names):
        self.motor_handles = [self._get_motor_handle(name) for name in motor_names]

    def _get_motor_handle(self, name):
        _, handle = sim.simxGetObjectHandle(self.client_id, name, sim.simx_opmode_blocking)
        return handle

    def move(self, speed):
        for handle in self.motor_handles:
            self._set_motor_speed(handle, speed)

    def stop(self):
        self.move(0)

    def _set_motor_speed(self, handle, speed):
        sim.simxSetJointTargetVelocity(self.client_id, handle, speed, sim.simx_opmode_streaming)


class PioneerP3DX(RobotBase):
    def __init__(self, client_id, motor_names):
        super().__init__(client_id, motor_names)

    def turn(self, left_speed, right_speed):
        if len(self.motor_handles) >= 2:
            self._set_motor_speed(self.motor_handles[0], left_speed)
            self._set_motor_speed(self.motor_handles[1], right_speed)


class KukaYouBot(RobotBase):
    def __init__(self, client_id, motor_names, omni_wheel_names, arm_joint_names, gripper_joint_names):
        super().__init__(client_id, motor_names)
        self._initialize_omni_wheels(omni_wheel_names)
        self._initialize_arm_joints(arm_joint_names)
        self._initialize_gripper_joints(gripper_joint_names)

    def _initialize_arm_joints(self, arm_joint_names):
        self.arm_joints = [self._get_motor_handle(name) for name in arm_joint_names]

    def _initialize_gripper_joints(self, gripper_joint_names):
        self.gripper_joints = [self._get_motor_handle(name) for name in gripper_joint_names]

    def _initialize_omni_wheels(self, omni_wheel_names):
        self.slipping_joints = [self._get_motor_handle(name) for name in omni_wheel_names]

    def set_arm_joint_position(self, joint_index, position):
        # Ustawia pozycję pojedynczego stawu manipulatora
        sim.simxSetJointTargetPosition(self.client_id, self.arm_joints[joint_index], position, sim.simx_opmode_oneshot)    

    def set_gripper_position(self, position):
        for joint in self.gripper_joints:
            sim.simxSetJointTargetPosition(self.client_id, joint, position, sim.simx_opmode_oneshot)

    def set_all_joints_speed(self, speeds):
        # Ustawia prędkości dla wszystkich stawów manipulatora
        for joint_handle, speed in zip(self.arm_joints, speeds):
            sim.simxSetJointTargetVelocity(self.client_id, joint_handle, speed, sim.simx_opmode_oneshot)

    def set_arm_joint_speed(self, joint_index, speed):
        # Ustawia prędkość pojedynczego stawu manipulatora
        sim.simxSetJointTargetVelocity(self.client_id, self.arm_joints[joint_index], speed, sim.simx_opmode_oneshot)

    def set_gripper_speed(self, speed):
        # Ustawia prędkość chwytaka
        for joint in self.gripper_joints:
            sim.simxSetJointTargetVelocity(self.client_id, joint, speed, sim.simx_opmode_oneshot)

    def set_all_joints_position(self, positions):
        # Ustawia pozycje dla wszystkich stawów manipulatora
        for joint_handle, position in zip(self.arm_joints, positions):
            sim.simxSetJointTargetPosition(self.client_id, joint_handle, position, sim.simx_opmode_oneshot)

    def set_gripper_speed(self, speed):
        # Ustawia prędkość chwytaka
        for joint in self.gripper_joints:
            sim.simxSetJointTargetVelocity(self.client_id, joint, speed, sim.simx_opmode_oneshot)

    def set_gripper_position(self, position):
        # Ustawia pozycje chwytaka
        for joint in self.gripper_joints:
            sim.simxSetJointTargetPosition(self.client_id, joint, position, sim.simx_opmode_oneshot)

    def set_omni_wheel_orientation(self):
        orientations = [[-math.pi/4, 0, 0], [math.pi/4, 0, math.pi], [-math.pi/4, 0, 0] , [math.pi/4, 0, math.pi]]
        for joint, orientation in zip(self.slipping_joints, orientations):
            sim.simxSetObjectOrientation(self.client_id, joint, -1, orientation, sim.simx_opmode_streaming)

    def setMovement(self, speeds):
        for handle, speed in zip(self.motor_handles, speeds):
            self._set_motor_speed(handle, speed)

    def synchronized_movement(self, speeds):
        self.set_omni_wheel_orientation()
        self.setMovement(speeds)


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