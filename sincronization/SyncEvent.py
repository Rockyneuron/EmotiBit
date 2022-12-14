"""Minimal example of how to send event triggers in PsychoPy with
LabStreamingLayer.
In this example, the words "hello" and "world" alternate on the screen, and
an event marker is sent with the appearance of each word.
TO RUN: open in PyschoPy Coder and press 'Run'. Or if you have the psychopy
Python package in your environment, run `python hello_world.py` in command line.
ID     EVENT
------------
1  --> hello
2  --> world
99 -->  test
------------
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
