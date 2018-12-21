def gradient2D(dem): # former grad2d(dem)
    '''
    Calculate the slope and gradient of a DEM
    '''
    from scipy import signal
    f0 = gaussianFilter(3)
    I = signal.convolve(dem,f0,mode='valid')
    f1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    f2 = f1.transpose()
    g1 = signal.convolve(I,f1,mode='valid')
    g2 = signal.convolve(I,f2,mode='valid')
    slope = np.sqrt(g1**2 + g2**2)
    aspect = np.arctan2(g2,g1)
    return slope, aspect