import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("enter city name: Chicago, New York City or Washington!").lower()
        if city not in CITIES:
            print("\nInvalid answer\n")
            continue   
        else:
            break   
            
    while True:
        month = input("enter month. like January, Feburary, March, April, May or June?").lower()
        if month not in MONTHS:
            print("enter valid")
            continue
        else:
            break
    while True:
        day = input("enter day. like Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
        if day not in DAYS:
            print("enter valid day name")
            continue 
        else:
            break 
            
    print("your city of interest is: {}".format(city))
    print("your month of interest is: {}".format(month))
    print("your choice of day is: {}".format(day))
    print('-'*40)
    return city, month, day
    


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_mnth = df['month'].mode()[0]
    print("the most common month of travel is:", common_mnth)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print("the most comon travel day of the week is:", common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is:", most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_common_station = df['Start Station'].value_counts().idxmax()
    print(most_common_station)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print(common_end)
    # TO DO: display most frequent combination of start station and end station tripp
    most_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(most_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
          
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    Total_travel = df['Trip Duration'].sum()
    print(Total_travel)
    # TO DO: display mean travel time
    Mean_travel = df['Trip Duration'].mean()
    print("the mean travel time is:", Mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    count_of_users = df['User Type'].value_counts()
    print("the number of user types is:", count_of_users)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_of_gender = df['Gender'].value_counts()
        print("the count of genders is:", count_of_gender)
    else:
        print("no gender for this city")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        year_of_birth = df['Birth Year']
        most_recent_yr_of_bth = year_of_birth.max()
        print("the most recent year of birth is: {}".format(most_recent_yr_of_bth))
        earliest_year_of_birth = year_of_birth.min()
        print("the earliest birth year is: {}".format(earliest_year_of_birth))
        most_comon_yr_of_bth =year_of_birth.value_counts().idxmax()
        print("the most common birth year is: {}".format(most_comon_yr_of_bth))
    else:
        print("no birth year record for this city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data == 'no':
            break
  


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
