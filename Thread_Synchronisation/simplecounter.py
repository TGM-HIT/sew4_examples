import threading

# Globaler Zaehler
counter = 0

class SimpleCounter(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    einen globalen Zaehler 1000-mal erhoeht.
    """

    def __init__(self):
        """
        Initialisiert die Basisklasse Thread.
        """
        threading.Thread.__init__(self)

    def run(self):
        """
        Erhoeht counter 1000-mal. run() wird
        aufgerufen, sobald der Thread über start()
        gestartet wird.
        :return: None
        """

        # Globale Variable counter "importieren"
        global counter
        for i in range(1000):
            curValue = counter
            print("Current Value:" + str(curValue))
            counter = curValue + 1


# 10 Instanzen der Thread-Klasse erstellen
threads = []
for i in range(0, 10):
    thread = SimpleCounter()
    threads += [thread]
    thread.start()

# Auf die Kind-Threads warten
for x in threads:
    x.join()

# Counter ausgeben
print(counter)
if counter != 10000:
    print("Wrong result - we should probably synchronize those threads!")