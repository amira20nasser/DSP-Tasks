from ui.ui_widgets import UI
from ui.task1_ui import Task1UI
from ui.task2_ui import Task2UI
from ui.task3_ui import Task3UI
from ui.task4_ui import Task4UI
from ui.task5_ui import Task5UI
from ui.task6_ui import Task6UI
from ui.task7_ui import Task7UI

from logic.fourier_transform import *
from logic.basic_signal_operations import*
def main():
    ui = UI()
    root, notebook = ui.initialize()

    """
    x_n = FourierTransform.idtf_transform([64,20.9050074380220 ,11.3137084989848 ,8.65913760233915 ,8 ,8.65913760233915 ,11.313708498984 ,20.9050074380220],
                                            [0,1.96349540849362,2.35619449019235,2.74889357189107 ,-3.14159265358979,-2.74889357189107,-2.35619449019235,-1.96349540849362]
    )
    """
    #x_k= FourierTransform.dtf_transform([1, 3, 5, 7, 9, 11, 13, 15],8)                                     
    # print(x_n)
    task7_tab = Task7UI(notebook,"Task 7")
    task7_tab.add()


    task5_tab = Task5UI(notebook,"Task 5")
    task5_tab.add()

    task4_tab = Task4UI(notebook,"Task 4")
    task4_tab.add()

    task3_tab = Task3UI(notebook, "Task 3")
    task3_tab.add()

    task2_tab = Task2UI(notebook, "Task 2")
    task2_tab.add()

    task1_tab = Task1UI(notebook, "Task 1")
    task1_tab.add()


    root.mainloop()

main()

