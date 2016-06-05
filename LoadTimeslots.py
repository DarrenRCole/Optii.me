import ImportRooms

num_timeslots = 7
timeslots = []

class Timeslot(object):
    def __init__(self, ID):
        self.ID = ID

def load_timeslots():
    global timeslots

    for x in range(num_timeslots):
        timeslots.append(Timeslot(ID = x))