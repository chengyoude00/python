#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    # def get_score(self):
    #     return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
# s.set_score(60)    #设置成绩
s.set_score(60)
# print s.get_score()  #获取成绩
# s.set_score(1000)
# print s.get_score()
