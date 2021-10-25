# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:09:25 2021

@author: JOSEPH
"""
class Student():
      def __init__(self, id):
          self.id = id
      def  set_id(self, new_id):
          self.id =new_id
      def get_id(self):
          return self.id
      def register(self):
          self.reg=True
          
class Person 