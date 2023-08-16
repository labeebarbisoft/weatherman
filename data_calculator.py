# This is a module for computing calculations given reading
class DataCalculator:
    @staticmethod
    def calculate_annual_max_min(data):
        # Data structure to hold calculations result
        calculations = {}

        for day, day_data in data.items():
            year = list(map(str, day.split("-")))[0]
            if year not in calculations:
                calculations[year] = {
                    "max_temp": day_data["max_temp"],
                    "min_temp": day_data["min_temp"],
                    "max_humidity": day_data["max_humidity"],
                    "min_humidity": day_data["min_humidity"],
                }
            else:
                # Updating row for the year
                calculations[year]["max_temp"] = max(
                    calculations[year]["max_temp"], day_data["max_temp"]
                )
                calculations[year]["min_temp"] = min(
                    calculations[year]["min_temp"], day_data["min_temp"]
                )
                calculations[year]["max_humidity"] = max(
                    calculations[year]["max_humidity"], day_data["max_humidity"]
                )
                calculations[year]["min_humidity"] = min(
                    calculations[year]["min_humidity"], day_data["min_humidity"]
                )

        return calculations

    @staticmethod
    def calculate_hottest_day(data):
        # Data structure to hold calculations result
        calculations = {}
        for day, day_data in data.items():
            year = list(map(str, day.split("-")))[0]
            if year not in calculations:
                calculations[year] = {
                    "hottest_date": day,
                    "hottest_temp": day_data["max_temp"],
                }
            else:
                if day_data["max_temp"] > calculations[year]["hottest_temp"]:
                    # Updating row for the year
                    calculations[year]["hottest_temp"] = day_data["max_temp"]
                    calculations[year]["hottest_date"] = day

        return calculations
