import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = ['chicago','new york city','washington']
    city = input("\nEnter the city you want [chicago, new york city, washington]: ").lower()
    while city not in cities:
        print("\nSorry, the city you entered is not among the list. Please, try again.")
        city = input("Enter the city you want [chicago, new york city, washington]: ").lower()
               

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    month = input("\nEnter the month you want (January, February, March, April, May, June) or all: ").lower()
    while month not in months:
        print("\nSorry, the month you entered is not among the list. Please, try again.")
        month = input("Enter the month you want (january, february, march, april, may, june) or all: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    day = input("\nEnter the day you want (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or all: ").lower()
    while day not in days:
        print("\nSorry, the day you entered is not among the list. Please, try again.")
        day = input("Enter the day you want (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or all: ").lower()


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
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("\nThe most common month in numbers is:",common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most common day is:",common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("\nThe most common hour is:",common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in df.columns:
        common_start_station = df['Start Station'].mode()[0]
        print("\nThe most commonly used start station is:", common_start_station)

        # TO DO: display most commonly used end station
        common_end_station = df['End Station'].mode()[0]
        print("\nThe most commonly used end station is:", common_end_station)

        # TO DO: display most frequent combination of start station and end station trip
        frequent_combination = "\nThe most frequent combination is from " + df['Start Station'] + " to " + df['End Station']
        print(frequent_combination.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in df.columns:
        total_travel_time = df['Trip Duration'].sum()
        print("\nThe total travel time is:",total_travel_time)


        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print("\nThe mean travel time is:",mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        counts_user_types = df['User Type'].value_counts()
        print("\nThe counts of user types:",counts_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print("\nThe counts of gender:",counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print("\nThe earliest year of birth is:",earliest_birth_year)
    
        recent_birth_year =  df['Birth Year'].max()
        print("\nThe most recent year of birth is:",recent_birth_year)
    
        common_birth_year =  df['Birth Year'].mode()[0]
        print("\nThe most common year of birth is:",common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    rawdata = input("\nWould you like to see raw data? Enter 'yes' or 'no': ").lower()
    counter = 0
    while rawdata == "yes":
        print(df[counter:counter+5])
        counter +=5
        rawdata = input("\nWould you like to see raw data? Enter 'yes' or 'no': ").lower()
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
