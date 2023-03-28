import calendar
import os

class utils:
    def get_month_name(month_number):
        """
        This function takes a month number as input and returns the name of the month.
        """
        # First, validate the input month number.
        if not 1 <= month_number <= 12:
            raise ValueError("Month number must be between 1 and 12.")

        # Use the calendar module to get the month name.
        month_name = calendar.month_name[month_number]

        return month_name[:3]
    def check_dir(directory_path):
        if os.path.exists(directory_path):
            return True
        else:
            # Do something else if the directory doesn't exist
            return False