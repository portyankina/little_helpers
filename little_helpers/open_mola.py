import numpy as np
import gdal
from gdalconst import *
from pymars import pdstools

def open_S_mola(filename, lat=90, lon=0, x_points=0, y_points=0):
    
    label_f = filename[:-3]+'lbl'
    label = pdstools.get_labels(label_f)
    RES = pdstools.get_angle(label, 'IMAGE_MAP_PROJECTION', 'MAP_RESOLUTION')
    mola_scale = pdstools.get_angle(label, 'IMAGE_MAP_PROJECTION', 'MAP_SCALE')
    scaling_factor = pdstools.get_angle(label, 'IMAGE', 'SCALING_FACTOR')
    offset = pdstools.get_angle(label, 'IMAGE', 'OFFSET')
    N = pdstools.get_angle(label, 'IMAGE', 'LINES')
    dataset = gdal.Open( label_f, GA_ReadOnly )
    if dataset is None: print 'no MOLA data'
    band = dataset.GetRasterBand(1)
    
    R = np.rad2deg(np.sin(np.deg2rad(lat + 90.0)))
    
    if lon >= 270:
        X = - R*np.sin(np.deg2rad(360.-lon))
        Y = - R*np.cos(np.deg2rad(360.-lon))
    elif lon >= 180:
        X = - R*np.sin(np.deg2rad(lon - 180.0))
        Y = R*np.cos(np.deg2rad(lon - 180.0))
    elif lon > 90:
        X = R*np.cos(np.deg2rad(lon - 90.))
        Y = R*np.sin(np.deg2rad(lon - 90.))
    else:
        X = R*np.sin(np.deg2rad(lon))
        Y = - R*np.cos(np.deg2rad(lon))
    
    #print X, Y, R   
    I = N/2 + X*RES +  0.5
    J = N/2 + Y*RES + 0.5
    sample = int(I - x_points/2)
    line = int(J - y_points/2)
    if x_points == 0: 
        x_points = band.XSize
        sample = 0
    if y_points == 0: 
        y_points = band.YSize
        line = 0

    #print sample, line, N, RES
    
    if sample < 0:
        sample = 0
        print 'subframe is out of MOLA polar coverage: shift subframe, i.e. sample = ', sample
    if line < 0:
        line = 0
        print 'subframe is out of MOLA polar coverage: shift subframe, i.e. line = ', line
    if sample + x_points >= N:
        sample = int(N - x_points)
        print 'subframe is larger then sample size in X direction: shift subframe, i.e. sample = ', sample
    if line + y_points >= N:
        line = int(N - y_points)
        print 'subframe is larger then line size in Y direction: shift subframe, i.e. line = ', line
    
    mola = band.ReadAsArray(sample, line, x_points, y_points)*scaling_factor + offset  # *scaling factor of mola + offset
    return mola, mola_scale, RES # mola_scale in km/pixel

