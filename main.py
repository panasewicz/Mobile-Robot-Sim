import sys
import time
from CoppeliaConnection import CoppeliaConnection
sys.path.append(r'C:\Users\przyz\Documents\GitHub\Robot_Tracking_Sim\Libs\python')
# LOCAL API 
import sim


# Tworzenie instancji i nawiązywanie połączenia
connection = CoppeliaConnection()
try:
    connection.connect()


    time.sleep(2)  # Czekaj przez 2 sekundy
finally:
    connection.disconnect()  # Upewnij się, że połączenie jest zawsze zamykane



   


