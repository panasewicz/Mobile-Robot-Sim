import time
from CoppeliaConnection import CoppeliaConnection
from Robots import PioneerP3DX  # Zaimportuj klasę PioneerP3DX
from Robots import KukaYouBot    # Zaimportuj klasę KukaYouBot

# Tworzenie instancji i nawiązywanie połączenia
connection = CoppeliaConnection()
try:
    connection.connect()

    # Tworzenie instancji robotów
    pioneer = PioneerP3DX(connection.client_id, ['Pioneer_p3dx_leftMotor', 'Pioneer_p3dx_rightMotor'])
    youbot = KukaYouBot(connection.client_id, ['rollingJoint_fl', 'rollingJoint_rl', 'rollingJoint_rr', 'rollingJoint_fr'], ['slippingJoint_fl', 'slippingJoint_rl', 'slippingJoint_rr', 'slippingJoint_fr'], ['youBotArmJoint0', 'youBotArmJoint1', 'youBotArmJoint2', 'youBotArmJoint3'], ['youBotGripperJoint1', 'youBotGripperJoint2'])
    

    # Ustawienie pozycji dla wszystkich stawów manipulatora
    joint_positions = [0.1, 0.7, 0.8, 1.3]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)

    youbot.set_gripper_position(1)
    time.sleep(0.5)

    gripper_speed = 0.5
    youbot.set_gripper_speed(gripper_speed)
    time.sleep(0.5)

    joint_positions = [0.1, 0.3, 0.4, 0.7]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)

    joint_positions = [0, 0, 0, 1.3]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)

    youbot.synchronized_movement([-4, -4, -4 , -4])
    pioneer.move(1)
    time.sleep(2)

    youbot.setMovement([-2.3, -2.3, 4.1 , 4.1])
    # Czekaj trochę, aby robot miał czas na skręt
    time.sleep(2.1)
    youbot.setMovement([-2.5, -2.5, -2.5 , -2.5])
    time.sleep(3.5)
    youbot.stop()
    pioneer.turn(0,1.1)
    time.sleep(1)
    pioneer.move(1.05)
    time.sleep(2.9)
    pioneer.turn(-0.1,0.8)
    time.sleep(1.2)
    pioneer.move(1)
    time.sleep(5.3)
    pioneer.stop()
    time.sleep(1)

    
    joint_positions = [-0.1, -0.3, -0.4, -0.7]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)

    joint_positions = [-0.1, -0.7, -0.8, -0.9]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)

    gripper_speed = -0.5
    youbot.set_gripper_speed(gripper_speed)
    time.sleep(0.5)

    youbot.set_gripper_position(-1)
    time.sleep(0.5)

    joint_positions = [-0.1, -0.3, -0.4, -0.7]  # Pozycje dla poszczególnych stawów       [max 2.3, max 1.6, max 2.3, max 1.8] [0, 0.7, 0.8, 1.3]
    youbot.set_all_joints_position(joint_positions)
    time.sleep(1)


except Exception as e:
    print(f"Wystąpił wyjątek: {e}")

finally:
    connection.disconnect()  # Zamykanie połączenia




   


