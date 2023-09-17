"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""
# Import the "ar" library
import arcade as ar

# Lib       Func    W    H         Title
ar.open_window(600, 600, "Drawing Example")

ar.set_background_color(ar.csscolor.SKY_BLUE)

# Get ready to draw
ar.start_render()

# (The drawing code will go here.)
ar.draw_lrtb_rectangle_filled(0, 599, 300, 0, ar.csscolor.GREEN)

# Trees left to right

ar.draw_rectangle_filled(100, 320, 20, 60, ar.csscolor.SIENNA)
ar.draw_circle_filled(100, 350, 30,ar.csscolor.DARK_GREEN)

ar.draw_rectangle_filled(200, 320, 20, 60, ar.csscolor.SIENNA )
ar.draw_ellipse_filled(200, 370, 60, 80, ar.csscolor.DARK_GREEN)

ar.draw_rectangle_filled(300,320, 20, 60, ar.csscolor.SIENNA)
ar.draw_arc_filled(300, 340, 60, 80, ar.csscolor.DARK_GREEN, 0, 180)

ar.draw_rectangle_filled(400, 320, 20, 60, ar.csscolor.SIENNA)
ar.draw_triangle_filled(400, 400, 370, 320, 430, 320, ar.csscolor.DARK_GREEN)

ar.draw_rectangle_filled(500, 320, 20, 60, ar.csscolor.SIENNA)
ar.draw_polygon_filled((
    (500, 400),
    (480, 360),
    (470, 320),
    (530, 320),
    (520, 360)
),
ar.csscolor.DARK_GREEN)

# Draw a sun
ar.draw_circle_filled(500, 550, 40, ar.color.YELLOW)

# Rays to the left, right, up, and down
ar.draw_line(500, 550, 400, 550, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 600, 550, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 500, 450, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 500, 650, ar.color.YELLOW, 3)

# Diagonal rays
ar.draw_line(500, 550, 550, 600, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 550, 500, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 450, 600, ar.color.YELLOW, 3)
ar.draw_line(500, 550, 450, 500, ar.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.
ar.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 ar.color.BLACK, 24)

ar.draw_arc_outline(center_x=300,
                        center_y=340,
                        width=60,
                        height=100,
                        color=ar.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=45)
# Finish drawing
ar.finish_render()

ar.run()