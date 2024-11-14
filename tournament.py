import time
from combat_manager import combat

def tournoi(participants, pokemons, update_arena, update_fight_images, img_label1, img_label2, name_label1, name_label2, show_winner):
    while len(participants) > 1:
        winners = []

        while len(participants) >= 2:
            fighter_1 = participants.pop(0)
            fighter_2 = participants.pop(0)

            pokemon1 = pokemons[f'pokemon_{fighter_1}']
            pokemon2 = pokemons[f'pokemon_{fighter_2}']

            update_fight_images(pokemon1, pokemon2, img_label1, img_label2, name_label1, name_label2)
            winner = combat(pokemon1, pokemon2, update_arena)

            winner_name = winner['name'].capitalize()
            combat_message = f"Combat entre {pokemon1['name'].capitalize()} et {pokemon2['name'].capitalize()} terminé! Gagnant : {winner_name}"
            update_arena(combat_message)

            winners.append(fighter_1 if winner['name'] == pokemon1['name'] else fighter_2)

        if len(participants) == 1:
            lone_participant = participants.pop(0)
            winners.append(lone_participant)
            update_arena(f"{pokemons[f'pokemon_{lone_participant}']['name'].capitalize()} passe automatiquement au tour suivant.")

        participants = winners
        update_arena("----------- NOUVEAU TOUR -----------")

    final_winner = participants[0]
    pokemon_final = pokemons[f'pokemon_{final_winner}']
    update_arena(f"Le grand gagnant du tournoi est : {pokemon_final['name'].capitalize()}")
    show_winner(pokemon_final)
