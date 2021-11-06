import time
import pandas as pd
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEK_DAYS = list(calendar.day_name)


def format_list(l):
    """
    Joins and formats a list of strings as options
    
    Args:
        (list[str]) l - list of strings to format
    Returns:
        (str) s - resulted string
    """
    if len(l) <= 1:
        s = ''.join(l)
    else:
        s = f"{', '.join(l[:-1])} or {l[-1]}"
    return s


def input_choice(prompt='', isValid=lambda c: True, err_msg='Invalid choice'):
    """
    Asks user to choose until his choice is valid
    
    Args:
        (str) prompt - message to the user, can be used to pass options to the user
        ((str)=>bool) isValid - function used to check if user's input is valid
        (str) err_msg - message to display when invalid input is entered
    Returns:
        (str) c - user's valid choice
    """
    c = input(prompt)
    while not isValid(c):
        print(err_msg)
        c = input(prompt)
    return c


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
    city = input_choice(
        f'Would you like to see data for {format_list(list(map(lambda e: e.title(), CITY_DATA.keys())))} ? ',
        lambda c: c.lower() in CITY_DATA.keys()
    ).lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_choice(
        f'Which month ? All | {format_list(list(map(lambda e: e.title(), MONTHS)))}: ',
        lambda c: c.lower() in MONTHS+['all']
    ).lower()
    if month == 'all':
        month = None

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_choice(
        f'Which day ? All | {format_list(WEEK_DAYS)}: ',
        lambda c: c.title() in WEEK_DAYS+['All']
    ).title()
    if day == 'All':
        day = None

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    try:
        month = MONTHS.index(month.lower()) + 1
    except Exception as e:
        month = None
    try:
        day = day.title()
        WEEK_DAYS.index(day)
    except Exception as e:
        day = None
    if month: df = df[df['Start Time'].dt.month == month]
    if day: df = df[df['Start Time'].dt.weekday_name == day]
     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_counts = df['Start Time'].dt.month.value_counts()
    print('Most popular month:', MONTHS[month_counts.index[0]-1].title(), ', Count:', month_counts.values[0])

    # TO DO: display the most common day of week
    weekday_counts = df['Start Time'].dt.weekday_name.value_counts()
    print('Most popular day of week:', weekday_counts.index[0], ', Count:', weekday_counts.values[0])

    # TO DO: display the most common start hour
    hour_counts = df['Start Time'].dt.hour.value_counts()
    print('Most popular hour:', hour_counts.index[0], ', Count:', hour_counts.values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    print('Most popular start station:', start_station_counts.index[0], ', Count:', start_station_counts.values[0])

    # TO DO: display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    print('Most popular end station:', end_station_counts.index[0], ', Count:', end_station_counts.values[0])

    # TO DO: display most frequent combination of start station and end station trip
    combo_counts = df.groupby(['Start Station', 'End Station'])['Start Station'].count()
    print('Most popular trip:', ' => '.join(combo_counts.idxmax()), ', Count:', combo_counts.max())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum(), 'seconds')

    # TO DO: display mean travel time
    print('Average travel time:', df['Trip Duration'].mean(), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('User types count:', list(zip(user_types_counts.index, user_types_counts)))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts(dropna=False)
        print('Gender count:', list(zip(gender_counts.index, gender_counts)))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_counts = df['Birth Year'].value_counts()
        print('Year of birth stats')
        print('Earliest:', int(df['Birth Year'].min()), ', Most recent:', int(df['Birth Year'].max()))
        print('Most common:', int(birth_year_counts.index[0]), 'Count:', birth_year_counts.values[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        it = df.iterrows()
        print_raw = input('Would you like to see 5 lines of raw data ? Enter yes or no: ')
        while(print_raw.lower() == 'yes'):
            for _ in range(5):
                print(next(it)[1].to_string())
                print()
            print_raw = input('Would you like another 5 lines ? Enter yes or no: ')

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

