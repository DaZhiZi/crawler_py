import turtle, random
from utils import log
from utils import ensure
from utils import isEquals

t = turtle.Turtle()
t.hideturtle()

turtle.tracer(10000, 0.0001)  # draw speed


def forward(step):
    t.forward(step)


# penup 可以把笔抬起来, 这样往前走就不会画线了
def penup():
    t.penup()


# pendown 后又可以画线了
def pendown():
    t.pendown()


# left 可以往左转, 参数是角度
def left(angle):
    t.left(angle)


def right(angle):
    t.right(angle)


# setHeading(注意大小写) 可以设置箭头的朝向, 0 就是朝右
# 90 和 -90 的朝向, 自行摸索一下
def setHeading(angle):
    t.setheading(angle)


def jump(x, y):  # jump 可以无痕走到某个坐标
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def fill_color(color):
    t.fillcolor(color)


def edge_color(color):
    t.color(color)


def start():
    t.begin_fill()


def end():
    t.end_fill()


def write(x, y, str, font_size, edgecolor):
    edge_color(edgecolor)
    jump(x, y)
    t.write(str, font=("宋体", font_size, "normal"))


def author_inform():
    str = "author：大侄子"
    write(-200, -250, str, 33, 'pink')


def rect(x, y, width, height, fillcolor, edgecolor):
    w = width
    h = height
    jump(x, y)
    setHeading(0)
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    i = 0
    while (i < 2):
        forward(w)
        right(90)
        forward(h)
        right(90)
        i = i + 1
    end()


def polygon(length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < n):
        forward(l)
        right(degree)
        # 特别注意，循环结束前一定要改变 i 的值
        # 否则循环永远不会结束的
        i = i + 1
    end()


def circle(x, y, r, fillcolor, edgecolor):
    jump(x, y)
    num = 36
    import math
    length = (2 * math.pi * r) / num
    jcdu = (90 + (360 / num) / 2)
    start()
    left(jcdu)
    forward(r)
    right(jcdu)
    end()
    polygon(length, num, fillcolor, edgecolor)


def sin(degree):
    import math
    # 如上课所述, 数学库里面的 sin 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    radians = degree * math.pi / 180
    return math.sin(radians)


def cos(degree):
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)


def triangle(x=0, y=0, length=101, fillcolor='gray', edgecolor='gray'):
    l = length
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    setHeading(180)
    while (i < 3):
        forward(l)
        right(120)
        i += 1
    end()


def triangle_y(x=0, y=0, length=10, fillcolor='gray', edgecolor='gray'):
    triangle(x, y, length, edgecolor, edgecolor)


def triangle_x(x=0, y=0, length=10, fillcolor='gary', edgecolor='gray'):
    l = length
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    setHeading(90)
    while (i < 3):
        forward(l)
        right(120)
        i += 1
    end()


def write_triangle_y(x, y, str, color):
    t = str
    move_size = 15
    x1 = x
    y1 = y + move_size
    write(x1, y1, t, 10, color)
    pass


def write_triangle_x(x, y, str, color):
    t = str
    move_size = 15
    x1 = x + move_size
    y1 = y
    write(x1, y1, t, 10, color)
    pass


def triangles(x, y, length, fillcolor, edgecolor, size):
    x1 = length / 2 + x
    y1 = size + y
    triangle_y(x1, y1, length, edgecolor, edgecolor)
    write_triangle_x(x1, y1, 'Movies /num', edgecolor)
    x2 = size + x
    y2 = -length / 2 + y
    triangle_x(x2, y2, length, edgecolor, edgecolor)
    write_triangle_x(x2, y2, 'Types', edgecolor)
    pass


def write_temp_cali(x, y, temp, color):
    t = str(temp)
    move_size = 22
    x1 = x - move_size
    y1 = y - 6
    write(x1, y1, t, 10, color)


def calibration(x, y, size, space, length, fillcolor, edgecolor):  # 刻度
    l = length
    time = int(size / space)
    x1 = x
    y1 = y
    edge_color(edgecolor)
    for i in range(time):
        temp = int(i * space / 5 * 2)
        jump(x1, y1)
        forward(l)
        write_temp_cali(x1, y1, temp, edgecolor)
        y1 += space
    end()


def calibration_x(x, y, size, fillcolor, edgecolor):  # y
    s = size
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    jump(x, y)
    forward(s)
    end()


def calibration_y(x, y, size, fillcolor, edgecolor):  # x
    s = size
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    jump(x, y)
    right(-90)
    forward(s)
    end()
    calibration(x, y, size, 25, 5, fillcolor, edgecolor)


# 绘制坐标轴
def coordinateAxis(x, y, size, fillcolor, edgecolor):  # 坐标轴
    # 在坐标原点处绘制两条坐标轴
    s = size
    calibration_x(x, y, s, fillcolor, edgecolor)
    calibration_y(x, y, s, fillcolor, edgecolor)
    length = 12  # 三角形的边长
    triangles(x, y, length, fillcolor, edgecolor, s)
    pass


def write_week(x, y, week, color):  # rect width  30
    move_size = 8
    x1 = x + 30 / 2 - move_size
    y1 = y - 13 - move_size
    write(x1, y1, week, 13, color)


def write_temp(x, y, h, temp, color):
    x1 = x + 30 / 2 - 6
    move_size = 4
    y1 = y + h + 13 - move_size
    write(x1, y1, temp, 13, color)


def cylindricals(x, y, temps, space, base, per_length):  # 所有柱形
    keys = [k for k in temps.keys()]
    per = per_length
    for i in range(len(keys)):
        week = keys[i]  # 'Mon'
        week_temp = temps[week]['temp']  # temp
        color = temps[week]['color']  # color
        h = (week_temp - base) * per
        x1 = (30 + space) * i + space + x  # rect width  30

        write_week(x1, y, week, color)
        rect(x1, y, 30, -h, color, 'black')
        write_temp(x1, y, h, week_temp, color)


def forecast_bar_charts(temps, space, base, per_length):  # bar charts
    x = -55
    y = -200
    # 原点 temp 0
    coordinateAxis(x, y, 550, fillcolor='white', edgecolor='gray')
    cylindricals(x, y, temps, space, base, per_length)
    pass


def test_forecast_bar_charts():
    # temps = []
    # Mon Tue Thu Wed Fri Sat Sun
    data = {
        'Mon': {
            'temp': 21,
            'color': '#FF7D40',
        },
        'Tue': {
            'temp': 19,
            'color': '#33A1C9',
        },
        'Thu': {
            'temp': 22,
            'color': '#FF7D40',
        },
        'Wed': {
            'temp': 24,
            'color': '#FF6347',
        },
        'Fri': {
            'temp': 25,
            'color': '#F00',
        },
        'Sun': {
            'temp': 30,
            'color': '#F00',
        },
    }
    forecast_bar_charts(data, 24, 0, 10)


def square(x, y, width, fillcolor, edgecolor):
    w = width
    jump(x, y)
    setHeading(0)
    fill_color(fillcolor)
    edge_color(edgecolor)
    i = 0
    start()
    while (i < 4):
        forward(w)
        right(90)
        i = i + 1
    end()


def center_square(x, y, width, fillcolor, edgecolor):
    w = width
    x1 = x + w / 2
    y1 = y + w / 2
    square(x1, y1, w, fillcolor, edgecolor)
    pass


def line(x1, y1, x2, y2, color):
    edge_color(color)
    start()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    end()


def connected_point(A, B):  # A点 和 B 点 相连
    x1 = A['x']
    y1 = A['y']
    jump(x1, y1)
    x2 = B['x']
    y2 = B['y']
    color = B['color']
    # import math
    # l = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    line(x1, y1, x2, y2, color)


def connected_points(arr):  # 所有点 相连
    l = len(arr)
    for i in range(l-1):
        A = arr[i]
        B = arr[i + 1]
        connected_point(A, B)
    connected_point(arr[l-2], arr[l-1])


def broken_lines(x, y, temps, space, base, per_length):  # 所有柱形
    keys = [k for k in temps.keys()]
    per = per_length
    points = []
    for i in range(len(keys)):
        week = keys[i]  # 'Mon'
        week_temp = temps[week]['temp']  # temp
        color = temps[week]['color']  # color
        h = (week_temp - base) * per
        x1 = (30 + space) * i + space + x  # rect width  30
        x1 = x1 + 30 / 2  # 中点横坐标

        write_week(x1, y, week, color)
        y1 = y + h + + 30 / 2  - 7 # 中点纵坐标
        center_square(x1, y1, 8, color, color)
        write_temp(x1, y + 10, h, week_temp, color)

        point = {}
        point['x'] = x1 + 7
        point['y'] = y1
        point['color'] = color
        points.append(point)
    connected_points(points)


def forecast_line_charts(temps, space, base, per_length):  # bar charts
    x = -55
    y = -200
    # 原点 temp 0
    coordinateAxis(x, y, 550, fillcolor='white', edgecolor='gray')
    broken_lines(x, y, temps, space, base, per_length)
    pass


"""
图：
    柱形图：
        坐标轴：
                x 轴：
                    箭头（三角形）
                    刻度
                    文本信息
                y 轴：
                    箭头（三角形）
                    刻度
                    文本信息
        rects:
                rect:
                    高度 （temp 温度）
                    宽度  （默认 30px）
                    颜色 ：
                        边缘
                        填充
                文本信息
                   
    折线图：
        坐标轴：
                x 轴：
                    箭头（三角形）
                    刻度
                    文本信息
                y 轴：
                    箭头（三角形）
                    刻度
                    文本信息
        lines:
                line:
                     point: 
                        x 坐标
                        y 坐标
                        颜色
                文本信息
                square:
                     中心 x 坐标
                     中心 y 坐标
                     颜色
"""
"""
ten_type = {
    '犯罪': 45,
    '剧情': 194,
    '爱情': 58,
    '动作': 30,
    '喜剧': 46,
    '动画': 32,
    '奇幻': 32,
    '悬疑': 33,
    '冒险': 45,
    '惊悚': 36,
}
"""
def movies_type_line_charts():
    data = {
        '犯罪': {
            'temp': 45,
            'color': '#FF7D40',
        },
        '剧情': {
            'temp': 194,
            'color': '#22DDDD',
        },
        '爱情': {
            'temp': 58,
            'color': '#FF3333',
        },
        '动作': {
            'temp': 30,
            'color': '#FF8533',
        },
        '喜剧': {
            'temp': 46,
            'color': '#FF33FF',
        },
        '动画': {
            'temp': 32,
            'color': '#FF8533',
        },
        '冒险': {
            'temp': 45,
            'color': '#FF33FF',
        },
        '惊悚': {
            'temp': 36,
            'color': '#FF8533',
        },
    }
    forecast_line_charts(data, 24, 0, 5 / 2)

def movies_type_bar_charts():
    data = {
        '犯罪': {
            'temp': 45,
            'color': '#FF7D40',
        },
        '剧情': {
            'temp': 194,
            'color': '#22DDDD',
        },
        '爱情': {
            'temp': 58,
            'color': '#FF3333',
        },
        '动作': {
            'temp': 30,
            'color': '#FF8533',
        },
        '喜剧': {
            'temp': 46,
            'color': '#FF33FF',
        },
        '动画': {
            'temp': 32,
            'color': '#FF8533',
        },
        '冒险': {
            'temp': 45,
            'color': '#FF33FF',
        },
        '惊悚': {
            'temp': 36,
            'color': '#FF8533',
        },
    }
    forecast_bar_charts(data, 24, 0, 5 / 2)


"""
{
  '美国': 144,
  '中国大陆': 48,    

  '法国': 24,
  '意大利': 12,
  '日本': 33,
  '英国': 34,
  '德国': 20,
  '加拿大': 7,
  '韩国': 9,
  '澳大利亚': 6,
  '西班牙': 6,
  }
"""
def movies_country_line_charts():
    data = {
        '美': {
            'temp': 144,
            'color': '#FF7D40',
        },
        '中': {
            'temp': 48,
            'color': '#22DDDD',
        },
        '法': {
            'temp': 24,
            'color': '#FF3333',
        },
        '意': {
            'temp': 12,
            'color': '#FF8533',
        },
        '英': {
            'temp': 34,
            'color': '#FF33FF',
        },
        '日': {
            'temp': 33,
            'color': '#FF8533',
        },
        '德': {
            'temp': 20,
            'color': '#FF33FF',
        },
        '韩': {
            'temp': 9,
            'color': '#FF8533',
        },
    }
    forecast_line_charts(data, 24, 0, 5 / 2)
# data = [
#     {
#         'id': 1,
#         'country': 'rerg',
#          'temp': 144,
#         'color': '#FF7D40',
#     },
#    {
#         'id': 2,
#         'country': '',
#          'temp': 144,
#         'color': '#FF7D40',
#     },
# ]
def movies_country_bar_charts():
    data = {
        '美': {
            'temp': 144,
            'color': '#FF7D40',
        },
        '中': {
            'temp': 48,
            'color': '#22DDDD',
        },
        '法': {
            'temp': 24,
            'color': '#FF3333',
        },
        '意': {
            'temp': 12,
            'color': '#FF8533',
        },
        '英': {
            'temp': 34,
            'color': '#FF33FF',
        },
        '日': {
            'temp': 33,
            'color': '#FF8533',
        },
        '德': {
            'temp': 20,
            'color': '#FF33FF',
        },
        '韩': {
            'temp': 9,
            'color': '#FF8533',
        },
    }
    forecast_bar_charts(data, 24, 0, 5 / 2)

def main():
    # author_inform()
    # movies_type_line_charts()
    # movies_type_bar_charts()
    # test_forecast_line_charts()
    # test_forecast_bar_charts()
    # movies_country_line_charts()
    movies_country_bar_charts()
    turtle.done()


if __name__ == '__main__':
    main()
