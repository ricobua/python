from manim import *


# terminal execute:
# python -m manim render .\main.py Test -pqm
class Test(Scene):
    def construct(self):
        circ = Circle(radius=3, color=RED)
        self.play(Create(circ))
