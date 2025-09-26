#!/usr/bin/env python3
"""
Module defining an abstract base class Animal
and two concrete subclasses: Dog and Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class inheriting from Animal.
    Implements the sound method to return "Bark".
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class inheriting from Animal.
    Implements the sound method to return "Meow".
    """

    def sound(self):
        return "Meow"
