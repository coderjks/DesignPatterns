class Singleton:
    instance = None

    def __init__(self):
        """
        Ideally the constructor is private so that it can be accessed by static method only, like in Java.
        """
        Singleton.instance = self

    @staticmethod
    def get_instance():
        if not Singleton.instance:
            print('Creating Singleton Object')
            Singleton.instance = Singleton()
        else:
            print('Singleton obj already available')

        return Singleton.instance


if __name__ == "__main__":
    singletonObject = Singleton.get_instance()
    Singleton.get_instance()
