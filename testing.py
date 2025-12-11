from Job import job, jobManager

def create_job(name, category, rate, date, hours):
    if rate <= 0 or hours <=0:
        raise ValueError('Rate and Hours must be positive')
    if hours > 6:
        raise ValueError('They cannot work longer than 6 hours')
    return job(name, category, rate, date, hours)

#Add sample jobs
job1 = create_job("Tiffany", "Teaching", 22.0, "05/04/2025", 2)
job2 = create_job("Poppy", "Marking", 14, "07/01/2024", 3)
job3 = create_job("Wing", "Teaching", 22.0, "20/11/2025", 5)
job4 = create_job("Ben", "Admin", 20.0, "08/12/2024", 6)
job5 = create_job("Murphy", "Marking", 10.0, "06/09/2023", 6)

manager = jobManager()

#Test adding jobs
print(manager.add_job(job1))
print(manager.add_job(job2))
print(manager.add_job(job4))

#test Adding job with more than 6 hours
try:
    job_7hours = create_job("Mochi", "Teaching", 10.0, "01/02/2025", 7)
except ValueError as e:
    print("Expected error", e)

#test daily work limit
manager.add_job(job3)
try:
    job_exceed_daily = create_job("Wing", "Teaching", 22.0, "20/11/2025", 4)
    total_today = sum(j.get_hours() for j in manager.search_by_name_and_date("Wing", "20/11/2025"))
    if total_today + job_exceed_daily.get_hours() > 8:
        raise ValueError("Cannot allocate more than 8 hours a day")
except ValueError as e:
    print("Expected error", e)

#Adding job5 should be allowed (only 6 hrs)
print(manager.add_job(job5))

#test displaying all jobs
for j in manager.get_jobs():
    print(j)

#test searching
print(manager.search_by_category("Teaching"))
print(manager.search_by_rate(22.0))
print(manager.search_by_name_and_date("Wing", "20/11/2025"))

#test editing jobs
job1_edited = create_job("Tiffany", "Teaching", 27.0, "05/04/2025", 2)
print(manager.edit_job(job1, job1_edited))
print(manager.get_jobs())

#test removing jobs
print(manager.remove_job(job2))
print(manager.get_jobs())

#test the total cost per a worker
total_costs = manager.get_total_cost_per_name()
print(total_costs)

#test the category count per a worker
category_counts = manager.get_category_count_per_name()
print(category_counts)

#test saving and loading into CSV file
manager.save_to_file("testing.csv")
print("Saved the jobs to testing.csv")

manager2 = jobManager()
manager2.load_from_file("testing.csv")
print("Loaded jobs from file:", manager2.get_jobs())

#test the exceptional cases
#negative rate
try:
    bad_job = create_job("Mia", "Teaching", -5.0, "04/02/2025", 2)
except ValueError as e:
    print("expected error:", e)

#negative hours
try:
    bad_job = create_job("Mia", "Teaching", 5.0, "04/02/2025", -2)
except ValueError as e:
    print("Caught expected exception:", e)