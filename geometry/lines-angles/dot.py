from manim import *

class Demo(Scene):
    def construct(self):
        # Scene 1: Title
        title_bn = Text("বিন্দু", 
                        font_size=48, font="Nikosh")
        title_en = Text("Dot", 
                        font_size=30).next_to(title_bn, DOWN*1.2)

        # Fade in both titles
        self.play(FadeIn(title_bn), FadeIn(title_en))
        self.wait(1)

        # Move Bangla title to top
        self.play(title_bn.animate.move_to(UP*3), run_time=1.5, rate_func=smooth)
        self.play(FadeOut(title_en))
        self.wait(0.5)
