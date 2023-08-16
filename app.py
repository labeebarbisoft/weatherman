import os
import argparse
from usage import Usage
from data_reader import DataReader
from data_calculator import DataCalculator
from report_generator import ReportGenerator


def main():
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
    args = parser.parse_args()
    if args.operation is None and args.location is None:
        Usage.print_usage()
    else:
        data = DataReader(args.location)
        if args.operation == "1":
            calculation = DataCalculator.calculate_annual_max_min(data.all_readings)
            report = ReportGenerator.generate_annual_max_min(calculation)
            for row in report:
                print(row)
        elif args.operation == "2":
            calculation = DataCalculator.calculate_hottest_day(data.all_readings)
            report = ReportGenerator.generate_hottest_day(calculation)
            for row in report:
                print(row)


if __name__ == "__main__":
    main()
