# whisper2graphite

Replay your whisper files into graphite

## Installing

Not really released since I haven't actually imported anything into Graphite yet.

`git clone git://github.com/philipcristiano/whisper2graphite.git && cd whisper2graphite && python setup.py install`

## Running

whisper2graphite --graphite-host graphite.example.com --whisper-path=whisper

This will take the directory structure and recreate the metric name. `{whisper-path}/metric/count.wsp` will become `metric.count`
