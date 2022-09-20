from classes_and_objects.project2.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        if player.guild != Player.default_guild:
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for current_player in self.players:
            if current_player.name == player_name:
                self.players.remove(current_player)
                current_player.guild = Player.default_guild
                return f'Player {current_player.name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        output = f'Guild: {self.name}\n'
        for current in self.players:
            output += current.player_info() + '\n'
        return output.strip()
