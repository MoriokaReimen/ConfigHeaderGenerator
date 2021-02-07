from View import View
from Control import Control

if __name__ == '__main__':
    control = Control.Control()
    view = View.View(control)
    view.start()