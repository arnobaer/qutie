import qutie as ui

app = ui.Application()

tree = ui.Tree()
tree.header = "ID", "Name", "Price"

tree.append([1200, "Ham", 2.39])
tree.append([1100, "Eggs", 1.05])

item = tree.insert(0, [1000, "Spam", 0.75])
item.append([1002, "Spam Hot & Spicy", 0.95])
item.append([1003, "Jalapeño Spam", 0.89])
item.insert(0, [1001, "Spam Classic", 0.75])

tree.fit(0)
tree.fit(2)

for item in tree:
    item[0].color = 'blue'
    item[1].icon = 'grey'
    item[1].checked = not tree.index(item[0]) % 2

for index in range(len(tree)):
    tree[index][2].color = 'red'

tree.title = f"items: {len(tree)}"

tree.minimum_size = 320, 240
tree.resize(320, 240)
tree.show()

app.run()
