from manim import *


class Demo(Scene):
    def construct(self):
        # Dot তৈরি
        dot = Dot(color=RED)
        self.add(dot)

        # Dot ধীরে ধীরে 3 গুণ বড় করা
        self.play(dot.animate.scale(10))

        # Dot আবার ছোট করা (0.5 গুণ)
        self.play(dot.animate.scale(0.5))

        # Dot কে ধীরে ধীরে 2 গুণ বড় করে ডানে সরানো
        #self.play(dot.animate.scale(2).shift(RIGHT * 2))

        self.wait(1)
