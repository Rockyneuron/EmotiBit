"""Send event triggers to LabStreamingLayer for posterior synchronization.
EmotiBit cant send streams directly to LSL but is able to capture a single channel 
stream from LSL.

"""
from pylsl import StreamInfo, StreamOutlet
import time

def main():
   
    # Set up LabStreamingLayer stream.
    info = StreamInfo(name='DataSyncMarker', type='Tags', channel_count=1,
                      channel_format='string', source_id='12345')
    outlet = StreamOutlet(info)  # Broadcast the stream.

    # This is not necessary but can be useful to keep track of markers and the
    # events they correspond to.
    markers = {
        'event': ['sync_event'],
        'test': ['test_event']
    }
    
    # Send triggers to test communication.
    for _ in range(5):
        outlet.push_sample(markers['test'])
    
    while True:
            outlet.push_sample(markers['event'])        
            time.sleep(0.5)

if __name__ == "__main__":
    main()
