from django.shortcuts import render
from scheduler.models import *
from django.http import HttpResponse
import math

#TEST

PROF_H_CONSTRAINT_PENALTY = 10000
PROF_H_CONSTRAINT_CODE = 2
PROF_S_CONSTRAINT_PENALTY = 10
PROF_S_CONSTRAINT_CODE = 1
ROOM_TOO_SMALL_PENALTY = 9999
ROOM_TOO_LARGE_PENALTY = 50
ROOM_IN_USE_PENALTY = 55555
NUM_DAILY_TIMESLOTS = 20
NUM_DAYS_IN_WEEK = 5

# Create your views here.
def start_algorithm(request):
    run_optimization()
    return HttpResponse("A-OK!")

def calculate_obj(professor, offering, starting_timeslot, day, duration, prof_unavailability, room):
    obj_value = 0
    
    #FIND PENALTY FOR PROF UNAVAILABILITY CONSTRAINT
    for i in range (duration):
        if prof_unavailability[day][starting_timeslot+i] == PROF_S_CONSTRAINT_CODE:
            obj_value += PROF_S_CONSTRAINT_PENALTY
        elif prof_unavailability[day][starting_timeslot+i] == PROF_H_CONSTRAINT_CODE:
            obj_value += PROF_H_CONSTRAINT_PENALTY

        room_array = room_usage.get(room.id)
        if room_array[day][starting_timeslot+i] == 1:
            obj_value += 55555


    #FIND PENALTY FOR CAPACITY CONSTRAINT
    if offering.capacity > room.capacity:
        obj_value += ROOM_TOO_SMALL_PENALTY
    elif offering.capacity < room.capacity:
        obj_value += ROOM_TOO_LARGE_PENALTY

    return obj_value


def load_unavailability(professor):
    prof_unavailability = [[0 for slots in range(NUM_DAILY_TIMESLOTS)] for days in range(NUM_DAYS_IN_WEEK)]
    for unavailability in professor.professorunavailability_set.all():
        day = unavailability.day
        if day == 'm':
            day = 0
        elif day == 't':
            day = 1
        elif day == 'w':
            day = 2
        elif day == 'r':
            day = 3
        elif day == 'f':
            day = 4
        elif day == 's':
            day = 5
        elif day == 'n':
            day = 6

        start_hour, start_minute = unavailability.start_time.split(":")
        start_hour = int(start_hour)
        start_minute = int(start_minute)
        end_hour, end_minute = unavailability.end_time.split(":")
        end_hour = int(end_hour)
        end_minute = int(end_minute)
        preference_level = unavailability.preference_level

        start_slot = int((start_hour - 8)*2 + math.floor(start_minute/30))
        end_slot = int((end_hour - 8)*2 + math.floor(end_minute/30))

        for slot in range (start_slot, end_slot):
            #CHECK PROF PREFERENCES
            if preference_level == 1:
                prof_unavailability[day][slot] = 1
            else:
                prof_unavailability[day][slot] = 2

    return prof_unavailability

def run_optimization():

    #INITIALIZE ROOM USAGE ARRAY
    global room_usage
    room_usage = {}

    for room in Room.objects.all():
        room_usage[room.id] = [[0 for slots in range(NUM_DAILY_TIMESLOTS)] for days in range(NUM_DAYS_IN_WEEK)]

    #ITERATE THROUGH ALL PROFESSORS
    for prof in Professor.objects.all():
        prof_unavailability = load_unavailability(prof)
        
        #ITERATE THROUGH ALL OFFERINGS FOR PROFESSOR N
        for offering in Offering.objects.filter(section__professor=prof):
            best_obj = 1000000
            best_day = False
            best_start_time = False
            best_room = False
            duration = int(math.ceil(offering.duration/30))

            for room in Room.objects.all():
                for i in range (len(prof_unavailability)):
                    for j in range (len(prof_unavailability[i])-duration+1):
                        current_obj = calculate_obj(professor=prof, offering=offering, starting_timeslot=j,
                            day=i, duration=duration, prof_unavailability=prof_unavailability, room=room)
                        if current_obj < best_obj:
                            best_obj = current_obj
                            best_day = i
                            best_start_time = j
                            best_room = room

            #SET ROOM USAGE ARRAY TO INCLUDE SCHEDULED OFFERING
            room_array = room_usage.get(best_room.id)
            for i in range (duration):
                room_array[best_day][best_start_time+i] = 1
            room_usage[best_room.id] = room_array

            print (best_obj, best_day, best_start_time, best_room.number, offering.capacity)
    print room_usage