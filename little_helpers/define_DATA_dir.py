import os

HOME = os.environ['HOME']


# def os.environ['HOME']:
#     return HOME


def define_DATA_dir():
    return HOME + '/Data'


def define_kernels_dir():
    return HOME + '/Dropbox/SternchenAndMe/SPICE_kernels'


def define_python_dir():
    return HOME + '/Dropbox/myPy'


class MyPaths(object):
    @property
    def user_dir(self):
        return os.environ['HOME']

    @property
    def DATA_dir(self):
        return define_DATA_dir()

    @property
    def kernels_dir(self):
        return define_kernels_dir()

    @property
    def python_dir(self):
        return define_python_dir()

# use like this, if you like:
# path = MyPaths()
# path.DATA_dir
# path.python_dir
# etc..
