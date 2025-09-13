from manim import *
import numpy as np

# Helper function to wrap text after a certain number of characters
def wrap_text(text, line_length=40):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return "\n".join(lines)

class Demo(Scene):
    def construct(self):
        
        # Add background music
        self.add_sound("back.mp3")
        
        # Set background color to a subtle gradient-like color
        self.camera.background_color = "#0f1419"
        
        # Scene control - Comment out scenes you don't want to test
        self.scene_background()
        self.scene_title()
        self.scene_main_content()
        self.scene_point_demonstration()
        self.scene_dot_applications()
        self.scene_conclusion()
    
    def scene_dot_applications(self):
        title1 = Text("দুই বিন্দু দিয়ে রেখা", font_size=48, font="Nikosh", color=YELLOW).to_edge(UP, buff=0.5)
        subtitle1 = Text("দুটি বিন্দু দিয়ে একটি রেখা নির্ধারণ করা যায়", font_size=30, font="Nikosh").next_to(title1, DOWN, buff=0.3)
        
        self.play(Write(title1), run_time=1.5)
        self.play(FadeIn(subtitle1), run_time=1.2)
        self.wait(1)

        # বিন্দু A, B তৈরি - better positioning
        A = Dot(LEFT*2.5 + DOWN*0.8, color=RED)
        B = Dot(RIGHT*2.5 + UP*0.8, color=BLUE)
        labelA = MathTex("A", color=RED, font_size=32).next_to(A, LEFT*0.4 + DOWN*0.3)
        labelB = MathTex("B", color=BLUE, font_size=32).next_to(B, RIGHT*0.4 + UP*0.3)

        # বিন্দুগুলো একসাথে দেখানো
        self.play(
            GrowFromCenter(A), 
            GrowFromCenter(B), 
            Write(labelA), 
            Write(labelB),
            run_time=1.5
        )
        self.wait(0.8)

        # রেখা আঁকা (A-B connect) - extend beyond points
        # line_ab = Line(A.get_center() + LEFT*1.5, B.get_center() + RIGHT*1.5, color=GREEN)
        line_ab = Line(A.get_center(), B.get_center(), color=GREEN)
        self.play(Create(line_ab), run_time=1.5)
        self.wait(1.2)

        # রেখার লেবেল
        line_label = MathTex(r"\overleftrightarrow{AB}", color=GREEN, font_size=28).move_to(DOWN*2)
        self.play(Write(line_label))
        self.wait(1.5)

        # ক্লিয়ার করে পরের সেকশনে যাওয়া
        self.play(
            FadeOut(VGroup(title1, subtitle1, A, B, labelA, labelB, line_ab, line_label)),
            run_time=1
        )
        self.wait(0.5)


        title2 = Text("তিন বিন্দু দিয়ে ত্রিভুজ", font="Nikosh", font_size=48, color=YELLOW).to_edge(UP, buff=0.5)
        subtitle2 = Text("তিনটি বিন্দু একসাথে একটি ত্রিভুজ গঠন করতে পারে", font="Nikosh", font_size=30).next_to(title2, DOWN, buff=0.3)
        
        self.play(Write(title2), run_time=1.5)
        self.play(FadeIn(subtitle2), run_time=1.2)
        self.wait(1)

        # A, B, C পজিশন নির্ধারণ - better triangle shape
        pA = np.array([-2.5, -1, 0])
        pB = np.array([0, 1.5, 0])
        pC = np.array([2.5, -1, 0])

        dotA = Dot(pA, color=RED)
        dotB = Dot(pB, color=GREEN)
        dotC = Dot(pC, color=BLUE)
        
        labelA = MathTex("A", color=RED, font_size=32).next_to(dotA, DOWN*0.4)
        labelB = MathTex("B", color=GREEN, font_size=32).next_to(dotB, UP*0.4)
        labelC = MathTex("C", color=BLUE, font_size=32).next_to(dotC, DOWN*0.4)

        # তিনটি বিন্দু একে একে আনা
        self.play(GrowFromCenter(dotA), Write(labelA), run_time=0.8)
        self.play(GrowFromCenter(dotB), Write(labelB), run_time=0.8)
        self.play(GrowFromCenter(dotC), Write(labelC), run_time=0.8)
        self.wait(0.5)

        # ত্রিভুজ তৈরি (Polygon) - step by step
        line1 = Line(pA, pB, color=YELLOW)
        line2 = Line(pB, pC, color=YELLOW)
        line3 = Line(pC, pA, color=YELLOW)
        
        self.play(Create(line1), run_time=0.8)
        self.play(Create(line2), run_time=0.8)
        self.play(Create(line3), run_time=0.8)
        self.wait(0.5)

        # ত্রিভুজের ভেতর রঙীন ফিল
        triangle = Polygon(pA, pB, pC, fill_color=BLUE, fill_opacity=0.3, stroke_width=0)
        self.play(FadeIn(triangle))
        self.wait(1.5)

        # ত্রিভুজ লেবেল
        triangle_label = MathTex(r"\triangle ABC", font_size=28).move_to(DOWN*2)
        self.play(Write(triangle_label))
        self.wait(1.5)

        # ক্লিয়ার
        self.play(
            FadeOut(VGroup(title2, subtitle2, dotA, dotB, dotC, labelA, labelB, labelC, 
                          line1, line2, line3, triangle, triangle_label)),
            run_time=1
        )
        self.wait(0.5)

        
        title3 = Text("বৃত্তের কেন্দ্র", font="Nikosh", font_size=48, color=YELLOW).to_edge(UP, buff=0.5)
        subtitle3 = Text("একটি বিন্দুই বৃত্তের কেন্দ্র হতে পারে", font="Nikosh", font_size=30).next_to(title3, DOWN, buff=0.3)
        
        self.play(Write(title3), run_time=1.5)
        self.play(FadeIn(subtitle3), run_time=1.2)
        self.wait(1)
        
        center = Dot(ORIGIN, color=RED)
        label_center = MathTex("O", color=RED, font_size=32).next_to(center, DOWN*0.4)
        center_text = Text("(কেন্দ্র)", font_size=20, color=RED).next_to(label_center, DOWN*0.3)
        
        self.play(GrowFromCenter(center), Write(label_center), Write(center_text), run_time=1.5)
        self.wait(0.8)
        

        # বৃত্ত আস্তে আস্তে বড় করে তৈরি
        circle = Circle(radius=2, color=BLUE).move_to(center.get_center())
        self.play(Create(circle), run_time=2)
        self.wait(0.8)

        # কেন্দ্র থেকে বৃত্তের রেডিয়াস দেখানো
        # radius_point = circle.point_from_proportion(0.125)  # 45 degree angle
        radius_point = circle.get_center() + RIGHT * circle.radius   # শুধুমাত্র ডান পাশে
        radius_line = Line(center.get_center(), radius_point, color=GREEN)
        radius_dot = Dot(radius_point, color=GREEN)
        radius_label = MathTex("r", color=GREEN, font_size=28).move_to(radius_line.get_center() + UP*0.3)
        
        self.play(
            Create(radius_line),
            GrowFromCenter(radius_dot),
            Write(radius_label),
            run_time=1.5
        )
        self.wait(1.5)

        # ক্লিয়ার
        self.play(
            FadeOut(VGroup(title3, subtitle3, center, label_center, center_text, 
                          circle, radius_line, radius_dot, radius_label)),
            run_time=1
        )
        self.wait(0.5)
        
        title4 = Text("কোঅর্ডিনেট জ্যামিতি", font="Nikosh", font_size=48, color=YELLOW).to_edge(UP, buff=0.5)
        subtitle4 = Text("কোঅর্ডিনেট সিস্টেমে প্রতিটি বিন্দু (x, y) দিয়ে অবস্থান প্রকাশ করা যায়", font="Nikosh",
                         font_size=24).next_to(title4, DOWN, buff=0.3)
        
        self.play(Write(title4), run_time=1.5)
        self.play(FadeIn(subtitle4), run_time=1.2)
        self.wait(1)

        # Number plane যোগ করা
        plane = NumberPlane(
            x_range=[-4, 4, 1], 
            y_range=[-3, 3, 1], 
            background_line_style={"stroke_opacity": 0.4, "stroke_width": 1},
            axis_config={"stroke_width": 2}
        ).scale(0.8).shift(DOWN*0.6)
        
        plane_labels = plane.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(plane), Write(plane_labels), run_time=2)
        self.wait(0.8)

        # কিছু specific পয়েন্ট প্লট করা
        points_data = [
            (2, 1, "P_1", RED),
            (-1, 2, "P_2", GREEN),
            (1, -1.5, "P_3", BLUE),
            (-2, -1, "P_4", YELLOW),
            (3, 0.5, "P_5", PURPLE),
        ]

        dots = VGroup()
        labels = VGroup()
        coords = VGroup()
        
        for x, y, name, color in points_data:
            pt = Dot(plane.coords_to_point(x, y), color=color)
            lab = MathTex(name, color=color, font_size=24).next_to(pt, UR*0.3)
            coord = MathTex(f"({x}, {y})", font_size=18, color=color).next_to(pt, DR*0.4)
            
            self.play(
                GrowFromCenter(pt), 
                Write(lab), 
                Write(coord),
                run_time=0.6
            )
            dots.add(pt)
            labels.add(lab)
            coords.add(coord)
            self.wait(0.2)

        self.wait(1)

        # শেষের ব্যাখ্যা টেক্সট - better positioning
        final_note = Text("প্রতিটি বিন্দু একটি স্থান নির্দেশ করে — (x, y)", font="Nikosh",
                         font_size=24, color=WHITE).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(final_note), run_time=1.5)
        self.wait(2)

        # Fade out সব কিছু দিয়ে শেষ
        self.play(FadeOut(Group(*self.mobjects)), run_time=2)
    
    def scene_background(self):
        """Create decorative background elements"""
        print("Running: Background Scene")
        
        # Create subtle geometric background pattern
        dots = VGroup()
        for i in range(15):
            for j in range(10):
                dot = Dot(radius=0.02, color=BLUE_E).set_opacity(0.3)
                dot.move_to([i * 0.8 - 5.6, j * 0.8 - 3.6, 0])
                dots.add(dot)
        
        self.background_dots = dots
        self.add(self.background_dots)
        
        print("Background Scene Complete")
    
    def scene_title(self):
        """Show animated title sequence"""
        print("Running: Title Scene")
        
        # Animated title card
        # title_card = Rectangle(width=12, height=8, fill_color=DARK_BLUE, fill_opacity=0.8)
        # title_card.set_stroke(BLUE, width=3)
        
        main_title_bn = Text("জ্যামিতি", font="Nikosh", font_size=72, color=YELLOW)
        main_title_en = Text("GEOMETRY", font="Arial", font_size=48, color=WHITE)
        subtitle = Text("বিন্দু - The Point", font="Nikosh", font_size=54, color=ORANGE)
        
        title_group = VGroup(main_title_bn, main_title_en, subtitle).arrange(DOWN, buff=0.5)
        
        # Animate title sequence
        # self.play(FadeIn(title_card, scale=0.8), run_time=1.5)
        self.play(Write(main_title_bn), run_time=1.5)
        self.play(Write(main_title_en), run_time=1)
        self.play(Write(subtitle), run_time=1)
        self.play(Indicate(subtitle, scale_factor=1.1), run_time=1)
        self.wait(1.5)
        
        # Fade out title card
        self.play(FadeOut(VGroup(title_group)), run_time=1)
        
        print("Title Scene Complete")
    
    def scene_main_content(self):
        """Show main content introduction"""
        print("Running: Main Content Scene")
        
        # Enhanced intro texts with better formatting
        bn_text = "আজ আমরা শিখব জ্যামিতির সবচেয়ে ছোট কিন্তু\nসবচেয়ে গুরুত্বপূর্ণ উপাদান —"
        bn_highlight = "বিন্দু"
        
        en_text = "Today we will learn about the smallest but\nmost important element of geometry —"
        en_highlight = "The Point"
        
        # Create text objects
        intro_title_bn = Text(bn_text, font="Nikosh", font_size=48, color=WHITE, line_spacing=1.1)
        bn_point_text = Text(bn_highlight, font="Nikosh", font_size=48, color=RED, weight=BOLD)
        
        intro_title_en = Text(en_text, font="Roboto", font_size=42, color=BLUE, line_spacing=1.1)
        en_point_text = Text(en_highlight, font="Roboto", font_size=42, color=RED, weight=BOLD)
        
        # Position elements
        intro_title_bn.move_to(UP * 1.5)
        bn_point_text.next_to(intro_title_bn, DOWN, buff=0.3)
        
        intro_title_en.next_to(bn_point_text, DOWN, buff=0.8)
        en_point_text.next_to(intro_title_en, DOWN, buff=0.3)
        
        # Load hand SVG file
        try:
            hand = SVGMobject("hand.svg").scale(0.3).set_color(YELLOW)
        except:
            # Fallback to created hand icon if SVG file not found
            hand = self.create_hand_icon().scale(0.4).set_color(YELLOW)
        
        # Animate content with improved timing
        self.play(
            Write(intro_title_bn),
            # FadeIn(hand.next_to(intro_title_bn, LEFT, buff=0.5)),
            run_time=2
        )
        self.play(
            Write(bn_point_text),
            # hand.animate.next_to(bn_point_text, LEFT, buff=0.5),
            FadeIn(hand.next_to(bn_point_text, LEFT, buff=0.5)),
            run_time=1.5
        )
        
        self.play(Indicate(bn_point_text, scale_factor=1.2), run_time=1)
        
        self.wait(0.5)
        
        self.play(
            Write(intro_title_en),
            #hand.animate.next_to(intro_title_en, LEFT, buff=0.5),
            run_time=2
        )
        self.play(
            Write(en_point_text),
            hand.animate.next_to(en_point_text, LEFT, buff=0.5),
            run_time=1.5
        )
        
        self.play(Indicate(en_point_text, scale_factor=1.2), run_time=1)
        
        self.wait(1)
        
        # Store for later use
        self.intro_group = VGroup(intro_title_bn, bn_point_text, intro_title_en, en_point_text)
        self.hand = hand
        
        print("Main Content Scene Complete")
    
    def scene_point_demonstration(self):
        """Demonstrate what a point is"""
        print("Running: Point Demonstration Scene")
        
        # Clear previous content
        self.play(
            FadeOut(self.intro_group),
            FadeOut(self.hand),
            run_time=1
        )
        
        # Point demonstration section
        demo_title = Text("What is a Point?", font_size=48, color=YELLOW)
        demo_title.to_edge(UP)
        
        self.play(Write(demo_title), run_time=1.5)
        
        # Create multiple points with labels
        points_group = VGroup()
        point_labels = VGroup()
        
        positions = [LEFT * 3 + UP * 2, ORIGIN + UP * 2, RIGHT * 3 + UP * 2]
        colors = [RED, BLUE, GREEN]
        names = ["A", "B", "C"]
        
        for i, (pos, color, name) in enumerate(zip(positions, colors, names)):
            # Create point with a slight glow effect
            point = Dot(pos, radius=0.12, color=color)
            point_glow = Dot(pos, radius=0.2, color=color, fill_opacity=0.3)
            
            # Create label
            label = Text(name, font_size=36, color=color)
            label.next_to(point, DOWN, buff=0.3)
            
            points_group.add(VGroup(point_glow, point))
            point_labels.add(label)
        
        # Animate points appearing
        for i in range(len(positions)):
            self.play(
                GrowFromCenter(points_group[i]),
                Write(point_labels[i]),
                run_time=0.8
            )
        
        self.wait(1)
        
        # Add explanation text with hand icons
        explanation_bn = Text(
            "বিন্দুর কোন দৈর্ঘ্য, প্রস্থ বা উচ্চতা নেই\nএটি শুধুমাত্র অবস্থান নির্দেশ করে",
            font="Nikosh",
            font_size=42,
            color=WHITE,
            line_spacing=1
        )
        
        explanation_en = Text(
            "A point has no length, width, or height\nIt only indicates position",
            font="Roboto",
            font_size=38,
            color=BLUE,
            line_spacing=1
        )
        
        explanations = VGroup(explanation_bn, explanation_en).arrange(DOWN, buff=0.5)
        explanations.shift(DOWN * 1)  # Shift both explanations down significantly
        
        # Create hand icon (reusable for both texts, same as previous scene)
        try:
            hand = SVGMobject("hand.svg").scale(0.3).set_color(YELLOW)
        except:
            # Fallback to created hand icon if SVG file not found
            hand = self.create_hand_icon().scale(0.4).set_color(YELLOW)
        
        # Animate content with improved timing (same as previous scene)
        self.play(
            Write(explanation_bn),
            FadeIn(hand.next_to(explanation_bn, LEFT, buff=0.5)),
            run_time=2
        )
        self.play(
            Write(explanation_en),
            hand.animate.next_to(explanation_en, LEFT, buff=0.5),
            run_time=1.5
        )
        self.wait(1)
        
        # Store for cleanup
        self.demo_elements = VGroup(demo_title, points_group, point_labels, explanations, hand)
        
        # Clear demonstration
        self.play(FadeOut(self.demo_elements), run_time=1)
        
        print("Point Demonstration Scene Complete")
    
    def scene_conclusion(self):
        """Show conclusion with sparkle effects"""
        print("Running: Conclusion Scene")
        
        
        # Final message
        conclusion_bn = Text(
            "বিন্দু হলো জ্যামিতির ভিত্তি!",
            font="Nikosh",
            font_size=42,
            color=GOLD
        )
        conclusion_en = Text(
            "The Point is the Foundation of Geometry!",
            font="Arial",
            font_size=36,
            color=GOLD
        )
        
        conclusion_group = VGroup(conclusion_bn, conclusion_en).arrange(DOWN, buff=0.5)
        
        # Create a decorative border
        border = SurroundingRectangle(
            conclusion_group,
            color=GOLD,
            buff=0.5,
            stroke_width=3
        )
        
        # Final animation with emphasis
        self.play(
            Write(conclusion_group),
            Create(border),
            run_time=2
        )
        
        # Add sparkle effects
        sparkles = VGroup()
        for _ in range(20):
            sparkle = Star(n=5, density=2, outer_radius=0.1, color=YELLOW, fill_opacity=0.8)
            sparkle.move_to([
                np.random.uniform(-6, 6),
                np.random.uniform(-3, 3),
                0
            ])
            sparkles.add(sparkle)
        
        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in sparkles], lag_ratio=0.1),
            run_time=2
        )
        
        self.wait(2)
        
        # Final fade out
        self.play(
            FadeOut(VGroup(conclusion_group, border, sparkles, self.background_dots)),
            run_time=1
        )
        
        print("Conclusion Scene Complete")
        
        end_title = Text("সমাপ্ত", font_size=72)
        self.play(
            Write(end_title),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)
        self.play(FadeOut(end_title), run_time=1.5, rate_func=smooth)

    def create_hand_icon(self):
        """Create a simple hand icon using basic shapes"""
        # Palm
        palm = Ellipse(width=0.8, height=1.2, color=YELLOW, fill_opacity=0.8)
        
        # Fingers
        fingers = VGroup()
        finger_positions = [UP * 0.6 + LEFT * 0.2, UP * 0.7, UP * 0.6 + RIGHT * 0.2, UP * 0.5 + RIGHT * 0.3]
        
        for pos in finger_positions:
            finger = RoundedRectangle(width=0.15, height=0.4, color=YELLOW, fill_opacity=0.8)
            finger.move_to(palm.get_center() + pos)
            fingers.add(finger)
        
        # Thumb
        thumb = RoundedRectangle(width=0.15, height=0.3, color=YELLOW, fill_opacity=0.8)
        thumb.rotate(PI/4)
        thumb.move_to(palm.get_center() + LEFT * 0.4 + UP * 0.1)
        
        hand_icon = VGroup(palm, fingers, thumb)
        return hand_icon