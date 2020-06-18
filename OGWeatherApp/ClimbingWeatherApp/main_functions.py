#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:13:19 2019

@author: ep9k
"""

class Food(object):
    def __init__(self):
        self.consumed = False

    def consume(self):
        self.consumed = True


class Fruit(Food):
    def __init__(self):
        super(Fruit, self).__init__()
        self.been_cut = False

    def cut(self):
        print("cut the fruit")
        self.been_cut = True


class Consumer(object):
    def __init__(self):
        self.apple = Fruit()
        self.banana = Fruit()

    def consume_food(self):
        food = self.pick_food()
        food.cut()
        print("consuming the food")
        food.consume()

    def pick_food(self):
        return self.apple