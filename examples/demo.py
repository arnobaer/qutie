import qutie as ui

app = ui.Application("demo", version="1.0a")
app.display_name=f"Demo {app.version}"
app.icon = 'orange'

tree = ui.Tree(
    header=("Key", "Value")
)

item = tree.append(["Color", "#33cc33"])
item[0].color = "#33cc33"
item[0].icon = "#33cc33"
item.append(["red", 51])[0].icon = 'red'
item.append(["green", 204])[0].icon = 'green'
item.append(["blue", 51])[0].icon = 'blue'

item = tree.append(["checked=0"])
item[0].checked = False
item[0].icon = '#123456'

item = tree.append(["checked=1"])
item[0].checked = True
item[0].icon = '#341256'

item = tree.append(["checkable=0"])
item[0].checkable = False
item[0].icon = 'yellow'
item[0].icon = None

item = tree.append(["checkable=1"])
item[0].checkable = True
item[0].icon = ui.Icon.from_theme('document-open')

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

tree.fit()

table = ui.Table(
    header=("Key", "Value")
)

item = table.append(["green", "spam"])
item[0].color = "green"
item[0].icon = 'blue'

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

table.fit()

list_ = ui.List(
    values=("red",)
)
list_[0].color = "red"

item = list_.append("green")
item.color = "green"
item.icon = ui.Icon.from_color('blue')

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
special_number = ui.Number(special_value='Off', minimum=0, maximum=7)
def reset_special_number():
    special_number.value = special_number.minimum
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
                ui.Row(
                    special_number,
                    ui.Button("&Reset", width=56, clicked=reset_special_number)
                ),
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
            ui.Select(["green", "red", "blue"], current="red"),
            ui.Label("Select, readonly=False"),
            ui.Select(["spam", 42, 4.2, True], current=42, changed=lambda item: ui.show_info(f"Selected: {item} ({type(item).__name__})")),
            ui.Label("Select, editable=True"),
            ui.Select(["green", "red", "blue"], editable=True),
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


def on_preferences():
    def on_click(button):
        if button == 'restore_defaults':
            ui.show_info("Reset to defaults.")
    def on_help():
        ui.show_info("Helpful information.")
    dialog = ui.Dialog(title="Preferences")
    dialog.layout = ui.Column(
        ui.Spacer(),
        ui.Row(
            ui.DialogButtonBox(
                buttons=('restore_defaults', 'close', 'help'),
                accepted=dialog.close,
                rejected=dialog.close,
                clicked=on_click,
                help_requested=on_help,
            )
        )
    )
    dialog.run()

window = ui.MainWindow(
    layout=tabs,
    close_event=lambda: ui.show_question("Quit application?")
)

edit_menu = window.menubar.append("&Edit")
edit_menu.append(ui.Action(
    text="&Preferences",
    triggered=on_preferences
))
abc_menu = edit_menu.append(ui.Menu(
    ui.Action("ABC", separator=True),
    ui.Action("B"),
    ui.Action(separator=True),
    ui.Action("C"),
    text="&More..."
))

file_menu = window.menubar.insert(edit_menu, "&File")
file_menu.append(ui.Action(
    text="&Quit",
    statustip="Quit application",
    shortcut="Ctrl+Q",
    triggered=on_quit
))

window.progress = ui.ProgressBar(0, minimum=0, maximum=len(tabs))
window.statusbar.append(window.progress)

window.show()

settings = ui.Settings()
settings.setdefault('size', (640, 480))
window.resize(*settings.get('size'))
tabs.qt.setCurrentIndex(settings.get('tab', 0, int))

app.run()

settings['size'] = window.size
settings['tab'] = tabs.qt.currentIndex()
