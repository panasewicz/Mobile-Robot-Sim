import time
from CoppeliaConnection import CoppeliaConnection
from Robots import PioneerP3DX  # Zaimportuj klasę PioneerP3DX
from Robots import KukaYouBot    # Zaimportuj klasę KukaYouBot


# # Tworzenie instancji robotów
    pioneer = PioneerP3DX(connection.client_id, ['Pioneer_p3dx_leftMotor', 'Pioneer_p3dx_rightMotor'])
    youbot = KukaYouBot(connection.client_id, ['rollingJoint_fl', 'rollingJoint_rl', 'rollingJoint_rr', 'rollingJoint_fr'])
    
    
    # Testowanie ruchu do przodu dla Pioneer P3-DX
    print("Poruszanie Pioneer P3-DX do przodu...")
    pioneer.move(2)
    time.sleep(10)  # Czekaj przez 2 sekundy
    pioneer.stop()
    print("Zatrzymanie Pioneer P3-DX.")

    # Krótka przerwa między testami
    time.sleep(1)

    # Testowanie ruchu do przodu dla Kuka YouBot
    print("Poruszanie Kuka YouBot do przodu...")
    youbot.move(-2)
    time.sleep(10)  # Czekaj przez 2 sekundy
    youbot.stop()
    print("Zatrzymanie Kuka YouBot.")
    time.sleep(1)




# Skręcanie 
    youbot.synchronized_movement([-1.9, -1.9, -1.9 , -1.9])
    time.sleep(5)

    youbot.setMovement([-2.3, -2.3, 2.3 , 2.3])
    # Czekaj trochę, aby robot miał czas na skręt
    time.sleep(2.2)
    youbot.setMovement([-1.9, -1.9, -1.9 , -1.9])
    time.sleep(3.5)
    youbot.stop()
    time.sleep(1)




#scene 

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