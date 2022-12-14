"""Script to read xdf files and check sync signal latency

"""

#%%
import pyxdf
import matplotlib.pyplot as plt
import numpy as np

data, header = pyxdf.load_xdf('sub-P001_sync_try.xdf')
#%%
for stream in data:
    y = stream['time_series']
    fig,ax = plt.subplots(1,1)

    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp)
            print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        plt.plot(stream['time_stamps'], y)
    else:
        raise RuntimeError('Unknown stream format')

# %%     Check signal latency
signal_latency=np.diff(stream['time_stamps'])

fig, ax = plt.subplots(1,1)
ax.hist(signal_latency,bins=10,histtype='barstacked')
ax.set_xlabel('Latency')
ax.set_ylabel('Frecuency')
ax.set_title('Signal latency')
ax.text(np.mean(signal_latency),2,'Max latency {}'.format(max(signal_latency)),fontsize=10)
ax.text(np.mean(signal_latency),1,'Mean latency {}'.format(np.mean(signal_latency)),fontsize=10)
plt.show()

