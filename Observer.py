class Subject:
 def __init__(self):
    self._observers = []
 def attach(self, observer):
    self._observers.append(observer)
 def notify(self, message):
    for observer in self._observers:
        observer.update(message)
class Observer:
 def update(self, message):
    print(f"Received: {message}")

if __name__ == "__main__":
    subject = Subject()
    observer1 = Observer()
    observer2 = Observer()
    observer3 = Observer()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.notify("Hello World!")  # Output: Received: Hello World! Received: Hello World! Received: Hello World!
    subject.notify("Goodbye World!")  # Output: Received: Goodbye World! Received
    # : Goodbye World! Received: Goodbye World!
    # Output: Received: Hello World! Received: Hello World! Received: Hello World!
    # Output: Received: Goodbye World
    # Output: Received: Goodbye World
    # Output: Received: Goodbye World
    # Output: Received: Hello World
    # Output: Received: Hello World
    # Output: Received: Hello World
    # Output: Received: Goodbye World
    # Output: Received: Goodbye World