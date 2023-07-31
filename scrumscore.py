# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import messagebox, font, ttk
import jdatetime as jalali
from farsikon import fdigit_replacer 
from placeholder import PlaceholderEntry
from guide import ToolTip


text1 = ".پروژه مربوطه را انتخاب نمائید"
text2 = ".امتیاز برگزاری جلسات روزانه را وارد کنید"
text3 = ".میزان نسبت استوری‌پوینت پیش‌بینی شده به ماکزیمم استوری‌پوینت را وارد کنید"
text4 = ".میزان نسبت مجموع تسک‌پوینت به استوری‌پوینت پیش‌بینی شده را وارد کنید"

# Predefined teams
teams = ["گروه اول", "گروه دوم", "گروه سوم", "گروه چهارم", "گروه پنجم"]

# Data storage
data = {}

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Scrum محاسبه امتیاز")
        self.geometry("400x200")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CalcPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        if cont == StartPage:
            self.geometry("400x260")
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        persian_bold = font.Font(family='Vazirmatn', size=10, weight="bold")
        persian_italic = font.Font(family='Vazirmatn', size=10, slant="italic")
        persian_font = font.Font(family='Vazirmatn', size=10)
        jalali_date = fdigit_replacer(jalali.datetime.now().strftime('%Y-%m-%d')) + ' :تاریخ امروز'
        tk.Label(self, text=str(jalali_date), font=persian_font).pack(pady=10,padx=10)


        tk.Label(self, text=text1, font=persian_bold, fg='#874545').pack(pady=10,padx=10)

        self.team_var = tk.StringVar(self)
        self.team_var.set(teams[0])  # default value

        drop = ttk.Combobox(self, textvariable=self.team_var, values=teams)
        drop.pack()

        button = tk.Button(self, text="ادامه", command=lambda: self.continue_to_calc(controller), font=persian_font)
        button.pack(pady=10)
        button2 = tk.Button(self, text="خروج", command=lambda: self.quit_program(controller), font=persian_font)
        button2.pack(pady=10)

    def continue_to_calc(self, controller):
        controller.geometry("400x350")  # change window size
        controller.frames[CalcPage].set_team(self.team_var.get())
        controller.show_frame(CalcPage)


    def quit_program(self, controller):
        controller.quit()


class CalcPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        persian_font = font.Font(family='Vazirmatn', size=10)

        self.team_label = tk.Label(self, font=persian_font)
        self.team_label.grid(row=0, column=0, columnspan=2)

        tk.Label(self, text=text2, font=persian_font).grid(row=1, column=0, columnspan=2)
        placeholder2 = ".از ۰ تا ۱ مقداری را وارد نمائید"
        self.g_entry = PlaceholderEntry(self, placeholder=placeholder2, font=persian_font, width=30)
        self.g_entry.grid(row=2, column=0, columnspan=2)
        g_tip = ToolTip(self.g_entry)
        hover_guide2 = ".امتیاز برگزاری جلسات روزانه به حضور حداکثری افراد، مشارکت فعال و نظم برگزاری جلسه بستگی دارد"
        self.g_entry.bind('<Enter>', lambda event: g_tip.showtip(hover_guide2))
        self.g_entry.bind('<Leave>', lambda event: g_tip.hidetip())



        tk.Label(self, text=text3, font=persian_font).grid(row=3, column=0, columnspan=2)
        placeholder3 = ".از ۰ تا ۱ مقداری را وارد نمائید"
        self.spr_entry = PlaceholderEntry(self, placeholder=placeholder3, font=persian_font, width=30)
        self.spr_entry.grid(row=4, column=0, columnspan=2)
        spr_tip = ToolTip(self.spr_entry)
        hover_guide3 = "نسبت میزان استوری‌پوینت‌های تعریف شده به حداکثر میزان استوری‌پوینت‌های ممکن در طول اسپرینت "
        self.spr_entry.bind('<Enter>', lambda event: spr_tip.showtip(hover_guide3))
        self.spr_entry.bind('<Leave>', lambda event: spr_tip.hidetip())

        tk.Label(self, text=text4, font=persian_font).grid(row=5, column=0, columnspan=2)
        placeholder4 = ".مقداری بزرگ‌تر از صفر وارد نمائید"
        self.tpr_entry = PlaceholderEntry(self, placeholder=placeholder4, font=persian_font, width=30)
        self.tpr_entry.grid(row=6, column=0, columnspan=2)
        tpr_tip = ToolTip(self.tpr_entry)
        hover_guide4 = "نسبت میزان تسک‌پوینت‌های تکمیل شده به میزان استوری‌پوینت تعریف شده در اسپرینت "
        self.tpr_entry.bind('<Enter>', lambda event: tpr_tip.showtip(hover_guide4))
        self.tpr_entry.bind('<Leave>', lambda event: tpr_tip.hidetip())
        
        
        tk.Frame(self, height=10).grid(row=7)  # Change the height value to adjust the space


        tk.Button(self, text="محاسبه امتیاز", command=self.calculate_score, font=persian_font).grid(row=8, column=0, columnspan=2)
        tk.Frame(self, height=10).grid(row=9)  # Change the height value to adjust the space
        tk.Button(self, text="بازگشت", command=lambda: self.back_home(controller), font=persian_font).grid(row=10, column=0, columnspan=2)
        tk.Frame(self, height=10).grid(row=11)  # Change the height value to adjust the space
        tk.Button(self, text="خروج", command=lambda: self.quit_program(controller), font=persian_font).grid(row=12, column=0, columnspan=2)



    def quit_program(self, controller):
        controller.quit()

    def back_home(self, controller):
        controller.geometry("400x300")  # change window size
        controller.show_frame(StartPage)

    def set_team(self, team):
        persian_bold = font.Font(family='Vazirmatn', size=10, weight="bold")
        self.team = team
        self.team_label.config(text=f"پروژه انتخابی: {self.team}", font=persian_bold)

    def calculate_score(self):
        try:
            g_value = float(self.g_entry.get())
            spr_value = float(self.spr_entry.get())
            tpr_value = float(self.tpr_entry.get())

            if not (0 <= g_value <= 1 and 0 <= spr_value <= 1 and tpr_value >= 0):
                raise ValueError

            # Save data
            if self.team not in data:
                data[self.team] = []
            data[self.team].append((g_value, spr_value, tpr_value))

            score = 10*g_value + 50*spr_value + 40*(1 - abs(1 - tpr_value))
            messagebox.showinfo("امتیاز", f"امتیاز محاسبه شده برای {self.team} برابر است با {score}")

            self.g_entry.delete(0, tk.END)
            self.spr_entry.delete(0, tk.END)
            self.tpr_entry.delete(0, tk.END)

        except ValueError:
            error_desc = "!مقادیر ورودی نامعتبر را اصلاح کنید"
            messagebox.showerror("ورودی غیرمعتبر", error_desc)
            self.g_entry.delete(0, tk.END)
            self.spr_entry.delete(0, tk.END)
            self.tpr_entry.delete(0, tk.END)

app = Application()
logo_path = os.path.abspath(r"path\to\logo.ico") # Change the path value to your desired icon
app.iconbitmap(logo_path)
app.wm_iconbitmap(logo_path)

app.mainloop()




