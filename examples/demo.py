import itertools
import logging
import random
import time

import qutie as ui

class NumbersTab(ui.Tab):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.special_number = ui.Number(special_value='Off', minimum=0, maximum=7)
        self.scroll_area = ui.ScrollArea(
            layout=ui.Row(
                ui.Column(
                    ui.Label("Unbound"),
                    ui.Number(editing_finished=lambda: ui.show_info("Editing finished.")),
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
                        self.special_number,
                        ui.Button("&Reset", width=56, clicked=self.on_reset)
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
        self.layout = self.scroll_area

    def on_reset(self):
        self.special_number.value = self.special_number.minimum

class TextTab(ui.Tab):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = ui.Column(
            ui.Label("Text, clearable"),
            ui.Text("Lorem ipsum et dolor.", clearable=True),
            ui.Label("Text, readonly, styled"),
            ui.Text("Lorem ipsum et dolor.", readonly=True, stylesheet="color: red"),
            ui.Label("Text Area"),
            ui.TextArea("Lorem ipsum et dolor.")
        )

class SelectTab(ui.Tab):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = ui.Row(
            ui.Column(
                ui.Label("Select, current='red'"),
                ui.ComboBox(["green", "red", "blue"], current="red"),
                ui.Label("Select, readonly=False"),
                ui.ComboBox(["spam", 42, 4.2, True], current=42, changed=self.on_changed),
                ui.Label("Select, editable=True"),
                ui.ComboBox(["green", "red", "blue"], editable=True),
                ui.Spacer()
            ),
            ui.Spacer(),
            stretch=(3, 7)
        )

    def on_changed(self, item):
        ui.show_info(f"Selected: {item} ({type(item).__name__})")

class ExclusiveTab(ui.Tab):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = ui.Row(
            ui.GroupBox(
                title="Exclusive 1",
                layout=ui.Column(
                    ui.RadioButton("First"),
                    ui.RadioButton("Second", checked=True),
                    ui.RadioButton("Third"),
                    ui.Spacer()
                )
            ),
            ui.GroupBox(
                title="Exclusive 2",
                layout=ui.Column(
                    ui.RadioButton("Red", icon='red'),
                    ui.RadioButton("Blue", icon='blue', checked=True),
                    ui.RadioButton("Green", icon='green', enabled=False),
                    ui.Spacer()
                )
            )
        )

class StackTab(ui.Tab):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = ui.List(selected=self.on_selected)
        self.stack = ui.Stack()
        self.layout = ui.Row(
            self.list,
            self.stack,
            stretch=(2, 5)
        )
        # Add pages
        self.add_item(ui.GroupBox("First", layout=ui.Column(
            ui.Label("Name"),
            ui.Text("Lorem ipsum"),
            ui.Spacer()
        )))
        self.add_item(ui.GroupBox("Second", layout=ui.Column(
            ui.ComboBox(["red", "green", "blue"]),
            ui.Spacer()
        )))
        self.add_item(ui.GroupBox("Third", layout=ui.Column(
            ui.TextArea("Lorem ipsum et dolor.", readonly=True),
            ui.Spacer()
        )))
        self.list.current = self.list[1]

    def add_item(self, item):
        self.list.append(item.title).ref = item
        self.stack.append(item)

    def on_selected(self, item, index):
        self.stack.current = item.ref

def main():
    app = ui.Application("demo", version="1.0a", organization="acme")
    app.display_name=f"Demo {app.version}"
    app.icon = 'orange'

    tree = ui.Tree(
        header=("Key", "Value")
    )

    item = tree.append(["Color", "#33cc33"])
    item[0].color = "#33cc33"
    item[0].background = "yellow"
    item[0].icon = "#33cc33"
    item.append(["red", 51])[0].icon = 'red'
    item.append(["green", 204])[0].icon = 'green'
    item.append(["blue", 51])[0].icon = 'blue'

    # Install blinking item background usign a timer
    colors = itertools.cycle(["yellow", "orange"])
    def toggle_color():
        tree[0][0].background = next(colors)
    timer = ui.Timer(interval=0.5, timeout=toggle_color)
    timer.start()

    item = tree.append(["checked=0"])
    item[0].checked = False
    item[0].icon = '#123456'

    item = tree.append(["checked=1"])
    item[0].checked = True
    item[0].icon = '#341256'

    item = tree.append(["checkable=0"])
    item.checkable = False
    item[0].icon = 'yellow'
    item[0].icon = None

    item = tree.append(["checkable=1"])
    item.checkable = True
    item[0].icon = ui.Icon.from_theme('document-open')

    item = tree.append(["checkable=0", "checked=0"])
    item.checkable = False
    item[0].checked = False

    item = tree.append(["checkable=1", "checked=0"])
    item.checkable = True
    item[0].checked = False

    item = tree.append(["checkable=0", "checked=1"])
    item.checkable = False
    item[0].checked = True

    item = tree.append(["checkable=1", "checked=1"])
    item.checkable = True
    item[0].checked = True

    tree.current = tree[3]
    tree.fit()

    table = ui.Table(
        header=("Key", "Value")
    )

    item = table.append(["green", "spam"])
    item[0].color = "green"
    item[0].background = "yellow"
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

    table.current = table[3][0]
    table.fit()

    list_ = ui.List(
        items=("red",)
    )
    list_[0].color = "red"

    item = list_.append("green")
    item.color = "green"
    item.background = "yellow"
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
    splitter = ui.Splitter(
        list_,
        ui.Label("Aside")
    )
    splitter.sizes = [3, 2]
    splitter.handle_width = 1
    tabs.append(ui.Tab(
        title="List",
        layout=splitter
    ))
    tabs.append(NumbersTab(title="Numbers"))
    tabs.insert(-1, TextTab(title="Text"))
    tabs.append(SelectTab(title="Select"))
    tabs.append(ExclusiveTab(title="Exclusive"))
    tabs.insert(-1, StackTab(title="Stack"))

    def on_tab_changed(index):
        window.progress.value = index + 1
    tabs.changed = on_tab_changed

    def on_quit():
        if ui.show_question("Quit application?"):
            app.quit()


    def on_preferences():
        defaults = ["Apples", "Pears", "Nuts"]
        def on_click(button):
            if button == 'restore_defaults':
                item_list.items = defaults
                ui.show_info("Reset to defaults.")
        def on_help():
            ui.show_info("Helpful information.")
        def on_add():
            item = ui.get_item(defaults)
            if item:
                item_list.append(item)
        def on_remove():
            item = item_list.current
            item_list.remove(item)
        def on_edit(index, item):
            value = ui.get_text(item.value, title="Item", label="Edit item")
            if value is not None:
                item.value = value
        dialog = ui.Dialog(title="Preferences")
        item_list = ui.List()
        item_list.double_clicked = on_edit
        add_button = ui.Button("&Add", clicked=on_add)
        remove_button = ui.Button("&Del", clicked=on_remove)
        dialog.layout = ui.Column(
            ui.Row(
                item_list,
                ui.Column(
                    add_button,
                    remove_button,
                    ui.Spacer()
                ),
                stretch=(1,0)
            ),
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
        # Load settings
        with ui.Settings() as settings:
            item_list.items = settings.setdefault("items", defaults)
        dialog.run()
        # Store settings
        with ui.Settings() as settings:
            settings["items"] = [item.value for item in item_list.items]

    window = ui.MainWindow(
        layout=tabs
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
        status_tip="Quit application",
        shortcut="Ctrl+Q",
        triggered=on_quit
    ))

    window.progress = ui.ProgressBar(0, minimum=0, maximum=len(tabs))
    window.statusbar.append(window.progress)

    window.progress2 = ui.ProgressBar(0, minimum=0, maximum=100)
    window.statusbar.append(window.progress2)

    window.message = ui.Label()
    window.statusbar.append(window.message)


    window.show()

    def on_run(worker):
        value = 0.0
        logging.info("worker:started")
        while not worker.stopping:
            worker.emit('progress', value)
            worker.emit('message', f"about {value:.1f} %")
            worker.set('reading', value)
            worker.emit('reading_available')
            value += random.random()
            time.sleep(random.random())
            if value >= 100.0:
                value = 0.0
        logging.info("worker:finished")

    def on_finished():
        print("DONE")
        ui.show_info("Worker finished.")

    def on_failed(e):
        ui.show_exception(e)

    worker = ui.Worker(target=on_run, finished=on_finished, failed=on_failed)
    def on_progress(value):
        window.progress2.value = value
    worker.progress = on_progress
    def on_message(text):
        window.message.text = text
    worker.message = on_message
    def on_reading_available():
        value = worker.get('reading')
        print("reading:", value)
    worker.reading_available = on_reading_available
    worker.start()

    def on_window_close():
        result = ui.show_question("Quit application?")
        if result:
            worker.stop()
            worker.join()
        return result
    window.close_event = on_window_close

    with ui.Settings() as settings:
        settings.setdefault('window/size', (640, 480))
        window.resize(*settings.get('window/size'))
        position = settings.setdefault('window/position', None)
        if position:
            window.move(*position)
        window.maximized = settings.setdefault('window/maximized', False)
        tabs.current = tabs[settings.get('window/tab', 0)]

    w = ui.Widget(title="Window")
    def show_alert(message):
        ui.show_warning(text=message, title="Alert")
    w.alert = show_alert
    w.layout = ui.Button("Trigger Alert", clicked=lambda: w.emit('alert', random.choice(["Alert!", "This is not an exercise!"])))
    w.modal = True # workaround to keep window in front
    w.show()

    app.run()
    worker.stop()
    with ui.Settings() as settings:
        if not window.maximized:
            settings['window/size'] = window.size
            settings['window/position'] = window.position
        settings['window/maximized'] = window.maximized
        settings['window/tab'] = tabs.index(tabs.current)
    worker.join()

if __name__ == '__main__':
    main()
