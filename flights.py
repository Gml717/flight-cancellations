import matplotlib.pyplot as plt
import pandas as pd


# split text over point komma into a list and extract the first element

# functions

def max_list(a):
    """" it gives the maximum value of a list"""
    a.sort()
    return a[-1]


def description(sentence):
    """" split text over ';' into a list and extract and return the first element"""
    city = sentence.split(",")
    return city[0]


def preprocessing_dataset(df):

    """Remove the columns that have 78% of their values missing. Remove unnecessary columns, encode nominal feature
    columns and replace missing values with the median of the specific column. """
    df = df.copy()
    # Remove missing columns with 78% missing values
    columns = df.loc[:, round(df.isna().mean(), 2) == 0.78].columns
    df = df.drop(columns, axis=1)
    # Drop unneeded columns
    df = df.drop(["TAIL_NUM", 'city origin airport', 'city destination airport'], axis=1)

    # One-hot encode nominal feature columns
    df = onehot_encode(
        df,
        column_dict={
            'FL_DATE': 'DATE',
            'CARRIER': 'CAR',
            'DESTINATION_AIRPORT': 'DA',
            'ORIGIN_AIRPORT': 'OA'

        })

    # replace missing values with median of the specific column
    df = df.iloc[:, :].where(pd.notna(df), df.mean(), axis="columns")

    return df


def onehot_encode(df, column_dict):
    """" Onehot encode targeted columns"""

    df = df.copy()
    for column, prefix in column_dict.items():
        # Get one hot encoding of column
        dummies = pd.get_dummies(df[column], prefix=prefix)

        # Drop column B as it is now encoded
        df = df.drop(column, axis=1)

        # Join the encoded df
        df = df.join(dummies)

    return df


# classes

class GroupField_datafield:
    # The group field is one of the following two options:
    # departure. Group on the departure time.
    # arrival. Group on the arrival time.
    # It's the field on which the data is grouped

    # The data field is one of the following options:
    # flights. Number of flights, each flight counts as one.
    # departure delays. The departure delay in minutes.
    # arrival delays. The arrival delay in minutes.
    # ad *. (with * = carrier, weather, nas, security, or late aircraft).
    # The arrival delay of the specified category.
    # It's the field of the data to collect.

    # Dataset provided doesn't contain record for cancelled or diverted flights
    #  due to not having a departure and/or arrival times

    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    sum_5 = 0
    sum_6 = 0
    sum_7 = 0
    sum_8 = 0
    sum_9 = 0
    sum_10 = 0
    sum_11 = 0
    sum_12 = 0

    def __init__(self, dataset, groupfield, datafield):
        self.dataset = dataset
        self.groupfield = groupfield
        self.datafield = datafield
        self.time_2h_interval = {}

    def __repr__(self):
        return "GroupField_datafield('{}' , '{}' , '{}')".format(self.dataset, self.groupfield, self.datafield)

    def __str__(self):
        return '{} - {} - {}'.format(self.dataset, self.groupfield, self.datafield)

    def data_analysis(self, dataset):
        """"" Analyses of the flight records in the dataset and calculate the number of flights or delay in minutes for
        2-hour intervals"""

        column_name_list = {"arrival_delays": "ARR_DELAY",
                            "departure delays": "",
                            "ad_carrier": "CARRIER_DELAY", "ad_weather": "WEATHER_DELAY", "ad_nas": "NAS_DELAY",
                            "ad_security": "SECURITY_DELAY",
                            "ad_late_aircraft": "LATE_AIRCRAFT_DELAY"}
        # dictionnairy with keys that correspond to the column names of the dataset

        if self.groupfield == "arrival":
            groupfield = "ARR_TIME"
        else:
            groupfield = "DEP_TIME"

        time = dataset[groupfield]
        minutes_delay = 0
        # remove the double quotation marks of the string with join and split method then covert it to a string
        if self.datafield != "flights":
            minutes_delay = dataset[column_name_list[self.datafield]]
        # We don’t count delays when it is an early departure or arrival (negative values).

        if 0 <= time <= 159 or time == 2400:
            if self.datafield == "flights":
                self.sum_1 += 1
            elif minutes_delay > 0:
                self.sum_1 += minutes_delay

        elif 200 <= time <= 359:
            if self.datafield == "flights":
                self.sum_2 += 1
            elif minutes_delay > 0:
                self.sum_2 += minutes_delay

        elif 400 <= time <= 559:
            if self.datafield == "flights":
                self.sum_3 += 1
            elif minutes_delay > 0:
                self.sum_3 += minutes_delay

        elif 600 <= time <= 759:
            if self.datafield == "flights":
                self.sum_4 += 1
            elif minutes_delay > 0:
                self.sum_4 += minutes_delay

        elif 800 <= time <= 959:
            if self.datafield == "flights":
                self.sum_5 += 1
            elif minutes_delay > 0:
                self.sum_5 += minutes_delay

        elif 1000 <= time <= 1159:
            if self.datafield == "flights":
                self.sum_6 += 1
            elif minutes_delay > 0:
                self.sum_6 += minutes_delay

        elif 1200 <= time <= 1359:
            if self.datafield == "flights":
                self.sum_7 += 1
            elif minutes_delay > 0:
                self.sum_7 += minutes_delay

        elif 1400 <= time <= 1559:
            if self.datafield == "flights":
                self.sum_8 += 1
            elif minutes_delay > 0:
                self.sum_8 += minutes_delay

        elif 1600 <= time <= 1759:
            if self.datafield == "flights":
                self.sum_9 += 1
            elif minutes_delay > 0:
                self.sum_9 += minutes_delay

        elif 1800 <= time <= 1959:
            if self.datafield == "flights":
                self.sum_10 += 1
            elif minutes_delay > 0:
                self.sum_10 += minutes_delay

        elif 2000 <= time <= 2159:
            if self.datafield == "flights":
                self.sum_11 += 1
            elif minutes_delay > 0:
                self.sum_11 += minutes_delay
        else:
            if self.datafield == "flights":
                self.sum_12 += 1
            elif minutes_delay > 0:
                self.sum_12 += minutes_delay

    def make_dictionary(self):

        """"Data_analysis method is called that provides the necessary information concerning the number of flights or
        delay in minutes. Creates a dictionary with the  number of flights or delays in minutes (Values), grouped in
        2-hour intervals (Keys)"""

        self.dataset.apply(self.data_analysis, axis=1)
        self.time_2h_interval = {" 0:00- 1:59:": self.sum_1, " 2:00- 3:59:": self.sum_2, " 4:00- 5:59:": self.sum_3,
                                 " 6:00- 7:59:": self.sum_4, " 8:00- 9:59:": self.sum_5, "10:00-11:59:": self.sum_6,
                                 "12:00-13:59:": self.sum_7, "14:00-15:59:": self.sum_8, "16:00-17:59:": self.sum_9,
                                 "18:00-19:59:": self.sum_10, "20:00-21:59:": self.sum_11, "22:00-23:59:": self.sum_12}

    def output_data(self):
        """""
        Output of the numbers specified by the dictionary values grouped in 2-hour intervals
        and plotted in the following way (the longest bar has a length of 20 stars and must always be completely filled,
         unless no data is available at all)."""

        # Create a list of all values in dict time_2h_interval
        list_values = list(self.time_2h_interval.values())

        list_values_1 = [int(x) for x in list_values]
        # convert the elements of the list to integers

        new_list_value_1 = list_values_1[:]
        # copy beacause  list is sorted by using max_list fuction

        star = max_list(list_values_1) / 20
        # (the longest bar has a length of 20 stars and must always be completely filled, unless no data
        # is available at all) ratio of star

        time_2h_interval = list(self.time_2h_interval.keys())
        # get keys as list from dict time_2h_interval

        sum_output_values = sum(list_values_1)

        output = ""
        for i in range(len(time_2h_interval)):
            number_star = int(new_list_value_1[i] / star)
            # number of stars

            whitespace = 20 - number_star
            whitespace_1 = 1 + len(str(sum_output_values)) - len(str(new_list_value_1[i]))
            output = time_2h_interval[
                         i] + " " + "|" + "*" * number_star + " " * whitespace + "|" + " " * whitespace_1 + str(
                new_list_value_1[i])
            print(output)
        print("-" * len(output))
        whitespace_2 = len(output) - len(str(sum_output_values))
        print(" " * whitespace_2 + str(sum_output_values))

    def barplot_data(self):
        """"" barplot of the numbers specified by the dictionary values """
        time = self.time_2h_interval

        plt.figure(figsize=(15, 10))
        plt.bar(range(len(time)), list(time.values()), align='center')

        plt.xticks(range(len(time)), list(time.keys()))
        if self.datafield == "flights":
            plt.ylabel("Number of " + self.datafield)
        else:
            plt.ylabel(self.datafield + "in minutes")
        plt.xlabel(" 2-hour intervals")

        plt.show()


class GroupField_datafield_filter(GroupField_datafield):

    # filter is a filter that can be used to filter on the relevant part of the flight dataset.
    def __init__(self, dataset, groupfield, datafield, filterargument):
        super(GroupField_datafield_filter, self).__init__(dataset, groupfield, datafield)
        self.filter = filterargument

    def __repr__(self):
        return "GroupField_datafield_filter('{}' , '{}' , '{}' , '{}')".format(self.dataset, self.groupfield,
                                                                               self.datafield, self.filter)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.dataset, self.groupfield, self.datafield, self.filter)

    def make_dictionary(self):
        """" filter argument(s) used on the flight dataset to subset its relevant part where after the data_analysis
        method is called on this data. Creates a dictionary with the  number of flights or delays in minutes (
        Values), grouped in 2-hour intervals (Keys) """

        filter_arguments = self.filter.split(";")
        # a list with the different filters as elements

        airline = [x[8:] for x in filter_arguments if "airline" in x]
        # list of the exact airline by carrier code

        plane = [x[6:] for x in filter_arguments if "plane" in x]
        # list of tail Number (identifier of the plane).

        d_city = [x[7:] for x in filter_arguments if "d_city" in x]
        # list of departure airport(s)

        a_city = [x[7:] for x in filter_arguments if "a_city" in x]
        # list of arrival airport(s)

        # Check If List is not Empty

        if len(airline) != 0:
            self.dataset = self.dataset[self.dataset["CARRIER"].isin(airline)]
        if len(plane) != 0:
            self.dataset = self.dataset[self.dataset["TAIL_NUM"].isin(plane)]
        if len(d_city) != 0:
            self.dataset = self.dataset[self.dataset["city origin airport"].isin(d_city)]
        if len(a_city) != 0:
            self.dataset = self.dataset[self.dataset["city destination airport"].isin(a_city)]
        # filter the dataset
        # filter rows of a dataframe on a set or collection of values you can use the isin() membership function.
        # This way, you can have only the rows that you’d like to keep based on the list values.

        self.dataset.apply(self.data_analysis, axis=1)
        self.time_2h_interval = {" 0:00- 1:59:": self.sum_1, " 2:00- 3:59:": self.sum_2, " 4:00- 5:59:": self.sum_3,
                                 " 6:00- 7:59:": self.sum_4, " 8:00- 9:59:": self.sum_5, "10:00-11:59:": self.sum_6,
                                 "12:00-13:59:": self.sum_7, "14:00-15:59:": self.sum_8, "16:00-17:59:": self.sum_9,
                                 "18:00-19:59:": self.sum_10, "20:00-21:59:": self.sum_11, "22:00-23:59:": self.sum_12}
