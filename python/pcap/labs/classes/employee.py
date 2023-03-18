class Employee:

    def __init__(self, first_name, last_name, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def email_signature(self):
        return f"Thanks from {self.first_name} {self.last_name} - {self.job_title}"
