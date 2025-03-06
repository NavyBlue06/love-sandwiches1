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


def get_sales_data():
    """
    Asks the user to input sales figures from the last market.
    Ensures the data is correctly formatted before proceeding.
    """
    while True:  # Keep asking for input until valid data is provided
        print("Please enter sales data from the last market")
        print("Data should be six numbers, separated by commas")
        print("Example: 10,20,30,40,50,60\n")

        # Take user input and strip extra spaces
        data_str = input("Enter your data here: ").strip()

        # Confirm the entered data
        print(f"The data provided is {data_str}")

        # Convert input string into a list
        sales_data = data_str.split(",")

        # Validate the data
        if validate_data(sales_data):
            print("Data is valid!")
            return sales_data  # Return valid data to be stored in Google Sheets


def validate_data(values):
    """
    Validates user input:
    - Ensures exactly 6 values are provided.
    - Checks that all values are integers.
    Returns True if valid, otherwise prompts user again.
    """
    try:
        # Check if there are exactly 6 values
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")

        # Convert values from strings to integers
        int_values = [int(value) for value in values]  # Will raise error if non-numeric

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False  # If invalid, return False to re-prompt user

    return True  # Data is valid


def update_sales_worksheet(data):
    """
    Updates the 'sales' worksheet in Google Sheets.
    Appends a new row with the latest sales data.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")  # Open 'sales' worksheet
    sales_worksheet.append_row([int(num) for num in data])  # Convert data to integers before appending
    print("Sales worksheet updated successfully!\n")


# Ensure script runs only when executed directly
if __name__ == "__main__":
    print("DEBUG: Script has started running!")  # Debugging message
    sales_data = get_sales_data()  # Get user input
    update_sales_worksheet(sales_data)  # Store the data in Google Sheets
    print(f"Final validated sales data: {sales_data}")
