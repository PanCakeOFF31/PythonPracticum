button = {
    'width': 200,
    'text': 'buy',
    'color': 'pink'
}

red_button = {
    # Деструктуризация словаря
    **button,
    'color': 'red',
}

fail_button = {
    'color': 'yellow',
    **button,
}

print(button)
print(red_button)
print(fail_button)


