from datetime import datetime
import tkinter
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def collatz_conjecture(n):
    """

    :param n:
    :return:
    """
    sequence = []
    while n > 1 and type(n) == int:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def update_graph():
    """

    """
    try:
        value = int(entry.get())
        sequence = collatz_conjecture(value)
        text_box.delete('1.0', tkinter.END)
        length = len(sequence)
        maximum = max(sequence)
        text_box.insert(tkinter.END, f"{length} steps in total and the maximum number is {maximum}: \n\n")
        for num in sequence:
            text_box.insert(tkinter.END, f'{num}\n')
        ax.cla()
        line_c = ax.plot(range(len(sequence)), sequence, linestyle='-', marker='.', linewidth=0.5)[0]
        ax.relim()
        ax.autoscale_view()
        ax.set_xlabel('n')
        ax.set_ylabel('T(n)')
        ax.legend([line_c], [f'T(1)={entry.get()}'], loc='upper right')
        canvas.draw()
    except ValueError:
        ax.cla()
        line_c = (ax.plot(range(len([])), [], linestyle='-', marker='.', linewidth=0.5, ))[0]
        ax.relim()
        ax.autoscale_view()
        ax.set_xlabel('n')
        ax.set_ylabel('T(n)')
        ax.legend([line_c], [f'T(1)={entry.get()}'], loc='upper right')
        canvas.draw()
        text_box.delete('1.0', tkinter.END)


def on_entry_change(event):
    """

    :param event:
    """
    update_graph()


def validate_input(value):
    """

    :param value:
    :return:
    """
    if value.isdigit() or value == "":
        return True
    else:
        return False


def save_canvas():
    """

    :return:
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = filedialog.asksaveasfilename(defaultextension='.png', initialfile='Canvas_' + timestamp + '.png')
    if not file_path:
        return
    canvas.draw()
    canvas.print_png(file_path)


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
    entry = tkinter.Entry(window, validate='key', validatecommand=(validate_i, '%P'), insertbackground="orange")
    entry.grid(row=0, column=2, columnspan=2, sticky="we")
    button = tkinter.Button(window, text='Save', command=save_canvas)
    button.grid(row=5, column=0, columnspan=4, sticky="we")
    text_box = tkinter.Text(window)
    text_box.grid(row=1, column=0, columnspan=4, rowspan=4, sticky="nsew")
    # style = ttk.Style()
    # style.theme_use("alt")
    # style.configure("TScrollbar")
    scrollbar = ttk.Scrollbar(window, command=text_box.yview)
    scrollbar.configure(command=text_box.yview)
    scrollbar.grid(row=1, column=4, rowspan=4, sticky="ns")
    text_box.configure(width=40, yscrollcommand=scrollbar.set)
    fig, ax = matplotlib.pyplot.subplots()
    line, = ax.plot([], [], 'b-')
    ax.set_xlabel('n')
    ax.set_ylabel('T(n)')
    ax.legend([line], [f'T(1)={entry.get()}'], loc='upper right')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=5, rowspan=6)
    update_graph()
    entry.bind('<KeyRelease>', on_entry_change)
    window.mainloop()
