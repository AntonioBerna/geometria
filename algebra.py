from tkinter import *
import numpy as np
from sympy import *


class LinearAlgebra:
    def __init__(self, root):
        self.root = root
        self.root.title("Algebra Lineare v3.0")
        self.root.geometry("700x700")

        # UP Frame
        self.up_frame = Frame(self.root)
        self.up_frame.pack(pady=10)

        self.rows_label = Label(self.up_frame, text="Righe", font=("Cascadia Code", 15))
        self.rows_label.grid(row=0, column=0)

        self.rows_entry = Entry(self.up_frame, width=5, font=("Cascadia Code", 15))
        self.rows_entry.grid(row=0, column=1)
        
        self.cols_label = Label(self.up_frame, text="Colonne", font=("Cascadia Code", 15))
        self.cols_label.grid(row=0, column=2)

        self.cols_entry = Entry(self.up_frame, width=5, font=("Cascadia Code", 15))
        self.cols_entry.grid(row=0, column=3)

        self.create_matrix_button = Button(
            self.up_frame,
            text="Crea",
            font=("Cascadia Code", 15),
            command=self.createEntries
        )
        self.create_matrix_button.grid(row=0, column=4)

        self.clear_matrix_button = Button(
            self.up_frame,
            text="Pulisci",
            font=("Cascadia Code", 15),
            command=self.clearEntries
        )
        self.clear_matrix_button.grid(row=0, column=5)

        # Matrix Frame
        self.matrix_frame = Frame(self.root)
        self.matrix_frame.pack(pady=10)

        # Buttons Frame
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=10)

        self.det_button = Button(
            self.button_frame,
            text="det",
            font=("Cascadia Code", 15),
            command=self.getDetMatrix
        )
        self.det_button.grid(row=0, column=0)

        self.rank_button = Button(
            self.button_frame,
            text="rk",
            font=("Cascadia Code", 15),
            command=self.getRankMatrix
        )
        self.rank_button.grid(row=0, column=1)

        self.inverse_button = Button(
            self.button_frame,
            text="inv",
            font=("Cascadia Code", 15),
            command=self.getInverseMatrix
        )
        self.inverse_button.grid(row=0, column=2)

        self.jordan_button = Button(
            self.button_frame,
            text="J",
            font=("Cascadia Code", 15),
            command=self.getJordanMatrix
        )
        self.jordan_button.grid(row=0, column=3)

        self.ker_im_button = Button(
            self.button_frame,
            text="ker",
            font=("Cascadia Code", 15),
            command=self.getKerIm
        )
        self.ker_im_button.grid(row=0, column=4)

        self.diagonal_button = Button(
            self.button_frame,
            text="diag",
            font=("Cascadia Code", 15),
            command=self.getDiagonal
        )
        self.diagonal_button.grid(row=0, column=5)

        self.T_button = Button(
            self.button_frame,
            text="T",
            font=("Cascadia Code", 15),
            command=self.getTranspose
        )
        self.T_button.grid(row=0, column=6)

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
        for widgets in self.matrix_frame.winfo_children():
            widgets.destroy()
    
    def createEntries(self):
        self.text.delete(1.0, END)

        if self.rows_entry.get() != "" and self.cols_entry.get() != "":
            self.rows = int(self.rows_entry.get())
            self.cols = int(self.cols_entry.get())

            self.deleteEntries()
        
            self.list_obj_components = []
            if self.rows > 0 and self.cols > 0:
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        e = Entry(self.matrix_frame, width=2, font=("Cascadia Code", 15))
                        e.grid(row=i, column=j)
                        self.list_obj_components.append(e)
            else:
                self.text.insert(END, "A chicco te devi da na svegliata!")
        else:
            self.text.insert(END, "A chicco te devi da na svegliata!")
    
    def makeMatrix(self):
        k = symbols("k")
        matrix_components = []
        for obj in self.list_obj_components:
            if "k" in obj.get():
                matrix_components.append(obj.get())
            else:
                matrix_components.append(float(obj.get()))
        
        array = np.array(matrix_components)
        self.matrix = np.reshape(array, (self.rows, self.cols))
    
    def clearEntries(self):
        self.rows_entry.delete(0, END)
        self.cols_entry.delete(0, END)
        self.text.delete(1.0, END)
        self.deleteEntries()
    
    def getDetMatrix(self):
        self.text.delete(1.0, END)
        self.makeMatrix()
        m = Matrix(self.matrix)
        if self.rows == self.cols:
            self.text.insert(END, f"det(M) = {round(float(m.det()), 2)}")
        else:
            self.text.insert(END, "La matrice inserita non è quadrata!")
    
    def getRankMatrix(self):
        self.text.delete(1.0, END)
        self.makeMatrix()
        m = Matrix(self.matrix)
        self.text.insert(END, f"Matrice a Scala:\n\nM =\n{pretty(nsimplify(m.echelon_form(), rational=True))}\n\nrk(M) = {m.rank()}")

    def getInverseMatrix(self):
        self.text.delete(1.0, END)
        if self.rows == self.cols:
            self.makeMatrix()
            m = Matrix(self.matrix)
            if round(float(m.det()), 2) != 0:
                self.text.insert(END, f"Matrice Inversa:\n\ninv(M) =\n{pretty(nsimplify(m.inv(), rational=True))}")
            else:
                self.text.insert(END, f"Dato che det(M) = {round(float(m.det()), 2)}, la matrice non è invertibile!")
        else:
            self.text.insert(END, "La matrice inserita non è quadrata!")
    
    def getJordanMatrix(self):
        self.text.delete(1.0, END)
        if self.rows == self.cols:
            self.makeMatrix()
            t = symbols("t")
            m = Matrix(self.matrix)
            P, J = m.jordan_form()
            Jt = J * t
            self.text.insert(END, f"J =\n{pretty(nsimplify(J, rational=True))}\n\nP =\n{pretty(nsimplify(P, rational=True))}\n\ninv(P) =\n{pretty(nsimplify(P.inv(), rational=True))}\n\ne^Jt = \n{pretty(nsimplify(Jt.exp(), rational=True))}\n\nP * e^Jt * inv(P) = \n{pretty(nsimplify(P * Jt.exp() * P.inv(), rational=True))}")
        else:
            self.text.insert(END, "La matrice inserita non è quadrata!")
    
    def getKerIm(self):
        self.text.delete(1.0, END)
        self.makeMatrix()
        m = Matrix(self.matrix)
        self.text.insert(END, f"ker(f) = Span\n{pretty(nsimplify(m.nullspace(), rational=True))}\n\nIm(f) = Span\n{pretty(nsimplify(m.columnspace(), rational=True))}")

    def getDiagonal(self):
        self.text.delete(1.0, END)
        if self.rows == self.cols:
            self.makeMatrix()
            t = symbols("t")
            m = Matrix(self.matrix)
            P, J = m.jordan_form()
            self.text.insert(END, f"p(t) = \n{pretty(factor(nsimplify(m.charpoly(t).as_expr(), rational=True)))}\n\nP =\n{pretty(nsimplify(P, rational=True))}\n\nD =\n{pretty(nsimplify(J, rational=True))}")
        else:
            self.text.insert(END, "La matrice inserita non è quadrata!")
    
    def getTranspose(self):
        self.text.delete(1.0, END)
        self.makeMatrix()
        m = Matrix(self.matrix)
        self.text.insert(END, f"M^T = \n{pretty(nsimplify(m.T, rational=True))}")


if __name__ == '__main__':
    root = Tk()
    LinearAlgebra(root)
    root.mainloop()