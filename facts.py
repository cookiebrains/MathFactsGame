import random


class Fact(object):
    def __init__(self, app_reference, initial_x, update_millis):
        self.initial_coords = [10 + initial_x, 60, 50 + initial_x, 0]  # [x1, y1, x2, y2]
        self.app_reference = app_reference
        self.color = "blue"
        self.top_num = random.randint(2, 9)
        self.bottom_num = random.randint(2, 9)
        self.answer_value = self.top_num + self. bottom_num
        self.update_millis = update_millis
        self.rectangle_sprite = self.draw_rectangle()
        self.text_sprite = self.draw_text()

    def go(self):
        self.move()

    def is_answer_value(self, answer_try):
        is_correct = answer_try == self.answer_value
        if is_correct:
            self.app_reference.canvas.itemconfig(self.rectangle_sprite, fill='green')
        return is_correct

    def move(self):
        # TODO: check if below bottom of canvas
        self.app_reference.canvas.move(self.rectangle_sprite, 0, 1)
        self.app_reference.canvas.move(self.text_sprite, 0, 1)
        self.app_reference.tk_instance.after(self.update_millis, self.move)
        pass

    def draw_rectangle(self):
        sprite = self.app_reference.canvas.create_rectangle(*self.initial_coords,
                                                            fill=self.color,
                                                            outline=self.color)
        return sprite

    def draw_text(self):
        sprite = self.app_reference.canvas.create_text(self.initial_coords[0] + 15,
                                                       self.initial_coords[1] - 30,
                                                       text=f'  {self.top_num}\n+{self.bottom_num}',
                                                       fill='white',
                                                       font=('Arial', 15))
        return sprite
