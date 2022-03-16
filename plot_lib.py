import numpy as np

import matplotlib.pyplot as plt
font = {'size'   : 16}

import matplotlib
matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True

from matplotlib.gridspec import GridSpec

def plot_cumulative_hist(e_,ax_,xlim=(0.,1.)):

    fraction = np.array([90.,80.,70.,60.])

    percentile = np.percentile(e_,fraction)

    fraction = fraction/100.

    #for p,f in zip(percentile,fraction):
    #    ax_.plot([p,1.],[f,f],"r")
    #    ax_.plot([p,p],[0,f],"r")

    ax_.set_title("Testing Error Cumulative Distribution")

    ax_.plot(percentile,fraction,'oC1')

    ax_.hist(e_,np.linspace(0,1,1000),density=True, histtype='step',cumulative=True)

    ax_.set_xlim(xlim[0],xlim[1])
    ax_.set_xticks(percentile)
    ax_.set_xticklabels(["{:.3f}".format(p) for p in percentile],rotation=90)
    ax_.set_yticks(fraction)

    ax_.set_ylim(0,1)
    ax_.grid()

def plot_active_energy(ax,s,spectral_fraction=.9):

    n_modes = np.where(np.cumsum(s/np.sum(s))>spectral_fraction)[0][0]

    spectrum = s/np.sum(s)

    ax.bar(np.arange(n_modes),spectrum[:n_modes],color='r')
    ax.bar(np.arange(n_modes,spectrum.shape[0]),spectrum[n_modes:],color='b')
    title = str(int(spectral_fraction*100))
    title +="\% of the spectrum, "
    title +=str(n_modes)
    title +=" modes."
    ax.set_title(title)
    ax.semilogy()
    ax.yaxis.grid(True)
    ax.set_yticks([1e-1,1e-2,1e-3])
    ax.set_ylim([1e-4,1.])


def plot_pod_result(D,Y,flux,pod_flux,pod_error):

    fig = plt.figure(constrained_layout=True,figsize=(16,6))

    gs = GridSpec(4, 8, figure=fig)

    ax0 = fig.add_subplot(gs[:2,0:5])
    ax1 = fig.add_subplot(gs[2:,0:5])
    ax2 = fig.add_subplot(gs[:,5:8])
    #ax2.get_yaxis().set_visible(False)

    ax2.yaxis.tick_right()

    ax0.pcolor(D,Y,flux,shading='auto')
    ax0.get_xaxis().set_visible(False)
    ax0.set_title("Original Sinogram")

    ax1.pcolor(D,Y,pod_flux,shading='auto')
    ax1.set_title("POD Reconstruction")
    ax1.set_xlabel("$\\theta$ [degrees]")

    plot_cumulative_hist(pod_error,ax2,(0.,.15))

    #ax2.set_xlim(0,.5)
    #ax2.set_ylim(0,1)
