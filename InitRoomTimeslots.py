import ImportRooms
import LoadTimeslots

room_timeslots = []

class RoomTimeslot(object):
    def __init__(self, room, timeslot, course_section_ID):
        self.room = room
        self.timeslot = timeslot
        self.course_section_ID = course_section_ID

def init_room_timeslots():
    global room_timeslots

    room_timeslots = [0 for x in (range(LoadTimeslots.num_timeslots * len(ImportRooms.rooms)))]
    room_timeslot_ID = 0

    for y in range(len(LoadTimeslots.timeslots)):
        for x in range(len(ImportRooms.rooms)):
            room_timeslots[room_timeslot_ID] = RoomTimeslot(room = ImportRooms.rooms[x],
                                                 timeslot = LoadTimeslots.timeslots[y],
                                                 course_section_ID = False)
            room_timeslot_ID += 1