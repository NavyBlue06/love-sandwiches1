# Import the gspread library, which allows interaction with Google Sheets
import gspread

# Import Credentials from google.oauth2.service_account to authenticate API requests
from google.oauth2.service_account import Credentials

# Define the scope (permissions) that our program needs to interact with Google Sheets and Drive
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',  # Grants access to Google Sheets
    'https://www.googleapis.com/auth/drive.file',    # Grants access to specific files in Google Drive
    'https://www.googleapis.com/auth/drive'         # Grants full access to Google Drive (not just files)
]

# Load credentials from a JSON file ('creds.json'), which contains the authentication keys
CREDS = Credentials.from_service_account_file('creds.json')

# Apply the defined SCOPE (permissions) to the credentials
SCOPE_CREDS = CREDS.with_scopes(SCOPE)

# Create a gspread client using the authorized credentials
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)

# Open the Google Sheet named 'love_sandwiches' and store it in a variable
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


# Define a function to collect sales data from the user
print('testing')
def get_sales_data():
    """
    This function asks the user to input sales figures from the last market.
    It ensures the data is formatted correctly before proceeding.
    """
while True: # Create an infinite loop that will keep asking for data until
    # the correct format is provided
    print("Please enter sales data from the last market")  # Display instructions to the user
    print("Data should be six numbers, separated by commas")  # Explain input format
    print("Example: 10,20,30,40,50,60\n")  # Provide an example input format

    # Take user input as a string (text)
    data_str = input("Enter your data here: ")

    # Print back what the user entered to confirm their input
    print(f"The data provided is {data_str}")

    # Convert the input string into a list by splitting at each comma
    sales_data = data_str.split(",")

    # Call the validate_data function to check if the input is valid
    validate_data(sales_data)

    if validate_data(sales_data): # If the data is valid
        print("Data is valid!")
        break # Exit the loop
    # If the data is invalid, the loop will continue to the next iteration
    # and prompt the user to enter the data again

# Define a function to validate the user input
def validate_data(values):
    """
    This function checks if the input data meets the required format:
    - It should contain exactly 6 values.
    - All values should be integers.
    If the input is invalid, the function prompts the user to re-enter the data.
    """
    try:
        [int(value) for value in values]  # Check if all values are integers
        # Check if the number of values in the list is exactly 6
        if len(values) != 6:
            raise ValueError(  # Raise an error if the number of values is incorrect
                f"Exactly 6 values required, you provided {len(values)}"
            )

        # Convert all values from strings to integers
        int_values = [int(value) for value in values]  # This will raise an error if a value is not a number
    
    except ValueError as e:  # If an error occurs (e.g., incorrect input format)
         print(f"Invalid data: {e}, please try again.\n")  # Show error message
    return False  # Return False if the data is invalid

return True  # Return True if the data is valid

get_sales_data()



# Next steps (to be implemented):
# 1. Add the sales data to the 'sales' worksheet in the Google Sheet.
# 2. Calculate surplus data (difference between stock and sales).
# 3. Add surplus data to the 'surplus' worksheet.
# 4. Calculate the average sales for the last 5 markets.
# 5. Add calculated stock numbers to the 'stock' worksheet.
