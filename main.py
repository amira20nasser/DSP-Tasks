
from ui.ui_widgets import UI
from ui.task1_ui import Task1UI
from ui.task2_ui import Task2UI

def main():
    ui = UI()
    root, notebook = ui.initialize()

    task1_tab = Task1UI(notebook, "Task 1")
    task1_tab.add()

    task2_tab = Task2UI(notebook, "Task 2")
    task2_tab.add()

    root.mainloop()

main()

