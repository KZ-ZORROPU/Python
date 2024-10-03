import time
import tkinter
from tkinter import ttk
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def collatz_conjecture(n):
    sequence = [n]
    while n > 1 and type(n) == int:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def update_graph():
    try:
        value = int(entry.get())
        sequence = collatz_conjecture(value)
        text_box.delete('1.0', tkinter.END)
        length = len(sequence)
        maximum = max(sequence)
        text_box.insert(tkinter.END, f'{length} steps in total and the maximum number is {maximum}: \n\n')
        for num in sequence:
            text_box.insert(tkinter.END, f'{num}\n')
        line.set_data(range(len(sequence)), sequence)
        ax.relim()
        ax.autoscale_view()
        ax.set_title(f'Line graph of Collatz Conjecture calculation process for {value}')
        canvas.draw()
    except ValueError:
        line.set_data(range(len([])), [])
        ax.relim()
        ax.autoscale_view()
        canvas.draw()
        text_box.delete('1.0', tkinter.END)


def on_entry_change(event):
    update_graph()


def validate_input(value):
    if value.isdigit() or value == "":
        return True
    else:
        return False


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Collatz Conjecture')
    window.geometry('1000x500')
    window.resizable(False, False)
    window.option_add('*Font', ('Unifont', 12, 'normal'))
    window.iconbitmap('KZ_ZORROPU.ico')

    label = tkinter.Label(window, text='Integer to calculate: ')
    label.grid(row=0, column=0, columnspan=2, sticky='e')

    validate_i = window.register(validate_input)
    entry = tkinter.Entry(window, validate='key', validatecommand=(validate_i, '%P'))
    entry.grid(row=0, column=2, columnspan=2, sticky="we")

    text_box = tkinter.Text(window)
    text_box.configure(font=("Unifont", 11))
    text_box.grid(row=1, column=0, columnspan=4, rowspan=5, sticky="nsew")

    scrollbar = ttk.Scrollbar(window, command=text_box.yview)

    scrollbar.config(command=text_box.yview)
    scrollbar.grid(row=1, column=4, rowspan=5, sticky="ns")

    text_box.config(width=40, yscrollcommand=scrollbar.set)

    fig, ax = matplotlib.pyplot.subplots()
    line, = ax.plot([], [], 'b-')
    ax.set_xlabel('n')
    ax.set_ylabel('T(n)')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=5, rowspan=6)

    update_graph()

    entry.bind('<KeyRelease>', on_entry_change)

    entry.insert(0, str(1))

    time.sleep(5)


    def increase_number():
        current_number = int(entry.get())
        new_number = current_number + 1
        entry.delete(0, tkinter.END)
        entry.insert(0, str(new_number))
        update_graph()
        window.after(1, increase_number)


    # 启动定时器
    window.after(1, increase_number)

    window.mainloop()
