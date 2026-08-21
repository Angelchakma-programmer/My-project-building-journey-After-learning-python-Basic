
"""
Game Data for Rangamati District Adventure.
Contains detailed information on Subdistricts (Upazilas), Tourist Spots,
Traditional Indigenous Cuisines, Quizzes, and Transport routes.
"""

UPAZILAS = {
    "sadar": {
        "name": "Rangamati Sadar (রাঙামাটি সদর)",
        "short_name": "Sadar",
        "description": "The administrative heart of Rangamati surrounded by the tranquil waters of Kaptai Lake. Famous for suspension bridges, Buddhist viharas, and tribal heritage.",
        "icon": "🏛️",
        "spots": [
            {
                "id": "hanging_bridge",
                "name": "Hanging Bridge (ঝুলন্ত সেতু)",
                "bengali_name": "ঝুলন্ত সেতু",
                "description": "The iconic 335-foot suspension bridge connecting two hills across Kaptai Lake. Known as the symbol of Rangamati tourism.",
                "cost": 50,
                "energy_cost": 15,
                "badge": "🌉 Bridge Crosser",
                "lore": "Built in the mid-1980s by the Bangladesh Parjatan Corporation, this bridge offers breathtaking panoramic views of the crystal-clear Kaptai Lake.",
                "secret_item": "Hanging Bridge Postcard"
            },
            {
                "id": "rajbana_vihara",
                "name": "Rajbana Vihara (রাজবন বিহার)",
                "bengali_name": "রাজবন বিহার",
                "description": "One of the most famous Buddhist monasteries in Bangladesh, established by the revered Ven. Sadhanananda Mahathero (Bon Bhante).",
                "cost": 20,
                "energy_cost": 10,
                "badge": "🕊️ Serenity Seeker",
                "lore": "The peaceful vihara complex is spread over 33 acres of forest and is a center of spiritual serenity and Theravada Buddhist learning.",
                "secret_item": "Meditation Bell Souvenir"
            },
            {
                "id": "polwel_park",
                "name": "Polwel Park & Love Point (পলওয়েল পার্ক)",
                "bengali_name": "পলওয়েল পার্ক",
                "description": "A modern lakeside eco-park with scenic viewpoints, wooden boardwalks, and sunset photo spots.",
                "cost": 80,
                "energy_cost": 15,
                "badge": "🌅 Sunset Watcher",
                "lore": "Developed on the bank of Kaptai Lake, it features romantic lakeside view cottages and leisure zones.",
                "secret_item": "Handmade Clay Souvenir"
            },
            {
                "id": "tribal_museum",
                "name": "Tribal Cultural Museum (ক্ষুদ্র নৃগোষ্ঠীর সাংস্কৃতিক জাদুঘর)",
                "bengali_name": "ক্ষুদ্র নৃগোষ্ঠীর সাংস্কৃতিক জাদুঘর",
                "description": "Showcases authentic historical attire, ornaments, musical instruments, and weapons of the 13 indigenous communities of CHT.",
                "cost": 40,
                "energy_cost": 15,
                "badge": "📜 Heritage Scholar",
                "lore": "Established in 1978, it preserves rare ethnographic artifacts of Chakma, Marma, Tripura, Tanchangya, Pankho, and Mro peoples.",
                "secret_item": "Traditional Pinon-Hadi Pattern Strip"
            }
        ],
        "foods": [
            {
                "id": "pajon",
                "name": "Pajon (পাঁচন)",
                "bengali_name": "পাঁচন",
                "price": 220,
                "energy_gain": 40,
                "description": "A signature festive mixed-vegetable dish cooked with over 32 kinds of wild forest roots, bamboo shoots, and herbs during the Bizu/Sangrai festival.",
                "taste_badge": "🌿 Master of Herbs"
            },
            {
                "id": "bash_korol_fry",
                "name": "Bash Korol Stir Fry (বাঁশ কোড়ল ভাজি)",
                "bengali_name": "বাঁশ কোড়ল ভাজি",
                "price": 180,
                "energy_gain": 35,
                "description": "Tender young bamboo shoots sliced thinly and stir-fried with green chilies, garlic, and wild coriander.",
                "taste_badge": "🎋 Bamboo Connoisseur"
            },
            {
                "id": "chapila_fry",
                "name": "Crispy Kaptai Chapila Fish (কাপ্তাই চাপিলা মাছ ফ্রাই)",
                "bengali_name": "কাপ্তাই চাপিলা মাছ ভাজা",
                "price": 200,
                "energy_gain": 45,
                "description": "Freshly caught sweet-water Chapila fish from Kaptai Lake, spiced with local turmeric and pan-fried crisp.",
                "taste_badge": "🐟 Lake Fisherman's Delight"
            }
        ],
        "hotels": [
            {"name": "Parjatan Motel Rangamati", "cost": 1200, "energy_gain": 100, "desc": "Comfortable government motel near the Hanging Bridge with lake view."},
            {"name": "Lakeside Eco Cottage", "cost": 700, "energy_gain": 70, "desc": "Cozy bamboo cottage right beside the lake water."}
        ]
    },
    "baghaichhari": {
        "name": "Baghaichhari / Sajek Valley (বাঘাইছড়ি - সাজেক ভ্যালি)",
        "short_name": "Sajek",
        "description": "The 'Roof of Rangamati' nestled among rolling green clouds and high mountain peaks. Famous for Ruilui Para, Konglak Hill, and mesmerizing sea of clouds.",
        "icon": "☁️",
        "spots": [
            {
                "id": "ruilui_para",
                "name": "Ruilui Para Village (রুইলুই পাড়া)",
                "bengali_name": "রুইলুই পাড়া",
                "description": "The main settlement in Sajek, primarily inhabited by the Lusai and Tripura indigenous groups, perched 1,800 feet above sea level.",
                "cost": 50,
                "energy_cost": 20,
                "badge": "🏘️ Mountain Dweller",
                "lore": "Ruilui Para was established in 1885. The stone-paved streets and wooden cottages offer charming vistas.",
                "secret_item": "Handwoven Lusai Shawl"
            },
            {
                "id": "konglak_peak",
                "name": "Konglak Peak (কংলাক পাহাড়)",
                "bengali_name": "কংলাক পাহাড়",
                "description": "The highest peak of Sajek Valley offering a 360-degree view of Lushai Hills of India and the cloud-filled valleys.",
                "cost": 100,
                "energy_cost": 35,
                "badge": "🏔️ Peak Conqueror",
                "lore": "From the top of Konglak, you can see orange orchards, clouds drifting beneath your feet, and the border hills.",
                "secret_item": "Wild Mountain Crystal"
            },
            {
                "id": "sajek_helipad",
                "name": "Sajek Sunset & Sunrise Helipad (সাজেক হেলিপ্যাড)",
                "bengali_name": "সাজেক হেলিপ্যাড",
                "description": "The ultimate viewpoint to witness early morning clouds floating like a white ocean and golden sunset skies.",
                "cost": 30,
                "energy_cost": 15,
                "badge": "☁️ Cloud Surfer",
                "lore": "Tourists gather here at 5:30 AM to watch the sun emerge above thick waves of misty white clouds.",
                "secret_item": "Sunrise Photo Print"
            }
        ],
        "foods": [
            {
                "id": "bamboo_chicken",
                "name": "Bamboo Chicken (বাঁশ মুরগি / ব্যাম্বু চিকেন)",
                "bengali_name": "বাঁশ মুরগি",
                "price": 380,
                "energy_gain": 60,
                "description": "Desi country chicken marinated with local hill spices and cooked inside a sealed raw bamboo stalk over a charcoal fire.",
                "taste_badge": "🔥 Bamboo Chef"
            },
            {
                "id": "hill_tea",
                "name": "Sajek Spiced Hill Lemon Tea (পাহাড়ি লেবু চা)",
                "bengali_name": "পাহাড়ি স্পাইস চা",
                "price": 50,
                "energy_gain": 20,
                "description": "Warm black tea brewed with fresh mountain mint, wild ginger, and fragrant hill kagoji lemon.",
                "taste_badge": "☕ Tea Enthusiast"
            },
            {
                "id": "papaya_salad",
                "name": "Spicy Hill Green Papaya Salad (পেঁপে সালাদ)",
                "bengali_name": "কাঁচা পেঁপে সালাদ",
                "price": 120,
                "energy_gain": 25,
                "description": "Shredded crisp green papaya tossed with fiery hill birds-eye chili (dhani morich), tamarind, and roasted peanuts.",
                "taste_badge": "🌶️ Fire Taster"
            }
        ],
        "hotels": [
            {"name": "Sajek Cloud Heaven Resort", "cost": 1800, "energy_gain": 100, "desc": "Premium wooden resort balcony floating right above the clouds."},
            {"name": "Ruilui Homestay", "cost": 800, "energy_gain": 70, "desc": "Authentic mountain village homestay with friendly hosts."}
        ]
    },
    "kaptai": {
        "name": "Kaptai (কাপ্তাই)",
        "short_name": "Kaptai",
        "description": "Lush green rainforests, the iconic Karnaphuli Hydroelectric Dam, national parks, and emerald-colored lake waterways.",
        "icon": "🌲",
        "spots": [
            {
                "id": "kaptai_dam",
                "name": "Karnaphuli Hydroelectric Dam (কাপ্তাই জলবিদ্যুৎ বাঁধ)",
                "bengali_name": "কাপ্তাই বাঁধ",
                "description": "Bangladesh's only hydroelectric power station, constructed in the 1960s across the Karnaphuli River.",
                "cost": 60,
                "energy_cost": 15,
                "badge": "⚡ Power Pioneer",
                "lore": "The construction of the dam in 1962 created the massive artificial Kaptai Lake covering 655 sq kilometers.",
                "secret_item": "Vintage Dam Blueprint Replica"
            },
            {
                "id": "kaptai_national_park",
                "name": "Kaptai National Park & Cable Car (কাপ্তাই জাতীয় উদ্যান)",
                "bengali_name": "কাপ্তাই জাতীয় উদ্যান",
                "description": "A protected wildlife haven with dense evergreen trees, monkeys, deer, and an exhilarating cable car ride.",
                "cost": 150,
                "energy_cost": 25,
                "badge": "🐒 Jungle Trekker",
                "lore": "Spread across 5,464 hectares, this national park is home to ancient teak trees and rare bird species.",
                "secret_item": "Teak Wood Carving"
            },
            {
                "id": "lake_paradise",
                "name": "Lake Paradise & Navy Camp (লেক প্যারাডাইজ)",
                "bengali_name": "লেক প্যারাডাইজ",
                "description": "A serene lakeside leisure point surrounded by hillocks, offering kayaking and speedboating.",
                "cost": 120,
                "energy_cost": 20,
                "badge": "🛶 Lake Kayaker",
                "lore": "The winding river bends here show the deepest turquoise waters in the entire hill tracts.",
                "secret_item": "Miniature Wooden Paddle"
            }
        ],
        "foods": [
            {
                "id": "kaptai_rui_curry",
                "name": "Kaptai Lake Rui Fish Curry (কাপ্তাই রুই মাছের ঝোল)",
                "bengali_name": "কাপ্তাই রুই মাছের কারি",
                "price": 260,
                "energy_gain": 50,
                "description": "Succulent big lake Rui fish simmered in a light aromatic gravy with fresh tomatoes and coriander.",
                "taste_badge": "🍲 Lake Feast Master"
            },
            {
                "id": "binni_pitha",
                "name": "Steamed Binni Rice Pitha (বিন্নী চালের পিঠা)",
                "bengali_name": "বিন্নী চালের পিঠা",
                "price": 100,
                "energy_gain": 30,
                "description": "Sweet fragrant sticky hill rice steamed inside banana leaves with grated coconut and date jaggery.",
                "taste_badge": "🌾 Sticky Rice Lover"
            }
        ],
        "hotels": [
            {"name": "Kaptai River View Resort", "cost": 1400, "energy_gain": 100, "desc": "Riverside luxury resort with private boating deck."},
            {"name": "Forest Rest House", "cost": 650, "energy_gain": 65, "desc": "Quiet government bungalow nestled in deep mahogany trees."}
        ]
    },
    "barkal": {
        "name": "Barkal / Shuvolong (বরকল - শুভলং)",
        "short_name": "Barkal",
        "description": "Famous for the spectacular Shuvolong Waterfalls cascading down steep mountain cliffs straight into the lake, and scenic border waterways.",
        "icon": "🌊",
        "spots": [
            {
                "id": "shuvolong_falls",
                "name": "Shuvolong Waterfalls (শুভলং ঝর্ণা)",
                "bengali_name": "শুভলং ঝর্ণা",
                "description": "A mesmerizing cascade falling from towering green mountains directly into Kaptai Lake water.",
                "cost": 100,
                "energy_cost": 20,
                "badge": "💦 Waterfall Explorer",
                "lore": "During monsoon and post-monsoon, the roaring water drops hundreds of feet, creating a refreshing spray mist.",
                "secret_item": "Waterfall Polished Pebble"
            },
            {
                "id": "shuvolong_market",
                "name": "Shuvolong Hill Market (শুভলং বাজার)",
                "bengali_name": "শুভলং হাট",
                "description": "A bustling traditional riverside tribal market where local hill farmers bring wild fruits, jhum vegetables, and handcrafts.",
                "cost": 20,
                "energy_cost": 15,
                "badge": "🧺 Tribal Trader",
                "lore": "Villagers travel by dugout wooden boats from remote hill villages every market day (Haat bar).",
                "secret_item": "Handwoven Bamboo Basket"
            }
        ],
        "foods": [
            {
                "id": "hebang_fish",
                "name": "Traditional Hebang (হেবাং - মাছের পাতা পোড়া/ভাপা)",
                "bengali_name": "হেবাং (মাছ)",
                "price": 250,
                "energy_gain": 50,
                "description": "Authentic Chakma Hebang: marinated fresh fish, wild hill onions, and herbs wrapped in banana leaf and baked under hot ash.",
                "taste_badge": "🍃 Hebang Gourmand"
            },
            {
                "id": "poda_mach",
                "name": "Smoked Fire-Roasted Fish (পোড়া মাছের ভর্তা)",
                "bengali_name": "পোড়া মাছের ভর্তা",
                "price": 160,
                "energy_gain": 35,
                "description": "Lake fish slow-smoked over open firewood, mashed with roasted green chilies, mustard oil, and wild mountain herbs.",
                "taste_badge": "🪵 Smoke & Spice Master"
            }
        ],
        "hotels": [
            {"name": "Barkal Lakeside Lodge", "cost": 900, "energy_gain": 85, "desc": "Simple wooden lodge on the lake shore overlooking Shuvolong hills."},
            {"name": "Fisherman's Homestay", "cost": 500, "energy_gain": 60, "desc": "Rustic stay with a local boatman family."}
        ]
    },
    "bilaichhari": {
        "name": "Bilaichhari (বিলাইছড়ি)",
        "short_name": "Bilaichhari",
        "description": "The paradise of untamed waterfalls, remote trekking routes, and the sacred Dhuppani Waterfall.",
        "icon": "🏕️",
        "spots": [
            {
                "id": "dhuppani_falls",
                "name": "Dhuppani Waterfall (ধুপপানি ঝর্ণা)",
                "bengali_name": "ধুপপানি ঝর্ণা",
                "description": "A breathtaking hidden waterfall in deep forest where water looks like milky white mist ('Dhuppani' means white water).",
                "cost": 200,
                "energy_cost": 45,
                "badge": "💧 White Water Pilgrim",
                "lore": "It was discovered by a meditating Buddhist monk in 2000. Reaching it requires a thrilling 2-hour forest trek.",
                "secret_item": "Monk's Blessing Bead"
            },
            {
                "id": "raikhong_river",
                "name": "Raikhong River Trail (রাইক্ষ্যং নদী ট্রেইল)",
                "bengali_name": "রাইক্ষ্যং নদী ট্রেইল",
                "description": "A serene boat ride along the pristine Raikhong canal surrounded by untouched jungle and indigenous hamlets.",
                "cost": 150,
                "energy_cost": 25,
                "badge": "🛶 River Pioneer",
                "lore": "The crystal clear river flows from the remote hills of Bilaichhari down to Kaptai Lake.",
                "secret_item": "River Shell Amulet"
            }
        ],
        "foods": [
            {
                "id": "chilly_creek_crab",
                "name": "Mountain Stream Crab Curry (পাহাড়ি কাঁকড়া ভুনা)",
                "bengali_name": "পাহাড়ি কাঁকড়া ভুনা",
                "price": 280,
                "energy_gain": 55,
                "description": "Freshwater crabs harvested from clear mountain streams, cooked with fiery red hill spices and wild ginger.",
                "taste_badge": "🦀 Creek Hunter Feast"
            },
            {
                "id": "bamboo_leaf_salad",
                "name": "Wild Herb & Forest Greens Salad (বুনো শাকের সালাদ)",
                "bengali_name": "পাহাড়ি বুনো শাকের সালাদ",
                "price": 130,
                "energy_gain": 30,
                "description": "Freshly foraged organic forest herbs, tender shoots, and roasted sesame seed dressing.",
                "taste_badge": "🌱 Forest Forager"
            }
        ],
        "hotels": [
            {"name": "Bilaichhari Eco Rest House", "cost": 750, "energy_gain": 80, "desc": "Clean eco-lodge run by local guides beside the canal."},
            {"name": "Trekker's Camp Tent", "cost": 450, "energy_gain": 55, "desc": "Camp under the stars near the river bank."}
        ]
    }
}

# Routes between Subdistricts: (from, to) -> {mode, cost, energy, desc}
ROUTES = {
    ("sadar", "baghaichhari"): {
        "mode": "Chander Gari (চান্দের গাড়ি / 4x4 Jeep)",
        "cost": 650,
        "energy": 30,
        "time_desc": "4.5 hours exciting scenic roller-coaster mountain road ride"
    },
    ("baghaichhari", "sadar"): {
        "mode": "Chander Gari (চান্দের গাড়ি / 4x4 Jeep)",
        "cost": 650,
        "energy": 30,
        "time_desc": "4.5 hours thrilling ride back down through the hill valleys"
    },
    ("sadar", "kaptai"): {
        "mode": "Lake Engine Boat / CNG Auto (বোট / সিএনজি)",
        "cost": 250,
        "energy": 15,
        "time_desc": "1.5 hours scenic ride along the lake and forest highway"
    },
    ("kaptai", "sadar"): {
        "mode": "Lake Engine Boat / CNG Auto (বোট / সিএনজি)",
        "cost": 250,
        "energy": 15,
        "time_desc": "1.5 hours scenic ride returning to Rangamati town"
    },
    ("sadar", "barkal"): {
        "mode": "Lake Trawler / Speedboat (ইঞ্জিন বোট / স্পিডবোট)",
        "cost": 300,
        "energy": 20,
        "time_desc": "2 hours mesmerizing boat journey across the broad Kaptai Lake"
    },
    ("barkal", "sadar"): {
        "mode": "Lake Trawler / Speedboat (ইঞ্জিন বোট / স্পিডবোট)",
        "cost": 300,
        "energy": 20,
        "time_desc": "2 hours boat cruise returning across Kaptai Lake"
    },
    ("kaptai", "bilaichhari"): {
        "mode": "Troller Engine Boat (নদী বোট)",
        "cost": 220,
        "energy": 20,
        "time_desc": "2.5 hours tranquil upstream cruise through the Raikhong river"
    },
    ("bilaichhari", "kaptai"): {
        "mode": "Troller Engine Boat (নদী বোট)",
        "cost": 220,
        "energy": 20,
        "time_desc": "2.5 hours downstream cruise returning to Kaptai Ghat"
    },
    ("sadar", "bilaichhari"): {
        "mode": "Direct Lake Engine Boat (সরাসরি বোট)",
        "cost": 400,
        "energy": 25,
        "time_desc": "3.5 hours long serene lake voyage into the remote wilderness"
    },
    ("bilaichhari", "sadar"): {
        "mode": "Direct Lake Engine Boat (সরাসরি বোট)",
        "cost": 400,
        "energy": 25,
        "time_desc": "3.5 hours boat cruise returning to Rangamati Sadar"
    }
}

TRIVIA_QUESTIONS = [
    {
        "upazila": "sadar",
        "question": "Which famous river was dammed in 1962 to create the majestic Kaptai Lake?",
        "question_bn": "১৯৬২ সালে কোন নদীর উপর বাঁধ দিয়ে বিশাল কাপ্তাই হ্রদ তৈরি করা হয়েছিল?",
        "options": [
            "A) Sangu River (সাঙ্গু নদী)",
            "B) Karnaphuli River (কর্ণফুলী নদী)",
            "C) Matamuhuri River (মাতামুহুরী নদী)",
            "D) Halda River (হালদা নদী)"
        ],
        "answer": "B",
        "explanation": "Kaptai Lake was created by damming the Karnaphuli River at Kaptai for hydroelectric power generation.",
        "reward_money": 150,
        "reward_xp": 50
    },
    {
        "upazila": "sadar",
        "question": "What is the primary traditional dish cooked during the Bizu/Sangrai festival using 30+ varieties of vegetables?",
        "question_bn": "বিজু বা সাংগ্রাই উৎসবে ৩০টিরও বেশি পদের সবজি ও পাহাড়ি ভেষজ দিয়ে কোন ঐতিহ্যবাহী খাবারটি রান্না করা হয়?",
        "options": [
            "A) Pajon (পাঁচন)",
            "B) Biryani (বিরিয়ানি)",
            "C) Khichuri (খিচুড়ি)",
            "D) Nappi (নাপ্পি)"
        ],
        "answer": "A",
        "explanation": "Pajon is a sacred and delicious vegetable stew cooked in every household during the CHT New Year festival.",
        "reward_money": 150,
        "reward_xp": 50
    },
    {
        "upazila": "baghaichhari",
        "question": "In which Upazila (Subdistrict) of Rangamati is the famous Sajek Valley situated?",
        "question_bn": "বিখ্যাত সাজেক ভ্যালি রাঙামাটি জেলার কোন উপজেলায় অবস্থিত?",
        "options": [
            "A) Kawkhali (কাউখালী)",
            "B) Rajasthali (রাজস্থলী)",
            "C) Baghaichhari (বাঘাইছড়ি)",
            "D) Jurachhari (জুরাছড়ি)"
        ],
        "answer": "C",
        "explanation": "Sajek Valley is located in Baghaichhari Upazila, the largest Upazila by area in Bangladesh!",
        "reward_money": 200,
        "reward_xp": 60
    },
    {
        "upazila": "baghaichhari",
        "question": "What is the name of the highest peak in Sajek Valley that offers a 360-degree panoramic view?",
        "question_bn": "সাজেক ভ্যালির সর্বোচ্চ চূড়া বা পাহাড়ের নাম কী যেখান থেকে চারপাশের মেঘের সমুদ্র দেখা যায়?",
        "options": [
            "A) Keokradong (কেওক্রাডং)",
            "B) Konglak Peak (কংলাক পাহাড়)",
            "C) Saka Haphong (সাকা হাফং)",
            "D) Marayan Thong (মারায়ান তং)"
        ],
        "answer": "B",
        "explanation": "Konglak Peak is the highest point of Sajek Valley, inhabited by the friendly Lusai community.",
        "reward_money": 200,
        "reward_xp": 60
    },
    {
        "upazila": "kaptai",
        "question": "What unique form of energy is produced at Kaptai in Bangladesh?",
        "question_bn": "কাপ্তাইয়ে বাংলাদেশের একমাত্র কোন ধরনের বিদ্যুৎ কেন্দ্র অবস্থিত?",
        "options": [
            "A) Nuclear Power (পারমাণবিক বিদ্যুৎ)",
            "B) Geothermal Power (ভূ-তাপীয় বিদ্যুৎ)",
            "C) Hydroelectric Power (জলবিদ্যুৎ)",
            "D) Coal Power (কয়লা বিদ্যুৎ)"
        ],
        "answer": "C",
        "explanation": "The Karnaphuli Hydro Power Station at Kaptai is the only hydroelectric power plant in Bangladesh.",
        "reward_money": 150,
        "reward_xp": 50
    },
    {
        "upazila": "barkal",
        "question": "Which iconic waterfall drops directly into Kaptai Lake and is a major attraction in Barkal?",
        "question_bn": "বরকলের কোন বিখ্যাত ঝর্ণাটি সরাসরি কাপ্তাই হ্রদের পানিতে গিয়ে মিশেছে?",
        "options": [
            "A) Shuvolong Waterfall (শুভলং ঝর্ণা)",
            "B) Madhabkunda Waterfall (মাধবকুণ্ড ঝর্ণা)",
            "C) Nafakhum (নাফাকুম)",
            "D) Amiakhum (আমিয়াখুম)"
        ],
        "answer": "A",
        "explanation": "Shuvolong Waterfall in Barkal cascades from high rocky mountain cliffs directly into the lake.",
        "reward_money": 180,
        "reward_xp": 55
    },
    {
        "upazila": "bilaichhari",
        "question": "What does the name 'Dhuppani' mean in the local dialect?",
        "question_bn": "স্থানীয় তঞ্চঙ্গ্যা/পাহাড়ি ভাষায় 'ধুপপানি' (Dhuppani) শব্দের অর্থ কী?",
        "options": [
            "A) Cold Water (ঠান্ডা পানি)",
            "B) White/Milky Water (সাদা/দুধের মতো স্বচ্ছ পানি)",
            "C) Fast Water (দ্রুত পানি)",
            "D) Deep Water (গভীর পানি)"
        ],
        "answer": "B",
        "explanation": "In Tanchangya dialect, 'Dhupp' means white (like incense smoke / milk), hence 'Dhuppani' translates to White Water Waterfall.",
        "reward_money": 200,
        "reward_xp": 70
    }
]

SOUVENIR_SHOP = [
    {"id": "bamboo_flute", "name": "Traditional Bamboo Flute (পাহাড়ি বাঁশের বাঁশি)", "cost": 150, "xp": 25, "desc": "Handcrafted melody flute made by local artisans."},
    {"id": "chakma_scarf", "name": "Handloom Tribal Scarf / Gamcha (হাতে বোনা গামছা)", "cost": 250, "xp": 40, "desc": "Woven with beautiful geometric indigenous patterns on back-strap loom."},
    {"id": "wild_honey", "name": "Pure Sajek Hill Honey (পাহাড়ি খাঁটি মধু)", "cost": 400, "xp": 50, "desc": "Bottled fresh wild bee honey harvested from deep mountain trees."}
]