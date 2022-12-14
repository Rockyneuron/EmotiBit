    """Script for testing if Emotibit is recieveing artificial pulses generated from LSL.
        The following is tested for data colected with different time interval marker streams
        One stream with intervals of 500ms
        Another stream of 10000ms (10s) intervals.
    """
#%%
import numpy as np
import matplotlib.pyplot   as plt
import pandas as pd
import sys
from pathlib import Path

sys.path.append(Path(r"C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL"))


#%%
%matplotlib inline
file1=r'C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL\2022-12-12_16-27-05-140907_TX_TL_LC.csv'
file2=r'C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL\2022-12-12_16-27-05-140907_TX_LC_LM.csv'
file3=r'C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL\2022-12-12_16-27-05-140907_AX.csv'
file4=r'C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL\2022-12-14_08-55-09-834278\2022-12-14_08-55-09-834278_TX_LC_LM.csv' #10s interval LSL
file5=r'C:\Users\ArturoV\Desktop\projects\EmotiBit\emotiBitData\LSL\2022-12-14_08-55-09-834278\2022-12-14_08-55-09-834278_BV.csv'

data1=pd.read_csv(file1,delimiter=",")
data2=pd.read_csv(file2,delimiter=",")
HR=pd.read_csv(file3,delimiter=",")
data4=pd.read_csv(file4,delimiter=",")
HR_data4=pd.read_csv(file5,delimiter=",")
# %%
fig,ax = plt.subplots(1,1)
ax.plot(HR['EmotiBitTimestamp'],HR['AX'],'-')
for vline in data2['EmotiBitTimestamp']:
    plt.axvline(vline, color = 'b', label = 'axvline - full height')

fig2,ax2 = plt.subplots(1,1)
ax2.plot(HR['LocalTimestamp'],HR['AX'],'o-')
for vline in data2['LocalTimestamp']:
    plt.axvline(vline, color = 'b', label = 'axvline - full height')

fig3,ax4 = plt.subplots(1,1)
ax4.plot(HR_data4['LocalTimestamp'],HR_data4['BV'],'o-')
for vline in data4['LocalTimestamp']:
    plt.axvline(vline, color = 'b', label = 'axvline - full height')


# %%
times1=np.array(data1['EmotiBitTimestamp'])
times2=np.array(data1['LocalTimestamp'])
times3=np.array(data4['LocalTimestamp'])

# %%
plt.plot(times1)
plt.plot(times2)

# %%
difftime1=np.diff(times1)
difftime2=np.diff(times2)
difftime3=np.diff(times3)
# %%
fig1,ax1=plt.subplots(1,1)
ax1.hist(difftime1,bins=20)

# %%
fig2,ax2=plt.subplots(1,1)
plt.hist(difftime2,bins=20)

# %%
fig3,ax3=plt.subplots(1,1)
plt.hist(difftime3,bins=20)
# %%
