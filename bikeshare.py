import pandas as pd

# Compute the Most Popular Start Hour
filename = 'chicago.csv'

# Load data file into a dataframe
df = pd.read_csv(filename)

# Convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# Find the most popular hour
popular_hour = df['hour'].mode()[0]
    
print('Most Popular Start Hour:', popular_hour)

# Display a Breakdown of User Types
user_types = df['User Type'].value_counts()
print(user_types)

# Load and Filter the Dataset
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

# Main function to handle user input and call the appropriate problem function
def main():
    # Solicit and handle user input
    city = input("Enter the name of the city: ")
    month = input("Enter the month (January, February, March, April, May, June): ")
    day = input("Enter the day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")

    # Call the load_data function based on user input
    df = load_data(city, month, day)

    # Perform further analysis or display results based on the problem requirements

# Call the main function to start the program
if __name__ == "__main__":
    main()
