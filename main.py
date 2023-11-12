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
    youbot = KukaYouBot(connection.client_id, ['rollingJoint_fl', 'rollingJoint_rl', 'rollingJoint_rr', 'rollingJoint_fr'], ['slippingJoint_fl', 'slippingJoint_rl', 'slippingJoint_rr', 'slippingJoint_fr'])
    

    # Skręcanie w prawo
    youbot.synchronized_movement([-4, -4, -4 , -4])
    pioneer.move(1)
    time.sleep(2)

    youbot.setMovement([-2.1, -2.1, 2.1 , 2.1])
    # Czekaj trochę, aby robot miał czas na skręt
    time.sleep(2.1)
    youbot.setMovement([-2.3, -2.3, -2.3 , -2.3])
    time.sleep(3.5)
    youbot.stop()
    pioneer.turn(0,1)
    time.sleep(1)
    pioneer.move(1)
    time.sleep(2.5)
    pioneer.turn(0,1.1)
    time.sleep(1.25)
    pioneer.move(1)
    time.sleep(5.4)
    pioneer.stop()
    time.sleep(1)

except Exception as e:
    print(f"Wystąpił wyjątek: {e}")

finally:
    connection.disconnect()  # Zamykanie połączenia




   


