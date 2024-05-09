from manim import *


class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1,
                line_moving,
                radius=0.5 +
                3 *
                SMALL_BUFF,
                other_angle=False).point_from_proportion(0.5))

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(
                line_ref.copy()).rotate(
                theta_tracker.get_value() *
                DEGREES,
                about_point=rotation_center))

        a.add_updater(
            lambda x: x.become(
                Angle(
                    line1,
                    line_moving,
                    radius=0.5,
                    other_angle=False)))
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1,
                    line_moving,
                    radius=0.5 +
                    3 *
                    SMALL_BUFF,
                    other_angle=False).point_from_proportion(0.5)))

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
