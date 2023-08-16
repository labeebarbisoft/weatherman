class Usage:
    @staticmethod
    def print_usage():
        usage = """
            Usage: weatherman [report#] [data_dir]

            [Report #]
            1 for Annual Max/Min Temperature
            2 for the Hottest day of each year

            [data_dir]
            The directory containing weather data files
            """
        print(usage)
