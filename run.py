import multiprocessing
from engine.features import hotWord
from main import start  # Make sure main.py has proper __main__ guard

# Start GUI and backend


def startTARS():
    print("[TARS] Process 1 running...")
    start()

# Hotword detection using Porcupine + sounddevice


def listenHotWord():
    print("[HotWord] Process 2 running...")
    hotWord()


if __name__ == "__main__":
    multiprocessing.freeze_support()  # Required for Windows executables (PyInstaller)

    p1 = multiprocessing.Process(target=startTARS)
    p2 = multiprocessing.Process(target=listenHotWord, daemon=True)

    p1.start()
    p2.start()

    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("[SYSTEM] TARS shut down.")
