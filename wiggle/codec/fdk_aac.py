from wiggle.codec import Codec


class FdkAac(Codec):
    def __init__(self):
        super().__init__()
        self.libname = 'fdk-aac'
