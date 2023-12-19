#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    big_park = NationalPark("Big Park")
    long_park = NationalPark("Long Park")
    wide_park = NationalPark("Wide Park")

    mario = Visitor("Mario")
    luigi = Visitor("Luigi")
    peach = Visitor("peach")

    trip01 = Trip(mario, big_park, "May 1st", "December 19th")
    trip02 = Trip(mario, wide_park, "May 1st", "December 19th")
    trip03 = Trip(mario, long_park, "May 1st", "December 19th")
    trip04 = Trip(mario, big_park, "May 1st", "December 19th")
    trip05 = Trip(mario, big_park, "May 1st", "December 19th")

    trip06 = Trip(luigi, big_park, "May 1st", "December 19th")
    trip07 = Trip(luigi, wide_park, "May 1st", "December 19th")
    
    trip08 = Trip(peach, big_park, "May 1st", "December 19th")
    trip09 = Trip(peach, long_park, "May 1st", "December 19th")
    trip10 = Trip(peach, long_park, "May 1st", "December 19th")
    trip11 = Trip(peach, long_park, "May 1st", "December 19th")
    trip12 = Trip(peach, long_park, "May 1st", "December 19th")
    trip13 = Trip(peach, long_park, "May 1st", "December 19th")

    ipdb.set_trace()
