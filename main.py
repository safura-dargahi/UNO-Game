#%%
import sys
import time
import argparse
import traceback
import logging
from typing import Optional, Any

from game import Game, Player, Card, CardColor, GameEvent, GameEventType, Turn, CardType
from exceptions import CardNotPlayableError, CardNotInPossessionError
from rich.console import Console
from time import sleep

__VERSION__: str = 'ALPHA-2025-06-02'

console = Console(color_system='standard')


def print_error(message: str) -> None:
    """Print error message in red color"""
    console.print(f"[bright_red]{message}[/bright_red]")


def print_version() -> None:
    """Print ASCII art logo and version"""
    console.print("[red]88   88[/red][green] 88b 88[/green][blue]  dP\"Yb  ")
    console.print("[red]88   88[/red][green] 88Yb88[/green][blue] dP   Yb ")
    console.print("[red]Y8   8P[/red][green] 88 Y88[/green][blue] Yb   dP ")
    console.print("[red]`YbodP'[/red][green] 88  Y8[/green][blue]  YbodP  ")
    console.print(f"\n[bright_red]U[bright_green]N[bright_blue]O[/bright_blue][bright_white] | version {__VERSION__}")


def main() -> None:
    """Main game loop"""
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-C', '--cheats', action='store_true', help="enable cheat codes (see README)")
    argparser.add_argument('-D', '--debug', action='store_true', help="enable debugging messages")
    argparser.add_argument('-V', '--version', action='store_true', help="print the version and exit")

    arguments = argparser.parse_args()
    cheats: bool = arguments.cheats
    debug: bool = arguments.debug

    print_version()

    if arguments.version:
        raise SystemExit

    print("---")

    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG if debug else logging.INFO,
        format='%(levelname)s: %(message)s'
    )

    if cheats:
        console.print("[yellow]WARNING: [/yellow][white]Cheat codes are enabled.[/white]")
    logging.debug("Debug messages are enabled.")

    # Get number of players
    players: list[Player] = []
    while True:
        try:
            number_of_players = int(input("Please enter the number of players: "))
            if number_of_players > 1:
                break
            print_error("The number can't be lower than 2.")
        except ValueError:
            print_error("Enter a valid number.")
    
    # Get player names
    print("Please enter the player names.")
    print("Hint: type \"computer\" to play with the computer.\n---")
    
    for i in range(1, number_of_players + 1):
        while True:
            player_name: str = input(f"Player #{i}: ").lower()
            if player_name in [player.name for player in players]:
                print_error("That player already exists.")
            else:
                break
        players.append(Player(player_name))
    
    # Get starting cards
    while True:
        try:
            starting_cards: int = int(input("Starting cards: "))
            if starting_cards > 1:
                break
            print_error("The number can't be lower than 2.")
        except ValueError:
            print_error("Enter a valid number.")
    
    # Get card stacking preference
    card_stacking_input = input("Similar card stacking (Y/n): ").lower()
    card_stacking: bool = card_stacking_input in ('y', '')

    # Initialize game
    rules: dict[str, Any] = {
        'starting_cards': starting_cards,
        'cheats': cheats,
        'card_stacking': card_stacking
    }
    game = Game(players, rules)

    # Main game loop
    while game.active:
        # Check for winner
        winner = game.get_winner()
        if winner is not None:
            game.win(winner)
            console.print(f"> [green]Winner: {winner.name}[/green]")
            break
        
        # Show turn indicator
        if not all(player.is_computer for player in players):  # Not fully automated game
            print("\n- Turn: [", end='')
            for player in game.players:
                if player == game.turn:
                    console.print(f' [bold][bright_white][underline]{player.name}[/bold][/bright_white][/underline]', end='')
                else:
                    console.print(f' {player.name}', end='')
            print(' ]')
        else:
            console.print(f"\n- Turn: [bold][italic]{game.turn.name}[/bold][/italic]")
        
        # Process turn
        while True:
            if game.turn.is_computer:
                # Computer turn
                computer_turn = Turn(game)
                card: Card = computer_turn.get_result()
                
                if not game.turn.is_computer or not game.next_turn.is_computer:
                    time.sleep(0.5)
                
                console.print(f"-> Computer put {card}")
                event: GameEvent = game.play(card, game.turn)
                
                # Handle events using if/elif instead of match/case for Python 3.9 compatibility
                if event.type == GameEventType.COLOR_CHANGED:
                    game.stack[0] = Card(None, event.payload['new_color'])
                    console.print(
                        f"{event.payload['player'].name} changed the color to "
                        f"[bright_{event.payload['new_color'].name.lower()}]"
                        f"{event.payload['new_color']}[bright_white]"
                    )
                elif event.type == GameEventType.AWAIT_COLOR_INPUT:
                    raise NotImplementedError("Computer should auto-select color")
                elif event.type == GameEventType.STACKING_ACTIVE:
                    for stacked_card in event.payload['stacked_cards']:
                        console.print(f"> Stacking {stacked_card}...")
                
                logging.debug(f"-  {game.turn.name}'s cards: {game.next_turn.format_hand_contents()}")
                print(f"-- Their remaining cards: {len(game.next_turn.hand)}")
            else:
                # Human turn
                if not game.turn.is_computer or not game.next_turn.is_computer:
                    time.sleep(0.25)
                
                console.print(
                    f"\n   [ [bright_cyan]-> [bright_blue]Current card[bright_white]: "
                    f"[bold][underline]{game.last_played_card}[/bold][/underline] "
                    f"[bright_cyan]<- [/bright_cyan]]\n"
                )
                
                if not game.turn.is_computer or not game.next_turn.is_computer:
                    time.sleep(0.25)
                
                console.print(f"-- Your cards: {game.turn.format_hand_contents()}\n")
                
                try:
                    card_input: str = console.input("Card ([bright_blue]Enter[/bright_blue] to draw) >[bright_white] ")
                except KeyboardInterrupt:
                    raise SystemExit
                
                # Handle cheat codes
                if game.rules['cheats'] and '#' in card_input:
                    try:
                        cheat_code: str = card_input.split('#')[1]
                        try:
                            exec(cheat_code)
                        except Exception:
                            print_error(traceback.format_exc())
                        break
                    except IndexError:
                        pass
                
                card_input = card_input.upper()
                
                # Handle drawing a card
                if card_input == '':
                    try:
                        game.deal_card(game.turn)
                        print("Drew a card.")
                        break
                    except IndexError:
                        print_error("Can't draw more cards.")
                
                # Handle passing turn
                elif card_input == 'PASS':
                    print("You passed the turn.")
                    game.set_next_turn()
                
                # Handle playing a card
                else:
                    # Parse card input
                    card_obj: Optional[Card] = None
                    if card_input in ('WILDCARD', '+4'):
                        card_type_enum = CardType["CARD_" + card_input.replace('+', "PLUS_")]
                        card_obj = Card(card_type_enum, None)
                    else:
                        card_obj = Card.from_str(card_input)
                    
                    # Validate card was parsed
                    if card_obj is None:
                        print_error("Incorrect input. Please enter a card name, for example: \"7 GREEN\"")
                        continue
                    
                    # Try to play the card
                    try:
                        event = game.play(card_obj, game.turn)
                        
                        # Handle events using if/elif
                        if event.type == GameEventType.COLOR_CHANGED:
                            game.stack[0] = Card(None, event.payload['new_color'])
                            console.print(
                                f"{event.payload['player'].name} changed the color to "
                                f"[bright_{event.payload['new_color'].name.lower()}]"
                                f"{event.payload['new_color']}[bright_white]"
                            )
                        elif event.type == GameEventType.AWAIT_COLOR_INPUT:
                            while True:
                                try:
                                    new_color = CardColor[input("New card color: ").upper()]
                                    break
                                except KeyError:
                                    console.print(
                                        "[bright_red]Incorrect input. "
                                        "Please type a card color, for example \"GREEN\"[/bright_red]"
                                    )
                            game.stack[0] = Card(None, new_color)
                        elif event.type == GameEventType.STACKING_ACTIVE:
                            for stacked_card in event.payload['stacked_cards']:
                                sleep(0.2)
                                console.print(f"> Stacking {stacked_card}...")
                        
                    except CardNotPlayableError:
                        print_error(f"The card {card_obj!r} is not playable.")
                        continue
                    except CardNotInPossessionError:
                        print_error(f"You do not have {card_obj!r} in your hand.")
                        continue
            
            break


if __name__ == '__main__':
    main()
# %%
