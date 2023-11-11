import time
from CoppeliaConnection import CoppeliaConnection
from Robots import PioneerP3DX  # Zaimportuj klasę PioneerP3DX
from Robots import KukaYouBot    # Zaimportuj klasę KukaYouBot

# Tworzenie instancji i nawiązywanie połączenia
connection = CoppeliaConnection()
try:
    connection.connect()

    # Tworzenie instancji robotów
    pioneer = PioneerP3DX(connection.client_id)
    youbot = KukaYouBot(connection.client_id)
    
    # Testowanie ruchu do przodu dla Pioneer P3-DX
    print("Poruszanie Pioneer P3-DX do przodu...")
    pioneer.move_forward(0.5)
    time.sleep(2)  # Czekaj przez 2 sekundy
    pioneer.stop()
    print("Zatrzymanie Pioneer P3-DX.")

    # Krótka przerwa między testami
    time.sleep(1)

    # Testowanie ruchu do przodu dla Kuka YouBot
    print("Poruszanie Kuka YouBot do przodu...")
    youbot.move_forward(0.5)
    time.sleep(2)  # Czekaj przez 2 sekundy
    youbot.stop()
    print("Zatrzymanie Kuka YouBot.")
    time.sleep(1)

except Exception as e:
    print(f"Wystąpił wyjątek: {e}")

finally:
    connection.disconnect()  # Zamykanie połączenia




   


