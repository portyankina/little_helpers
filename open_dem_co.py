""" this is open_dem_co.py
"""
from __future__ import print_function
import gdal
from gdalconst import *


def open_dem(filename, x_start=0, y_start=0, x_points=0, y_points=0):
    dataset = gdal.Open(filename, GA_ReadOnly)
    if dataset is None:
        print('no dem data')
    band = dataset.GetRasterBand(1)
    #print band.XSize, band.YSize
    if x_points == 0:
        x_points = band.XSize
    if y_points == 0:
        y_points = band.YSize
    data = band.ReadAsArray(x_start, y_start, x_points, y_points)

    return data, band.XSize, band.YSize


def open_GDAL_data(filename, x_start, y_start, x_points, y_points,
                   filetype):
    #open slope map created by gdaldem
    dataset = gdal.Open(filename, GA_ReadOnly)
    if dataset is None:
        print('no slope data')
    band = dataset.GetRasterBand(1)
    print('gdal {} size: X, Y'.format(filetype), band.XSize, band.YSize)
    data = band.ReadAsArray(x_start, y_start, x_points, y_points)
    nr_nans = np.array(np.where(
                       data == band.GetNoDataValue())).size
    if nr_nans > 0:
        data[data == band.GetNoDataValue()] = np.nan
    return data


def open_slope(slope_file, x_start, y_start, x_points, y_points):
    return(open_GDAL_data(slope_file, x_start, y_start,
                          x_points, y_points, 'slope'))


def open_aspect(aspect_file, x_start, y_start, x_points, y_points):
    return(open_GDAL_data(aspect_file, x_start, y_start,
                          x_points, y_points, 'aspect'))
