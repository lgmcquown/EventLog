import math

ID = 42
location = [3,4,5]
energy_MeV = 2.3 
atom_type = {"N_atomic": "1", "m_atomic_kg": 3.344*10**-27} 
reaction_type = 102

last_collision = [8,1,2]

vector = ["a","b","c"]

#vector[0]  = location[0]-last_collision[0]
#vector[1]  = location[1]-last_collision[1]
#vector[2]  = location[2]-last_collision[2]


for n in [0,1,2] :                    # vector:
    vector[n]  = location[n]-last_collision[n]

#print(vector)


distance  = math.sqrt((vector[0]*vector[0]) +(vector[1]*vector[1]) +(vector[2]*vector[2]))
unit_vector = ["a","b","c"]

#unit_vector[0]  = vector[0]/distance
#unit_vector[1]  = vector[1]/distance
#unit_vector[2]  = vector[2]/distance

for n in [0,1,2] :
    unit_vector[n] = vector[n]/distance

#print(unit_vector)

energy_eV = energy_MeV*1000


EVENT_LOG = {"Particle": ID, "Particle_location": location, "Particle_Direction": unit_vector, "Particle_energy_eV": energy_eV, "Particle_type": atom_type, "Collision_Type": reaction_type}

#print(EVENT_LOG)

set_of_events = [EVENT_LOG]*3
print(set_of_events)

