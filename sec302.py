#post zdupe engels klaar voor dwonload
import random

def my_random_choice(a_list):
    random_index = random.randint(0, len(a_list) - 1)
    return a_list[random_index]

def custom_shuffle(a_list):
    # Implements a shuffle without random.shuffle()
    n = len(a_list)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)  # Pick a random index from 0 to i
        a_list[i], a_list[j] = a_list[j], a_list[i]  # Swap elements

def puntjes():
    i = 0
    while i < 6:
        print("")
        i = i + 1

def _input():
    global running1
    global running2
    global running3
    global new_game
    global running1_on

    user_input = input()

    if user_input == '-':
        puntjes()
        print('Game ended.')

        if running1_on == 0:
            print("Again? - 1")

        print("New game? - 2")
        print("Stop game? - 3")

        while True:
            choice = input()

            if choice == '1':
                if running1_on == 0:
                    print("Starting new round...")
                    partial_reset()
                    running1 = False
                    running2 = True
                    return "NEW_ROUND"
                else:
                    puntjes()
                    print("Invalid input.")
                    print("New game? - 2")
                    print("Stop game? - 3")

            elif choice == '2':
                print("Starting new game...")
                full_reset()
                running1 = True
                running2 = False
                new_game = True
                return "NEW_GAME"

            elif choice == '3':
                print("Goodbye!")
                running1 = False
                running2 = False
                running3 = False
                return "STOP_GAME"

            else:
                puntjes()
                print("Invalid input.")
                if running1_on == 0:
                    print("Again? - 1")
                print("New game? - 2")
                print("Stop game? - 3")

    return user_input

def show_points():
    puntjes()

    n_local = 1
    while n_local <= Players:
        if n_local == 1:
            print('Blue : ' + str(Blue_points))
        elif n_local == 2:
            print('Red : ' + str(Red_points))
        elif n_local == 3:
            print('Green : ' + str(Green_points))
        elif n_local == 4:
            print('Yellow : ' + str(Yellow_points))
        elif n_local == 5:
            print('Orange : ' + str(Orange_points))

        n_local = n_local + 1

    print('EXE to continue')
    _input()
    puntjes()

def show_words():
    puntjes()
    for word in Current_words:
        print(word)

def wait(seconds):
  timers = seconds*137500
  for _ in range(timers):
    pass

def full_reset():
    global words_not_used1
    global words_not_used2
    global words_not_used3
    global words_not_used4
    global words_not_used5
    global Players
    global Players_list
    global Players_team_list
    global Current_words
    global Team
    global Blue_points
    global Red_points
    global Green_points
    global Yellow_points
    global Orange_points
    global n

    words_not_used1 = words1.copy()
    custom_shuffle(words_not_used1)
    words_not_used2 = words2.copy()
    custom_shuffle(words_not_used2)
    words_not_used3 = words3.copy()
    custom_shuffle(words_not_used3)
    words_not_used4 = words4.copy()
    custom_shuffle(words_not_used4)
    words_not_used5 = words5.copy()
    custom_shuffle(words_not_used5)
    Players = 0
    Players_list = []
    Players_team_list = ['Blue', 'Red', 'Green', 'Yellow', 'Orange']
    Current_words = []
    Team = 0

    Blue_points = 0
    Red_points = 0
    Green_points = 0
    Yellow_points = 0
    Orange_points = 0

    n = 0

def partial_reset():
    global Blue_points
    global Red_points
    global Green_points
    global Yellow_points
    global Orange_points
    global n

    Blue_points = 0
    Red_points = 0
    Green_points = 0
    Yellow_points = 0
    Orange_points = 0
    n = 0

words1 = [
    'running', 'walking', 'jumping', 'sitting', 'standing', 'lying', 'sleeping', 'waking',
    'eating', 'drinking', 'cooking', 'baking', 'cutting', 'chopping', 'mixing', 'stirring',
    'pouring', 'boiling', 'frying', 'grilling', 'tasting', 'biting', 'smelling', 'hearing',
    'listening', 'watching', 'looking', 'seeing', 'touching', 'feeling', 'grabbing', 'dropping',
    'throwing', 'catching', 'kicking', 'hitting', 'lifting', 'carrying', 'dragging', 'rolling',
    'spinning', 'turning', 'stretching', 'breaking', 'building', 'destroying', 'opening', 'closing',
    'typing', 'writing', 'reading', 'drawing', 'painting', 'coloring', 'erasing', 'signing',
    'sending', 'giving', 'buying', 'selling', 'paying', 'earning', 'spending', 'saving',
    'driving', 'riding', 'flying', 'swimming', 'diving', 'climbing', 'sneaking', 'hiding',
    'searching', 'losing', 'winning', 'trying', 'learning', 'teaching', 'studying', 'forgetting',
    'thinking', 'starting', 'stopping', 'beginning', 'continuing', 'pausing', 'waiting', 'hurrying',
    'rushing', 'arriving', 'leaving', 'entering', 'exiting', 'returning', 'traveling', 'exploring',
    'hiking', 'jogging', 'balancing', 'swinging', 'skating', 'skiing', 'snowboarding', 'surfing',
    'paddling', 'rowing', 'sailing', 'snorkeling', 'kayaking', 'dancing', 'singing', 'clapping',
    'whistling', 'shouting', 'whispering', 'laughing', 'crying', 'smiling', 'frowning', 'yawning',
    'sneezing', 'coughing', 'blinking', 'winking', 'pointing', 'nodding', 'shaking', 'waving',
    'bowing', 'hugging', 'kissing', 'tickling', 'combing', 'shaving', 'washing', 'drying',
    'ironing', 'cleaning', 'sweeping', 'vacuuming', 'watering', 'planting', 'digging', 'knitting',
    'gluing', 'hammering', 'sawing', 'drilling', 'measuring', 'marking', 'tying', 'untying',
    'wrapping', 'unwrapping', 'assembling', 'disassembling', 'sorting', 'arranging', 'decorating', 'designing',
    'sketching', 'tracing', 'scribbling', 'highlighting', 'underlining', 'circling', 'checking', 'labeling',
    'tearing', 'ripping', 'scratching', 'rubbing', 'patting', 'pinching', 'poking',
    'bouncing', 'dribbling', 'shooting', 'passing', 'blocking', 'defending', 'attacking', 'scoring',
    'competing', 'coaching', 'celebrating', 'cheering', 'screaming', 'hopping', 'skipping', 'falling',
    'rising', 'kneeling', 'rotating', 'flipping', 'vaulting', 'leaping', 'sprinting', 'chasing',
    'escaping', 'dodging', 'pacing', 'wandering', 'strolling', 'trekking', 'descending', 'ascending',
    'gliding', 'floating', 'sinking', 'drifting', 'cycling', 'biking', 'massaging', 'snapping',
    'pressing', 'toothbrush', 'toothpaste', 'hairbrush', 'sunlight', 'moonlight', 'rainbow', 'snowball',
    'firetruck', 'policecar', 'racecar', 'spaceship', 'notebook', 'bookstore', 'supermarket', 'soccer ield',
    'basketball court', 'tennis court', 'swimming pool', 'bedroom', 'bathroom', 'classroom', 'playground', 'lighthouse',
    'airport', 'railway', 'highway', 'seaport', 'skyscraper', 'fireplace', 'bookshelf', 'doorbell',
    'keychain', 'wallet', 'handbag', 'raincoat', 'sunglasses', 'shoelace', 'bedframe', 'headphones',
    'smartwatch', 'touchscreen', 'fingerprint', 'password', 'username', 'software', 'hardware', 'database',
    'breakfast', 'lunchbox', 'milkshake', 'cupcake', 'cheesecake', 'meatball', 'footballer', 'goalkeeper',
    'fireman', 'policeman', 'snowman', 'mailbox', 'mailman', 'newspaper', 'tv show', 'rockband',
    'popstar', 'sciencefiction', 'history book', 'mathbook', 'creditcard', 'speedlimit', 'traffic light'
]


words2 = [
    'roadsign', 'parkinglot', 'bikelane', 'skatepark', 'airplane', 'submarine', 'spacesuit', 'telescope',
    'microscope', 'laboratory', 'experiment', 'theater', 'bookcase', 'sunflower', 'butterfly', 'dragonfly',
    'ladybug', 'seahorse', 'starfish', 'jellyfish', 'goldfish', 'blueberry', 'strawberry', 'blackberry',
    'watermelon', 'pineapple', 'snowflake', 'raindrop', 'campfire', 'wildfire', 'earthquake', 'sandstorm',
    'thunderstorm', 'toothpick', 'earring', 'necklace', 'bracelet', 'shoebox', 'backpack', 'handshake',
    'keyboard', 'mousepad', 'desktop', 'laptop', 'smartphone', 'videogame', 'boardgame', 'controller',
    'toothache', 'sunburn', 'snowstorm', 'hailstorm', 'windmill', 'waterfall', 'riverbank', 'lakeside',
    'seaside', 'beachball', 'sandcastle', 'sunshade', 'moonrise', 'sunset', 'sunrise', 'nightfall',
    'daylight', 'bedside', 'bookseller', 'housemate', 'roommate', 'classmate', 'teammate', 'playmate',
    'schoolyard', 'schoolbag', 'schoolbook', 'workplace', 'workshop', 'workbench', 'homepage', 'notepad',
    'bookmark', 'bookclub', 'doorstep', 'doormat', 'doorknob', 'doorframe', 'handprint', 'footprint',
    'eyelash', 'eyebrow', 'hairline', 'haircut', 'hairband', 'hairdryer', 'rainfall', 'snowfall',
    'coastline', 'deadline', 'lifeline', 'outline', 'headline', 'mainframe', 'keyhole', 'keystone',
    'keepsake', 'rainwater', 'freshwater', 'saltwater', 'underwater', 'overheat', 'underground', 'underwear',
    'underworld', 'backyard', 'frontyard', 'sidewalk', 'crosswalk', 'driveway', 'highchair', 'armchair',
    'wheelchair', 'bedspread', 'bedsheet', 'bedtime', 'bedrock', 'firewood', 'fireball', 'fireproof',
    'firefighter', 'firealarm', 'snowboard', 'snowmobile', 'snowshoe', 'snowcap', 'rainstorm', 'rainforest',
    'toothfairy', 'toothless', 'lifetime', 'parttime', 'fulltime', 'sunbed', 'sunlamp', 'sunhat',
    'sunblock', 'suncream', 'moonwalk', 'moonstone', 'starlight', 'starship', 'earthworm', 'earthbound',
    'earthrise', 'sandpaper', 'sandbox', 'sandstone', 'sandpit', 'toothmark', 'toothline', 'hairclip',
    'hairtie', 'hairgel', 'bedcover', 'bedpost', 'bedroll', 'bookend', 'bookshop', 'bookworm',
    'bookstand', 'rain check', 'raincloud', 'rainmaker', 'snowdrift', 'snowfield', 'Nike',
    'Adidas', 'Puma', 'Apple', 'Samsung', 'Sony', 'Microsoft', 'Google', 'Amazon',
    'Tesla', 'McDonalds', 'Burger King', 'KFC', 'Subway', 'Starbucks', 'CocaCola', 'Pepsi',
    'RedBull', 'Spotify', 'Netflix', 'YouTube', 'TikTok', 'Instagram', 'WhatsApp', 'Snapchat',
    'Discord', 'PlayStation', 'Xbox', 'Nintendo', 'LEGO', 'IKEA', 'H&M', 'Shell',
    'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Ford', 'Toyota', 'Honda', 'Uber',
    'Airbnb', 'PayPal', 'Visa', 'Mastercard', 'Intel', 'AMD', 'Dell', 'Netherlands',
    'Germany', 'France', 'Spain', 'Italy', 'United States', 'Brazil', 'China', 'India',
    'Australia', 'Canada', 'Russia', 'Japan', 'Mexico', 'Argentina', 'South Africa', 'Egypt',
    'Turkey', 'Sweden', 'Norway', 'London', 'Paris', 'New York', 'Tokyo', 'Dubai',
    'Amsterdam', 'Berlin', 'Rome', 'Madrid', 'Sydney', 'LosAngeles', 'Chicago', 'Toronto',
    'Beijing', 'Shanghai', 'Bangkok', 'Singapore', 'HongKong', 'Barcelona', 'Moscow', 'Grand Canyon',
    'Mount Everest', 'Sahara desert', 'Amazon river', 'Niagara falls', 'Great Wall of China', 'Eiffel Tower', 'Colosseum', 'Statue of Liberty',
    'Big Ben'
]


words3 = [
    'Golden Gate bridge', 'Mount Fuji', 'Great Barrier reef', 'Times square', 'Central Park', 'Burj Khalifa', 'Stonehenge', 'Hollywood',
    'Disneyland', 'Alps', 'second', 'minute', 'hour', 'day', 'week', 'month',
    'year', 'decade', 'century', 'millennium', 'morning', 'afternoon', 'evening', 'night',
    'yesterday', 'today', 'tomorrow', 'weekend', 'weekday', 'holiday', 'birthday', 'past',
    'present', 'future', 'Stone age', 'Bronze age', 'Iron age', 'Middle ages', 'Renaissance', 'prehistory',
    'childhood', 'adulthood', 'spring', 'summer', 'autumn', 'winter', 'Google Maps', 'Android',
    'iPhone', 'Windows', 'MacBook', 'iPad', 'AirPods', 'PlayStore', 'AppStore', 'Chrome',
    'Firefox', 'Safari', 'Twitter', 'X', 'LinkedIn', 'Reddit', 'Twitch', 'Prime Video',
    'DisneyPlus', 'HBO', 'eBay', 'AliExpress', 'Wish', 'Shein', 'UberEats', 'Dominos',
    'Pringles', 'Oreo', 'KitKat', 'Snickers', 'Mars', 'Fanta', 'Sprite', 'Monster Energy',
    'Nescafe', 'Nutella', 'Heineken', 'Rolex', 'Casio', 'Gucci', 'Napoleon', 'Julius Caesar',
    'Cleopatra', 'Shakespeare', 'Columbus', 'Albert Einstein', 'Stephen Hawking', 'Galileo', 'Walt Disney', 'Steve Jobs',
    'Bill Clinton', 'George Washington', 'Abraham Lincoln', 'Gandhi', 'Pope Francis', 'Queen Elizabeth', 'King Charles', 'Prince Harry',
    'Elon Musk', 'Jeff Bezos', 'Mark Zuckerberg', 'Jackie Chan', 'Bruce Lee', 'ArnoldSchwarzenegger', 'Keanu Reeves', 'Leonardo DiCaprio',
    'Robert Downey Jr.', 'Chris Hemsworth', 'car', 'beach', 'doctor', 'pizza', 'school', 'phone',
    'music', 'river', 'mountain', 'teacher', 'computer', 'movie', 'camera', 'bicycle',
    'train', 'hotel', 'coffee', 'football', 'basketball', 'tennis', 'guitar', 'piano',
    'book', 'library', 'internet', 'email', 'screen', 'office', 'meeting', 'project',
    'wedding', 'party', 'concert', 'museum', 'park', 'zoo', 'sun', 'moon',
    'star', 'planet', 'space', 'rain', 'snow', 'storm', 'wind', 'cloud',
    'forest', 'desert', 'island', 'ocean', 'lake', 'bridge', 'road', 'city',
    'village', 'country', 'family', 'friend', 'enemy', 'game', 'story', 'idea',
    'dream', 'light', 'dark', 'fire', 'water', 'king', 'queen', 'soldier',
    'pirate', 'robot', 'alien', 'ghost', 'monster', 'wizard', 'dragon', 'castle',
    'tower', 'police', 'hospital', 'prison', 'market', 'restaurant', 'bakery', 'factory',
    'bed', 'chair', 'table', 'mirror', 'window', 'door', 'floor', 'ceiling',
    'roof', 'garden', 'yard', 'garage', 'kitchen', 'toilet', 'shower', 'sink',
    'fridge', 'freezer', 'oven', 'microwave', 'toaster', 'blender', 'knife', 'fork',
    'spoon', 'plate', 'bowl', 'cup', 'glass', 'bottle', 'napkin', 'towel',
    'blanket', 'pillow', 'mattress'
]


words4 = [
    'lamp', 'lightbulb', 'fan', 'heater', 'remote', 'television', 'radio', 'speaker',
    'microphone', 'tripod', 'battery', 'charger', 'cable', 'plug', 'switch', 'button',
    'handle', 'lock', 'key', 'purse', 'suitcase', 'passport', 'ticket', 'map',
    'compass', 'clock', 'watch', 'calendar', 'alarm', 'timer', 'calculator', 'pen',
    'pencil', 'eraser', 'marker', 'highlighter', 'ruler', 'scissors', 'glue', 'tape',
    'folder', 'document', 'paper', 'envelope', 'stamp', 'magazine', 'poster', 'banner',
    'sign', 'billboard', 'menu', 'recipe', 'cookbook', 'diary', 'journal', 'letter',
    'chat', 'conversation', 'argument', 'discussion', 'speech', 'presentation', 'lecture', 'lesson',
    'class', 'course', 'exam', 'test', 'quiz', 'homework', 'assignment', 'research',
    'study', 'practice', 'engine', 'wheel', 'tire', 'brake', 'dashboard', 'seatbelt',
    'fuel', 'gasoline', 'diesel', 'indicator', 'horn', 'taxi', 'runway', 'cockpit',
    'pilot', 'luggage', 'customs', 'elevator', 'stairs', 'hallway', 'corridor', 'balcony',
    'curtain', 'pillowcase', 'wardrobe', 'hanger', 'drawer', 'intercom', 'sprinkler', 'bandage',
    'medicine', 'thermometer', 'stethoscope', 'x-ray', 'scan', 'diagnosis', 'treatment', 'surgery',
    'crutches', 'ambulance', 'paramedic', 'appointment', 'checkup', 'vaccination', 'injection', 'heartbeat',
    'pulse', 'breathing', 'insurance', 'bill', 'receipt', 'cash', 'balance', 'transaction',
    'deposit', 'withdrawal', 'loan', 'interest', 'mortgage', 'rent', 'payment', 'invoice',
    'budget', 'salary', 'income', 'expense', 'investment', 'company', 'business', 'conference',
    'schedule', 'attachment', 'bug', 'fix', 'patch', 'login', 'website', 'webpage',
    'browser', 'tab', 'history', 'cookie', 'server', 'network', 'wifi', 'router',
    'signal', 'connection', 'notification', 'alert', 'message', 'emoji', 'sticker', 'privacy',
    'security', 'verification', 'code', 'barcode', 'scanner', 'printer', 'photo', 'gallery',
    'video', 'recording', 'broadcast', 'channel', 'subscriber', 'comment', 'share', 'block',
    'ban', 'moderator', 'admin', 'guest', 'member', 'group', 'community', 'forum',
    'post', 'reply', 'delete', 'save', 'cancel', 'confirm', 'form', 'input',
    'output', 'data', 'information', 'knowledge', 'fact', 'truth', 'lie', 'rumor',
    'news', 'article', 'journalist', 'reporter', 'interview', 'question', 'answer', 'response',
    'reaction', 'emotion', 'thought', 'memory', 'imagination', 'creativity', 'inspiration', 'motivation',
    'plan', 'strategy', 'decision', 'choice', 'option', 'selection', 'preference', 'taste',
    'style', 'fashion', 'trend', 'design', 'pattern', 'color', 'shape', 'size',
    'weight', 'height', 'length', 'width', 'depth', 'temperature', 'heat', 'cold',
    'warmth', 'coolness', 'energy', 'power', 'force', 'speed', 'velocity', 'acceleration',
    'motion', 'movement', 'position', 'location', 'distance', 'area', 'time', 'moment',
    'event', 'occasion', 'festival', 'ceremony', 'tradition'
]


words5 = [
    'culture', 'custom', 'habit', 'routine', 'vacation', 'trip', 'journey', 'adventure',
    'exploration', 'discovery', 'experience', 'storytelling', 'joke', 'humor', 'laughter', 'smile',
    'happiness', 'sadness', 'anger', 'fear', 'surprise', 'shock', 'confusion', 'understanding',
    'education', 'math', 'science', 'geography', 'language', 'english', 'dutch', 'french',
    'spanish', 'german', 'italian', 'speaking', 'grammar', 'vocabulary', 'sentence', 'paragraph',
    'essay', 'title', 'author', 'publisher', 'blackboard', 'whiteboard', 'chalk', 'tourist',
    'housekeeping', 'conditioner', 'drain', 'pipe', 'plumbing', 'electricity', 'bulb', 'carpet',
    'rug', 'umbrella', 'jeans', 'jacket', 'sweater', 'hoodie', 'sneakers', 'sandals',
    'slippers', 'socks', 'belt', 'ring', 'bluetooth', 'earbuds', 'tablet', 'resolution',
    'brightness', 'volume', 'playlist', 'song', 'album', 'artist', 'podcast', 'episode',
    'noise', 'silence', 'background', 'foreground', 'focus', 'blur', 'editing', 'filter',
    'contrast', 'saturation', 'exposure', 'zoom', 'shot', 'scene', 'script', 'director',
    'producer', 'studio', 'costume', 'makeup', 'animation', 'cartoon', 'character', 'storyline',
    'plot', 'ending', 'middle', 'twist', 'climax', 'conflict', 'solution', 'problem',
    'challenge', 'difficulty', 'success', 'failure', 'win', 'loss', 'score', 'point',
    'goal', 'target', 'aim', 'attempt', 'effort', 'result', 'outcome', 'achievement',
    'reward', 'prize', 'medal', 'trophy', 'competition', 'contest', 'tournament', 'league',
    'season', 'match', 'gameplay', 'skill', 'talent', 'ability', 'strength', 'weakness',
    'training', 'coach', 'team', 'player', 'opponent', 'referee', 'rule', 'penalty',
    'foul', 'kick', 'pass', 'defense', 'attack', 'counterattack', 'formation', 'fans',
    'cheer', 'chant', 'celebration', 'victory', 'defeat', 'draw', 'scoreboard', 'whistle',
    'halftime', 'substitution', 'bench', 'locker', 'uniform', 'jersey', 'number', 'captain',
    'leader', 'assistant', 'manager', 'club', 'transfer', 'contract', 'sponsor', 'advertisement',
    'commercial', 'marketing', 'promotion', 'campaign', 'product', 'service', 'customer', 'client',
    'feedback', 'review', 'rating', 'survey', 'questionnaire', 'analysis', 'report', 'summary',
    'overview', 'detail', 'description', 'example', 'evidence', 'proof', 'debate', 'introduction',
    'greeting', 'farewell', 'goodbye', 'hello', 'welcome', 'thanks', 'please', 'sorry',
    'help', 'support', 'assistance', 'guidance', 'advice', 'tip', 'suggestion', 'recommendation',
    'instruction', 'direction', 'guide', 'manual', 'rulebook', 'policy', 'law', 'regulation',
    'requirement', 'condition', 'agreement', 'signature', 'approval', 'rejection', 'confirmation', 'denial',
    'acceptance', 'submission', 'application', 'registration', 'reset', 'gps', 'route', 'destination',
    'delay', 'announcement', 'echo', 'icon', 'symbol', 'entrance', 'gate', 'fence',
    'wall', 'barrier', 'border', 'limit', 'edge', 'corner', 'center', 'side',
    'front', 'back', 'top', 'bottom', 'inside', 'outside', 'near', 'far',
    'close', 'crowd', 'intersection', 'roundabout', 'mechanic', 'toolbox'
]

def clean_lists(lists):
    for i in range(len(lists)):
        seen = set()
        new_list = []
        for word in lists[i]:
            if word not in seen:
                new_list.append(word)
                seen.add(word)
        lists[i][:] = new_list

clean_lists([words1, words2, words3, words4, words5])

words_not_used1 = words1.copy()
words_not_used2 = words2.copy()
words_not_used3 = words3.copy()
words_not_used4 = words4.copy()
words_not_used5 = words5.copy()

Players = 0
Players_list = []
Players_team_list = ['Blue', 'Red', 'Green', 'Yellow', 'Orange']
Current_words = []
Team = 0

Blue_points = 0
Red_points = 0
Green_points = 0
Yellow_points = 0
Orange_points = 0

n = 0
new_game = False
running1 = True
running2 = True
running3 = True
running1_on = 0

while running3:

    puntjes()

    while running1:
        running1_on = 1
        full_reset()
        new_game = False

        print('How many teams?')

        try:
            Players = int(input())

            if Players > 1:
                if Players <= 5:
                    Players_list = list(range(1, Players + 1))
                    break
                else:
                    puntjes()
                    print('Enter 2-5.')
            else:
                puntjes()
                print('Enter 2-5.')

        except:
            puntjes()
            print('Enter 2-5.')

    show_points()

    n = 0
    running1_on = 0
    running2 = True

    if running3 == False:
      break
    if running1 == False:
      running2 = True
      running1 = True

    if new_game:
        continue

    while running2:

        n = n + 1

        if n > Players:
            n = 1

        Team = n

        if Blue_points >= 30:
            print('Blue won!')
            input()
            show_points()
        if Red_points >= 30:
            print('Red won!')
            input()
            show_points()
        if Green_points >= 30:
            print('Green won!')
            input()
            show_points()
        if Yellow_points >= 30:
            print('Yellow won!')
            input()
            show_points()
        if Orange_points >= 30:
            print('Orange won!')
            input()
            show_points()

        if n == 1:
            print("Blue's turn")
        elif n == 2:
            print("Red's turn")
        elif n == 3:
            print("Green's turn")
        elif n == 4:
            print("Yellow's turn")
        elif n == 5:
            print("Orange's turn")

        print('- = end game')
        print('EXE to continue')

        cmd = _input()

        if cmd == "NEW_ROUND":
            running1 = False
            running2 = True
            break
        elif cmd == "NEW_GAME":
            running1 = True
            running2 = False
            new_game = True
            break
        elif cmd == "STOP_GAME":
            running3 = False
            break

        Current_words = []

        words_not_used_lists = [words_not_used1, words_not_used2, words_not_used3, words_not_used4, words_not_used5]
        original_words_lists = [words1, words2, words3, words4, words5]

        i = 0
        while i < 5:
            list_index = random.randint(0, 4) # Choose index from 0 to 4
            selected_not_used_list = words_not_used_lists[list_index]
            selected_original_list = original_words_lists[list_index]

            if not selected_not_used_list: # If the list is empty, replenish and shuffle
                selected_not_used_list[:] = selected_original_list.copy()
                custom_shuffle(selected_not_used_list)
                # Update the global list reference (necessary for lists of lists)
                if list_index == 0: words_not_used1 = selected_not_used_list
                elif list_index == 1: words_not_used2 = selected_not_used_list
                elif list_index == 2: words_not_used3 = selected_not_used_list
                elif list_index == 3: words_not_used4 = selected_not_used_list
                elif list_index == 4: words_not_used5 = selected_not_used_list

            word = my_random_choice(selected_not_used_list)
            selected_not_used_list.remove(word)
            Current_words.append(word)

            i = i + 1

        timer = 30
        puntjes()
        show_words()
        print('Exe to start timer?')

        cmd = _input()

        if cmd == "NEW_ROUND":
            partial_reset()
            running1 = False
            running2 = True
            break
        elif cmd == "NEW_GAME":
            full_reset()
            running1 = True
            new_game = True
            break
        elif cmd == "STOP_GAME":
            running3 = False
            break

        wait(30)

        while True:
            print('How many points?')

            user_value = _input()

            if user_value == "NEW_ROUND":
                partial_reset()
                running1 = False
                break
            elif user_value == "NEW_GAME":
                full_reset()
                running1 = True
                new_game = True
                break
            elif user_value == "STOP_GAME":
                running3 = False
                break

            try:
                Points_given = int(user_value)

                if Points_given >= 0:
                    if Points_given <= 5:
                        break
                    else:
                        puntjes()
                        print('Enter 0-5.')
                else:
                    puntjes()
                    print('Enter 0-5.')

            except:
                puntjes()
                print('Enter 0-5.')

        if running3 == False:
            break
        if new_game == True:
            break
        if running2 == False:
            break

        if n == 1:
            Blue_points = Blue_points + Points_given
        elif n == 2:
            Red_points = Red_points + Points_given
        elif n == 3:
            Green_points = Green_points + Points_given
        elif n == 4:
            Yellow_points = Yellow_points + Points_given
        elif n == 5:
            Orange_points = Orange_points + Points_given

        show_points()