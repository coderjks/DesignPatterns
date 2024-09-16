class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            print('Creating Singleton Object')
            Singleton()
        else:
            print('Singleton obj already available')

        return Singleton._instance


if __name__ == "__main__":
    singleton_obj = Singleton.get_instance()
    singleton_obj.get_instance()
