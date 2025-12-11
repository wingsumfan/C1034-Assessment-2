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

import csv
from Job import job
class jobManager:

    def __init__(self, jobs=None):
        if jobs is None:
            self._jobs = []
        else:
            self._jobs = jobs

    def get_jobs(self):
        return self._jobs

    def __str__(self):
        return f"jobManager({self._jobs})"

    def __repr__(self):
        return self.__str__()

    def _is_worker_available(self, job):
        return job not in self._jobs

    def add_job(self, job):
        if self._is_worker_available(job):
            self._jobs.append(job)
            return True
        return False

    def remove_job(self, job):
        if job in self._jobs:
            self._jobs.remove(job)
            return True
        return False

    def edit_job(self, old_job, new_job):
        if old_job not in self._jobs:
            return False
        if new_job in self._jobs and new_job != old_job:
            return False

        index = self._jobs.index(old_job)
        self._jobs[index] = new_job
        return True

    def search_by_category(self, category):
        return [job for job in self._jobs if job.get_category() == category]

    def search_by_rate(self, rate):
        return [job for job in self._jobs if job.get_rate() == rate]

    def search_by_name_and_date(self, name, date):
        return [job for job in self._jobs if job.get_worker_name() == name and job.get_date() == date]

    def get_total_cost_per_name(self):
        result = {}
        for job in self._jobs:
            name = job.get_worker_name()
            cost = job.get_rate() * job.get_hours()
            if name not in result:
                result[name] = 0
            result[name] += cost
        return result

    def get_category_count_per_name(self):
        result = {}
        for job in self._jobs:
            name = job.get_worker_name()
            category = job.get_category()

            if name not in result:
                result[name] = {}

            if category not in result[name]:
                result[name][category] = 0

            result[name][category] += 1

        return result

    def load_from_file(self, file_name):
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, category, rate, date, hours = row
                job = job(name, category, float(rate), date, int(hours))

    def save_to_file(self, file_name):
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            for job in self._jobs:
                writer.writerow([job.get_name(), job.get_category(), job.get_rate(), job.get_date(), job.get_hours()])