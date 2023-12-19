class NationalPark:
    all = []

    def most_visited():
        most_visited = None
        most_visits = 0
        for park in NationalPark.all:
            visits = park.total_visits()
            if visits > most_visits:
                most_visits = visits
                most_visited = park
            if visits == most_visits:
                # What should we do if two parks are tied for most visits?
                pass
        return most_visited


    def __init__(self, name):
        self.name = name
        self.trips_list = []
        NationalPark.all.append(self)
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        if hasattr(self, "name"):
            raise ValueError("Cannot change name of park")
        elif not isinstance(name, str):
            raise ValueError("not a string")
        elif (len(name) < 3 ):
            raise ValueError("too short")
        else:
            self._name = name
    
    name = property(get_name, set_name)

    def add_trip(self, trip):
        self.trips_list.append(trip)

    def trips(self):
        return self.trips_list
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips_list)
    
    def best_visitor(self):
        best_visitor = None
        most_visits = 0
        for visitor in self.visitors():
            visits = len([trip for trip in self.trips() if trip.visitor == visitor])
            if visits > most_visits:
                most_visits = visits
                best_visitor = visitor
        return best_visitor
            


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.national_park.add_trip(self)
        self.visitor.add_trip(self)
        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date
        
    def set_start_date(self, start_date):
        if isinstance(start_date, str):
            if len(start_date) >= 7:
                self._start_date = start_date
            else:
                raise ValueError("too short")
        else:
            raise ValueError("not a string")
        
    start_date = property(get_start_date, set_start_date)

    def get_end_date(self):
        return self._end_date
        
    def set_end_date(self, end_date):
        if isinstance(end_date, str):
            if len(end_date) >= 7:
                self._end_date = end_date
            else:
                raise ValueError("too short")
        else:
            raise ValueError("not a string")
        
    end_date = property(get_end_date, set_end_date)

class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        self.trips_list = []
        Visitor.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        # if hasattr(self, "name"):
        #     pass
        if not isinstance(name, str):
            raise ValueError("not a string")
        elif not (1 <= len(name) <= 15):
            raise ValueError("name must be from 1 to 15 characters")
        else:
            self._name = name
    
    name = property(get_name, set_name)

    def add_trip(self, trip):
        self.trips_list.append(trip)
        
    def trips(self):
        return self.trips_list
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips if self.trips.national_park == park])