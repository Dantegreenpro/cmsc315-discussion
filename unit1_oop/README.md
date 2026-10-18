# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

Did the OOP assignment with inheritance, namespaces, and copying. Used a basic soldier / team leader setup so it made sense instead of random generic classes.

## What I Did

Finished all the TODOs in unit1_discussion.py.

1. ParentClass has a class variable for branch, instance variables for name/rank/MOS, a constructor, and a status method.
2. ChildClass inherits from that, adds its own unit class variable plus team size and specialty, overrides the status method, and adds equipment and movement methods.
3. Namespace function makes two ChildClass objects, reads the class variable from both the class and an object, sticks an extra attribute on only one of them, and prints the __dict__ so you can see the difference.
4. Copy function builds an object with a nested equipment list, does a shallow copy and a deep copy, changes the original, and prints all three so the difference is obvious.
5. Main creates both a parent and child object, calls the methods, then runs the two demo functions. Also added a quick check that throws a ValueError if someone tries to make an object with an empty name or negative team size.

## Why It Makes Sense

Parent/child is basically how a regular soldier and a team leader share the same base structure but the leader has extra stuff. Class variables are the shared things (branch, unit). Instance stuff stays with each person. Shallow vs deep copy matters when the object holds a list or other mutable data you don’t want accidentally shared.

## Reflection

Learned that class variables live on the class while instance data stays with the object, and that shallow copy only copies the top level so nested lists stay shared. Main thing that tripped me up was forgetting the equipment list would still be the same object on the shallow copy. Fixed it by just printing both after the change so it was clear. OOP is better than just writing a bunch of separate functions here because the common status format and branch info only live in one place. If that ever needs to change I only fix it once instead of hunting through every function. Makes it easier to add another subclass later without rewriting everything.