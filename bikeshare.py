


# Function for problem 1
def problem1():Compute the Most Popular Start Hour
    # Code for problem 1
    import pandas as pd

filename = 'chicago.csv'

## load data file into a dataframe
df = pd.read_csv(chicago)

## convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

## extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

## find the most popular hour
popular_hour = df['hour'].mode()[0]
    
print('Most Popular Start Hour:', popular_hour)


# Function for problem 2
def problem2():Display a Breakdown of User Types
    # Code for problem 2
import pandas as pd

df = pd.read_csv('chicago.csv')
user_types = df['User Type'].value_counts()

print(user_types)
# Function for problem 3
def problem3():Load and Filter the Dataset
    # Code for problem 3
import pandas as pd

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    month = input("Enter the month (January, February, march, april, may, june, july, august, september, october, november, december): ")
    day = input("Enter the day of the week (Monday, Tuesday, wednesday, thursday, friday, saturday, sunday): ")

    # Map month names to month numbers using a dictionary
    month_mapping = {
...         "January": 1,
...         "February": 2,
...         "March": 3,
...         "April": 4,
...         "May": 5,
...         "June": 6,
...         "July": 7,
...         "August": 8,
...         "September": 9,
...         "October": 10,
...         "November": 11,
...         "December": 12
...     }
... 
...     # Map day names to title case using a dictionary
...     day_mapping = {
...         "monday": "Monday",
...         "tuesday": "Tuesday",
...         "wednesday": "Wednesday",
...         "thursday": "Thursday",
...         "friday": "Friday",
...         "saturday": "Saturday",
...         "sunday": "Sunday"
...     }
... 
...     # Convert month and day to their corresponding values
...     month_number = month_mapping.get(month.title())
...     day_of_week = day_mapping.get(day.lower())
... 
...     # Call the appropriate problem function based on user input
...     if city == "load_and_filter":
...         load_data(city, month_number, day_of_week)
...     elif city == "other_function":
...         other_function(month_number, day_of_week)
...     else:
...         print("Invalid input. Please try again.")
... 
... # Call the main function to start the program
... if __name__ == "__main__":
