import sqlite3
sqlite3.sqlite_version
from matplotlib import pyplot as plt
import itertools
from matplotlib.animation import FuncAnimation


conn = sqlite3.connect('CSVDB.db')
c= conn.cursor()

def dynamic_data_entry(seconds,totallength,total_car, total_motorbike, total_person, total_bus, total_cycle,total_truck):
    c.execute("INSERT INTO recording (time,total,total_car,total_bus, total_person, total_bike, total_cycle, total_truck) VALUES (?,?,?,?,?,?,?,?)", (seconds,totallength,total_car,total_bus,total_person,total_motorbike,total_cycle,total_truck))
    conn.commit()