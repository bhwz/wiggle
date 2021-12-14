import wave
from pathlib import Path
from typing import Type, Optional

from wiggle.codec import Codec
from wiggle.native import find_native


def convert_file(file_in: str, file_out: str, codec: Type[Codec], quiet: bool, natives_override: Optional[str]) -> bool:
    # Input validation start.
    wav_meta: dict = {
        'channels': None,
        'sample_width': None,
        'frequency': None,
        'frame_count': None,
        'compression_type': None,
    }

    if not Path(file_in).is_file():
        print('Input file was not found!')
        return False

    try:
        wav: wave.Wave_read = wave.open(file_in, 'rb')
        wav_meta['channels'] = wav.getnchannels()
        wav_meta['sample_width'] = wav.getsampwidth()
        wav_meta['frequency'] = wav.getframerate()
        wav_meta['frame_count'] = wav.getnframes()
        wav_meta['compression_type'] = wav.getcomptype()
    except wave.Error:
        print('Invalid input file. Please make sure it is a valid PCM stream in wav format.')
        return False

    if wav_meta['compression_type'] != 'NONE':
        print('Compressed input formats are not supported.')
        return False

    if not quiet:
        print('Found the following metadata for input: ' + str(wav_meta))

    # Native validation start.
    native_path = find_native(codec, natives_override)
    if not native_path:
        print("Unable to locate natives.")
        return False

    # TODO

    return True
