import os

# Get a list of all log files in the Logs directory Hint: Use the os.listdir() function
log_files = os.listdir('./Logs')
# print(log_files)


# Process each log file Hint: Use a for loop to iterate over the log files
for log_file in log_files:
    # Initialize counters for each type of event
    # Hint: You can use simple variables for this
    error_count = 0
    warning_count = 0
    info_count = 0

    # Open the log file
    # Hint: Use the 'with open()' statement to open the file for reading
    with open(f"./Logs/{log_file}", "r") as file:
        # Read each line in the log file
        # Hint: Use a for loop to iterate over the lines in the file
        for line in file:
            # Count the number of each type of event
            # Hint: Use if statements and the 'in' keyword to check if a string is in the line
            if "ERROR" in line:
                error_count +=1
            elif "WARNING" in line:
                warning_count +=1
            elif "INFO" in line:
                info_count +=1
    # Write the counts to the report file
    # Hint: Use the 'with open()' statement to open the file for writing
    # Hint: Use the 'write()' method to write a line to the file
    with open (f'./Reports/Report_for_{log_file}', 'w') as report_file:
        report_file.write(f"ERROR: {error_count}\n")
        report_file.write(f'WARNING: {warning_count}\n')
        report_file.write(f'INFO: {info_count}\n')