from first_steps_in_oop.project.pokemon import Pokemon


class Trainer:
    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        self.pokemons = []

    def add_pokemon(self, pokemon_name: Pokemon):
        if pokemon_name in self.pokemons:
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon_name)
        return pokemon_name.pokemon_details()

    def release_pokemon(self, pokemon_name: str):
        for current_pokemon in self.pokemons:
            if current_pokemon.pokemon_name == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        string = f'Pokemon Trainer {self.trainer_name}\n'
        string += f'Pokemon count {len(self.pokemons)}\n'
        for pokemon in self.pokemons:
            string += f'- {pokemon.pokemon_details()}\n'
        return string.strip()