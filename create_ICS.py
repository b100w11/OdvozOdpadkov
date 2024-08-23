#!/usr/bin/env python3.9
# Import libraries
import argparse
from ics import  Calendar, Event
# Import data
from sezana import Sezana
locations_list = []
groups_list = []
for group in Sezana:
	temp_places = group.get("places")
	locations_list = [*locations_list, *temp_places]
	temp_groups = group.get("group")
	groups_list = [*groups_list, *temp_groups]

# define the day and ticket length in minutes
parser = argparse.ArgumentParser(description='Create a waste collection schedule ICS file for location/group')
parser.add_argument('-l', '--location', help='Define the location', choices=locations_list )
parser.add_argument('-g', '--group', help='Define the group', choices=groups_list )

args = parser.parse_args()

# Define variables
EventName = "Odvoz odpadkov"

c = Calendar()
e = Event()
e.name = EventName 
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events
exit()
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
# and it's done !
