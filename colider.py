import math

def colided(lhs, rhs):
    xDistance = lhs.x - rhs.x
    yDistance = lhs.y - rhs.y
    distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
    return distance <= (lhs.radious + rhs.radious)


def colide(ents):
    if colided(ents[0], ents[1]):
        x0, y0 = ents[1].x - ents[0].x, ents[1].y - ents[0].y
        x1, y1 = ents[0].x - ents[1].x, ents[0].y - ents[1].y
        xDistance = ents[0].x - ents[1].x
        yDistance = ents[0].y - ents[1].y
        distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))

        x0 = x0 / distance
        x1 = x1 / distance
        y0 = y0 / distance
        y1 = y1 / distance

        dot0 = (ents[0].velocity[0] * x0) + (ents[0].velocity[1] * y0)
        dot1 = (ents[1].velocity[0] * x1) + (ents[1].velocity[1] * y1)

        odwX0 = x0 * dot0 * -1
        odwY0 = y0 * dot0 * -1

        sumaX = odwX0 + x1 * dot1
        sumaY = odwY0 + y1 * dot1

        prawdziweX1 =  - (sumaX/2)*1.5
        prawdziweY1 =  - (sumaY/2)*1.5

        velocity0 = - prawdziweX1, - prawdziweY1
        velocity1 = prawdziweX1, prawdziweY1
        ents[0].applyForce(velocity0[0], velocity0[1])
        ents[1].applyForce(velocity1[0], velocity1[1])
