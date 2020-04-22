# Qutie

Yet another pythonic UI library for rapid prototyping using PyQt5.

## Quick start

```python
import qutie as ui

app = ui.Application()
w = ui.Widget(
    title="Example",
    layout=ui.Column(
        ui.Label(text="Hello world!"),
        ui.Row(
            ui.Button(text="Click!", clicked=lambda: ui.show_info("Hello world!")),
            ui.Button(text="Quit", clicked=app.quit)
        )
    )
)
w.show()
app.run()
```
