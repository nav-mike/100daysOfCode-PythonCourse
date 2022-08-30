import tkinter


def miles_to_km(miles: int) -> str:
    return f"{miles * 1.60934:.2f}"


def miles_value_handler() -> None:
    km_value_label.config(text=miles_to_km(int(miles_entry.get())))


window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.maxsize(width=250, height=150)
window.config(padx=20, pady=20)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_value_label = tkinter.Label(text="0", pady=20)
km_value_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=miles_value_handler)
button.grid(row=2, column=1)

window.mainloop()
