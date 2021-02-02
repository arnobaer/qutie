import qutie as ui
from qutie.qutie import Qt

app = ui.Application()

exclusive_group = ui.GroupBox(
    title="Exclusive",
    cursor='forbidden',
    layout=ui.Column(
        ui.Button("A", checkable=True),
        ui.PushButton("B", checkable=True, icon='red'),
        ui.ToolButton("C", checkable=True, arrow_type='no'),
        ui.ToolButton("D", checkable=True, arrow_type='left')
    )
)
g = ui.ButtonGroup(*list(exclusive_group.layout))
print(len(g))
print(list(g))

nonexlusive_group = ui.GroupBox(
    title="Exclusive",
    layout=ui.Column(
        ui.Button("A", checkable=True),
        ui.PushButton("B", checkable=True, icon='blue'),
        ui.ToolButton("C", checkable=True, arrow_type='up'),
        ui.ToolButton("D", checkable=True, arrow_type='right')
    )
)

radio_group = ui.GroupBox(
    title="Radio",
    layout=ui.Column(
        ui.RadioButton("A"),
        ui.RadioButton("B"),
        ui.RadioButton("C")
    )
)

radio2_group = ui.GroupBox(
    title="Radio",
    layout=ui.Column(
        ui.RadioButton("A"),
        ui.RadioButton("B"),
        ui.RadioButton("C")
    )
)
g2 = ui.ButtonGroup(*list(radio2_group.layout), exclusive=False)

window = ui.Widget(
    title="Buttons",
    layout=ui.Row(
        exclusive_group,
        nonexlusive_group,
        radio_group,
        radio2_group
    )
)
window.show()

# print(window.cursor)
# window.cursor = 'wait'
# print(window.cursor)
# window.cursor = None
# print(window.cursor)
# window.cursor = 'wait'
# print(window.cursor)

app.run()
