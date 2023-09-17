# Drawingcircles all over the place
import arcade as ar

ar.open_window(600, 600, "Arcade games drawing test")

ar.set_background_color(ar.csscolor.SIENNA)

ar.start_render()

ar.draw_rectangle_filled(0, 0, 1200, 150, ar.csscolor.WHITE)
ar.draw_text("Welcome!", 200, 30, ar.csscolor.BLACK, 24)
ar.draw_circle_filled(300, 300, 80, ar.csscolor.DARK_BLUE)



ar.finish_render()

ar.run()