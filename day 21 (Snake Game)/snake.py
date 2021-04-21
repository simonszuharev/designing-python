import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.list_snake = []
        self.create()
        self.head = self.list_snake[0]

    def __create_the_snake(self):
        x = 0
        for i in range(0, 3):
            i = turtle.Turtle(shape="square")
            i.color("white")
            i.penup()
            i.goto(x=x, y=0)
            x -= 20
            self.list_snake.append(i)
        return self.list_snake

    def move(self):
        for item_num in range(len(self.list_snake) - 1, 0, -1):
            new_x = self.list_snake[item_num - 1].xcor()
            new_y = self.list_snake[item_num - 1].ycor()
            self.list_snake[item_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #Extension function
    def __get_fat(self):
        x_cor = self.list_snake[len(self.list_snake)-1].xcor()
        y_cor = self.list_snake[len(self.list_snake) - 1].ycor()
        i = turtle.Turtle(shape="square")
        i.color("white")
        i.penup()
        i.goto(x=x_cor, y=y_cor)
        self.list_snake.append(i)

    def __up_move(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def __down_move(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def __left_move(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def __right_move(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def create(self):
        self.__create_the_snake()

    def left(self):
        self.__left_move()

    def right(self):
        self.__right_move()

    def up(self):
        self.__up_move()

    def down(self):
        self.__down_move()

    def add_element(self):
        self.__get_fat()
