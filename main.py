import tkinter as tk
import sys
from game_brain import MyApp


def esc_close(tk_instance):
    tk_instance.withdraw()
    sys.exit()


if __name__ == '__main__':
    root = tk.Tk()

    # Close the app when you press esc key
    root.bind('<Escape>', lambda x: esc_close(root))

    game_window = MyApp(root)
    root.mainloop()

#
