def on_gesture_tilt_right():
    music.play_melody("F D C F G A F - ", 120)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_a():
    music.play_melody("C C F G A A A - ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    music.play_melody("A A C5 A G F D - ", 120)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    music.play_melody("A C5 C5 A F A G - ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("Hello!")
basic.forever(on_forever)
