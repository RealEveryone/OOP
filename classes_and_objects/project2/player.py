class Player:
    default_guild = 'Unaffiliated'

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.default_guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        output = f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n'
        for key, value in self.skills.items():
            output += f'==={key} - {value}\n'
        return output.strip()
