class job:

    def __init__(self, name, category, rate, date, hours):
        self.name = name
        self.category = category
        self.rate = rate
        self.date = date
        self.hours = hours

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_rate(self):
        return self.rate

    def get_date(self):
        return self.date

    def get_hours(self):
        return self.hours

    def __eq__(self, other):
        if not isinstance(other, job):
            return False
        return (self.name == other.name and self.category == other.category and self.date == other.date and self.hours == other.hours)

    def __hash__(self):
        return hash((self.name, self.category, self.rate, self.date, self.hours))

    def __str__(self):
        return f'job({self.name}, {self.category}, {self.rate}, {self.date}, {self.hours})'

    def __repr__(self):
        return self.__str__()

