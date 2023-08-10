from mobile import Mobile
from state import SilentState

if __name__ == "__main__":
    nokia_mobile = Mobile('Nokia Supernova')
    nokia_mobile.ring()

    nokia_mobile.set_state(SilentState())
    nokia_mobile.ring()
