from tkinter import *
from sympy import *


class LinearAndNonLinearSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear And Non Linear System")
        self.root.geometry("700x600")

        # UP Frame
        self.up_frame = Frame(self.root)
        self.up_frame.pack(pady=10)

        self.n_equations_label = Label(self.up_frame, text="Equazioni", font=("Cascadia Code", 15))
        self.n_equations_label.grid(row=0, column=0)

        self.n_equations_entry = Entry(self.up_frame, width=2, font=("Cascadia Code", 15))
        self.n_equations_entry.grid(row=0, column=1)
        
        self.n_variables_label = Label(self.up_frame, text="Incognite", font=("Cascadia Code", 15))
        self.n_variables_label.grid(row=0, column=2)

        self.n_variables_entry = Entry(self.up_frame, width=2, font=("Cascadia Code", 15))
        self.n_variables_entry.grid(row=0, column=3)

        self.create_equations_button = Button(
            self.up_frame,
            text="Crea",
            font=("Cascadia Code", 15),
            command=self.createEntries
        )
        self.create_equations_button.grid(row=0, column=4)

        self.clear_equations_button = Button(
            self.up_frame,
            text="Pulisci",
            font=("Cascadia Code", 15),
            command=self.clearEntries
        )
        self.clear_equations_button.grid(row=0, column=5)

        # Equations Frame
        self.equations_frame = Frame(self.root)
        self.equations_frame.pack(pady=10)

        # Buttons Frame
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=10)

        self.solve_system_button = Button(
            self.button_frame,
            text="Risolvi",
            font=("Cascadia Code", 15),
            command=self.solveSystem
        )
        self.solve_system_button.grid(row=0, column=0)

        # Text Frame
        self.text_frame = Frame(self.root)
        self.text_frame.pack(pady=10, expand=True, fill=BOTH)

        self.text = Text(
            self.text_frame,
            bg="#fff",
            fg="#000",
            font=("Cascadia Code", 20),
            selectbackground="orange",
            selectforeground="black",
            highlightthickness=0,
            borderwidth=0
        )
        self.text.pack(expand=True, fill=BOTH)
    
    def deleteEntries(self):
        for widgets in self.equations_frame.winfo_children():
            widgets.destroy()

    def createEntries(self):
        self.text.delete(1.0, END)

        if self.n_equations_entry.get() != "" and self.n_variables_entry.get() != "":
            self.n_equations = int(self.n_equations_entry.get())
            self.n_variables = int(self.n_variables_entry.get())

            self.deleteEntries()
        
            self.list_obj_components = []
            if self.n_equations > 0 and self.n_variables > 0:
                for i in range(0, self.n_equations):
                    e = Entry(self.equations_frame, width=50, font=("Cascadia Code", 15))
                    e.grid(row=i, column=0)
                    l = Label(self.equations_frame, text="= 0", font=("Cascadia Code", 15))
                    l.grid(row=i, column=1)
                    self.list_obj_components.append(e)
            else:
                self.text.insert(END, "A chicco te devi da na svegliata!")
        else:
            self.text.insert(END, "A chicco te devi da na svegliata!")
    
    def clearEntries(self):
        self.n_equations_entry.delete(0, END)
        self.n_variables_entry.delete(0, END)
        self.text.delete(1.0, END)
        self.deleteEntries()
    
    def solveSystem(self):
        self.text.delete(1.0, END)

        x, y, z, t, w, k = symbols("x, y, z, t, w, k")
        system = []
        for obj in self.list_obj_components:
            system.append(obj.get())

        variables = [x, y, z, t, w]
        v = []
        for i in range(0, self.n_variables):
            v.append(variables[i])

        self.text.insert(END, f"Soluzione generale del sistema:\n\n{pretty(nsimplify(linsolve(system, v), rational=True))}")


if __name__ == '__main__':
    root = Tk()
    LinearAndNonLinearSystem(root)
    root.mainloop()