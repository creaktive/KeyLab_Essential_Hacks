#edited for relative encoder functionality
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

def make_encoder(name, channel, number, midi_message_type):
    return EncoderElement(midi_message_type, channel, number, Live.MidiMap.MapMode.relative_signed_bit, name=name)

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        # self.add_button('Play', 0, 118, MIDI_CC_TYPE)
        # self.add_button('Record', 0, 119, MIDI_CC_TYPE)
        # self.add_button('Stop', 0, 117, MIDI_CC_TYPE)
        # self.add_button('Loop', 0, 114, MIDI_CC_TYPE)
        # self.add_button('Forward', 0, 116, MIDI_CC_TYPE)
        # self.add_button('Backward', 0, 115, MIDI_CC_TYPE)
        self.add_matrix('Encoders', make_encoder, 0, [[16,
          17,
          18,
          19,
          20,
          21,
          22,
          23]], MIDI_CC_TYPE)
        # self.add_matrix('Drum_Pads', make_button, 1, [[67,
        #   69,
        #   71,
        #   72], [60,
        #   62,
        #   64,
        #   65]], MIDI_NOTE_TYPE)


class KeyLabEssential2(ControlSurface):

    def __init__(self, *a, **k):
        super(KeyLabEssential2, self).__init__(*a, **k)
        with self.component_guard():
            midimap = MidiMap()
            # drum_rack = DrumRackComponent(name='Drum_Rack', is_enabled=False, layer=Layer(pads=midimap['Drum_Pads']))
            # drum_rack.set_enabled(True)
            # transport = TransportComponent(name='Transport', is_enabled=False, layer=Layer(play_button=midimap['Play'], record_button=midimap['Record'], stop_button=midimap['Stop'], seek_forward_button=midimap['Forward'], seek_backward_button=midimap['Backward'], loop_button=midimap['Loop']))
            # transport.set_enabled(True)
            device = DeviceComponent(name='Device', is_enabled=False, layer=Layer(parameter_controls=midimap['Encoders']))
            device.set_enabled(True)
            self.set_device_component(device)
            self._device_selection_follows_track_selection = True
