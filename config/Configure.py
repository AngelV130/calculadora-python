import os

class Configure:
    def __init__(self, path):
        self.path = path
    @staticmethod
    def ROOT_DIR():
        return Configure.path
    @staticmethod
    def RESOURCES_DIR():
        return os.path.join(Configure.path, 'resources')
    @staticmethod
    def CONTROLLERS_DIR():
        return os.path.join(Configure.path, 'app/Controllers')