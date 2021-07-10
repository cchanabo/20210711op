input.onGesture(Gesture.TiltRight, function () {
    music.playMelody("F D C F G A F - ", 120)
})
input.onButtonPressed(Button.A, function () {
    music.playMelody("C C F G A A A - ", 120)
})
input.onGesture(Gesture.TiltLeft, function () {
    music.playMelody("A A C5 A G F D - ", 120)
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("A C5 C5 A F A G - ", 120)
})
basic.forever(function () {
	
})
