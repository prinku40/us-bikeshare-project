import pandas as pd

def compute_popular_start_hour(df):
    """
    Compute the most popular start hour from the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

def end_time_analysis(df):
    """
    Perform analysis on the end time field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Calculate the trip duration in seconds
    df['Trip Duration'] = (df['End Time'] - df['Start Time']).dt.total_seconds()

    # Calculate the total trip duration
    total_duration = df['Trip Duration'].sum()

    # Calculate the average trip duration
    average_duration = df['Trip Duration'].mean()

    print('Total Trip Duration:', total_duration)
    print('Average Trip Duration:', average_duration)

def start_station_analysis(df):
    """
    Perform analysis on the start station field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Calculate the most popular start stations
    popular_start_stations = df['Start Station'].value_counts().head(5)

    print('Most Popular Start Stations:')
    print(popular_start_stations)

    # Calculate the distribution of trips across different start stations
    station_distribution = df['Start Station'].value_counts(normalize=True)

    print('Distribution of Trips across Start Stations:')
    print(station_distribution)

def end_station_analysis(df):
    """
    Perform analysis on the end station field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Calculate the most popular end stations
    popular_end_stations = df['End Station'].value_counts().head(5)

    print('Most Popular End Stations:')
    print(popular_end_stations)

    # Calculate the distribution of trips across different end stations
    station_distribution = df['End Station'].value_counts(normalize=True)

    print('Distribution of Trips across End Stations:')
    print(station_distribution)

def user_type_analysis(df):
    """
    Perform analysis on the user type field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Calculate the number of subscribers and customers
    user_type_counts = df['User Type'].value_counts()

    print('User Type Counts:')
    print(user_type_counts)

def gender_analysis(df):
    """
    Perform analysis on the gender field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Calculate the distribution of trips by gender
    gender_counts = df['Gender'].value_counts()

    print('Gender Counts:')
    print(gender_counts)

def birth_year_analysis(df):
    """
    Perform analysis on the birth year field of the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    # Calculate statistics based on birth year
    average_age = 2021 - df['Birth Year'].mean()
    oldest_user = 2021 - df['Birth Year'].max()
    youngest_user = 2021 - df['Birth Year'].min()

    print('Average Age of Users:', average_age)
    print('Oldest User:', oldest_user)
    print('Youngest User:', youngest_user)

def load_data(city, month, day):
    """
    Load and filter the bikeshare data based on the given city, month, and day.

    Args:
        city (str): Name of the city.
        month (str): Name of the month.
        day (str): Name of the day.

    Returns:
        pandas.DataFrame: Filtered DataFrame containing bikeshare data.
    """
    # Load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august','septembr','octoer','november','december']
        month = months.index(month) + 1
    
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def display_data(df):
    """
    Display individual trip data from the given DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing bikeshare data.

    Returns:
        None
    """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    """
    Main function to handle user input and call the appropriate problem function.

    Args:
        None

    Returns:
        None
    """
    # Solicit and handle user input
    while True:
        city = input("Enter the name of the city (Chicago, New York City, Washington): ").lower()  # Convert to lowercase

        # Validate user input
        valid_cities = ['chicago', 'new york city', 'washington']
        if city in valid_cities:
            break
        else:
            print("Invalid city. Please enter a valid city.")

    while True:
        month = input("Enter the month (January, February, March, April, May, June): ").lower()  # Convert to lowercase

        # Validate user input
        valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month in valid_months or month == 'all':
            break
        else:
            print("Invalid month. Please enter a valid month.")

    while True:
        day = input("Enter the day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()  # Convert to lowercase

        # Validate user input
        valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day in valid_days or day == 'all':
            break
        else:
            print("Invalid day. Please enter a valid day.")

    # Call the load_data function based on user input
    df = load_data(city, month, day)

    # Perform further analysis or display results based on the problem requirements
    compute_popular_start_hour(df)
    end_time_analysis(df)
    start_station_analysis(df)
    end_station_analysis(df)
    user_type_analysis(df)

    if city in ['chicago', 'new york city']:
        gender_analysis(df)
        birth_year_analysis(df)

    # Calculate the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # Calculate the most common day of the week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', most_common_day)

    # Calculate the most common hour of the day
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour of Day:', most_common_hour)

    # Calculate the most common start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)

    # Calculate the most common end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_end_station)

    # Calculate the most common trip from start to end
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print('Most Common Trip:', most_common_trip)

    # Calculate the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Calculate the average travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time:', average_travel_time)

    # Calculate the counts of each user type
    user_type_counts = df['User Type'].value_counts()
    print('User Type Counts:')
    print(user_type_counts)

    if city in ['chicago', 'new york city']:
        # Calculate the counts of each gender
        gender_counts = df['Gender'].value_counts()
        print('Gender Counts:')
        print(gender_counts)

        # Calculate the earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Year of Birth:', earliest_birth_year)

        # Calculate the most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        print('Most Recent Year of Birth:', most_recent_birth_year)

        # Calculate the most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth:', most_common_birth_year)

    # Call the display_data function
    display_data(df)

# Dictionary to map city names to data file names
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# Call the main function to start the program
if __name__ == "__main__":
    main()
