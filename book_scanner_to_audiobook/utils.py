import numpy as np
import matplotlib.pyplot as plt

def draw_frame(frame, figsize=(20,20)):
    #added for grayscale images below
    shape=np.shape(frame)
    fig=plt.figure(figsize = figsize)
    if len(shape)==2:
        plt.imshow(frame, cmap='gray', vmin=0, vmax=255, interpolation="nearest")
    else:
        plt.imshow(frame, interpolation="nearest")
    plt.show()


