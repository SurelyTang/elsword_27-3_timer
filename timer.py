import tkinter as tk
import keyboard 

def close_window():
    root.destroy()

font_size=10

class CountdownTimer:
    def __init__(self, root, timer_name, initial_seconds, row, column):
        self.root = root
        self.timer_name = timer_name
        self.remaining_time = tk.StringVar()
        self.initial_seconds = initial_seconds
        self.remaining_seconds = initial_seconds

        self.time_label = tk.Label(root, textvariable=self.remaining_time, font=("Helvetica", font_size))
        self.time_label.grid(row=row, column=column, padx=10, pady=5)

        self.start_button = tk.Button(root, text=f"重置计时 {timer_name}", command=self.reset_and_start, font=("Times", font_size))
        self.start_button.grid(row=row+1, column=column, padx=10, pady=5)

        self.is_running = False
        self.timer_id = None

    
    def reset_and_start(self):
        self.reset_countdown()
        self.start_countdown()
        
        
    def start_countdown(self):
        if not self.is_running:
            self.is_running = True
            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)  # 取消先前的定时器
            self.update_clock()

    def reset_countdown(self):
        self.is_running = False
        self.remaining_seconds = self.initial_seconds
        mins, secs = divmod(self.remaining_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.remaining_time.set(f"{self.timer_name}: {timeformat}")

    def update_clock(self):
        if self.remaining_seconds >= 0 and self.is_running:
            mins, secs = divmod(self.remaining_seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.remaining_time.set(f"{self.timer_name}: {timeformat}")
            self.remaining_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_clock)  # 更新定时器

        elif not self.is_running:
            self.is_running = False
    
    def update_clock(self):
        if self.remaining_seconds >= 0 and self.is_running:
            mins, secs = divmod(self.remaining_seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.remaining_time.set(f"{self.timer_name}: {timeformat}")

            if self.remaining_seconds <= 15:
                self.time_label.config(fg="red")  # 将字体颜色更改为红色
            else:
                self.time_label.config(fg="black")  # 恢复字体颜色为黑色

            self.remaining_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_clock)  # 更新定时器

        elif not self.is_running:
            self.is_running = False

def on_f1_press(event):
    timer0.reset_countdown()
    timer0.start_countdown()

def on_f2_press(event):
    timer1.reset_countdown()
    timer1.start_countdown()

def on_f3_press(event):
    timer2.reset_countdown()
    timer2.start_countdown()

def on_f4_press(event):
    timer3.reset_countdown()
    timer3.start_countdown()

def on_f5_press(event):
    timer4.reset_countdown()
    timer4.start_countdown()

def on_f6_press(event):
    timer5.reset_countdown()
    timer5.start_countdown()

def on_f7_press(event):
    timer6.reset_countdown()
    timer6.start_countdown()

def on_f8_press(event):
    timer7.reset_countdown()
    timer7.start_countdown()

if __name__ == '__main__':
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', 1)  # 窗口置于顶层
    root.title('27-3计时器 作者联系方式1051742287')
    #全部烧掉时禁锢小花都可以按了，最开始可以按镰刀，4分钟+冰冻延时差不多就好，第一次禁锢按蛋壳，第二次地刺后30秒回修地板，会因为控被延迟
    #修地板从持续17秒左右，结束按来得及
    #控的久可能先地刺再蛋壳
    timer0 = CountdownTimer(root, "地刺", 158, 0, 0)
    timer1 = CountdownTimer(root, "冰冻", 90, 0, 1)
    timer2 = CountdownTimer(root, "禁锢", 80, 0, 2)
    timer3 = CountdownTimer(root, "小花", 75, 0, 3)
    timer4 = CountdownTimer(root, "镰刀", 240, 0, 4)
    timer5 = CountdownTimer(root, "蛋壳", 240, 0, 5)
    timer6 = CountdownTimer(root, "修地板", 300, 0, 6)
    timer7 = CountdownTimer(root, "延迟", 30, 0, 7)
    keyboard.on_press_key('F1', on_f1_press)
    keyboard.on_press_key('F2', on_f2_press)
    keyboard.on_press_key('F3', on_f3_press)
    keyboard.on_press_key('F4', on_f4_press)
    keyboard.on_press_key('F5', on_f5_press)
    keyboard.on_press_key('F6', on_f6_press)
    keyboard.on_press_key('F7', on_f7_press)
    keyboard.on_press_key('F8', on_f8_press)


    #keyboard.add_hotkey('alt+1', on_f2_press)
    #root.bind("<F2>", on_f2_press)
    
    
    close_button = tk.Button(root, text="关闭", command=close_window)
    close_button.grid(row=0, column=8, columnspan=6)  # 使用grid布局管理器

    root.mainloop()