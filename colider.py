import math

def colided(lhs, rhs):
    xDistance = lhs.x - rhs.x
    yDistance = lhs.y - rhs.y
    distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
    return distance <= (lhs.radious + rhs.radious)


def colide(ents):
    i = 1
    for e in ents:

        for candidate in ents[i:]:
            if colided(e, candidate):
                x0, y0 = candidate.x - e.x, candidate.y - e.y
                x1, y1 = e.x - candidate.x, e.y - candidate.y
                xDistance = e.x - candidate.x
                yDistance = e.y - candidate.y
                distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))

                x0 = x0 / distance
                x1 = x1 / distance
                y0 = y0 / distance
                y1 = y1 / distance

                dot0 = (e.velocity[0] * x0) + (e.velocity[1] * y0)
                dot1 = (candidate.velocity[0] * x1) + (candidate.velocity[1] * y1)

                odwX0 = x0 * dot0 * -1
                odwY0 = y0 * dot0 * -1

                sumaX = odwX0 + x1 * dot1
                sumaY = odwY0 + y1 * dot1

                prawdziweX1 =  - (sumaX/2)*1.5
                prawdziweY1 =  - (sumaY/2)*1.5

                velocity0 = - prawdziweX1, - prawdziweY1
                velocity1 = prawdziweX1, prawdziweY1
                e.applyForce(velocity0[0], velocity0[1])
                candidate.applyForce(velocity1[0], velocity1[1])
        i += 1
