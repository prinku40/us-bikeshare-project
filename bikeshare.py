import pandas as pd

# Function to compute the most popular start hour
def compute_popular_start_hour(df):
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

# Function to perform analysis on the end time field
def end_time_analysis(df):
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

# Function to perform analysis on the start station field
def start_station_analysis(df):
    # Calculate the most popular start stations
    popular_start_stations = df['Start Station'].value_counts().head(5)

    print('Most Popular Start Stations:')
    print(popular_start_stations)

    # Calculate the distribution of trips across different start stations
    station_distribution = df['Start Station'].value_counts(normalize=True)

    print('Distribution of Trips across Start Stations:')
    print(station_distribution)

# Function to perform analysis on the end station field
def end_station_analysis(df):
    # Calculate the most popular end stations
    popular_end_stations = df['End Station'].value_counts().head(5)

    print('Most Popular End Stations:')
    print(popular_end_stations)

    # Calculate the distribution of trips across different end stations
    station_distribution = df['End Station'].value_counts(normalize=True)

    print('Distribution of Trips across End Stations:')
    print(station_distribution)

# Function to perform analysis on the user type field
def user_type_analysis(df):
    # Calculate the number of subscribers and customers
    user_type_counts = df['User Type'].value_counts()

    print('User Type Counts:')
    print(user_type_counts)

# Function to perform analysis on the gender field
def gender_analysis(df):
    # Calculate the distribution of trips by gender
    gender_counts = df['Gender'].value_counts()

    print('Gender Counts:')
    print(gender_counts)

# Function to perform analysis on the birth year field
def birth_year_analysis(df):
    # Calculate statistics based on birth year
    average_age = 2021 - df['Birth Year'].mean()
    oldest_user = 2021 - df['Birth Year'].max()
    youngest_user = 2021 - df['Birth Year'].min()

    print('Average Age of Users:', average_age)
    print('Oldest User:', oldest_user)
    print('Youngest User:', youngest_user)

# Function to load and filter the dataset
def load_data(city, month, day):
    # Load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
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
    compute_popular_start_hour(df)
    end_time_analysis(df)
    start_station_analysis(df)
    end_station_analysis(df)
    user_type_analysis(df)

    if city in ['chicago', 'new york city']:
        gender_analysis(df)
        birth_year_analysis(df)

# Dictionary to map city names to data file names
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# Call the main function to start the program
if __name__ == "__main__":
    main()
