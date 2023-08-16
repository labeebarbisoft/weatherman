import os
import argparse
from usage import Usage
from data_reader import DataReader
from data_calculator import DataCalculator
from report_generator import ReportGenerator
from arg_parser import parse_arguments
import report_type_constants


def main():
    args = parse_arguments()
    if args.operation is None and args.location is None:
        Usage.print_usage()
    else:
        data = DataReader(args.location)
        if args.operation == report_type_constants.ANNUAL_MAX_MIN:
            calculation = DataCalculator.calculate_annual_max_min(data.all_readings)
            report = ReportGenerator.generate_annual_max_min(calculation)
            for row in report:
                print(row)
        elif args.operation == report_type_constants.HOTTEST_DAY:
            calculation = DataCalculator.calculate_hottest_day(data.all_readings)
            report = ReportGenerator.generate_hottest_day(calculation)
            for row in report:
                print(row)


if __name__ == "__main__":
    main()
