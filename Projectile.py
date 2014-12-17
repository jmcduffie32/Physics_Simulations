from visual import*

soldier = sphere(pos=(0,20,0),radius=0.5, color=color.blue)
cliff = box(pos=(-20,10,0), size=(40,20,10), color=color.green)
soldier.velocity = vector(5,5,0)
soldier.acceleration = vector(0,-9.8,0)
t=0
deltat = 0.005
soldier.trail = curve(color=soldier.color)
soldier.trail2 = curve(color=color.red)
y = soldier.pos.y
x = soldier.pos.x
z = soldier.pos.z
soldier.trail2.append(soldier.pos)
for t in range(1,1000):
    t = t*.001*3
    x = soldier.velocity.x*t
    y =20+5.0*t-4.9*t**2
    
    soldier.trail2.append((x,y,z))

while soldier.pos.y > 0:
    rate(100)
    soldier.velocity.y += soldier.acceleration.y*deltat
    soldier.pos.y += soldier.velocity.y/2*deltat
    soldier.pos.x += soldier.velocity.x*deltat
    soldier.trail.append(soldier.pos)
    
print "t=",t,"x=",x    
