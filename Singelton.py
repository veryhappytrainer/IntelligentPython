class Singleton:
 _instance = None
 def __new__(cls):
    if cls._instance is None:
        cls._instance = super().__new__(cls)
    return cls._instance
 
if __name__ == "__main__":
    # Create two instances of Singleton
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()

    # Check if both instances are the same
    print(f"Instance1 is instance2: {instance1 is instance2}")
    print(f"Instance1 is instance3: {instance1 is instance3}")
    print(f"Instance2 is instance3: {instance2 is instance3}")
