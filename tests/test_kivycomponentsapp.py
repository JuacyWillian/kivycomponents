#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from kivy.clock import Clock
from kivycomponents import KivycomponentsApp


class TestKivycomponentsApp(unittest.TestCase):
    """TestCase for KivycomponentsApp.
    """

    def setUp(self):
        self.app = KivycomponentsApp()
        Clock.schedule_once(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

    def test_name(self):
        self.assertEqual(self.app.get_application_name(), 'Kivy Components')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
