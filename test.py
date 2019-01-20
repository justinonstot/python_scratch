fav_langs = {
    'jenn':'python',
    'nick': 'python',
    'adam': 'haskel',
    'steve': 'c#',
    'bill': 'R'}

for key, value in fav_langs.items():
    print("\nThe key is: " + key)
    print('The value is: ' + value)

for name in sorted(fav_langs.keys()):
    print(name.title() + " thank you for answering")