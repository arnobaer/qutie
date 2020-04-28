import qutie as ui

app = ui.Application(__name__)

tree = ui.Tree(
    header=("Key", "Value")
)

item = tree.append(["green", "#33cc33"])
item[0].color = "#33cc33"
item.append(["r", 51])
item.append(["g", 204])
item.append(["b", 51])

item = tree.append(["checked=0"])
item[0].checked = False

item = tree.append(["checked=1"])
item[0].checked = True

item = tree.append(["checkable=0"])
item[0].checkable = False

item = tree.append(["checkable=1"])
item[0].checkable = True

item = tree.append(["checkable=0", "checked=0"])
item[0].checkable = False
item[0].checked = False

item = tree.append(["checkable=1", "checked=0"])
item[0].checkable = True
item[0].checked = False

item = tree.append(["checkable=0", "checked=1"])
item[0].checkable = False
item[0].checked = True

item = tree.append(["checkable=1", "checked=1"])
item[0].checkable = True
item[0].checked = True

table = ui.Table(
    header=("Key", "Value")
)

item = table.append(["green", "spam"])
item[0].color = "green"

item = table.append(["checked=0"])
item[0].checked = False

item = table.append(["checked=1"])
item[0].checked = True

item = table.append(["checkable=0"])
item[0].checkable = False

item = table.append(["checkable=1"])
item[0].checkable = True

item = table.append(["checkable=0", "checked=0"])
item[0].checkable = False
item[0].checked = False

item = table.append(["checkable=1", "checked=0"])
item[0].checkable = True
item[0].checked = False

item = table.append(["checkable=0", "checked=1"])
item[0].checkable = False
item[0].checked = True

item = table.append(["checkable=1", "checked=1"])
item[0].checkable = True
item[0].checked = True

list_ = ui.List(
    values=("red",)
)
list_[0].color = "red"

item = list_.append("green")
item.color = "green"

item = list_.append("checked=0")
item.checked = False

item = list_.append("checked=1")
item.checked = True

item = list_.append("checkable=0")
item.checkable = False

item = list_.append("checkable=1")
item.checkable = True

item = list_.append("checkable=0, checked=0")
item.checkable = False
item.checked = False

item = list_.append("checkable=1, checked=0")
item.checkable = True
item.checked = False

item = list_.append("checkable=0, checked=1")
item.checkable = False
item.checked = True

item = list_.append("checkable=1, checked=1")
item.checkable = True
item.checked = True

tabs = ui.Tabs(
    ui.Tab(
        title="Tree",
        layout=tree
    ),
    ui.Tab(
        title="Table",
        layout=table
    ),
)
tabs.append(ui.Tab(
    title="List",
    layout=list_
))
tabs.append(ui.Tab(
    title="Numbers",
    layout=ui.ScrollArea(
        layout=ui.Row(
            ui.Column(
                ui.Label("Unbound"),
                ui.Number(),
                ui.Label("Unbound, decimals=1"),
                ui.Number(42, decimals=1),
                ui.Label("Unbound, decimals=3, step=.01"),
                ui.Number(.042, decimals=3, step=.01),
                ui.Label("Unbound, decimals=3, adaptive=True"),
                ui.Number(.042, decimals=3, adaptive=True),
                ui.Label("0...3, value=1"),
                ui.Number(1, minimum=0, maximum=3),
                ui.Label("0...7, special_value='Off'"),
                ui.Number(special_value='Off', minimum=0, maximum=7),
                ui.Label("readonly"),
                ui.Number(42, readonly=True),
                ui.Label("readonly, styled"),
                ui.Number(42, readonly=True, stylesheet="color: red; background: #eee"),
                ui.Spacer(),
            ),
            ui.Spacer(),
            stretch=(3, 7)
        )
    )
))
tabs.insert(-1, ui.Tab(
    title="Text",
    layout=ui.Column(
        ui.Label("Text, clearable"),
        ui.Text("Lorem ipsum et dolor.", clearable=True),
        ui.Label("Text, readonly, styled"),
        ui.Text("Lorem ipsum et dolor.", readonly=True, stylesheet="color: red"),
        ui.Label("Text Area"),
        ui.TextArea("Lorem ipsum et dolor.")
    )
))
tabs.append(ui.Tab(
    title="Select",
    layout=ui.Row(
        ui.Column(
            ui.Label("Select, current='red'"),
            ui.Select(["green", "red", "blue"], current='red'),
            ui.Label("Select, readonly=False"),
            ui.Select(["Item"], readonly=False),
            ui.Spacer()
        ),
        ui.Spacer(),
        stretch=(3, 7)
    )
))

def on_tab_changed(index):
    window.progress.value = index + 1
tabs.changed = on_tab_changed

def on_quit():
    if ui.show_question("Quit application?"):
        app.quit()

window = ui.MainWindow(
    title="Main Window",
    layout=tabs
)
file_menu = window.menubar.append("&File")
file_menu.append_action(ui.Action(
    text="&Quit",
    tooltip="Quit application",
    shortcut="Ctrl+Q",
    triggered=on_quit
))

window.progress = ui.ProgressBar(0, minimum=0, maximum=len(tabs))
window.statusbar.append(window.progress)

window.resize(800, 600)
window.show()

app.run()
