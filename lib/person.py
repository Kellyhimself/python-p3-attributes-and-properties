#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="", job="General Management"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25 and name is not None:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs. \n")

    name = property(get_name, set_name)
    job = property(get_job, set_job)