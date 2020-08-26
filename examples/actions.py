import qutie as ui

app = ui.Application()

window = ui.MainWindow(title="Actions")
window.resize(800, 600)
window.show()

quit_action = ui.Action("&Quit", triggered=window.close)
file_menu = window.menubar.append("&File")
file_menu.append(quit_action)

ods_import = ui.Action("&ODS")

import_menu = file_menu.insert(
    file_menu.index(quit_action),
    ui.Menu(
        "&CSV",
        text="&Import"
    )
)
import_menu.insert(0, ods_import)

edit_menu = window.menubar.append("&Edit")
first_menu = edit_menu.append(ui.Menu(text="&First"))
second_menu = first_menu.append(ui.Menu(text="&Second"))
action = second_menu.insert(0, "&Go!")
foo_menu = edit_menu.append(ui.Menu(
    ui.Menu(
        ui.Action("Baz"),
        text="Bar"
    ),
    ui.Action("Spam", checkable=True),
    text="Foo"
))

fish_action = ui.Action("&Fish", checkable=True, checked=True)
chips_action = ui.Action("&Chips", checkable=True)
foo_menu.insert(1, fish_action)
foo_menu.insert(2, chips_action)
foo_menu.insert(3, "----")


from PyQt5 import QtWidgets
group = QtWidgets.QActionGroup(foo_menu.qt)
group.addAction(fish_action.qt)
group.addAction(chips_action.qt)

main_toolbar = window.toolbars.add("main")
for action in foo_menu:
    main_toolbar.append(action)

app.run()
