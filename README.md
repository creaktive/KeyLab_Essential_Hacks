![Groovy!](https://i.imgur.com/ioepBJO.jpg)

Disgusting hack put together during a rainy weekend to enable Instant Mapping for Arturia KeyLab Essential MIDI controller in Ableton Live 10.
That's right, the knobs are no longer tied to the marginally useful track panning! Instead, they are automagically mapped to the controls of the selected device
with the blue hand icon (just like it's meant to be). You can now tweak them macros like a boss!

To install, go to `/Applications/Ableton Live 10 Suite.app/Contents/App-Resources/MIDI Remote Scripts/` and rename `KeyLab_Essential` directory to `KeyLab_Essential_BACKUP`.
Then, copy the corresponding directory from this repository.
This will release the encoder knobs from their hardcoded panning function.
To assign the knobs to Instant Mapping, also copy the `KeyLab_Essential2` directory.
To activate add _KeyLab Essential2_ as *another* Control Surface in MIDI preferences. Input should be the same as of _KeyLab Essential_:

![Ableton Live Preferences](https://i.imgur.com/JyMziTk.png)

Reference projects:
 - [Ableton Live and Akai’s Endless Encoders](https://richardmedek.com/2016/01/13/ableton-live-and-akais-endless-encoders/)
 - [Live 10.1 MIDI Remote Python Scripts Sources uncompiled](https://julienbayle.studio/ableton-live-midi-remote-scripts/) ([GitHub repo](https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts))
 - [Setup your Arturia Keylab essential for Ableton Live](https://drolez.com/blog/music/arturia-keylab-ableton-setup.php)
