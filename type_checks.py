# Resolve 1
import os
import sys
from collection import defaultdict

def say_hello():
    print("HEllo world")

def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)

if __name__ == "__main__":
    heights = [5.5, 6, 5.9]
    greet_all(heights)
