import unittest
from pam import *

class PamTest(unittest.TestCase):

    """Test case utilisé pour tester les methodes de la classe Pam"""
    def setUp(self):
        self.pam = Pam("test", "..\\Cartes\\Facile.txt")
        self.assertEqual(Pam, type(self.pam))
        
    def test_robot(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        self.pam.robot("R,0,0")
        self.assertIn(self.pam.robots, 'R')
        self.assertIn(self.pam.robots.values(),(0,0))
