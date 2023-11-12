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
    youbot = KukaYouBot(connection.client_id, ['rollingJoint_fl', 'rollingJoint_rl', 'rollingJoint_rr', 'rollingJoint_fr'])
    

    # Skręcanie w prawo
    youbot.synchronized_movement(-1.9, -1.9, -1.9 , -1.9)
    time.sleep(5)

    youbot.setMovement(-1.9, -1.9, 2.2 , 2.2)
    # Czekaj trochę, aby robot miał czas na skręt
    time.sleep(2.2)
    youbot.setMovement(-1.9, -1.9, -1.9 , -1.9)
    time.sleep(3.5)
    youbot.stop()
    time.sleep(1)

except Exception as e:
    print(f"Wystąpił wyjątek: {e}")

finally:
    connection.disconnect()  # Zamykanie połączenia




   


