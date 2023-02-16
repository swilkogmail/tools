from employee import Employee

class Manager:

    def __init__(self, first_name, last_name, job_title):
        super().__init__(first_name, last_name, job_title)
        self.meetings = []

    def schedule_meeting(self, invitees, time):
        self.meetings.append({"invitees": invitees, "time": time})
        self.meetings.sort(key=lambda m: m["time"])

    def run_next_meeting(self):
        return self.meetings.pop(0)
