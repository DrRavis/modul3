calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    length = len(string)
    cortege = (length, string.upper(), string.lower())
    return cortege

def is_contains(string, list_to_search):
    count_calls()
    checked = False
    for s in list_to_search:
        if string.lower() == s.lower():
            checked = True
    return checked
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)