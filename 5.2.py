import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def box(x, y, z):
    if -1 * z <= x <= z or -1 * z <= y <= z:
        return abs(x) - z if abs(x) - z > abs(y) - z else abs(y) - z
    elif -1 * z <= x <= z and -1 * z <= y <= z:
        return z - abs(x) if z - abs(x) > z - abs(y) else z - abs(y)
    else:
        return abs(x) - z if abs(x) - z > abs(y) - z else abs(y) - z


def sdf_func(x, y):
    return box(x, y, 0.4)


def shader(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    print(d)
    return d > 0, abs(d) * 3, 0


main(shader)
