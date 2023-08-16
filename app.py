import os
import argparse
from usage import Usage
from data_reader import DataReader
from data_calculator import DataCalculator
from report_generator import ReportGenerator
from arg_parser import parse_arguments


def main():
    args = parse_arguments()
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
