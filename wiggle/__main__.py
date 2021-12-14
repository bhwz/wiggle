import argparse
import sys
from typing import Optional, Type

from wiggle import convert_file
from wiggle.codec import Codec, FdkAac


def main() -> int:
    arg_parser = argparse.ArgumentParser(description='Wiggle CLI.')
    arg_parser.add_argument('input', type=str, help='Input file to convert in wav format.')
    arg_parser.add_argument('output', type=str, help='Output file destination.')
    arg_parser.add_argument('--quiet', action='store_true', dest='quiet', help='Disable progress messages.')
    arg_parser.add_argument('--natives-path', '--natives', dest='natives_override', type=str,
                            help='''
                            Directory to search for natives. If not specified various system paths will be checked.''')
    args = arg_parser.parse_args()

    file_in: str = args.input
    file_out: str = args.output
    quiet: bool = args.quiet
    natives_override: Optional[str] = args.natives_override

    # noinspection PyTypeChecker
    codec: Type[Codec] = FdkAac()  # TODO: Codec picking.

    if convert_file(file_in, file_out, codec, quiet, natives_override):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
