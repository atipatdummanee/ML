import tkinter as tk
import turtle as t


def draw_flower():
    # สร้างหน้าต่างใหม่สำหรับการแสดงรูป
    flower_window = tk.Toplevel(root)
    flower_window.title("Flower")
    canvas = tk.Canvas(flower_window, width=400, height=400)
    canvas.pack()

    # ใช้ turtle วาดดอกไม้ใน tkinter canvas
    screen = t.TurtleScreen(canvas)
    screen.bgcolor("white")
    pen = t.RawTurtle(screen)
    pen.speed(0)

    # ฟังก์ชันวาดกลีบดอกไม้แบบคาร์เนชั่น
    def draw_carnation_petal(pen):
        pen.color("red")
        pen.begin_fill()
        for _ in range(2):
            pen.circle(60, 60)
            pen.left(120)
            pen.circle(60, 60)
            pen.left(120)
        pen.end_fill()

    # ฟังก์ชันวาดดอกไม้
    def draw_full_flower():
        pen.penup()
        pen.goto(0, 100)
        pen.setheading(0)
        pen.pendown()
        for _ in range(8):
            draw_carnation_petal(pen)
            pen.right(45)
        # วาดเกสรดอกไม้ตรงกลาง
        pen.penup()
        pen.goto(0, 90)
        pen.pendown()
        pen.color("yellow")
        pen.begin_fill()
        pen.circle(10)
        pen.end_fill()

    # ฟังก์ชันวาดลำต้น
    def draw_stem(length):
        pen.penup()
        pen.goto(0, 100)
        pen.setheading(-90)
        pen.color("green")
        pen.width(4)
        pen.pendown()
        pen.forward(length)

    # ฟังก์ชันวาดใบไม้
    def draw_leaf(size, angle):
        pen.begin_fill()
        pen.circle(size, angle)
        pen.left(180 - angle)
        pen.circle(size, angle)
        pen.end_fill()

    # ฟังก์ชันวาดใบไม้หลายใบ
    def draw_leaves():
        pen.width(2)
        pen.color("green")
        leaf_positions = [(-15, -50), (15, -80), (-15, -110), (15, -140)]
        leaf_angles = [35, -35, 25, -25]
        leaf_sizes = [25, 30, 20, 30]

        for pos, angle, size in zip(leaf_positions, leaf_angles, leaf_sizes):
            pen.penup()
            pen.goto(pos)
            pen.setheading(angle)
            pen.pendown()
            draw_leaf(size, 60)

    # วาดลำต้นและใบก่อน จากนั้นจึงวาดดอกไม้ด้านบน
    draw_stem(150)
    draw_leaves()
    draw_full_flower()

    # ซ่อนปากกา
    pen.hideturtle()


# สร้างหน้าต่างหลักและป้ายข้อความที่ดูเหมือนลิงก์
root = tk.Tk()
root.title("Flower Display")

# ป้ายข้อความที่มีลักษณะเป็นลิงก์
link_label = tk.Label(root, text="Click here to display the flower", fg="blue", cursor="hand2",
                      font=("Arial", 12, "underline"))
link_label.pack(pady=20)
link_label.bind("<Button-1>", lambda e: draw_flower())  # คลิกแล้วเรียกฟังก์ชันวาดดอกไม้

root.mainloop()
