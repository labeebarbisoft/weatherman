# This is a report generator for creating the reports given the computation results
class ReportGenerator:
    @staticmethod
    def generate_annual_max_min(calculations):
        report = [
            "{:<12}{:<15}{:<15}{:<19}{:<12}".format(
                "Year",
                "MAX Temp",
                "MIN Temp",
                "MAX Humidity",
                "MIN Humidity",
            ),
            "-" * (12 + 15 + 15 + 19 + 12),
        ]

        for year, weather_data in sorted(calculations.items()):
            max_temp = weather_data["max_temp"]
            min_temp = weather_data["min_temp"]
            max_humidity = weather_data["max_humidity"]
            min_humidity = weather_data["min_humidity"]
            report.append(
                f"{year:<12}{max_temp:<15}{min_temp:<15}{max_humidity:<19}{min_humidity:<12}"
            )

        return report

    @staticmethod
    def generate_hottest_day(calculations):
        report = [
            "{:<12}{:<15}{:<4}".format(
                "Year",
                "Date",
                "Temp",
            ),
            "-" * (12 + 15 + 4),
        ]

        for year, weather_data in sorted(calculations.items()):
            hottest_date = weather_data["hottest_date"]
            hottest_temp = weather_data["hottest_temp"]
            report.append(f"{year:<12}{hottest_date:<15}{hottest_temp:<4}")

        return report
