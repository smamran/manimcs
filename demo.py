from manim import *

class Demo(Scene):
    def construct(self):
        
        self.add_sound("back.mp3")
        
        # Scene 1: Title
        title_bn = Text("জ্যামিতির বিভিন্ন আকার", font_size=48, font="Nikosh")
        title_en = Text("Various Geometric Shapes", font_size=36).next_to(title_bn, DOWN*1.2)
        
        # Fade in both titles
        self.play(FadeIn(title_bn), FadeIn(title_en))
        self.wait(1)
        
        # Move Bangla title to top
        self.play(title_bn.animate.move_to(UP*3), run_time=1.5, rate_func=smooth)
        self.wait(0.5)
        
        # List of shapes and their names
        shapes = [
            (Circle(radius=1, color=BLUE), "Circle"),
            (Square(side_length=2, color=GREEN), "Square"),
            (Triangle(color=RED), "Triangle"),
            (Rectangle(width=3, height=1.5, color=YELLOW), "Rectangle"),
            (Ellipse(width=3, height=1.5, color=PURPLE), "Ellipse"),
            (RegularPolygon(n=5, color=ORANGE), "Pentagon"),
            (RegularPolygon(n=6, color=TEAL), "Hexagon"),
            (RegularPolygon(n=8, color=PINK), "Octagon"),
            (Star(color=GOLD, fill_opacity=0.5), "Star")
        ]

        previous_shape = None
        previous_name = None

        for i, (shape, name_text) in enumerate(shapes):
            shape_name = Text(name_text, font_size=36).next_to(shape, DOWN*1.5)
            
            if i == 0:
                # Morph English subtitle to first shape name
                self.play(
                    ReplacementTransform(title_en, shape_name),
                    Create(shape),
                    run_time=1.5,
                    rate_func=smooth
                )
            else:
                self.play(
                    ReplacementTransform(previous_shape, shape),
                    ReplacementTransform(previous_name, shape_name),
                    run_time=1.5,
                    rate_func=smooth
                )
            
            previous_shape = shape
            previous_name = shape_name
            self.wait(0.5)

        # Last scene: all objects morph to "সমাপ্ত" and fade out
        end_title = Text("সমাপ্ত", font_size=72)
        self.play(
            ReplacementTransform(title_bn, end_title),
            ReplacementTransform(previous_shape, end_title),
            ReplacementTransform(previous_name, end_title),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)
        self.play(FadeOut(end_title), run_time=1.5, rate_func=smooth)