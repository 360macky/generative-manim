from manim import *


class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0,
            height=5.0,
            fill_opacity=0.5,
            color=BLUE,
            stroke_width=10).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText(
            "<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(
            bool_ops_text,
            ellipse1,
            ellipse2).move_to(
            LEFT *
            3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(
            i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(
            e.animate.scale(0.3).next_to(
                u,
                DOWN,
                buff=exclusion_text.height *
                3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(
            d.animate.scale(0.3).next_to(
                u,
                LEFT,
                buff=difference_text.height *
                3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))
