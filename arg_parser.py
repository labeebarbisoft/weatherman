import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Weather Data Processor")
    parser.add_argument(
        "operation",
        choices=["1", "2"],
        nargs="?",
        help="Choose operation: 1 or 2",
    )
    parser.add_argument(
        "location",
        choices=["weatherdata/"],
        nargs="?",
        help="Location for weather data processing",
    )
    return parser.parse_args()
