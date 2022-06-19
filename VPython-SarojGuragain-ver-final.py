#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:18:50 2022

@author: sarojguragain
"""
import vpython as vp 

'''
DESCRIPTION:
This program 2D-simulates motion of a pos and neg charged particles in a constant perpendicular electric field.
The user has choice to give input by clicking what type of charged particle they want to simulate into the electric ffield perpendiucularly.
The user can increace and decrease the speed of simulation using slider in the output window.

'''
# Defining canvas for 2D simulation

scene2 =vp.canvas(title='CHARGED PARTICLE MOTION SIMULATION ON A PERPENDICULAR E-FILED(RED trial-positive particle, GREEN trial- negative particle)', width=700, height=400, center=vp.vector(0,0,0) ,opacity=0.9)
# Defining Box and beam of particle

#creating arrows and charges 
for i in range (-12, 13):
    vp.arrow(pos=vp.vector(i,-5,0),axis=vp.vector(0,10,0), shaftwidth=0.1,opacity=0.9,color=vp.color.cyan)
    vp.text(text = "+", pos = vp.vector(-i,-6,0), axis=vp.vector(10,0,0),color=vp.color.red )
    vp.text(text = "-", pos = vp.vector(-i,5,0), axis=vp.vector(10,0,0),color=vp.color.green )
T = vp.text(text='ELECTRIC FIELD REGION',align='center',color=vp.color.magenta)

lEbox = 10 # Size of box of electric field
lmax = 30 # Size of simulation area
Ebox = vp.box(pos =vp.vector (0,0,5), size =vp.vector (2*lEbox,lEbox,lEbox), color = vp.color.yellow, opacity=0.1)

#list of the charged particles
path=[]

print("PLEASE MAKE A CHOICE OF PARTICLE FOR SIMULATION")
choice=input("Choose (P/p) for positive particle(RED), (N/n) for negative particle(GREEN) or (B/b) for both particles:" )
#The trail of this sphere will show individual points rather than a continuous line, it will display spheres at every 20th sphere location, and it will retain only the most recent 200 of these points.
#it is related to make trial and interval and retain will keep the trial displayed
if choice=="P" or choice=="p":
 particle = vp.sphere(pos = vp.vector(-lEbox*2,1,0), radius = 0.5, velocity =vp.vec(10,0,0), charge = 1, mass = 10, color =vp.color.red, make_trail=True, trail_type="curve", interval=20, retain=200)
 #adding 1st charged particle to list
 path.append(particle)

if choice=="N" or choice=="n":
  particle1 =vp.sphere( pos =vp.vector(-lEbox*2,-1,0), radius = 0.5, velocity = vp.vec(10,0,0), charge = -1, mass = 10, color =vp.color.green, make_trail=True, trail_type="curve", interval=20, retain=200)
  # adding 2nd charged particle to list
  path.append(particle1)

if choice=="B" or choice=="b":
  particle =vp.sphere( pos = vp.vector(-lEbox*2,1,0), radius = 0.5, velocity =vp.vec(10,0,0), charge = 1, mass = 10, color =vp.color.red, make_trail=True, trail_type="curve", interval=20, retain=200)
  particle1 =vp.sphere( pos =vp.vector(-lEbox*2,-1,0), radius = 0.5, velocity = vp.vec(10,0,0), charge = -1, mass = 10, color =vp.color.green, make_trail=True, trail_type="curve", interval=20, retain=200)
  #if user chooses both particles
  path.append(particle) # adding 1st charged particle to list
  path.append(particle1)# adding 2nd charged particle to list

#slider function
def setspeed(s):
    wt.text = 'Slide to Change the speed of Simulation:  {:1.2f}'.format(s.value)
    
sl =vp.slider(min=50, max=250, value=50, length=220, bind=setspeed, right=15)
wt =vp.wtext(text="Slide to Change the speed of Simulation:  {:1.2f}".format(sl.value))

# Defining function to calculation Electric field
def E(r):
    #r points to a.pos (particle.pos)
    #assigning manual e field value if its higher deflection occurs early
  E_mag = 12
  E_dir = (vp.vec(0,1,0))
  if (particle.pos.x>= -Ebox.size.x/2. and particle.pos.x <= Ebox.size.x/2. and particle.pos.y>= -Ebox.size.y/2. and particle.pos.y <= Ebox.size.y/2. and particle.pos.z>= -Ebox.size.z/2. and particle.pos.z <= Ebox.size.z/2.):
    E_val = E_mag*E_dir
  else:
    E_val = 0*E_dir
  return E_val

# Defining function to calculate acceleration due to electric force
#returns acceleration
def acc(particle):
    #a points to  acc(particle) i.e particle
  force = particle.charge*E(particle.pos)
  return force/particle.mass

# Updating postion of particle in loop
t = 0
dt = 0.002
while (t < 15):
  vp.rate(sl.value)
  for particle in path:
    # Stop updating position of particle if goes outside region of interest
    if (particle.pos.x > lmax or particle.pos.x < -lmax):
      continue 
    #v=u+at updating velocity
    particle.velocity = particle.velocity + acc(particle)*dt
    #if you multiply velocity with time you get position
    particle.pos = particle.pos + particle.velocity*dt
    
  t = t+dt