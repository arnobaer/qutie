import qutie as ui

app = ui.Application()

table = ui.Table()
table.header = "ID", "Name", "Price"
table.vertical_header = True

table.append([1002, "Ham", 2.39])
table.append([1003, "Eggs", 1.05])
table.insert(0, [1000, "Spam", 0.75])
table.append([0, "Other", 0])
table.remove_row(-1)

table.fit(0)
table.fit(2)

for row in table:
    row[0].color = 'blue'
    row[1].icon = 'grey'
    row[1].checked = not table.row(row[0]) % 2

for row in range(len(table)):
    table[row][2].color = 'red'

table.title = f"rows: {len(table)}"

table.minimum_size = 320, 240
table.resize(320, 240)
table.show()

app.run()
