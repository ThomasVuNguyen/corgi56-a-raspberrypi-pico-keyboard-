print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,board.GP6,board.GP7)
keyboard.row_pins = (board.GP16,board.GP17 ,board.GP18,board.GP19,board.GP20,board.GP12,board.GP13,board.GP14,board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
[KC.Y, KC.T, KC.R, KC.NO, KC.NO, KC.E, KC.W, KC.Q, KC.BSPC, KC.A, KC.P, KC.NO, KC.NO, KC.O, KC.I, KC.U, KC.J, KC.H, KC.G, KC.NO, KC.NO, KC.F, KC.D, KC.S, KC.V, KC.C, KC.X, KC.NO, KC.NO, KC.Z, KC.L, KC.K, KC.ENT, KC.TAB, KC.CAPS, KC.ESC , KC.M , KC.N , KC.B, KC.SPC,KC.N3, KC.N2 , KC.N1 , KC.NO, KC.NO, KC.EQL , KC.PGUP , KC.MINS, KC.N6 , KC.N5 , KC.N4, KC.NO, KC.NO, KC.RIGHT , KC.QUOTE , KC.LEFT,KC.N9 , KC.N8 , KC.N7, KC.NO, KC.NO , KC.COMM , KC.PGDN , KC.SCLN, KC.RSFT , KC.N0 , KC.LCTL, KC.NO, KC.NO, KC.SLASH , KC.DOT ,KC.LALT, ]
]

keyboard.go()