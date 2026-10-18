"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1: Parent class completed
class ParentClass:
    """Base class representing a service member."""
    branch = "U.S. Army"          # class variable shared by all instances

    def __init__(self, name, rank, mos):
        self.name = name           # instance variable
        self.rank = rank           # instance variable
        self.mos = mos             # instance variable

    def status_report(self):
        """Return a basic status string."""
        return f"{self.rank} {self.name} | MOS: {self.mos} | Branch: {ParentClass.branch}"

    def __str__(self):
        return self.status_report()


# TODO 2: Child class completed
class ChildClass(ParentClass):
    """Team Leader subclass that extends the base service member."""
    unit = "497th MRBC"           # new class variable

    def __init__(self, name, rank, mos, team_size, specialty):
        super().__init__(name, rank, mos)
        self.team_size = team_size         # new instance variable
        self.specialty = specialty         # new instance variable
        self.equipment = []                # mutable nested data for copy demo

    def status_report(self):
        """Override parent method to include team-leader specific info."""
        base = super().status_report()
        return f"{base} | Unit: {ChildClass.unit} | Team size: {self.team_size} | Specialty: {self.specialty}"

    def add_equipment(self, item):
        """New method: add an item to the leader's equipment list."""
        self.equipment.append(item)
        return f"Added {item} to {self.name}'s gear."

    def lead_movement(self):
        """New method unique to the child class."""
        return f"{self.rank} {self.name} is leading a movement with {self.team_size} personnel."


# TODO 3: Namespace demonstration completed
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    leader1 = ChildClass("Dante", "SPC", "12C", 4, "Bridge Ops")
    leader2 = ChildClass("Sem", "SPC", "25B", 3, "Cyber")

    # Access class variable through the class
    print(f"Class variable via class: ChildClass.unit = {ChildClass.unit}")
    # Access same class variable through an object
    print(f"Class variable via object: leader1.unit = {leader1.unit}")

    # Add a new attribute to only one object after creation
    leader1.radio_callsign = "Viper 1"
    print(f"\nAdded radio_callsign only to leader1: {leader1.radio_callsign}")

    # Display each object's namespace
    print(f"\nleader1.__dict__: {leader1.__dict__}")
    print(f"leader2.__dict__: {leader2.__dict__}")

    # Class namespace info
    print(f"\nChildClass.__dict__ keys (partial): {[k for k in ChildClass.__dict__ if not k.startswith('_')]}")
    print(f"ParentClass.branch (inherited): {ParentClass.branch}")


# TODO 4: Shallow vs deep copy demonstration completed
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass("Dante", "SPC", "12C", 4, "Bridge Ops")
    original.add_equipment("radio")
    original.add_equipment("bridge panel")

    # Shallow copy (shares nested mutable objects)
    shallow = copy(original)
    # Deep copy (fully independent nested objects)
    deep = deepcopy(original)

    # Modify the original's nested data
    original.equipment.append("extra fuel can")
    original.team_size = 5

    print(f"Original equipment: {original.equipment} | team_size: {original.team_size}")
    print(f"Shallow copy equipment: {shallow.equipment} | team_size: {shallow.team_size}")
    print(f"Deep copy equipment: {deep.equipment} | team_size: {deep.team_size}")
    # Shallow copy sees the equipment change because the list is shared.
    # Deep copy does not. The team_size change is only on the original because
    # it is a simple attribute, not nested.


# TODO 5: Main function completed + student extension
def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent object
    soldier = ParentClass("Jones", "PFC", "12C")
    print(f"\nParent object: {soldier}")
    print(soldier.status_report())

    # Child object
    leader = ChildClass("Dante", "SPC", "12C", 4, "Bridge Ops")
    print(f"\nChild object: {leader}")
    print(leader.status_report())
    print(leader.lead_movement())
    print(leader.add_equipment("Akorn Jr grill"))

    # Demonstrate inheritance
    print(f"\nInheritance check - child can still access parent class var: {leader.branch}")

    demonstrate_namespaces()
    demonstrate_copying()

    # Student-created extension: simple input validation / error handling
    print("\n=== Extension: Edge-case handling ===")
    try:
        bad = ChildClass("", "SPC", "12C", -1, "Invalid")
        if not bad.name or bad.team_size < 1:
            raise ValueError("Name cannot be empty and team size must be positive.")
    except ValueError as e:
        print(f"Caught invalid object creation: {e}")


if __name__ == "__main__":
    main()