import math

def colided(lhs, rhs):
    colisionDistance = lhs.radious + rhs.radious
    if (lhs.x <= rhs.x + colisionDistance and
        lhs.y <= rhs.y + colisionDistance and
        lhs.x >= rhs.x - colisionDistance and
        lhs.y >= rhs.y - colisionDistance ):

        xDistance = lhs.x - rhs.x
        yDistance = lhs.y - rhs.y
        distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
        if distance <= colisionDistance:
            if distance:
                distanceRatio = colisionDistance/distance
                lhs.x = (xDistance * distanceRatio) + rhs.x
                lhs.y = (yDistance * distanceRatio) + rhs.y
            else:
                lhs.x = colisionDistance + rhs.x
            return True
        else:
            return False
    else:
        return False


def colide(ents):
    bounceFactor = 2
    i = 1
    for e in ents:
        for candidate in ents[i:]:
            if colided(e, candidate):

                distanceX, distanceY = e.x - candidate.x, e.y - candidate.y
                distance = e.radious + candidate.radious

                normalizedDistanceX = distanceX / distance
                normalizedDistanceY = distanceY / distance

                dot0 = (e.velocity[0] * -normalizedDistanceX) + (e.velocity[1] * -normalizedDistanceY)
                dot1 = (candidate.velocity[0] * normalizedDistanceX) + (candidate.velocity[1] * normalizedDistanceY)

                collisionForceX = normalizedDistanceX * (dot0 + dot1)
                collisionForceY = normalizedDistanceY * (dot0 + dot1)

                forceX = (collisionForceX/2) * bounceFactor
                forceY = (collisionForceY/2) * bounceFactor

                e.applyForce(forceX, forceY)
                candidate.applyForce(-forceX, -forceY)
        i += 1
