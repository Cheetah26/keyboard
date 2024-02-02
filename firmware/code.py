import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4)
keyboard.row_pins = (board.GP22, board.GP20, board.GP23, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.modules.split import Split, SplitType
split = Split(
    split_flip=True,
    split_side=None,
    split_type=SplitType.UART,
    split_target_left=True,
    uart_interval=20,
    data_pin=board.GP2,
    data_pin2=board.GP3,
    uart_flip=True,
    use_pio=True,
)
keyboard.modules.append(split)

from kmk.modules.holdtap import HoldTap
keyboard.modules.append(HoldTap())
SPC_LSFT = KC.HT(KC.SPC, KC.LSFT)
ENT_LGUI = KC.HT(KC.ENT, KC.LGUI)

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())
TO_BASE = KC.TO(0)
TO_STENO = KC.TO(3)
MO_NUM = KC.MO(1)
MO_MISC = KC.MO(2)

from kmk.modules.combos import Combos, Chord
combos = Combos(
  combos=[
        Chord((SPC_LSFT, ENT_LGUI), KC.LALT),
        Chord((MO_NUM, KC.BSPC), MO_MISC)
])
keyboard.modules.append(combos)

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.steno import Steno
keyboard.modules.append(Steno())

keyboard.keymap = [
    [ # Base layer
        KC.ESC, KC.Q, KC.W, KC.E, KC.R,     KC.T,         KC.Y,     KC.U,     KC.I,    KC.O,   KC.P,    KC.LBRC,
        KC.TAB, KC.A, KC.S, KC.D, KC.F,     KC.G,         KC.H,     KC.J,     KC.K,    KC.L,   KC.QUOT, KC.SCLN,
        KC.LCTL,KC.Z, KC.X, KC.C, KC.V,     KC.B,         KC.N,     KC.M,     KC.COMM, KC.DOT, KC.SLSH, KC.RBRC,
        KC.NO,  KC.NO,KC.NO,KC.NO,MO_NUM, KC.BSPC,      SPC_LSFT, ENT_LGUI, KC.NO,KC.NO,KC.NO,KC.NO,
    ],
    [ # Numbers / navigation
        KC.TRNS, KC.GRAVE,  KC.N6, KC.N5, KC.N4, KC.MINS,            KC.HOME, KC.PGDOWN, KC.PGUP, KC.END, KC.NO, KC.NO,
        TO_STENO, KC.EQL, KC.N3, KC.N2, KC.N1, KC.N0,              KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.NO, KC.NO,
        KC.TRNS, KC.BSLASH,  KC.N9, KC.N8, KC.N7, KC.PDOT,            KC.NO,   KC.NO,   KC.NO, KC.NO,   KC.NO, KC.NO,
        KC.NO,   KC.NO,  KC.NO, KC.NO, KC.TRNS,KC.TRNS,           KC.TRNS, KC.TRNS, KC.NO, KC.NO,    KC.NO, KC.NO,
    ],
    [ # Misc.
        KC.TRNS, KC.NO,  KC.F6, KC.F5, KC.F4, KC.F10,            KC.HOME, KC.PGDOWN, KC.PGUP, KC.END,    KC.NO, KC.NO,
        KC.TRNS, KC.NO, KC.F3, KC.F2, KC.F1, KC.F11,            KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT,KC.MPLY, KC.NO,
        KC.TRNS, KC.NO,  KC.F9, KC.F8, KC.F7, KC.F12,            KC.NO,   KC.NO,   KC.NO, KC.NO,   KC.NO, KC.NO,
        KC.NO,   KC.NO,  KC.NO, KC.NO, KC.TRNS,KC.TRNS,          KC.TRNS, KC.TRNS, KC.NO, KC.NO,    KC.NO, KC.NO,
    ],
    [ # Steno
        KC.ESC, KC.STN_LS1, KC.STN_LT, KC.STN_LP, KC.STN_LH, KC.NO,       KC.STN_AS3, KC.STN_RF, KC.STN_RP, KC.STN_RL, KC.STN_RT, KC.STN_RD,
        TO_BASE, KC.STN_LS2, KC.STN_LK, KC.STN_LW, KC.STN_LR, KC.NO,       KC.STN_AS4, KC.STN_RR, KC.STN_RB, KC.STN_RG, KC.STN_RS, KC.STN_RZ,
        KC.NO, KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,       KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
        KC.NO,   KC.NO,      KC.NO,     KC.NO,     KC.STN_A,  KC.STN_O,    KC.STN_E,  KC.STN_U,  KC.NO,     KC.NO,     KC.NO,     KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()