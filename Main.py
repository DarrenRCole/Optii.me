import LoadTimeslots
import ImportRooms
import ImportProfs
import ImportProfConstraints
import ImportCourseSections
import InitRoomTimeslots
import RunOpti

def output_schedule():
    for x in range(len(LoadTimeslots.timeslots)):
        for y in range(len(ImportRooms.rooms)):
            room_timeslot_ID = y + x * len(ImportRooms.rooms)
            if (InitRoomTimeslots.room_timeslots[room_timeslot_ID].course_section_ID):
                print("Room", ImportRooms.rooms[y].name,
                      "Timeslot", InitRoomTimeslots.room_timeslots[room_timeslot_ID].timeslot.ID,
                      "Course", InitRoomTimeslots.room_timeslots[room_timeslot_ID].course_section_ID)

#ENVIRONMENT RUNTIME SETUP

ImportProfs.load_profs() #loads professors from data file
ImportProfConstraints.load_prof_constraints() #loads professors' constraints from data file
ImportRooms.load_rooms() #loads rooms from data file
ImportCourseSections.load_course_sections() #loads course data from data file
LoadTimeslots.load_timeslots() #initializes timeslots
InitRoomTimeslots.init_room_timeslots() #map room+timeslot combinations

#RUN OPTIMIZATION
RunOpti.run_optimization()

#TEXT OUTPUT OF SOLUTION SCHEDULE
output_schedule()
