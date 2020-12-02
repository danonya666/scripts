import tkinter
from math import cos, sin, radians

from scipy import optimize


def deg_sin(degs):
    return sin(radians(degs))


def deg_cos(degs):
    return cos(radians(degs))


fields_for_straight_task = ('X', 'Y', 'X0', 'Y0', 'α', 't')
fields_for_inverted_task = (str(x) for x in range(10))
labels = ('n', 'alfa', 't', 'x0', 'y0')
inverted_results = ('x02', 'y02', 'alpha2', 't2')


def monthly_payment(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n = float(entries['Number of Payments'].get())
    remaining_loan = float(entries['Remaining Loan'].get())
    q = (1 + r) ** n
    monthly = r * ((q * loan - remaining_loan) / (q - 1))
    monthly = ("%8.2f" % monthly).strip()
    entries['Monthly Payment'].delete(0, tkinter.END)
    entries['Monthly Payment'].insert(0, monthly)
    print("Monthly Payment: %f" % float(monthly))


def final_balance(entries):
    # period rate:

    x = float(entries['X'].get())
    y = float(entries['Y'].get())
    x0 = float(entries['X0'].get())
    y0 = float(entries['Y0'].get())
    alpha = float(entries['α'].get())
    t = float(entries['t'].get())

    result1 = x0 + x * t * deg_cos(alpha) - y * t * deg_sin(alpha)
    result2 = y0 + x * t * deg_sin(alpha) + y * t * deg_cos(alpha)
    entries['result1'].insert(0, round(result1, 2))
    entries['result2'].insert(0, round(result2, 2))


def handle_inverted(f):
    return optimize.minimize(f)


def makeform(root, fields):
    entries = {}
    ent0 = tkinter.Label(root, text="КООРДИНАТЫ", font='Helvetica 18 bold')
    ent0.pack(expand=tkinter.YES, fill=tkinter.X)

    с = 0
    for field in fields:
        row = tkinter.Frame(root)
        lab = tkinter.Label(row, width=22, text=field + ": ", anchor='w')
        ent = tkinter.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        lab.pack(side=tkinter.LEFT)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
        entries[field] = ent
        с += 1
        if с == 2:
            ent0 = tkinter.Label(root, text="ПАРАМЕТРЫ ПЕРЕХОДОВ", font='Helvetica 18 bold')
            ent0.pack(expand=tkinter.YES, fill=tkinter.X)

    ent0 = tkinter.Label(root, text="КООРДИНАТЫ В ДРУГОЙ СИСТЕМЕ (x, y):", font='Helvetica 18 bold')
    ent0.pack(expand=tkinter.YES, fill=tkinter.X)
    row = tkinter.Frame(root)
    row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

    ent = tkinter.Entry(row)
    ent.insert(0, "0")
    ent.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.X)
    ent2 = tkinter.Entry(row)
    ent2.insert(0, "0")
    ent2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
    entries["result1"] = ent
    entries["result2"] = ent2

    return entries


def make_2_column_form(root, fields):
    entries = {}
    ent0 = tkinter.Label(root, text="ПЕРВАЯ СИСТЕМА КООРДИНАТ (x, y)", font='Helvetica 18 bold')
    ent0.pack(expand=tkinter.YES, fill=tkinter.X)
    c = 0
    for field in fields:
        row = tkinter.Frame(root)
        # lab = tkinter.Label(row, width=22, text=field + ": ", anchor='w')
        ent3 = tkinter.Label(root, text="x                                y")
        ent = tkinter.Entry(row)
        ent2 = tkinter.Entry(row)
        ent.insert(0, "0")
        ent2.insert(0, "0")
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        # lab.pack(side=tkinter.LEFT)
        # ent3.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.N)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        ent2.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        entries[field] = ent
        entries[f'{field}2'] = ent2
        c += 1
        if c == 5:
            ent0 = tkinter.Label(root, text="ВТОРАЯ СИСТЕМА КООРДИНАТ (x, y)", font='Helvetica 18 bold')
            ent0.pack(expand=tkinter.YES, fill=tkinter.X)

    ent0 = tkinter.Label(root, text="ПАРАМЕТРЫ ПЕРЕХОДА", font='Helvetica 18 bold')
    ent0.pack(expand=tkinter.YES, fill=tkinter.X)
    for i in range(5):
        row = tkinter.Frame(root)
        # lab = tkinter.Label(row, width=22, text=field + ": ", anchor='w')
        ent3 = tkinter.Label(root, text="x                                y")
        ent = tkinter.Entry(row)
        ent2 = tkinter.Label(row, text=labels[i])
        ent.insert(0, "0")
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        # lab.pack(side=tkinter.LEFT)
        # ent3.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.N)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        ent2.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        entries[f'ass{i}'] = ent

    ent0 = tkinter.Label(root, text="РЕЗУЛЬТАТ", font='Helvetica 18 bold')
    ent0.pack(expand=tkinter.YES, fill=tkinter.X)

    for i in range(4):
        row = tkinter.Frame(root)
        # lab = tkinter.Label(row, width=22, text=field + ": ", anchor='w')
        ent3 = tkinter.Label(root, text="x                                y")
        ent = tkinter.Entry(row)
        ent2 = tkinter.Label(row, text=inverted_results[i])
        ent.insert(0, "0")
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        # lab.pack(side=tkinter.LEFT)
        # ent3.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.N)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        ent2.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.X, anchor=tkinter.S)
        entries[f'invres{i}'] = ent
    return entries


def inverted_task():
    root = tkinter.Tk()
    root.title("ОБРАТНАЯ ЗАДАЧА")
    ents = make_2_column_form(root, fields_for_inverted_task)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    def inverted_solver(p: list):
        xcl = [float(ents[f'{str(x)}'].get()) for x in range(5)]
        ycl = [float(ents[f'{str(x)}2'].get()) for x in range(5)]
        xgl = [float(ents[f'{str(x)}'].get()) for x in range(5, 10)]
        ygl = [float(ents[f'{str(x)}2'].get()) for x in range(5, 10)]
        s = 0
        n = 5
        alpha = p[0]
        t = p[1]
        x0 = p[2]
        y0 = p[3]
        for i in range(len(xcl)):
            xc = xcl[i]
            yc = ycl[i]
            xg = xgl[i]
            yg = ygl[i]
            s += xc - (x0 + xc * t * cos(alpha) - yc * t * sin(alpha)) ** 2 + (yc - (y0 + xc * t * sin(alpha) + yc * t * cos(alpha))) ** 2

        return s

    def minim(params, entries):
        xcl = [float(ents[f'{str(x)}'].get()) for x in range(5)]
        ycl = [float(ents[f'{str(x)}2'].get()) for x in range(5)]
        xgl = [float(ents[f'{str(x)}'].get()) for x in range(5, 10)]
        ygl = [float(ents[f'{str(x)}2'].get()) for x in range(5, 10)]
        res = optimize.minimize(inverted_solver, x0=params).x
        print('MINIMIZED: ', res)
        entries['invres0'].insert(0, round(res[0], 2))
        entries['invres1'].insert(0, round(res[1], 2))
        entries['invres2'].insert(0, round(res[2], 2))
        entries['invres3'].insert(0, round(res[3], 2))

    params = [float(ents[f'ass{x}'].get()) for x in range(1, 5)]
    b1 = tkinter.Button(root, text=BUTTON1_TEXT,
                        command=(lambda e=ents: minim(params, ents)))
    b1.pack(side=tkinter.LEFT, padx=5, pady=5)
    b3 = tkinter.Button(root, text='ВЫХОД', command=root.quit)
    b3.pack(side=tkinter.LEFT, padx=5, pady=5)

    root.mainloop()


LABEL_TEXT = "Прямая задача"

BUTTON1_TEXT = "РЕШЕНИЕ"
BUTTON2_TEXT = "ОБРАТНАЯ ЗАДАЧА"

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("ПРЯМАЯ ЗАДАЧА")
    ents = makeform(root, fields_for_straight_task)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b1 = tkinter.Button(root, text=BUTTON1_TEXT,
                        command=(lambda e=ents: final_balance(e)), fg='black', bg='white')
    b1.pack(side=tkinter.LEFT, padx=5, pady=5)
    b2 = tkinter.Button(root, text=BUTTON2_TEXT,
                        command=(lambda e=ents: inverted_task()), fg='black', bg='white')
    b2.pack(side=tkinter.LEFT, padx=5, pady=5)
    b3 = tkinter.Button(root, text='ВЫХОД', command=root.quit, fg='black', bg='white')
    b3.pack(side=tkinter.LEFT, padx=5, pady=5)

    root.mainloop()
