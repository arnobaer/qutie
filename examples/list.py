import qutie as ui

app = ui.Application()

listing = ui.List()

listing.append("Ham")
listing.append("Eggs")
listing.insert(0, "Spam")

# listing.view_mode = 'icon'
# listing.resize_mode = 'adjust'
# listing.icon_size = 64

for item in listing:
    item.color = 'blue'
    item.icon = 'grey'
    item.checkable = True
    item.checked = not listing.index(item) % 2

for index in range(len(listing)):
    listing[index].color = 'red'

listing.title = f"items: {len(listing)}"

listing.resize(320, 240)
listing.show()

app.run()
