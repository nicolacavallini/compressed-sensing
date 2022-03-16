import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    y = np.linspace(-1,1,100)
    t_ids = np.arange(360,dtype=np.float64)

    [T_ids,Y] = np.meshgrid(t_ids,y)

    t = t_ids/359.
    T = T_ids/359.

    M = .8 * np.sin(2*np.pi*T)

    sigma = .1
    F = np.exp(-.5*((Y-M)/sigma)**2)/(sigma*np.sqrt(2*np.pi))

    u, s, vh = np.linalg.svd(F, full_matrices=False)

    fig, ax = plt.subplots(2,1)

    ax[0].pcolor(T,Y,F,shading="auto")
    ax[1].plot(s/np.sum(s),'-o')
    plt.show()
