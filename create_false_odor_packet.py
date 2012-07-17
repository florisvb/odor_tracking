#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def make_gaussian(size, center, fwhm = 20):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size[0], 1, np.float32)
    y = np.arange(0, size[1], 1, np.float32)[:,np.newaxis]
    x0 = center[0]
    y0 = center[1]
    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)


def make_odor_movie(wind_speed):
    
    framerate = 100.
    resolution = 1000 # 1mm
    size = [1.,0.33]
    
    n_secs = size[0] / wind_speed
    n_frames = int(n_secs*framerate)
    
    pixels = (np.array(size)*resolution).astype(int)
    
    odor_movie = np.zeros([n_frames, pixels[1], pixels[0]])
    t = 0
    dt = 1/framerate
    
    for i in range(n_frames):
        
        x_center = (0 + wind_speed*t)*resolution
        
        center = [x_center, 0]
        frame = make_gaussian(pixels, center, fwhm=20)
        odor_movie[i,:,:] = frame
        
        t += dt
        
    return odor_movie
    
    
    
class Play_Odor_Movie:
    def __init__(self, odor_movie):
        
        self.odor_movie = odor_movie
        self.fig = plt.figure()
        self.frame = 0
        self.im = plt.imshow(self.odor_movie[self.frame, :, :])
        self.frame += 1
                
        self.animation = animation.FuncAnimation(self.fig, self.update_fig, interval=50, blit=True)
        plt.show()
        
        
    def update_fig(self, *args):
        self.im.setarray(self.odor_movie[self.frame,:,:])
        self.frame += 1
        return self.im,
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
