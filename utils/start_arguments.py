from argparse import ArgumentParser, RawDescriptionHelpFormatter

from config import NAME


def parse_arguments():
    args_parser = ArgumentParser(
        prog=NAME,
        formatter_class=RawDescriptionHelpFormatter,
        description="Game about Frog whose kill balls.",
        epilog="Author: tuenut"
    )

    parsed_arguments = args_parser.parse_args()

    return parsed_arguments
