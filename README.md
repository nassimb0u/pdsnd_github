# Explore US Bikeshare Data

Explore US Bikeshare Data is a Python application to explore data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington.

## Specifications

### The Datasets

Datasets used for all three cities are randomly selected data for the first six months of 2017. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City data files also have the following two columns:

* Gender
* Birth Year

### Statistics Computed

The app computes a variety of descriptive statistics to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)

    * most common month
    * most common day of week
    * most common hour of day

2. Popular stations and trip

    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

    * total travel time
    * average travel time

4. User info

    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Getting Started

### Installing Dependencies

#### Python

Follow instructions to install the latest stable version of python for your platform in the python docs for [Unix](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) or [Windows](https://docs.python.org/3.9/using/windows.html).
