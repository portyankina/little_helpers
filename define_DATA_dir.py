def define_user_dir():
    import platform
    this_comp = platform.node()
    if this_comp[0:8] == 'macd2657':
        user_dir = '/Users/gapo7695/'
    else:
        user_dir = '/Users/Anya/'
    
    return user_dir

def define_DATA_dir():
    import platform
    this_comp = platform.node()
    if this_comp[0:8] == 'macd2657':
        data_dir = '/Users/gapo7695/Data/'
    else:
        data_dir = '/Users/Anya/Data/'
    
    return data_dir
    
def define_kernels_dir():
    import platform
    this_comp = platform.node()
    if this_comp[0:8] == 'macd2657':
        kernels_dir = '/Users/gapo7695/Dropbox/SternchenAndMe/SPICE_kernels/'
    else:
        kernels_dir = '/Users/Anya/Dropbox/SternchenAndMe/SPICE_kernels/'
    
    return kernels_dir
    
def define_python_dir():
    import platform
    this_comp = platform.node()
    if this_comp[0:8] == 'macd2657':
        python_dir = '/Users/gapo7695/Dropbox/myPy'
    else:
        python_dir = '/Users/Anya/Dropbox/myPy'
    
    return python_dir