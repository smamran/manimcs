from manim import *

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
        # Bangla text with highlighted "বিন্দু"
        bn_text = "আজ আমরা শিখব জ্যামিতির সবচেয়ে ছোট কিন্তু সবচেয়ে গুরুত্বপূর্ণ উপাদান — <span fgcolor='#FF5733'><b>বিন্দু</b></span>"
        intro_title_bn = MarkupText(
            wrap_text(bn_text, line_length=40),
            font_size=48,
            font="Nikosh",
            line_spacing=0.5
        )

        # English text with highlighted "The Point"
        en_text = "Today we will learn about the smallest but most important element of geometry — <span fgcolor='#FF5733'><b>The Point</b></span>"
        intro_title_en = MarkupText(
            wrap_text(en_text, line_length=50),
            font_size=42,
            font="Times New Roman",
            line_spacing=0.5
        )

        # Stack texts vertically and center
        V_SPACING = 0.5
        intro_group = VGroup(intro_title_bn, intro_title_en).arrange(DOWN, buff=V_SPACING).move_to(ORIGIN)

        # Hand icon
        hand = SVGMobject("hand.svg").scale(0.3).set_color(YELLOW)
        hand.next_to(intro_title_bn, LEFT, buff=0.3)

        # Animate Bangla text and hand
        self.play(Write(intro_title_bn), FadeIn(hand, shift=RIGHT), run_time=2)
        self.wait(1)

        # Move hand to English text
        self.play(hand.animate.next_to(intro_title_en, LEFT, buff=0.3), run_time=1)

        # Animate English text
        self.play(Write(intro_title_en), run_time=2)
        self.wait(2)

        # Fade out hand at the end
        self.play(FadeOut(hand))
        self.wait()
