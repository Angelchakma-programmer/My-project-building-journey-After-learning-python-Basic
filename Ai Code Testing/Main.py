"""
Main Game Controller for Rangamati Adventure Game.
A text-based RPG exploring Rangamati District's Upazilas, sights, foods, and tribal culture.
"""

import sys
import os
import random
from typing import Optional

from game_data import UPAZILAS, ROUTES, TRIVIA_QUESTIONS, SOUVENIR_SHOP
from player import Player
from ui_helper import (
    Colors, clear_screen, print_banner, print_header, print_box,
    print_status_bar, slow_print, press_enter_to_continue
)

SAVE_FILE = "rangamati_save.json"

def display_ascii_map():
    map_art = f"""{Colors.BRIGHT_GREEN}
         ▲ ▲ ▲  RANGAMATI DISTRICT (রাঙামাটি জেলা)  ▲ ▲ ▲
                       [Baghaichhari / Sajek] ☁️
                                │ (Chander Gari 4x4)
                                ▼
                       [Rangamati Sadar] 🏛️ ═══════════ [Barkal / Shuvolong] 🌊
                         (Kaptai Lake)  │               (Waterfalls & Haat)
                                        │ (Speedboat / Lake Boat)
                                        ▼
                                 [Kaptai] 🌲
                                (Dam & Forest)
                                        │ (Raikhong River Boat)
                                        ▼
                            [Bilaichhari] 🏕️
                         (Dhuppani Waterfall){Colors.RESET}
    """
    print(map_art)

def handle_energy_collapse(player: Player):
    """Triggered when player energy hits 0."""
    clear_screen()
    print_header("⚠️ EXHAUSTED & FAINTED", "You ran out of energy!")
    print(f"{Colors.RED}Your vision blurs as the mountain heat and long trek catch up with you...{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_CYAN}Fortunately, friendly local villagers noticed you!{Colors.RESET}")
    print(f"They kindly carried you on a bamboo stretcher to the nearest village homestay,")
    print(f"fed you warm hill herbal soup, and let you rest safely on a cot.")
    
    rescue_fee = min(player.money, 200)
    player.modify_money(-rescue_fee)
    player.energy = 50
    player.journal.append("Collapsed from exhaustion but was warmly rescued by local hill villagers.")
    print(f"\n{Colors.YELLOW}Paid ৳ {rescue_fee} for herbal medicine & stay. Energy restored to 50%.{Colors.RESET}")
    press_enter_to_continue()

def check_quest_progress(player: Player):
    """Check explorer quest goals and display achievement status."""
    clear_screen()
    print_header("🏆 THE ULTIMATE RANGAMATI EXPLORER QUEST", "Your Journey & Achievements")
    
    upazilas_visited = set()
    for upazila_id, upazila in UPAZILAS.items():
        for spot in upazila["spots"]:
            if spot["id"] in player.visited_spots:
                upazilas_visited.add(upazila_id)
                break
                
    total_spots = sum(len(u["spots"]) for u in UPAZILAS.values())
    total_foods = sum(len(u["foods"]) for u in UPAZILAS.values())
    
    print(f"🎖️  Current Title: {Colors.BRIGHT_YELLOW}{player.get_title()}{Colors.RESET}\n")
    print(f"• Upazilas Explored:    [{len(upazilas_visited)}/5] {'✅' if len(upazilas_visited) == 5 else '⏳'}")
    print(f"• Tourist Spots Visited: [{len(player.visited_spots)}/{total_spots}] {'✅' if len(player.visited_spots) >= 8 else '⏳'}")
    print(f"• Local Foods Tasted:   [{len(player.tasted_foods)}/{total_foods}] {'✅' if len(player.tasted_foods) >= 5 else '⏳'}")
    print(f"• Badges Earned:        [{len(player.badges)}/15]")
    print(f"• Cultural XP:          {player.xp} points")
    
    if len(upazilas_visited) == 5 and len(player.visited_spots) >= 8 and len(player.tasted_foods) >= 5:
        print(f"\n{Colors.BRIGHT_GREEN}{'★'*60}")
        print(f" 🎉 CONGRATULATIONS! YOU COMPLETED THE RANGAMATI EXPLORER QUEST! 🎉")
        print(f" You are a true champion of Rangamati's culture, hills, and waterways!")
        print(f"{'★'*60}{Colors.RESET}")
    else:
        print(f"\n{Colors.CYAN}💡 Tip: Visit all 5 Upazilas, see at least 8 spots, and taste 5 local dishes to complete the quest!{Colors.RESET}")
    press_enter_to_continue()

def explore_spots(player: Player):
    """Explore tourist attractions in the current Upazila."""
    while True:
        clear_screen()
        curr = UPAZILAS[player.current_location]
        print_header(f"🏔️ Tourist Spots in {curr['name']}", "Choose a scenic attraction to visit")
        print_status_bar(player)
        
        spots = curr["spots"]
        for idx, spot in enumerate(spots, 1):
            visited_mark = f"{Colors.BRIGHT_GREEN}✓ Visited{Colors.RESET}" if spot["id"] in player.visited_spots else f"{Colors.YELLOW}New!{Colors.RESET}"
            print(f" [{idx}] {spot['name']} ({spot['bengali_name']}) - [{visited_mark}]")
            print(f"     Fee: ৳ {spot['cost']} | Energy Required: {spot['energy_cost']}%")
            print(f"     {Colors.DIM}{spot['description']}{Colors.RESET}\n")
            
        print(f" [{len(spots)+1}] 🔙 Back to Main Menu")
        
        choice = input(f"\n{Colors.BOLD}Select a spot to visit (1-{len(spots)+1}): {Colors.RESET}").strip()
        
        if choice == str(len(spots)+1):
            break
            
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(spots):
            print(f"{Colors.RED}Invalid option! Please enter a valid number.{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        spot = spots[int(choice) - 1]
        
        # Check energy & money
        if player.energy < spot["energy_cost"]:
            print(f"\n{Colors.RED}❌ You are too tired! (Need {spot['energy_cost']}% energy, you have {player.energy}%). Rest at a hotel or eat food first.{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        if player.money < spot["cost"]:
            print(f"\n{Colors.RED}❌ Insufficient funds! (Need ৳ {spot['cost']}, you have ৳ {player.money}). Help guides in trivia to earn cash!{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        # Deduct cost and energy
        player.modify_money(-spot["cost"])
        player.modify_energy(-spot["energy_cost"])
        is_new = player.visit_spot(spot)
        
        clear_screen()
        print_header(f"📍 Visiting {spot['name']}", spot['bengali_name'])
        print(f"{Colors.BRIGHT_WHITE}{spot['description']}{Colors.RESET}\n")
        print(f"{Colors.CYAN}📖 History & Lore: {spot['lore']}{Colors.RESET}\n")
        
        if is_new:
            print(f"{Colors.BRIGHT_GREEN}✨ First Time Bonus! Earned Badge: {spot['badge']}{Colors.RESET}")
            if "secret_item" in spot:
                print(f"{Colors.BRIGHT_YELLOW}🎁 Discovered Souvenir Item: {spot['secret_item']} (Added to Backpack){Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}⭐ +50 XP gained!{Colors.RESET}")
        else:
            print(f"{Colors.DIM}You enjoyed the peaceful scenery once again.{Colors.RESET}")
            
        press_enter_to_continue()
        
        if player.energy <= 0:
            handle_energy_collapse(player)
            break

def taste_food(player: Player):
    """Visit local food stalls and taste traditional hill dishes."""
    while True:
        clear_screen()
        curr = UPAZILAS[player.current_location]
        print_header(f"🍲 Local Indigenous Food Stalls in {curr['short_name']}", "Taste authentic Chakma, Marma, and Hill tribal delicacies")
        print_status_bar(player)
        
        foods = curr["foods"]
        for idx, food in enumerate(foods, 1):
            tasted_mark = f"{Colors.BRIGHT_GREEN}✓ Tasted{Colors.RESET}" if food["id"] in player.tasted_foods else f"{Colors.YELLOW}Untasted!{Colors.RESET}"
            print(f" [{idx}] {food['name']} - [{tasted_mark}]")
            print(f"     Price: ৳ {food['price']} | Restores: +{food['energy_gain']}% Energy")
            print(f"     {Colors.DIM}{food['description']}{Colors.RESET}\n")
            
        print(f" [{len(foods)+1}] 🔙 Back to Main Menu")
        
        choice = input(f"\n{Colors.BOLD}Select a delicacy to order (1-{len(foods)+1}): {Colors.RESET}").strip()
        
        if choice == str(len(foods)+1):
            break
            
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(foods):
            print(f"{Colors.RED}Invalid option! Please enter a valid number.{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        food = foods[int(choice) - 1]
        
        if player.money < food["price"]:
            print(f"\n{Colors.RED}❌ Not enough Taka! (Need ৳ {food['price']}, you have ৳ {player.money}).{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        player.modify_money(-food["price"])
        actual_gain = player.modify_energy(food["energy_gain"])
        is_new = player.taste_food(food)
        
        clear_screen()
        print_header("🍽️ A Delicious Hill Feast!", food['name'])
        print(f"You savor the hot and aromatic {food['name']}...")
        print(f"{Colors.CYAN}{food['description']}{Colors.RESET}\n")
        print(f"{Colors.BRIGHT_GREEN}⚡ Energy restored by +{actual_gain}% (Current: {player.energy}%){Colors.RESET}")
        
        if is_new:
            print(f"{Colors.BRIGHT_GREEN}🏅 Earned Foodie Badge: {food['taste_badge']}{Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}⭐ +30 Cultural XP!{Colors.RESET}")
            
        press_enter_to_continue()

def talk_to_guide_and_trivia(player: Player):
    """Interact with local elder or tour guide and answer trivia questions to earn money and XP."""
    clear_screen()
    curr = UPAZILAS[player.current_location]
    print_header(f"🗣️ Local Guide & Cultural Trivia in {curr['short_name']}", "Test your knowledge of Rangamati to earn Taka & XP")
    print_status_bar(player)
    
    # Filter questions for current location or general
    unanswered = [
        (idx, q) for idx, q in enumerate(TRIVIA_QUESTIONS)
        if idx not in player.answered_trivia and (q["upazila"] == player.current_location or q["upazila"] == "general")
    ]
    
    if not unanswered:
        unanswered = [(idx, q) for idx, q in enumerate(TRIVIA_QUESTIONS) if idx not in player.answered_trivia]
        
    if not unanswered:
        print(f"{Colors.BRIGHT_GREEN}🎉 You have mastered all local trivia questions in Rangamati! The elders revere your wisdom.{Colors.RESET}")
        press_enter_to_continue()
        return
        
    q_index, q_data = random.choice(unanswered)
    
    print(f"{Colors.BRIGHT_YELLOW}An elder guide smiles and asks you a question about Rangamati:{Colors.RESET}\n")
    print(f"{Colors.BOLD}{q_data['question']}{Colors.RESET}")
    print(f"{Colors.CYAN}{q_data['question_bn']}{Colors.RESET}\n")
    
    for opt in q_data["options"]:
        print(f"  {opt}")
        
    print(f"\n  Reward: 💰 ৳ {q_data['reward_money']} | ⭐ {q_data['reward_xp']} XP")
    ans = input(f"\n{Colors.BOLD}Your Answer (A/B/C/D) or [Q] to Quit: {Colors.RESET}").strip().upper()
    
    if ans == "Q":
        return
        
    if ans == q_data["answer"]:
        player.answered_trivia.add(q_index)
        player.modify_money(q_data["reward_money"])
        player.add_xp(q_data["reward_xp"])
        print(f"\n{Colors.BRIGHT_GREEN}✅ Correct! Excellent!{Colors.RESET}")
        print(f"{Colors.CYAN}{q_data['explanation']}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}💰 Received ৳ {q_data['reward_money']} | ⭐ +{q_data['reward_xp']} XP{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Incorrect!{Colors.RESET}")
        print(f"The correct answer was: {Colors.BRIGHT_GREEN}{q_data['answer']}{Colors.RESET}")
        print(f"{Colors.CYAN}{q_data['explanation']}{Colors.RESET}")
        
    press_enter_to_continue()

def visit_souvenir_shop(player: Player):
    """Buy tribal handicrafts and souvenirs."""
    while True:
        clear_screen()
        print_header("🛍️ Indigenous Handicraft & Souvenir Market", "Support local hill artisans & collect authentic mementos")
        print_status_bar(player)
        
        for idx, item in enumerate(SOUVENIR_SHOP, 1):
            already_own = any(i["name"] == item["name"] for i in player.backpack)
            own_str = f"{Colors.BRIGHT_GREEN}✓ Owned{Colors.RESET}" if already_own else f"{Colors.YELLOW}Available{Colors.RESET}"
            print(f" [{idx}] {item['name']} - [{own_str}]")
            print(f"     Price: ৳ {item['cost']} | Cultural XP: +{item['xp']}")
            print(f"     {Colors.DIM}{item['desc']}{Colors.RESET}\n")
            
        print(f" [{len(SOUVENIR_SHOP)+1}] 🔙 Back to Main Menu")
        choice = input(f"\n{Colors.BOLD}Choose an item to purchase (1-{len(SOUVENIR_SHOP)+1}): {Colors.RESET}").strip()
        
        if choice == str(len(SOUVENIR_SHOP)+1):
            break
            
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(SOUVENIR_SHOP):
            print(f"{Colors.RED}Invalid choice!{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        item = SOUVENIR_SHOP[int(choice) - 1]
        
        if player.money < item["cost"]:
            print(f"\n{Colors.RED}❌ You do not have enough Taka (Need ৳ {item['cost']}).{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        player.modify_money(-item["cost"])
        player.add_xp(item["xp"])
        player.backpack.append({"name": item["name"], "type": "handicraft"})
        player.journal.append(f"Bought {item['name']} from the handicraft market.")
        
        print(f"\n{Colors.BRIGHT_GREEN}🎁 Purchased {item['name']}! Stored safely in your backpack.{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}⭐ +{item['xp']} Cultural XP!{Colors.RESET}")
        press_enter_to_continue()

def rest_at_hotel(player: Player):
    """Rest at a local eco-resort or homestay to recover stamina/energy."""
    while True:
        clear_screen()
        curr = UPAZILAS[player.current_location]
        print_header(f"🛏️ Accommodations & Resorts in {curr['short_name']}", "Rest, take a bath, and recharge your energy")
        print_status_bar(player)
        
        hotels = curr.get("hotels", [])
        for idx, hotel in enumerate(hotels, 1):
            print(f" [{idx}] {hotel['name']}")
            print(f"     Nightly Rate: ৳ {hotel['cost']} | Restores: {hotel['energy_gain']}% Energy")
            print(f"     {Colors.DIM}{hotel['desc']}{Colors.RESET}\n")
            
        print(f" [{len(hotels)+1}] 🔙 Back to Main Menu")
        choice = input(f"\n{Colors.BOLD}Select accommodation to stay (1-{len(hotels)+1}): {Colors.RESET}").strip()
        
        if choice == str(len(hotels)+1):
            break
            
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(hotels):
            print(f"{Colors.RED}Invalid option!{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        hotel = hotels[int(choice) - 1]
        
        if player.money < hotel["cost"]:
            print(f"\n{Colors.RED}❌ Not enough Taka! (Need ৳ {hotel['cost']}, you have ৳ {player.money}).{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        player.modify_money(-hotel["cost"])
        gain = player.modify_energy(hotel["energy_gain"])
        player.journal.append(f"Rested at {hotel['name']} in {curr['short_name']}.")
        
        clear_screen()
        print_header("🌙 A Good Night's Sleep", hotel['name'])
        print(f"You enjoy the cool hill breeze and calm lake sounds.")
        print(f"{Colors.BRIGHT_GREEN}⚡ Fully refreshed! Restored +{gain}% Energy (Current: {player.energy}%){Colors.RESET}")
        press_enter_to_continue()
        break

def travel_to_upazila(player: Player):
    """Travel from current Upazila to another via boat or Chander Gari."""
    while True:
        clear_screen()
        curr_id = player.current_location
        curr = UPAZILAS[curr_id]
        print_header(f"🚤 Travel Hub from {curr['name']}", "Available Routes & Transports")
        print_status_bar(player)
        display_ascii_map()
        
        available_destinations = []
        for (f, t), route_info in ROUTES.items():
            if f == curr_id:
                dest_name = UPAZILAS[t]["name"]
                available_destinations.append((t, dest_name, route_info))
                
        if not available_destinations:
            print(f"{Colors.RED}No direct routes available from here. Return via previous route.{Colors.RESET}")
            press_enter_to_continue()
            break
            
        for idx, (dest_id, dest_name, route_info) in enumerate(available_destinations, 1):
            print(f" [{idx}] Travel to {dest_name}")
            print(f"     Vehicle: {Colors.CYAN}{route_info['mode']}{Colors.RESET}")
            print(f"     Fare: ৳ {route_info['cost']} | Energy Cost: {route_info['energy']}%")
            print(f"     Duration: {Colors.DIM}{route_info['time_desc']}{Colors.RESET}\n")
            
        print(f" [{len(available_destinations)+1}] 🔙 Stay in Current Upazila")
        
        choice = input(f"\n{Colors.BOLD}Where would you like to travel? (1-{len(available_destinations)+1}): {Colors.RESET}").strip()
        
        if choice == str(len(available_destinations)+1):
            break
            
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available_destinations):
            print(f"{Colors.RED}Invalid destination choice!{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        dest_id, dest_name, route_info = available_destinations[int(choice) - 1]
        
        if player.energy < route_info["energy"]:
            print(f"\n{Colors.RED}❌ You are too tired for this long journey! (Need {route_info['energy']}% energy). Eat or sleep first.{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        if player.money < route_info["cost"]:
            print(f"\n{Colors.RED}❌ Insufficient fare! (Need ৳ {route_info['cost']}, you have ৳ {player.money}).{Colors.RESET}")
            press_enter_to_continue()
            continue
            
        # Execute travel
        player.modify_money(-route_info["cost"])
        player.modify_energy(-route_info["energy"])
        player.current_location = dest_id
        player.add_xp(40)
        player.journal.append(f"Traveled by {route_info['mode']} to {UPAZILAS[dest_id]['short_name']}.")
        
        clear_screen()
        print_header("🚢 On the Move!", f"Traveling to {dest_name}")
        print(f"Boarding {Colors.BRIGHT_CYAN}{route_info['mode']}{Colors.RESET}...")
        print(f"{route_info['time_desc']} with breathtaking views of blue water and emerald mountains.")
        print(f"\n{Colors.BRIGHT_GREEN}Arrived safely at {dest_name}!{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}⭐ +40 Exploration XP!{Colors.RESET}")
        press_enter_to_continue()
        
        if player.energy <= 0:
            handle_energy_collapse(player)
        break

def view_backpack_and_journal(player: Player):
    """View collected items, badges, and travel diary."""
    clear_screen()
    print_header(f"🎒 {player.name}'s Explorer Backpack & Diary", f"Title: {player.get_title()}")
    print_status_bar(player)
    
    print(f"{Colors.BOLD}{Colors.BRIGHT_GREEN}🏅 BADGES EARNED ({len(player.badges)}):{Colors.RESET}")
    if player.badges:
        for badge in sorted(player.badges):
            print(f"   • {badge}")
    else:
        print("   (No badges earned yet. Explore spots and try local food!)")
        
    print(f"\n{Colors.BOLD}{Colors.BRIGHT_YELLOW}🎁 SOUVENIRS & ITEMS ({len(player.backpack)}):{Colors.RESET}")
    if player.backpack:
        for item in player.backpack:
            print(f"   • {item['name']}")
    else:
        print("   (Your backpack is empty. Find secrets at tourist spots or visit shops!)")
        
    print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}📜 TRAVEL JOURNAL (Recent Entries):{Colors.RESET}")
    for entry in player.journal[-6:]:
        print(f"   - {entry}")
        
    press_enter_to_continue()

def save_game(player: Player):
    """Save player state to JSON file."""
    try:
        player.save_to_file(SAVE_FILE)
        print(f"\n{Colors.BRIGHT_GREEN}✅ Game progress successfully saved to '{SAVE_FILE}'!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error saving game: {e}{Colors.RESET}")
    press_enter_to_continue()

def load_game() -> Optional[Player]:
    """Load player state from JSON file."""
    try:
        if not os.path.exists(SAVE_FILE):
            print(f"\n{Colors.RED}❌ No save file found at '{SAVE_FILE}'!{Colors.RESET}")
            press_enter_to_continue()
            return None
        p = Player.load_from_file(SAVE_FILE)
        print(f"\n{Colors.BRIGHT_GREEN}✅ Welcome back, {p.name}! Game progress successfully loaded.{Colors.RESET}")
        press_enter_to_continue()
        return p
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error loading game: {e}{Colors.RESET}")
        press_enter_to_continue()
        return None

def start_new_game() -> Player:
    clear_screen()
    print_banner()
    print(f"{Colors.BRIGHT_YELLOW}Welcome to Rangamati District - The Queen of Hills & Lakes!{Colors.RESET}\n")
    name = input(f"{Colors.BOLD}Enter your Explorer Name (or press Enter for 'Trekker'): {Colors.RESET}").strip()
    if not name:
        name = "Trekker"
    player = Player(name=name)
    clear_screen()
    print_header(f"🌄 Welcome, {player.name}!", "Your Rangamati journey begins")
    print(f"You have arrived at {Colors.BRIGHT_CYAN}Rangamati Sadar{Colors.RESET} by bus.")
    print("In your pocket, you have a travel budget of ৳ 3,500 and a fresh journal.")
    print("Your mission: Explore the subdistricts (Sadar, Sajek/Baghaichhari, Kaptai, Barkal, Bilaichhari),")
    print("taste traditional tribal cuisine, conquer mountain peaks, and earn the title of Grand Master Explorer!")
    press_enter_to_continue()
    return player

def main_menu():
    player: Optional[Player] = None
    
    while True:
        if player is None:
            clear_screen()
            print_banner()
            print(" [1] 🚀 Start New Adventure")
            print(" [2] 📂 Load Saved Game")
            print(" [3] 🗺️ View Rangamati Map & Overview")
            print(" [4] 🚪 Exit Game")
            
            choice = input(f"\n{Colors.BOLD}Enter choice (1-4): {Colors.RESET}").strip()
            if choice == "1":
                player = start_new_game()
            elif choice == "2":
                loaded = load_game()
                if loaded:
                    player = loaded
            elif choice == "3":
                clear_screen()
                print_header("🗺️ RANGAMATI DISTRICT OVERVIEW", "Geography & Subdistricts")
                display_ascii_map()
                for key, upazila in UPAZILAS.items():
                    print(f"{upazila['icon']} {Colors.BOLD}{upazila['name']}{Colors.RESET}:")
                    print(f"   {upazila['description']}\n")
                press_enter_to_continue()
            elif choice == "4":
                print(f"\n{Colors.BRIGHT_YELLOW}Thank you for playing Rangamati Explorer! শুভ বিদায়!{Colors.RESET}\n")
                sys.exit(0)
            continue
            
        # In-game loop
        clear_screen()
        curr = UPAZILAS[player.current_location]
        print_header(f"📍 Location: {curr['name']}", curr['description'])
        print_status_bar(player)
        
        print(" [1] 🏔️  Explore Tourist Attractions")
        print(" [2] 🍲  Taste Local Indigenous Cuisine")
        print(" [3] 🗣️  Talk to Local Guide & Cultural Trivia (Earn ৳ & XP)")
        print(" [4] 🛍️  Visit Tribal Handicraft & Souvenir Market")
        print(" [5] 🛏️  Rest at Hotel / Eco-Resort (Restore Energy)")
        print(" [6] 🚤  Travel to Another Upazila (Subdistrict)")
        print(" [7] 🎒  View Backpack, Badges & Travel Diary")
        print(" [8] 🏆  Check Quest Status & Badges")
        print(" [9] 💾  Save Game Progress")
        print(" [10] 🚪 Main Menu / Quit to Title")
        
        choice = input(f"\n{Colors.BOLD}What would you like to do? (1-10): {Colors.RESET}").strip()
        
        if choice == "1":
            explore_spots(player)
        elif choice == "2":
            taste_food(player)
        elif choice == "3":
            talk_to_guide_and_trivia(player)
        elif choice == "4":
            visit_souvenir_shop(player)
        elif choice == "5":
            rest_at_hotel(player)
        elif choice == "6":
            travel_to_upazila(player)
        elif choice == "7":
            view_backpack_and_journal(player)
        elif choice == "8":
            check_quest_progress(player)
        elif choice == "9":
            save_game(player)
        elif choice == "10":
            confirm = input(f"{Colors.YELLOW}Return to main title screen? Any unsaved progress will be lost. (y/n): {Colors.RESET}").strip().lower()
            if confirm == 'y':
                player = None

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_YELLOW}Game interrupted. Hope to see you back in the hills soon!{Colors.RESET}\n")