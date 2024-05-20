button_info = {
    'text': 'buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
}

button = {
    *button_info,
    *button_style
}

print(button)

button = {
    **button_info,
    **button_style
}

print(button)

button = button_style | button_info
print(button)


