from visual import *

ball = sphere(pos=(0,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0),size=(0.2,12,12), color=color.green)
wallL = box(pos=(-6,0,0),size=(0.2,12,12), color=color.green)
wallTop = box(pos=(0,6,0),size=(12,0.2,12), color=color.blue)
wallBott = box(pos=(0,-6,0),size=(12,0.2,12), color=color.blue)
WallBack = box(pos=(0,0,-6), size=(12,12,0.2), color=color.red)

ball.velocity = vector(25,2,-3)
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
deltat = 0.005
t = 0

ball.trail = curve(color=ball.color)


while true :
    rate(100)
    if ball.pos.x > wallR.pos.x or ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallTop.pos.y or ball.pos.y < wallBott.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z > 6 or ball.pos.z < -6:
        ball.velocity.z = -ball.velocity.z
    ball.pos = ball.pos + ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    varr.pos = ball.pos
    varr.axis = vscale*ball.velocity
    t = t+deltat
