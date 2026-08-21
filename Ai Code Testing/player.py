
"""
Player Class for Rangamati Adventure Game.
Tracks inventory, budget, energy, badges, journal entries, and visited spots.
"""

from typing import Dict, List, Set, Any
import json
import os

class Player:
    def __init__(self, name: str = "Hill Trekker"):
        self.name: str = name
        self.current_location: str = "sadar"
        self.money: int = 3500  # Starting budget in Taka (৳)
        self.energy: int = 100  # Max 100
        self.xp: int = 0
        
        # Collections
        self.backpack: List[Dict[str, Any]] = []
        self.badges: Set[str] = set()
        self.visited_spots: Set[str] = set()
        self.tasted_foods: Set[str] = set()
        self.answered_trivia: Set[int] = set()
        self.journal: List[str] = []
        
        # Initial greeting log
        self.journal.append(f"Arrived at Rangamati Sadar. Ready to explore the scenic lakes and hills!")

    def modify_energy(self, amount: int) -> int:
        """Modify energy within bounds [0, 100]. Returns actual change."""
        old = self.energy
        self.energy = max(0, min(100, self.energy + amount))
        return self.energy - old

    def modify_money(self, amount: int) -> bool:
        """Modify money. Returns True if successful, False if insufficient funds."""
        if self.money + amount < 0:
            return False
        self.money += amount
        return True

    def add_xp(self, amount: int):
        self.xp += amount

    def visit_spot(self, spot_dict: Dict[str, Any]) -> bool:
        spot_id = spot_dict["id"]
        is_first_time = spot_id not in self.visited_spots
        self.visited_spots.add(spot_id)
        
        if is_first_time:
            if "badge" in spot_dict:
                self.badges.add(spot_dict["badge"])
            if "secret_item" in spot_dict:
                self.backpack.append({"name": spot_dict["secret_item"], "type": "souvenir"})
            self.add_xp(50)
            self.journal.append(f"Explored {spot_dict['name']} in {self.current_location.capitalize()}.")
        return is_first_time

    def taste_food(self, food_dict: Dict[str, Any]) -> bool:
        food_id = food_dict["id"]
        is_first_time = food_id not in self.tasted_foods
        self.tasted_foods.add(food_id)
        
        if is_first_time:
            if "taste_badge" in food_dict:
                self.badges.add(food_dict["taste_badge"])
            self.add_xp(30)
            self.journal.append(f"Tasted {food_dict['name']} ({food_dict.get('bengali_name', '')}).")
        return is_first_time

    def get_title(self) -> str:
        count = len(self.badges)
        if count >= 12:
            return "👑 Grand Master Explorer of Rangamati (পাহাড় ও হ্রদের সম্রাট)"
        elif count >= 8:
            return "🦅 Master Hill Wanderer (অভিজ্ঞ পাহাড়িয়া পর্যটক)"
        elif count >= 4:
            return "🎒 Active Lake Trekker (সক্রিয় পরিব্রাজক)"
        else:
            return "🌱 Novice Traveler (নবীন পর্যটক)"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "current_location": self.current_location,
            "money": self.money,
            "energy": self.energy,
            "xp": self.xp,
            "backpack": self.backpack,
            "badges": list(self.badges),
            "visited_spots": list(self.visited_spots),
            "tasted_foods": list(self.tasted_foods),
            "answered_trivia": list(self.answered_trivia),
            "journal": self.journal
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Player":
        p = cls(data.get("name", "Explorer"))
        p.current_location = data.get("current_location", "sadar")
        p.money = data.get("money", 3500)
        p.energy = data.get("energy", 100)
        p.xp = data.get("xp", 0)
        p.backpack = data.get("backpack", [])
        p.badges = set(data.get("badges", []))
        p.visited_spots = set(data.get("visited_spots", []))
        p.tasted_foods = set(data.get("tasted_foods", []))
        p.answered_trivia = set(data.get("answered_trivia", []))
        p.journal = data.get("journal", [])
        return p

    def save_to_file(self, filepath: str = "savegame.json"):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

    @classmethod
    def load_from_file(cls, filepath: str = "savegame.json") -> "Player":
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Save file {filepath} not found.")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)