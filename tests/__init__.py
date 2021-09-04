import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Modules to import
import src


# Constants
A_CONSTANT = 12345


# Functions
def equals(thing_a, thing_b):
    """Asserts if thing_a equals thing_b."""
    assert thing_a == thing_b
