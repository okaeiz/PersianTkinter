import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text...", color='grey', **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.put_placeholder()

        if 'font' in kwargs:
            self.configure(font=kwargs['font'])

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
        self['justify'] = 'right'

    def remove_placeholder(self):
        self.delete(0, tk.END)
        self['fg'] = self.default_fg_color
        self['justify'] = 'left'

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.remove_placeholder()

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

if __name__ == '__main__':
    root = tk.Tk()

    # Create a placeholder entry widget
    entry = PlaceholderEntry(root, placeholder="Enter text...", font=('Arial', 12), width=30)
    entry.pack()

    root.mainloop()