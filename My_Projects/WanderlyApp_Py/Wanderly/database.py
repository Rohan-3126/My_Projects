import sqlite3


def Create_Database():
    connection = sqlite3.connect("Cities.db")
    cursor = connection.cursor()

    # Create table with expanded structure
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cities (
        sno INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT NOT NULL,
        city_pin TEXT NOT NULL,
        city_distance TEXT,
        attractions TEXT,
        affordability TEXT,
        accessibility TEXT,
        activities TEXT,
        amenities TEXT,
        accommodation TEXT
    );
    """)

    cities = [
    ("Agra", "282 001", "2,400 Km", "Taj Mahal,Agra Fort,Mehtab Bagh,Fatehpur Sikri", "₹₹ (Moderate)", "Well-connected by road, rail, and Agra airport", "Heritage walks, Photography, Guided monument tours, Local crafts shopping", "Good public transport, clean lodging, tourist help centers ⭐⭐⭐⭐", "Best: The Oberoi Amarvilas , Budget: Hotel Sidhartha"),
    ("Amritsar", "143 001", "2,800 Km", "Golden Temple,Jallianwala Bagh,Wagah Border", "₹ (Affordable)", "Amritsar Junction, well-connected roads", "Temple visits, History tours, Evening retreat at Wagah", "Clean roads, police help booths, rich food outlets ⭐⭐⭐⭐", "Best: Hyatt Regency , Budget: Hotel Hong Kong Inn"),
    ("Bangalore", "560 001", "585 Km", "Lal Bagh,Bangalore Palace,Bannerghatta National Park", "₹₹ (Moderate)", "International airport, major railway hub", "Garden walks, Wildlife safari, Shopping", "Smart metro, tech-savvy amenities ⭐⭐⭐⭐", "Best: Taj MG Road , Budget: Treebo Trend Hotel"),
    ("Bangkok", "10200", "2,900 Km", "Grand Palace,Wat Arun,Floating Markets,Chatuchak Market", "₹₹₹ (Expensive)", "International flights, efficient MRT", "Street shopping, Temple hopping, Night cruises", "Well-developed transport and amenities ⭐⭐⭐⭐⭐", "Best: Mandarin Oriental , Budget: Ibis Styles Bangkok"),
    ("Chennai", "600 001", "600 Km", "Mahabalipuram,Marina Beach,Fort St. George,Sea shell Museum", "₹₹ (Moderate)", "Metro city with airport, trains, and good roadways", "Beach walks, Temple visits, Cultural shows, Food tasting", "Efficient city buses, sea breeze cafes, decent public amenities ⭐⭐⭐⭐", "Best: ITC Grand Chola , Budget: Hotel Pandian"),
    ("Coimbatore", "641 001", "430 Km", "Marudamalai Temple,VOC Park,Gass Forest Museum", "₹ (Affordable)", "Air, rail, road accessible", "Temple visits, Local shopping, Science museum", "Quiet city with clean facilities ⭐⭐⭐", "Best: Vivanta Coimbatore , Budget: Hotel CAG Pride"),
    ("Darjeeling", "734 101", "2,600 Km", "Tiger Hill,Batasia Loop,Darjeeling Himalayan Railway", "₹₹ (Moderate)", "Toy train, Hill roads", "Tea tasting, Hiking, Photography", "Eco-friendly, Scenic rest stops ⭐⭐⭐", "Best: Mayfair , Budget: Revolver Hotel"),
    ("Delhi", "110 001", "2,600 Km", "Red Fort,India Gate,Qutub Minar,Lotus Temple,Akshardham", "₹₹ (Moderate)", "Metro, Airport, Buses", "Historic tours, Street shopping", "Fast metro, good lodging options ⭐⭐⭐⭐", "Best: The Imperial , Budget: Zostel Delhi"),
    ("Dubai", "00000", "2,600 Km", "Burj Khalifa,Desert Safari,Dubai Mall,Palm Jumeirah", "₹₹₹₹ (Luxury)", "World-class international transport", "Desert adventures, Luxury shopping", "Elite tourist centers and metro ⭐⭐⭐⭐⭐", "Best: Atlantis The Palm , Budget: Rove Downtown"),
    ("Gangtok", "737 101", "2,900 Km", "MG Marg,Nathula Pass,Rumtek Monastery,Tsomgo Lake", "₹₹ (Moderate)", "By road from Siliguri or Bagdogra airport", "Nature walks, Buddhist monastery visits", "Mountain stay amenities ⭐⭐⭐", "Best: Mayfair Spa Resort , Budget: Hotel Tashi Thendup"),
    ("Goa", "403 001", "1,100 Km", "Baga Beach,Fort Aguada,Basilica of Bom Jesus,Dona Paula", "₹₹ (Moderate)", "Flights, trains, buses", "Beach fun, Water sports, Churches", "Popular with clean beaches and cafes ⭐⭐⭐⭐", "Best: Taj Exotica , Budget: The Hosteller Goa"),
    ("Hyderabad", "500 001", "1,150 Km", "Charminar,Golconda Fort,Ramoji Film City", "₹₹ (Moderate)", "Rajiv Gandhi Airport, railway network", "Film tours, History walks", "IT city with great public services ⭐⭐⭐⭐", "Best: Taj Falaknuma Palace , Budget: Hotel Geetanjali"),
    ("Istanbul", "34122", "5,800 Km", "Hagia Sophia,Blue Mosque,Grand Bazaar,Topkapi Palace", "₹₹₹ (Expensive)", "Istanbul International Airport", "Cultural immersion, Market tours", "Historical city with great transport ⭐⭐⭐⭐", "Best: Four Seasons Istanbul , Budget: Hotel Sirkeci Mansion"),
    ("Jaipur", "302 001", "2,100 Km", "Hawa Mahal,Amber Fort,City Palace,Jantar Mantar", "₹ (Affordable)", "Jaipur Airport, train, buses", "Fort climbs, Local shopping", "Desert culture vibes with amenities ⭐⭐⭐", "Best: Rambagh Palace , Budget: Zostel Jaipur"),
    ("Kanyakumari", "629 702", "215 Km", "Vivekananda Rock,Thiruvalluvar Statue,Sunset Point", "₹ (Affordable)", "By road and train", "Sunset view, Memorial visit", "Peaceful tourist spot ⭐⭐⭐", "Best: Sparsa Resort , Budget: Sea View Lodge"),
    ("London", "SW1A 1AA", "8,000 Km", "Big Ben,Buckingham Palace,London Eye,Tower of London", "₹₹₹₹ (Luxury)", "Heathrow, underground trains", "Museums, City strolls, River tours", "Top-tier global city ⭐⭐⭐⭐⭐", "Best: The Savoy , Budget: EasyHotel Victoria"),
    ("Madurai", "625 001", "150 Km", "Meenakshi Amman Temple,Thirumalai Nayakar Palace", "₹ (Affordable)", "Buses, Trains", "Temple darshan, Cultural trails", "Rich culture, simple living ⭐⭐⭐", "Best: The Gateway Hotel , Budget: Astoria Hotel"),
    ("Mysore", "570 001", "555 Km", "Mysore Palace,Chamundi Hills,Brindavan Gardens", "₹ (Affordable)", "Connected via trains and highways", "Garden light shows, Palace walks", "Heritage city amenities ⭐⭐⭐", "Best: Royal Orchid Metropole , Budget: Hotel Roopa"),
    ("New York", "10001", "12,000 Km", "Statue of Liberty,Times Square,Central Park,Empire State Building", "₹₹₹₹ (Luxury)", "JFK, subway, metro", "City life, Museums, Broadway", "Global tourist city ⭐⭐⭐⭐⭐", "Best: The Plaza , Budget: Pod Times Square"),
    ("Paris", "75001", "7,200 Km", "Eiffel Tower,Louvre Museum,Notre-Dame,Champs-Élysées", "₹₹₹ (Expensive)", "CDG Airport, Metro", "Art museums, River cruise", "City of love and light ⭐⭐⭐⭐⭐", "Best: Le Meurice , Budget: Hotel Ekta"),
    ("Pondicherry", "605 001", "460 Km", "Auroville,Promenade Beach,French Quarter", "₹ (Affordable)", "By road from Chennai", "Beachside cycling, Café lounging", "Colonial calmness ⭐⭐⭐", "Best: Palais de Mahe , Budget: Villa Krish"),
    ("Rishikesh", "249 201", "2,400 Km", "Laxman Jhula,Triveni Ghat,Neelkanth Temple", "₹ (Affordable)", "Haridwar connection, road travel", "Yoga retreats, River rafting", "Spiritual town with hostels ⭐⭐⭐", "Best: Divine Resort , Budget: Live Free Hostel"),
    ("Rome", "00184", "6,500 Km", "Colosseum,St. Peter’s Basilica,Trevi Fountain,Pantheon", "₹₹₹ (Expensive)", "International flights, Metro", "Vatican tours, Street food", "Tourist-centric infrastructure ⭐⭐⭐⭐", "Best: Hassler Roma , Budget: Hotel Mimosa"),
    ("Shimla", "171 001", "2,700 Km", "The Ridge,Mall Road,Jakhoo Temple,Kufri", "₹₹ (Moderate)", "By road/train from Kalka", "Snow trekking, Street shopping", "Hill station services ⭐⭐⭐", "Best: Oberoi Cecil , Budget: Hotel Prestige"),
    ("Singapore", "018989", "3,000 Km", "Marina Bay Sands,Gardens by the Bay,Sentosa,Merlion Park", "₹₹₹ (Expensive)", "Changi Airport, MRT", "Theme parks, River walks", "Cleanest city, world-class services ⭐⭐⭐⭐⭐", "Best: Marina Bay Sands , Budget: Capsule Pod"),
    ("Sydney", "2000", "10,200 Km", "Sydney Opera House,Bondi Beach,Harbour Bridge,Taronga Zoo", "₹₹₹ (Expensive)", "Sydney Airport, Buses, Trains", "Beach time, Opera tours", "Modern city amenities ⭐⭐⭐⭐", "Best: Park Hyatt , Budget: Wake Up! Sydney"),
    ("Tokyo", "100-0001", "6,000 Km", "Tokyo Tower,Shibuya Crossing,Senso-ji Temple,Akihabara", "₹₹₹ (Expensive)", "Narita Airport, Subway", "Tech shopping, Culture walks", "Super safe, modern systems ⭐⭐⭐⭐⭐", "Best: The Peninsula , Budget: Sakura Hotel"),
    ("Trivandrum", "695 001", "340 Km", "Sree Padmanabhaswamy Temple,Kovalam Beach,Napier Museum", "₹ (Affordable)", "By train, air, or road", "Temple tour, Museum visit", "Well-equipped for tourists ⭐⭐⭐", "Best: Taj Green Cove , Budget: Classic Sarovar"),
    ("Udaipur", "313 001", "2,000 Km", "City Palace,Lake Pichola,Jag Mandir,Sajjangarh Palace", "₹₹ (Moderate)", "By train, flights to Udaipur", "Lake boat rides, Palace visits", "Royal heritage, neat facilities ⭐⭐⭐⭐", "Best: Taj Lake Palace , Budget: Mewar Haveli"),
    ("Varanasi", "221 001", "2,200 Km", "Kashi Vishwanath Temple,Ganga Ghats,Sarnath", "₹ (Affordable)", "By road/train/air", "Boat ride, Temple rituals", "Holy city with basic services ⭐⭐⭐", "Best: BrijRama Palace , Budget: Ganpati Guest House")
]

    
    for city in cities:
        cursor.execute("SELECT * FROM Cities WHERE city_name = ?", (city[0],))
        if cursor.fetchone() is None:
            cursor.execute("""INSERT INTO Cities (city_name, city_pin, city_distance,attractions ,affordability ,accessibility ,activities ,amenities ,accommodation )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", city)
    connection.commit()
    connection.close()

def findCity(city):
    connection = sqlite3.connect("Cities.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Cities WHERE LOWER(city_name) = LOWER(?)", (city,))
    result = cursor.fetchone()

    connection.close()

    if result:
        (sno, name, pin, dist, attractions,affordability, accessibility, activities,amenities, accommodation) = result

        print(f"\nDetails for {name}:")
        print(f"PIN Code                    : {pin}")
        print(f"Distance from Tuticorin     : {dist}")
        print(f"Tourist Attractions         : {attractions}")


        return (name, pin, dist, attractions)
    else:
        print("\nCity not found in the database.")
        return None
