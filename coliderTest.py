#! /usr/bin/python3
import unittest
from colider import colide

class EntityMock:
    def __init__(self, x = 0, y = 0, r = 0, velocity = (0, 0)):
        self.forceApplied = 0, 0
        self.x = x
        self.y = y
        self.radious = r
        self.velocity = velocity

    def applyForce(self, x, y):
        self.forceApplied = self.forceApplied[0] + x, self.forceApplied[1] + y

class TestColider(unittest.TestCase):
    def test_shouldDoNothingWhenThereIsOnlyOne(self):
        entities = [EntityMock()]
        colide(entities)
        self.assertTupleEqual(entities[0].forceApplied, (0, 0))

    def test_shouldDoNothingWhenEntitiesDontColide(self):
        entities = [EntityMock(0, 0, 1), EntityMock(0, 4, 1)]
        colide(entities)
        for e in entities:
            self.assertTupleEqual(e.forceApplied, (0, 0))

    def test_kuleZTymSamymKierunkiemRuchLeczOPrzeciwnychZwrotachPowinnySieOdbic(self):
        entities = [EntityMock(0, 0, 1, (2, 0)),
                    EntityMock(2, 0, 1, (-2, 0))]
        colide(entities)
        #self.assertTupleEqual(entities[0].forceApplied, (-3, 0))
        self.assertTupleEqual(entities[1].forceApplied, (3, 0))





if __name__ == '__main__':
    unittest.main()

