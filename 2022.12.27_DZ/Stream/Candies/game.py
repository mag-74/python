import commands


def start():
    commands.set_player_names()
    if commands.draw():
        commands.switch_player()
    while commands.get_total() > 0:
        commands.game_turn()
    print(f'{commands.get_current_player_name()} забрал последние конфеты и победил!')