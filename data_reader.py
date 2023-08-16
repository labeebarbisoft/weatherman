import os


class DataReader:
    def __init__(self, location):
        self.location = location
        # This is the data structure for holding each weather reading
        self.all_readings = {}
        # Read all files when object of class is created
        self.process_files()

    def process_files(self):
        for filename in os.listdir(self.location):
            self.process_file(filename)

    # This is a parser for parsing the files and populating the all_readings data structure.
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
                        mean_temp,
                        min_temp,
                        dew_point,
                        mean_dew,
                        min_dew,
                        max_humidity,
                        mean_humidity,
                        min_humidity,
                        max_sea_pressure,
                        mean_sea_pressure,
                        min_sea_pressure,
                        max_visibility,
                        mean_visibility,
                        min_visibility,
                        max_wind_speed,
                        mean_wind_speed,
                        max_gust_speed,
                        precipitation,
                        cloud_cover,
                        events,
                        wind_directions,
                    ) = line.strip().split(",")
                    try:
                        max_temp = int(max_temp)
                        min_temp = int(min_temp)
                        max_humidity = int(max_humidity)
                        min_humidity = int(min_humidity)
                    except ValueError:
                        # If a field is missing then discard the current row
                        continue
                    self.all_readings[date] = {
                        "max_temp": max_temp,
                        "min_temp": min_temp,
                        "max_humidity": max_humidity,
                        "min_humidity": min_humidity,
                    }
