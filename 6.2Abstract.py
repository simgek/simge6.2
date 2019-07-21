from abc import ABCMeta, abstractmethod


class BaseClass():
    __metaclass__ = ABCMeta

    #@abstractmethod
    def printHam(self):
        return "default ses"


class Personel(BaseClass):
    departman = ""

    def printHam(self):
        return "default ses"

base = BaseClass()
base.printHam()

per = Personel()
print(per.printHam())
