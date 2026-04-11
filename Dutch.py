#NL zonder dupe zonder cliemnt enqu&ecirc;te' post dupe

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
'rennen', 'lopen', 'springen', 'zitten', 'staan', 'liggen', 'slapen',
'wakker worden', 'eten', 'drinken', 'koken', 'bakken', 'snijden', 'hakken',
'mengen', 'roeren', 'gieten', 'grillen', 'proeven', 'bijten', 'ruiken', 'horen',
'luisteren', 'kijken', 'zien', 'aanraken', 'voelen', 'pakken', 'laten vallen',
'gooien', 'vangen', 'schoppen', 'slaan', 'optillen', 'dragen', 'slepen', 'rollen',
'draaien', 'omdraaien', 'strekken', 'breken', 'bouwen', 'vernietigen', 'openen',
'sluiten', 'typen', 'schrijven', 'lezen', 'tekenen', 'schilderen', 'inkleuren',
'wissen', 'ondertekenen', 'verzenden', 'geven', 'kopen', 'verkopen', 'betalen',
'verdienen', 'uitgeven', 'sparen', 'rijden', 'vliegen', 'zwemmen', 'duiken',
'klimmen', 'sluipen', 'verstoppen', 'zoeken', 'verliezen', 'winnen', 'proberen',
'leren', 'onderwijzen', 'studeren', 'vergeten', 'denken', 'beginnen', 'stoppen',
'doorgaan', 'pauzeren', 'wachten', 'haasten', 'aankomen', 'vertrekken', 'binnenkomen',
'verlaten', 'terugkeren', 'reizen', 'verkennen', 'wandelen', 'joggen', 'balanceren',
'zwaaien', 'schaatsen', 'skien', 'snowboarden', 'surfen', 'peddelen', 'roeien', 'zeilen',
'snorkelen', 'kajakken', 'dansen', 'zingen', 'klappen', 'fluiten', 'schreeuwen',
'fluisteren', 'lachen', 'huilen', 'glimlachen', 'fronsen', 'gapen', 'niezen', 'hoesten',
'knipperen', 'knipogen', 'aanwijzen', 'knikken', 'schudden', 'buigen', 'knuffelen', 
'kussen', 'kietelen', 'kammen', 'scheren', 'wassen', 'drogen', 'strijken', 'schoonmaken',
'vegen', 'stofzuigen', 'water geven', 'planten', 'graven', 'breien', 'lijmen', 'hameren',
'zagen', 'boren', 'meten', 'markeren', 'vastbinden', 'losmaken', 'inpakken', 'uitpakken',
'monteren', 'demonteren', 'sorteren', 'rangschikken', 'decoreren', 'ontwerpen', 'schetsen',
'overtrekken', 'krabbelen', 'onderstrepen', 'omcirkelen', 'controleren', 'labelen', 'scheuren',
'rukken', 'krabben', 'wrijven', 'kloppen', 'strelen', 'knijpen', 'porren', 'stuiteren', 'dribbelen',
'schieten', 'passen', 'blokkeren', 'verdedigen', 'aanvallen', 'scoren', 'concurreren', 'coachen',
'vieren', 'aanmoedigen', 'gillen', 'huppelen', 'overslaan', 'vallen', 'opstaan', 'knielen', 'roteren',
'flippen', 'sprinten', 'achtervolgen', 'ontsnappen', 'ontwijken', 'ijsberen', 'rondzwerven', 'slenteren',
'trekken', 'afdalen', 'stijgen', 'glijden', 'drijven', 'zinken', 'afdrijven', 'fietsen', 'masseren', 'knippen',
'drukken', 'tandenborstel', 'tandpasta', 'haarborstel', 'zonlicht', 'maanlicht', 'regenboog', 'sneeuwbal',
'brandweerwagen', 'politieauto', 'raceauto', 'ruimteschip', 'notitieboek', 'boekwinkel', 'supermarkt', 'voetbalveld',
]

words2 = [
'basketbalveld', 'tennisbaan', 'zwembad', 'slaapkamer', 'badkamer', 'klaslokaal', 'speelplaats', 'vuurtoren',
'luchthaven', 'spoorweg', 'snelweg', 'haven', 'wolkenkrabber', 'open haard', 'boekenplank', 'deurbel',
'sleutelhanger', 'portemonnee', 'handtas', 'regenjas', 'zonnebril', 'schoenveter', 'bedframe', 'koptelefoon',
'smartwatch', 'aanraakscherm', 'vingerafdruk', 'wachtwoord', 'gebruikersnaam', 'software', 'hardware',
'database', 'ontbijt', 'lunchbox', 'milkshake', 'cupcake', 'cheesecake', 'gehaktbal', 'voetballer', 'doelman',
'brandweerman', 'politieagent', 'sneeuwman', 'brievenbus', 'postbode', 'krant', 'tv-programma', 'rockband',
'popstar', 'sciencefiction', 'geschiedenisboek', 'wiskundeboek', 'creditcard', 'snelheidslimiet', 'verkeerslicht',
'verkeersbord', 'parkeerplaats', 'fietspad', 'skatepark', 'vliegtuig', 'onderzeeer', 'ruimtepak', 'telescoop',
'microscoop', 'laboratorium', 'experiment', 'theater', 'boekenkast', 'zonnebloem', 'vlinder', 'libel',
'lieveheersbeestje', 'zeepaardje', 'zeester', 'kwal', 'goudvis', 'bosbes', 'aardbei', 'braam', 'watermeloen',
'ananas', 'sneeuwvlok', 'regendruppel', 'kampvuur', 'bosbrand', 'aardbeving', 'zandstorm', 'onweersbui',
'tandenstoker', 'oorbel', 'ketting', 'armband', 'schoenendoos', 'rugzak', 'handdruk', 'toetsenbord', 'muismat',
'desktop', 'laptop', 'smartphone', 'videospel', 'bordspel', 'controller', 'kiespijn', 'zonnebrand', 'sneeuwstorm',
'hagelstorm', 'windmolen', 'waterval', 'rivieroever', 'meerzijde', 'zeekant', 'strandbal', 'zandkasteel',
'zonnescherm', 'maanopkomst', 'zonsondergang', 'zonsopgang', 'avondschemer', 'daglicht', 'bedzijde', 'boekverkoper',
'huisgenoot', 'kamergenoot', 'klasgenoot', 'teamgenoot', 'speelmaat', 'schoolplein', 'schooltas', 'schoolboek',
'werkplek', 'werkplaats', 'werkbank', 'homepage', 'notitieblok', 'bladwijzer', 'boekenclub', 'drempel', 'deurmat',
'deurknop', 'deurkozijn', 'handafdruk', 'voetafdruk', 'wimper', 'wenkbrauw', 'haarlijn', 'kapsel', 'haarband',
'haardroger', 'regenval', 'sneeuwval', 'kustlijn', 'deadline', 'levenslijn', 'omtrek', 'kopregel', 'mainframe',
'sleutelgat', 'hoeksteen', 'aandenken', 'regenwater', 'zoetwater', 'zoutwater', 'onderwater', 'oververhitten',
'ondergronds', 'ondergoed', 'onderwereld', 'achtertuin', 'voortuin', 'stoep', 'zebrapad', 'oprit', 'kinderstoel',
'leunstoel', 'rolstoel', 'bedsprei', 'laken', 'bedtijd', 'gesteente', 'brandhout', 'vuurbal', 'brandveilig',
'brandalarm', 'snowboard', 'sneeuwscooter', 'sneeuwschoen', 'sneeuwtop', 'regenstorm', 'regenwoud', 'tandenfee',
'tandeloos', 'levensduur', 'part time', 'full time', 'zonnebed', 'zonlamp', 'zonnehoed', 'zonnebrandmiddel',
'zonnecreme', 'maanwandeling', 'maansteen', 'sterrenlicht', 'regenworm', 'aardgebonden', 'aardeopkomst', 'schuurpapier',
'zandbak', 'zandsteen', 'zandkuil', 'tandafdruk', 'tandlijn', 'haarklem', 'haarelastiek', 'haargel', 'bedovertrek',
'bedpaal', 'bedrol', 'boekensteun', 'boekenwurm', 'boekenstandaard', 'boekenlijst', 'regencheck', 'regenwolk',
]

words3 = [
'regenmaker', 'sneeuwduin', 'sneeuwveld', 'Nike', 'Adidas', 'Puma', 'Apple', 'Samsung', 'Sony', 'Microsoft', 'Google',
'Amazon', 'Tesla', 'McDonalds', 'BurgerKing', 'KFC', 'Subway', 'Starbucks', 'CocaCola', 'Pepsi', 'RedBull', 'Spotify',
'Netflix', 'YouTube', 'TikTok', 'Instagram', 'WhatsApp', 'Snapchat', 'Discord', 'PlayStation', 'Xbox', 'Nintendo', 'LEGO',
'IKEA', 'H&M', 'Shell', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Ford', 'Toyota', 'Honda', 'Uber', 'Airbnb', 'PayPal',
'Visa', 'Mastercard', 'Intel', 'AMD', 'Dell', 'Nederland', 'Duitsland', 'Frankrijk', 'Spanje', 'Italie', 'Verenigde Staten',
'Brazilie', 'China', 'India', 'Australie', 'Canada', 'Rusland', 'Japan', 'Mexico', 'Argentinie', 'Zuid-Afrika', 'Egypte',
'Turkije', 'Zweden', 'Noorwegen', 'Londen', 'Parijs', 'New York', 'Tokio', 'Dubai', 'Amsterdam', 'Berlijn', 'Rome', 'Madrid',
'Sydney', 'Los Angeles', 'Chicago', 'Toronto', 'Beijing', 'Shanghai', 'Bangkok', 'Singapore', 'Hongkong', 'Barcelona', 'Moskou',
'Grand Canyon', 'Mount Everest', 'Sahara woestijn', 'Amazone rivier', 'Niagara watervallen', 'Grote Muur', 'Eiffeltoren',
'Colosseum', 'Vrijheidsbeeld', 'Big Ben', 'Golden Gate Bridge', 'Mount Fuji', 'Great Barrier Reef', 'Times Square',
'Central Park', 'Burj Khalifa', 'Stonehenge', 'Hollywood', 'Disneyland', 'Alpen', 'seconde', 'minuut', 'uur', 'dag',
'week', 'maand', 'jaar', 'decennium', 'eeuw', 'millennium', 'ochtend', 'middag', 'avond', 'nacht', 'gisteren', 'vandaag',
'morgen', 'weekend', 'werkdag', 'feestdag', 'verjaardag', 'verleden', 'heden', 'toekomst', 'Steentijd', 'Bronstijd',
'IJzertijd', 'Middeleeuwen', 'Renaissance', 'prehistorie', 'kinderjaren', 'volwassenheid', 'lente', 'zomer', 'herfst',
'winter', 'Google Maps', 'Android', 'iPhone', 'Windows', 'MacBook', 'iPad', 'AirPods', 'Play Store', 'App Store',
'Chrome', 'Firefox', 'Safari', 'Twitter', 'X', 'LinkedIn', 'Reddit', 'Twitch', 'Prime Video', 'Disney Plus', 'HBO',
'eBay', 'AliExpress', 'Wish', 'Shein', 'Uber Eats', 'Dominos', 'Pringles', 'Oreo', 'KitKat', 'Snickers', 'Mars',
'Fanta', 'Sprite', 'Monster Energy', 'Nescafe', 'Nutella', 'Heineken', 'Rolex', 'Casio', 'Gucci', 'Napoleon',
'Julius Caesar', 'Cleopatra', 'Shakespeare', 'Columbus', 'Albert Einstein', 'Stephen Hawking', 'Galileo', 'Walt Disney',
'Steve Jobs', 'Bill Clinton', 'George Washington', 'Abraham Lincoln', 'Gandhi', 'Paus Franciscus', 'Koningin Elizabeth',
'Koning Charles', 'Prins Harry', 'Elon Musk', 'Jeff Bezos', 'Mark Zuckerberg', 'Jackie Chan', 'Bruce Lee',
'Arnold Schwarzenegger', 'Keanu Reeves', 'Leonardo DiCaprio', 'Robert Downey Jr.', 'Chris Hemsworth', 'appel',
'auto', 'strand', 'dokter', 'pizza', 'school', 'telefoon', 'muziek', 'rivier', 'berg', 'leraar', 'computer', 'film',
'camera', 'fiets', 'trein', 'hotel', 'koffie', 'voetbal', 'basketbal', 'tennis', 'gitaar', 'piano', 'schilderij', 'boek',
'bibliotheek', 'internet', 'e-mail', 'scherm', 'kantoor', 'vergadering', 'project', 'vakantie', 'bruiloft', 'feest',
'concert', 'museum', 'park', 'dierentuin', 'zon', 'maan', 'ster', 'planeet', 'ruimte', 'regen', 'sneeuw', 'storm', 'wind',
'wolk', 'bos', 'woestijn', 'eiland', 'oceaan', 'meer', 'brug', 'weg', 'stad', 'dorp', 'land', 'familie', 'vriend', 'vijand',
'spel', 'verhaal', 'idee', 'droom', 'licht', 'donker', 'vuur', 'water', 'koning', 'koningin', 'soldaat', 'piraat', 'robot',
'alien', 'geest', 'monster', 'tovenaar', 'draak', 'kasteel', 'toren', 'politie', 'ziekenhuis', 'gevangenis', 'markt',
]

words4 = [
'restaurant', 'bakkerij', 'fabriek', 'bed', 'stoel', 'tafel', 'spiegel', 'raam', 'deur', 'vloer', 'plafond', 'dak',
'tuin', 'erf', 'garage', 'keuken', 'toilet', 'douche', 'gootsteen', 'koelkast', 'vriezer', 'oven', 'magnetron',
'broodrooster', 'blender', 'mes', 'vork', 'lepel', 'bord', 'kom', 'kopje', 'glas', 'fles', 'servet', 'handdoek',
'deken', 'matras', 'lamp', 'gloeilamp', 'ventilator', 'verwarming', 'afstandsbediening', 'televisie', 'radio',
'luidspreker', 'microfoon', 'statief', 'batterij', 'oplader', 'kabel', 'stekker', 'schakelaar', 'knop', 'handvat',
'slot', 'sleutel', 'koffer', 'paspoort', 'ticket', 'kaart', 'kompas', 'klok', 'horloge', 'kalender', 'alarm', 'timer',
'rekenmachine', 'pen', 'potlood', 'gum', 'marker', 'markeerstift', 'liniaal', 'schaar', 'lijm', 'plakband', 'map',
'document', 'papier', 'envelop', 'postzegel', 'tijdschrift', 'poster', 'banner', 'reclamebord', 'menu', 'recept',
'kookboek', 'dagboek', 'journaal', 'brief', 'chat', 'gesprek', 'ruzie', 'discussie', 'toespraak', 'presentatie',
'lezing', 'les', 'klas', 'cursus', 'examen', 'toets', 'quiz', 'huiswerk', 'opdracht', 'onderzoek', 'studie', 'oefening',
'motor', 'wiel', 'band', 'rem', 'dashboard', 'veiligheidsgordel', 'brandstof', 'benzine', 'diesel', 'richtingaanwijzer',
'claxon', 'metro', 'taxi', 'startbaan', 'cockpit', 'piloot', 'bagage', 'douane', 'lift', 'trap', 'gang',
'corridor', 'balkon', 'gordijn', 'kussensloop', 'kledingkast', 'hanger', 'lade', 'intercom', 'sprinkler', 'verband',
'medicijn', 'thermometer', 'stethoscoop', 'scan', 'diagnose', 'behandeling', 'operatie', 'krukken', 'ambulance',
'paramedicus', 'afspraak', 'controle', 'vaccinatie', 'injectie', 'hartslag', 'pols', 'ademhaling', 'verzekering',
'rekening', 'bon', 'contant geld', 'saldo', 'transactie', 'storting', 'opname', 'lening', 'rente', 'hypotheek',
'huur', 'betaling', 'factuur', 'budget', 'salaris', 'inkomen', 'uitgave', 'besparing', 'investering', 'bedrijf',
'zaak', 'conferentie', 'schema', 'bijlage', 'bug', 'oplossing', 'patch', 'inloggen', 'website', 'webpagina', 'browser',
'tabblad', 'geschiedenis', 'cookie', 'server', 'netwerk', 'wifi', 'router', 'signaal', 'verbinding', 'melding',
'waarschuwing', 'bericht', 'emoji', 'sticker', 'privacy', 'beveiliging', 'verificatie', 'code', 'barcode', 'scanner',
'printer', 'foto', 'galerij', 'video', 'uitzending', 'kanaal', 'abonnee', 'reactie', 'delen', 'verbannen', 'moderator',
'beheerder', 'gast', 'lid', 'groep', 'gemeenschap', 'forum', 'antwoord', 'verwijderen', 'opslaan', 'annuleren', 'bevestigen',
'formulier', 'invoer', 'uitvoer', 'gegevens', 'informatie', 'kennis', 'feit', 'waarheid', 'leugen', 'gerucht',
'nieuws', 'kop', 'artikel', 'journalist', 'verslaggever', 'interview', 'vraag', 'emotie', 'gevoel', 'gedachte',
'geheugen', 'verbeelding', 'creativiteit', 'inspiratie', 'motivatie', 'plan', 'strategie', 'beslissing', 'keuze',
'optie', 'selectie', 'voorkeur', 'smaak', 'stijl', 'mode', 'trend', 'ontwerp', 'patroon', 'kleur', 'vorm', 'grootte',
'gewicht', 'hoogte', 'lengte', 'breedte', 'diepte', 'temperatuur', 'hitte', 'kou', 'warmte', 'koelte', 'energie',
]

words5 = [
'kracht', 'snelheid', 'versnelling', 'beweging', 'positie', 'locatie', 'afstand', 'oppervlakte', 'tijd', 'moment',
'gebeurtenis', 'gelegenheid', 'festival', 'ceremonie', 'traditie', 'cultuur', 'gewoonte', 'routine', 'reis', 'avontuur',
'verkenning', 'ontdekking', 'ervaring', 'herinnering', 'verhalen vertellen', 'grap', 'humor', 'gelach', 'glimlach',
'geluk', 'verdriet', 'woede', 'angst', 'verrassing', 'shock', 'verwarring', 'begrip', 'onderwijs', 'wiskunde',
'wetenschap', 'aardrijkskunde', 'taal', 'Engels', 'Nederlands', 'Frans', 'Spaans', 'Duits', 'Italiaans', 'spreken',
'grammatica', 'woordenschat', 'zin', 'alinea', 'essay', 'titel', 'auteur', 'uitgever', 'schoolbord', 'whiteboard',
'krijt', 'toerist', 'huishouding', 'conditioner', 'afvoer', 'pijp', 'loodgieterij', 'elektriciteit', 'tapijt', 'kleed',
'paraplu', 'jeans', 'jas', 'trui', 'hoodie', 'sneakers', 'sandalen', 'pantoffels', 'sokken', 'riem', 'ring', 'bluetooth',
'oordopjes', 'tablet', 'resolutie', 'helderheid', 'volume', 'afspeellijst', 'lied', 'album', 'artiest', 'podcast',
'aflevering', 'geluid', 'stilte', 'achtergrond', 'voorgrond', 'focus', 'onscherpte', 'bewerken', 'filter', 'contrast',
'verzadiging', 'belichting', 'zoom', 'script', 'regisseur', 'producent', 'studio', 'kostuum', 'make-up', 'animatie',
'tekenfilm', 'personage', 'verhaallijn', 'plot', 'einde', 'begin', 'midden', 'twist', 'climax', 'conflict', 'probleem',
'uitdaging', 'moeilijkheid', 'succes', 'mislukking', 'winst', 'verlies', 'score', 'punt', 'doel', 'doelwit', 'poging',
'inspanning', 'resultaat', 'uitkomst', 'prestatie', 'beloning', 'prijs', 'medaille', 'trofee', 'competitie', 'wedstrijd',
'toernooi', 'seizoen', 'gameplay', 'vaardigheid', 'talent', 'vermogen', 'zwakte', 'training', 'coach', 'team', 'speler',
'tegenstander', 'scheidsrechter', 'regel', 'straf', 'overtreding', 'schop', 'pass', 'shot', 'verdediging', 'aanval',
'tegenaanval', 'formatie', 'fans', 'juichen', 'gezang', 'viering', 'overwinning', 'nederlaag', 'gelijkspel', 'scorebord',
'fluit', 'rust', 'eindtijd', 'wissel', 'bank', 'kluis', 'uniform', 'shirt', 'nummer', 'aanvoerder', 'leider', 'assistent',
'manager', 'club', 'transfer', 'contract', 'sponsor', 'advertentie', 'reclame', 'marketing', 'promotie', 'campagne', 'product',
'dienst', 'klant', 'feedback', 'beoordeling', 'waardering', 'vragenlijst', 'analyse', 'rapport', 'samenvatting', 'overzicht',
'detail', 'beschrijving', 'voorbeeld', 'bewijs', 'argument', 'debat', 'introductie', 'begroeting', 'afscheid', 'tot ziens',
'hallo', 'welkom', 'bedankt', 'alsjeblieft', 'sorry', 'hulp', 'ondersteuning', 'assistentie', 'begeleiding', 'advies',
'tip', 'suggestie', 'aanbeveling', 'instructie', 'richting', 'gids', 'handleiding', 'regelboek', 'beleid', 'wet',
'regelgeving', 'vereiste', 'voorwaarde', 'overeenkomst', 'handtekening', 'goedkeuring', 'afwijzing', 'bevestiging',
'ontkenning', 'acceptatie', 'indiening', 'aanvraag', 'registratie', 'reset', 'gps', 'route', 'bestemming', 'vertraging',
'aankondiging', 'echo', 'icoon', 'symbool', 'ingang', 'poort', 'hek', 'muur', 'grens', 'limiet', 'rand', 'hoek',
'centrum', 'zijde', 'voorkant', 'achterkant', 'bovenkant', 'onderkant', 'binnen', 'buiten', 'dichtbij', 'ver',
'dicht', 'menigte', 'kruispunt', 'rotonde', 'monteur', 'gereedschapskist'
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

            word_to_add = my_random_choice(selected_not_used_list)
            selected_not_used_list.remove(word_to_add)
            Current_words.append(word_to_add)

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