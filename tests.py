#! /usr/bin/python3
import unittest
import math
from entity import Entity

class TestEntityCreation(unittest.TestCase):
    def test_canBeCreatedWithDefaultParameters(self):
        e = Entity()
        self.assertTupleEqual((e.x, e.y, e.velocity, e.mass),
                              (0,     0,     (0, 0),      1))



    def test_canBeConstructedWithArguments(self):
        pos_x = 1
        pos_y = 3
        velocity = (4, 5)
        mass = 3
        e = Entity(pos_x, pos_y, velocity, mass)
        self.assertTupleEqual((  e.x,   e.y, e.velocity, e.mass),
                              (pos_x, pos_y,   velocity,   mass))

class TestEntityAcceleration(unittest.TestCase):
    def setUp(self):
        self.e = Entity()

    def test_shouldAccumulateAccelerationWhenForceIsAppliedOnce(self):
        self.e.applyForce(1, 2)
        self.assertTupleEqual(self.e.acceleration, (1, 2))

    def test_shouldAccumulateAccelerationWhenForceIsAppliedMultipleTimes(self):
        self.e.applyForce(3, 4)
        self.e.applyForce(5, 6)
        self.e.applyForce(1, 0)
        self.assertTupleEqual(self.e.acceleration, (9, 10))

    def test_shouldConsiderMassWhenForceIsAplied(self):
        self.e.mass = 3
        self.e.applyForce(1, 3)
        self.e.applyForce(5, 0)
        self.assertTrue(math.isclose(self.e.acceleration[0], 2.0) and
                        math.isclose(self.e.acceleration[1], 1.0))


class TestEntityMovement(unittest.TestCase):
    def setUp(self):
        self.e = Entity()

    def test_shouldNotChangePositionWhenMovedBeforeApplyingForce(self):
        self.e.move()
        self.assertTupleEqual((self.e.x, self.e.y), (0, 0))

    def test_shouldChangePositionAfterForceIsAplied(self):
        self.e.applyForce(1,2)
        self.e.move()
        self.assertTupleEqual((self.e.x, self.e.y), (1, 2))

    def test_shouldResetAccelerationAfterMove(self):
        self.e.applyForce(3,4)
        self.e.move()
        self.assertTupleEqual((self.e.x, self.e.y), (3, 4))
        self.e.move()
        self.assertTupleEqual((self.e.x, self.e.y), (6, 8))



if __name__ == '__main__':
    unittest.main()
