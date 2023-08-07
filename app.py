import os
import argparse


class WeatherDataProcessor:
    def __init__(self, location):
        self.location = location
        self._data = {}
        # Read all the data when the object of class is created
        self.process_files()

    def process_files(self):
        for filename in os.listdir(self.location):
            self.process_file(filename)

    def process_file(self, filename):
        with open(self.location + filename, "r") as file:
            # Skip the empty line
            next(file)
            # Skip the header line
            next(file)
            for line in file:
                # Do not read the last line of format: <!-- 0.289:0 -->
                if not line.startswith("<"):
                    (
                        date,
                        max_temp,
                        _,
                        min_temp,
                        _,
                        _,
                        _,
                        max_humidity,
                        _,
                        min_humidity,
                        *_,
                    ) = line.strip().split(",")
                    year = date.split("-")[0]
                    self.update_data(
                        year, max_temp, min_temp, max_humidity, min_humidity, date
                    )

    def update_data(self, year, max_temp, min_temp, max_humidity, min_humidity, date):
        # Will throw an exception while converting if the field is missing
        try:
            max_temp = int(max_temp)
            min_temp = int(min_temp)
            max_humidity = int(max_humidity)
            min_humidity = int(min_humidity)
        except ValueError:
            # If a field is missing then discard the current row
            return

        # Adding new row for the year
        if year not in self._data:
            self._data[year] = {
                "max_temp": max_temp,
                "min_temp": min_temp,
                "max_humidity": max_humidity,
                "min_humidity": min_humidity,
                "hottest_date": date,
                "hottest_temp": max_temp,
            }
        # Updating previously existing row for the year
        else:
            data_year = self._data[year]
            data_year["max_temp"] = max(data_year["max_temp"], max_temp)
            data_year["min_temp"] = min(data_year["min_temp"], min_temp)
            data_year["max_humidity"] = max(data_year["max_humidity"], max_humidity)
            data_year["min_humidity"] = min(data_year["min_humidity"], min_humidity)

            if max_temp > data_year["hottest_temp"]:
                data_year["hottest_temp"] = max_temp
                data_year["hottest_date"] = date

    def generate_report_1(self):
        print(
            "{:<12}{:<15}{:<15}{:<19}{:<12}".format(
                "Year",
                "MAX Temp",
                "MIN Temp",
                "MAX Humidity",
                "MIN Humidity",
            )
        )
        print("-" * (12 + 15 + 15 + 19 + 12))
        for year, weather_data in sorted(self._data.items()):
            max_temp = weather_data["max_temp"]
            min_temp = weather_data["min_temp"]
            max_humidity = weather_data["max_humidity"]
            min_humidity = weather_data["min_humidity"]
            print(
                f"{year:<12}{max_temp:<15}{min_temp:<15}{max_humidity:<19}{min_humidity:<12}"
            )

    def generate_report_2(self):
        print(
            "{:<12}{:<15}{:<4}".format(
                "Year",
                "Date",
                "Temp",
            )
        )
        print("-" * (12 + 15 + 4))
        for year, weather_data in sorted(self._data.items()):
            hottest_date = weather_data["hottest_date"]
            hottest_temp = weather_data["hottest_temp"]
            print(f"{year:<12}{hottest_date:<15}{hottest_temp:<4}")


def main():
    usage = """
            Usage: weatherman [report#] [data_dir]

            [Report #]
            1 for Annual Max/Min Temperature
            2 for the Hottest day of each year

            [data_dir]
            The directory containing weather data files
            """

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
        print(usage)
    else:
        weather_object = WeatherDataProcessor(args.location)
        if args.operation == "1":
            weather_object.generate_report_1()
        elif args.operation == "2":
            weather_object.generate_report_2()


if __name__ == "__main__":
    main()
