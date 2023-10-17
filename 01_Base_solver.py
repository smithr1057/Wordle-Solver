# Functions

# Lets you change color of printed text easily
def color_text(text, color):
    # Code was found using chatGpt using prompt
    # "Python function that allows me to change the text color"
    # Code was changed a bit as some parts were unneeded

    # list of colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'forest_green': '\033[32m'
    }

    # Prints text in specified color
    print(f"{colors[color]}{text}\033[0m")


# Adds decorations to selected text
def statement_generator(statement, decoration, lines=None):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    # use 3 lines for headings / heavy decoration
    if lines == 3:
        new_statement = f"{top_bottom}\n{statement}\n{top_bottom}"

    else:
        # default is one single line
        new_statement = statement

    return new_statement


# checks user answers with valid answer
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        color_text(error, 'red')
        print()


# Main routine

# lists
word_list = [
    "aback", "assay", "blurb", "chafe", "craze", "draft", "faint", "front", "guess", "itchy", "lucky", "music",
    "perch", "queer", "rupee", "shrug", "sperm", "swear", "track", "vital", "abase", "asset", "blurt", "chaff",
    "crazy", "drain", "fairy", "frost", "guest", "ivory", "lumen", "musky", "peril", "quell", "rural", "shuck",
    "spice", "sweat", "tract", "vivid", "abate", "atoll", "blush", "chain", "creak", "drake", "faith", "froth",
    "guide", "jaunt", "lumpy", "musty", "perky", "query", "rusty", "shunt", "spicy", "sweep", "trade", "vixen",
    "abbey", "atone", "board", "chair", "cream", "drama", "fancy", "frown", "guild", "jazzy", "lunar", "myrrh",
    "pesky", "quest", "sadly", "shush", "spied", "sweet", "trail", "vocal", "abbot", "attic", "boast", "chalk",
    "credo", "drank", "fanny", "froze", "guile", "jelly", "lunch", "nadir", "pesto", "queue", "safer", "shyly",
    "spiel", "swell", "train", "vodka", "abhor", "audio", "bobby", "champ", "creed", "drape", "farce", "fruit",
    "guilt", "jerky", "lunge", "naive", "petal", "quick", "saint", "siege", "spike", "swept", "trait", "vogue",
    "abide", "audit", "boney", "chant", "creek", "drawl", "fatal", "fudge", "guise", "jetty", "lupus", "nanny",
    "petty", "quiet", "salad", "sieve", "spiky", "swift", "tramp", "voice", "abled", "augur", "bongo", "chaos",
    "creep", "drawn", "fatty", "fugue", "gulch", "jewel", "lurch", "nasal", "phase", "quill", "sally", "sight",
    "spill", "swill", "trash", "voila", "abode", "aunty", "bonus", "chard", "creme", "dread", "fault", "fully",
    "gully", "jiffy", "lurid", "nasty", "phone", "quilt", "salon", "sigma", "spilt", "swine", "trawl", "vomit",
    "abort", "avail", "booby", "charm", "crepe", "dream", "fauna", "fungi", "gumbo", "joint", "lusty", "natal",
    "phony", "quirk", "salsa", "silky", "spine", "swing", "tread", "voter", "about", "avert", "boost", "chart",
    "crept", "dress", "favor", "funky", "gummy", "joist", "lying", "naval", "photo", "quite", "salty", "silly",
    "spiny", "swirl", "treat", "vouch", "above", "avian", "booth", "chase", "cress", "dried", "feast", "funny",
    "guppy", "joker", "lymph", "navel", "piano", "quota", "salve", "since", "spire", "swish", "trend", "vowel",
    "abuse", "avoid", "booty", "chasm", "crest", "drier", "fecal", "furor", "gusto", "jolly", "lyric", "needy",
    "picky", "quote", "salvo", "sinew", "spite", "swoon", "triad", "vying", "abyss", "await", "booze", "cheap",
    "crick", "drift", "feign", "furry", "gusty", "joust", "macaw", "neigh", "piece", "quoth", "sandy", "singe",
    "splat", "swoop", "trial", "wacky", "acorn", "awake", "boozy", "cheat", "cried", "drill", "fella", "fussy",
    "gypsy", "judge", "macho", "nerdy", "piety", "rabbi", "saner", "siren", "split", "sword", "tribe", "wafer",
    "acrid", "award", "borax", "check", "crier", "drink", "felon", "fuzzy", "habit", "juice", "macro", "nerve",
    "piggy", "rabid", "sappy", "sissy", "spoil", "swore", "trice", "wager", "actor", "aware", "borne", "cheek",
    "crime", "drive", "femme", "gaffe", "hairy", "juicy", "madam", "never", "pilot", "racer", "sassy", "sixth",
    "spoke", "sworn", "trick", "wagon", "acute", "awash", "bosom", "cheer", "crimp", "droit", "femur", "gaily",
    "halve", "jumbo", "madly", "newer", "pinch", "radar", "satin", "sixty", "spoof", "swung", "tried", "waist",
    "adage", "awful", "bossy", "chess", "crisp", "droll", "fence", "gamer", "handy", "jumpy", "mafia", "newly",
    "piney", "radii", "satyr", "skate", "spook", "synod", "tripe", "waive", "adapt", "awoke", "botch", "chest",
    "croak", "drone", "feral", "gamma", "happy", "junta", "magic", "nicer", "pinky", "radio", "sauce", "skier",
    "spool", "syrup", "trite", "waltz", "adept", "axial", "bough", "chick", "crock", "drool", "ferry", "gamut",
    "hardy", "junto", "magma", "niche", "pinto", "rainy", "saucy", "skiff", "spoon", "tabby", "troll", "warty",
    "adieu", "axiom", "boule", "chide", "crone", "droop", "fetal", "gassy", "harem", "juror", "maize", "niece",
    "piper", "raise", "sauna", "skill", "spore", "table", "troop", "waste", "admin", "axion", "bound", "chief",
    "crony", "dross", "fetch", "gaudy", "harpy", "kappa", "major", "night", "pique", "rajah", "saute", "skimp",
    "sport", "taboo", "trope", "watch", "admit", "azure", "bowel", "child", "crook", "drove", "fetid", "gauge",
    "harry", "karma", "maker", "ninja", "pitch", "rally", "savor", "skirt", "spout", "tacit", "trout", "water",
    "adobe", "bacon", "boxer", "chili", "cross", "drown", "fetus", "gaunt", "harsh", "kayak", "mambo", "ninny",
    "pithy", "ralph", "savoy", "skulk", "spray", "tacky", "trove", "waver", "adopt", "badge", "brace", "chill",
    "croup", "druid", "fever", "gauze", "haste", "kebab", "mamma", "ninth", "pivot", "ramen", "savvy", "skull",
    "spree", "taffy", "truce", "waxen", "adore", "badly", "braid", "chime", "crowd", "drunk", "fewer", "gavel",
    "hasty", "khaki", "mammy", "noble", "pixel", "ranch", "scald", "skunk", "sprig", "taint", "truck", "weary",
    "adorn", "bagel", "brain", "china", "crown", "dryer", "fiber", "gawky", "hatch", "kinky", "manga", "nobly",
    "pixie", "randy", "scale", "slack", "spunk", "taken", "truer", "weave", "adult", "baggy", "brake", "chirp",
    "crude", "dryly", "ficus", "gayer", "hater", "kiosk", "mange", "noise", "pizza", "range", "scalp", "slain",
    "spurn", "taker", "truly", "wedge", "affix", "baker", "brand", "chock", "cruel", "duchy", "field", "gayly",
    "haunt", "kitty", "mango", "noisy", "place", "rapid", "scaly", "slang", "spurt", "tally", "trump", "weedy",
    "afire", "baler", "brash", "choir", "crumb", "dully", "fiend", "gazer", "haute", "knack", "mangy", "nomad",
    "plaid", "rarer", "scamp", "slant", "squad", "talon", "trunk", "weigh", "afoot", "balmy", "brass", "choke",
    "crump", "dummy", "fiery", "gecko", "haven", "knave", "mania", "noose", "plain", "raspy", "scant", "slash",
    "squat", "tamer", "truss", "weird", "afoul", "banal", "brave", "chord", "crush", "dumpy", "fifth", "geeky",
    "havoc", "knead", "manic", "north", "plait", "ratio", "scare", "slate", "squib", "tango", "trust", "welch",
    "after", "banjo", "bravo", "chore", "crust", "dunce", "fifty", "geese", "hazel", "kneed", "manly", "nosey",
    "plane", "ratty", "scarf", "sleek", "stack", "tangy", "truth", "welsh", "again", "barge", "brawl", "chose",
    "crypt", "dusky", "fight", "genie", "heady", "kneel", "manor", "notch", "plank", "raven", "scary", "sleep",
    "staff", "taper", "tryst", "whack", "agape", "baron", "brawn", "chuck", "cubic", "dusty", "filer", "genre",
    "heard", "knelt", "maple", "novel", "plant", "rayon", "scene", "sleet", "stage", "tapir", "tubal", "whale",
    "agate", "basal", "bread", "chump", "cumin", "dutch", "filet", "ghost", "heart", "knife", "march", "nudge",
    "plate", "razor", "scent", "slept", "staid", "tardy", "tuber", "wharf", "agent", "basic", "break", "chunk",
    "curio", "duvet", "filly", "ghoul", "heath", "knock", "marry", "nurse", "plaza", "reach", "scion", "slice",
    "stain", "tarot", "tulip", "wheat", "agile", "basil", "breed", "churn", "curly", "dwarf", "filmy", "giant",
    "heave", "knoll", "marsh", "nutty", "plead", "react", "scoff", "slick", "stair", "taste", "tulle", "wheel",
    "aging", "basin", "briar", "chute", "curry", "dwell", "filth", "giddy", "heavy", "known", "mason", "nylon",
    "pleat", "ready", "scold", "slide", "stake", "tasty", "tumor", "whelp", "aglow", "basis", "bribe", "cider",
    "curse", "dwelt", "final", "gipsy", "hedge", "koala", "masse", "nymph", "plied", "realm", "scone", "slime",
    "stale", "tatty", "tunic", "where", "agony", "baste", "brick", "cigar", "curve", "dying", "finch", "girly",
    "hefty", "krill", "match", "oaken", "plier", "rearm", "scoop", "slimy", "stalk", "taunt", "turbo", "which",
    "agree", "batch", "bride", "cinch", "curvy", "eager", "finer", "girth", "heist", "label", "matey", "obese",
    "pluck", "rebar", "scope", "sling", "stall", "tawny", "tutor", "whiff", "ahead", "bathe", "brief", "circa",
    "cutie", "eagle", "first", "given", "helix", "labor", "mauve", "occur", "plumb", "rebel", "score", "slink",
    "stamp", "teach", "twang", "while", "aider", "baton", "brine", "civic", "cyber", "early", "fishy", "giver",
    "hello", "laden", "maxim", "ocean", "plume", "rebus", "scorn", "sloop", "stand", "teary", "tweak", "whine",
    "aisle", "batty", "bring", "civil", "cycle", "earth", "fixer", "glade", "hence", "ladle", "maybe", "octal",
    "plump", "rebut", "scour", "slope", "stank", "tease", "tweed", "whiny", "alarm", "bawdy", "brink", "clack",
    "cynic", "easel", "fizzy", "gland", "heron", "lager", "mayor", "octet", "plunk", "recap", "scout", "slosh",
    "stare", "teddy", "tweet", "whirl", "album", "bayou", "briny", "claim", "daddy", "eaten", "fjord", "glare",
    "hilly", "lance", "mealy", "odder", "plush", "recur", "scowl", "sloth", "stark", "teeth", "twice", "whisk",
    "alert", "beach", "brisk", "clamp", "daily", "eater", "flack", "glass", "hinge", "lanky", "meant", "oddly",
    "poesy", "recut", "scram", "slump", "start", "tempo", "twine", "white", "algae", "beady", "broad", "clang",
    "dairy", "ebony", "flail", "glaze", "hippo", "lapel", "meaty", "offal", "point", "reedy", "scrap", "slung",
    "stash", "tenet", "twirl", "whole", "alibi", "beard", "broil", "clank", "daisy", "eclat", "flair", "gleam",
    "hippy", "lapse", "mecca", "offer", "poise", "refer", "scree", "slunk", "state", "tenor", "twist", "whoop",
    "alien", "beast", "broke", "clash", "dally", "edict", "flake", "glean", "hitch", "large", "medal", "often",
    "poker", "refit", "screw", "slurp", "stave", "tense", "twixt", "whose", "align", "beech", "brood", "clasp",
    "dance", "edify", "flaky", "glide", "hoard", "larva", "media", "olden", "polar", "regal", "scrub", "slush",
    "stead", "tenth", "tying", "widen", "alike", "beefy", "brook", "class", "dandy", "eerie", "flame", "glint",
    "hobby", "lasso", "medic", "older", "polka", "rehab", "scrum", "slyly", "steak", "tepee", "udder", "wider",
    "alive", "befit", "broom", "clean", "datum", "egret", "flank", "gloat", "hoist", "latch", "melee", "olive",
    "polyp", "reign", "scuba", "smack", "steal", "tepid", "ulcer", "widow", "allay", "began", "broth", "clear",
    "daunt", "eight", "flare", "globe", "holly", "later", "melon", "ombre", "pooch", "relax", "sedan", "small",
    "steam", "terra", "ultra", "width", "alley", "begat", "brown", "cleat", "dealt", "eject", "flash", "gloom",
    "homer", "lathe", "mends", "omega", "poppy", "relay", "seedy", "smart", "steed", "terse", "umbra", "wield",
    "allot", "beget", "brunt", "cleft", "death", "eking", "flask", "glory", "honey", "latte", "mercy", "onion",
    "porch", "relic", "segue", "smash", "steel", "testy", "uncle", "wight", "allow", "begin", "brush", "clerk",
    "debar", "elate", "fleck", "gloss", "honor", "laugh", "merge", "onset", "poser", "remit", "seize", "smear",
    "steep", "thank", "uncut", "willy", "alloy", "begun", "brute", "click", "debit", "elbow", "fleet", "glove",
    "horde", "layer", "merit", "opera", "posit", "renal", "semen", "smell", "steer", "theft", "under", "wimpy",
    "aloft", "being", "buddy", "cliff", "debug", "elder", "flesh", "glyph", "horny", "leach", "merry", "opine",
    "posse", "renew", "sense", "smelt", "stein", "their", "undid", "wince", "alone", "belch", "budge", "climb",
    "debut", "elect", "flick", "gnash", "horse", "leafy", "metal", "opium", "pouch", "repay", "sepia", "smile",
    "stern", "theme", "undue", "winch", "along", "belie", "buggy", "cling", "decal", "elegy", "flier", "gnome",
    "hotel", "leaky", "meter", "optic", "pound", "repel", "serif", "smirk", "stick", "there", "unfed", "windy",
    "aloof", "belle", "bugle", "clink", "decay", "elfin", "fling", "godly", "hotly", "leant", "metro", "orbit",
    "pouty", "reply", "serum", "smite", "stiff", "these", "unfit", "wiser", "aloud", "belly", "build", "cloak",
    "decor", "elide", "flint", "going", "hound", "leapt", "micro", "order", "power", "rerun", "serve", "smith",
    "still", "theta", "unify", "wispy", "alpha", "below", "built", "clock", "decoy", "elite", "flirt", "golem",
    "house", "learn", "midge", "organ", "prank", "reset", "setup", "smock", "stilt", "thick", "union", "witch",
    "altar", "bench", "bulge", "clone", "decry", "elope", "float", "golly", "hovel", "lease", "midst", "other",
    "prawn", "resin", "seven", "smoke", "sting", "thief", "unite", "witty", "alter", "beret", "bulky", "close",
    "defer", "elude", "flock", "gonad", "hover", "leash", "might", "otter", "preen", "retch", "sever", "smoky",
    "stink", "thigh", "unity", "woken", "amass", "berry", "bully", "cloth", "deign", "email", "flood", "goner",
    "howdy", "least", "milky", "ought", "press", "retro", "sewer", "smote", "stint", "thing", "unlit", "woman",
    "amaze", "berth", "bunch", "cloud", "deity", "embed", "floor", "goody", "human", "leave", "mimic", "ounce",
    "price", "retry", "shack", "snack", "stock", "think", "unmet", "women", "amber", "beset", "bunny", "clout",
    "delay", "ember", "flora", "gooey", "humid", "ledge", "mince", "outdo", "prick", "reuse", "shade", "snail",
    "stoic", "third", "unset", "woody", "amble", "betel", "burly", "clove", "delta", "emcee", "floss", "goofy",
    "humor", "leech", "miner", "outer", "pride", "revel", "shady", "snake", "stoke", "thong", "untie", "wooer",
    "amend", "bevel", "burnt", "clown", "delve", "empty", "flour", "goose", "humph", "leery", "minim", "outgo",
    "pried", "revue", "shaft", "snaky", "stole", "thorn", "until", "wooly", "amiss", "bezel", "burst", "cluck",
    "demon", "enact", "flout", "gorge", "humus", "lefty", "minor", "ovary", "prime", "rhino", "shake", "snare",
    "stomp", "those", "unwed", "woozy", "amity", "bible", "bused", "clued", "demur", "endow", "flown", "gouge",
    "hunch", "legal", "minty", "ovate", "primo", "rhyme", "shaky", "snarl", "stone", "three", "unzip", "wordy",
    "among", "bicep", "bushy", "clump", "denim", "enema", "fluff", "gourd", "hunky", "leggy", "minus", "overt",
    "print", "rider", "shale", "sneak", "stony", "threw", "upper", "world", "ample", "biddy", "butch", "clung",
    "dense", "enemy", "fluid", "grace", "hurry", "lemon", "mirth", "ovine", "prior", "ridge", "shall", "sneer",
    "stood", "throb", "upset", "worry", "amply", "bigot", "butte", "coach", "depot", "enjoy", "fluke", "grade",
    "husky", "lemur", "miser", "ovoid", "prism", "rifle", "shalt", "snide", "stool", "throw", "urban", "worse",
    "amuse", "bilge", "buxom", "coast", "depth", "ennui", "flume", "graft", "hussy", "leper", "missy", "owing",
    "privy", "right", "shame", "sniff", "stoop", "thrum", "urine", "worst", "angel", "billy", "buyer", "cobra",
    "derby", "ensue", "flung", "grail", "hutch", "level", "mocha", "owner", "prize", "rigid", "shank", "snipe",
    "store", "thumb", "usage", "worth", "anger", "binge", "bylaw", "cocoa", "deter", "enter", "flunk", "grain",
    "hydro", "lever", "modal", "oxide", "probe", "rigor", "shape", "snoop", "stork", "thump", "usher", "would",
    "angle", "bingo", "cabal", "colon", "detox", "entry", "flush", "grand", "hyena", "libel", "model", "ozone",
    "prone", "rinse", "shard", "snore", "storm", "thyme", "using", "wound", "angry", "biome", "cabby", "color",
    "deuce", "envoy", "flute", "grant", "hymen", "liege", "modem", "paddy", "prong", "ripen", "share", "snort",
    "story", "tiara", "usual", "woven", "angst", "birch", "cabin", "comet", "devil", "epoch", "flyer", "grape",
    "hyper", "light", "mogul", "pagan", "proof", "riper", "shark", "snout", "stout", "tibia", "usurp", "wrack",
    "anime", "birth", "cable", "comfy", "diary", "epoxy", "foamy", "graph", "icily", "liken", "moist", "paint",
    "prose", "risen", "sharp", "snowy", "stove", "tidal", "utile", "wrath", "ankle", "bison", "cacao", "comic",
    "dicey", "equal", "focal", "grasp", "icing", "lilac", "molar", "paler", "proud", "riser", "shave", "snuck",
    "strap", "tiger", "utter", "wreak", "annex", "bitty", "cache", "comma", "digit", "equip", "focus", "grass",
    "ideal", "limbo", "moldy", "palsy", "prove", "risky", "shawl", "snuff", "straw", "tight", "vague", "wreck",
    "annoy", "black", "cacti", "conch", "dilly", "erase", "foggy", "grate", "idiom", "limit", "money", "panel",
    "prowl", "rival", "shear", "soapy", "stray", "tilde", "valet", "wrest", "annul", "blade", "caddy", "condo",
    "dimly", "erect", "foist", "grave", "idiot", "linen", "month", "panic", "proxy", "river", "sheen", "sober",
    "strip", "timer", "valid", "wring", "anode", "blame", "cadet", "conic", "diner", "erode", "folio", "gravy",
    "idler", "liner", "moody", "pansy", "prude", "rivet", "sheep", "soggy", "strut", "timid", "valor", "wrist",
    "antic", "bland", "cagey", "copse", "dingo", "error", "folly", "graze", "idyll", "lingo", "moose", "papal",
    "prune", "roach", "sheer", "solar", "stuck", "tipsy", "value", "write", "anvil", "blank", "cairn", "coral",
    "dingy", "erupt", "foray", "great", "igloo", "lipid", "moral", "paper", "psalm", "roast", "sheet", "solid",
    "study", "titan", "valve", "wrong", "aorta", "blare", "camel", "corer", "diode", "essay", "force", "greed",
    "iliac", "lithe", "moron", "parer", "pubic", "robin", "sheik", "solve", "stuff", "tithe", "vapid", "wrote",
    "apart", "blast", "cameo", "corny", "dirge", "ester", "forge", "green", "image", "liver", "morph", "parka",
    "pudgy", "robot", "shelf", "sonar", "stump", "title", "vapor", "wrung", "aphid", "blaze", "canal", "couch",
    "dirty", "ether", "forgo", "greet", "imbue", "livid", "mossy", "parry", "puffy", "rocky", "shell", "sonic",
    "stung", "toast", "vault", "wryly", "aping", "bleak", "candy", "cough", "disco", "ethic", "forte", "grief",
    "impel", "llama", "motel", "parse", "pulpy", "rodeo", "shied", "sooth", "stunk", "today", "vaunt", "yacht",
    "apnea", "bleat", "canny", "could", "ditch", "ethos", "forth", "grill", "imply", "loamy", "motif", "party",
    "pulse", "roger", "shift", "sooty", "stunt", "toddy", "vegan", "yearn", "apple", "bleed", "canoe", "count",
    "ditto", "etude", "forty", "grime", "inane", "loath", "motor", "pasta", "punch", "rogue", "shine", "sorry",
    "style", "token", "venom", "yeast", "apply", "bleep", "canon", "coupe", "ditty", "evade", "forum", "grimy",
    "inbox", "lobby", "motto", "paste", "pupil", "roomy", "shiny", "sound", "suave", "tonal", "venue", "yield",
    "apron", "blend", "caper", "court", "diver", "event", "found", "grind", "incur", "local", "moult", "pasty",
    "puppy", "roost", "shire", "south", "sugar", "tonga", "verge", "young", "aptly", "bless", "caput", "coven",
    "dizzy", "every", "foyer", "gripe", "index", "locus", "mound", "patch", "puree", "rotor", "shirk", "sower",
    "suing", "tonic", "verse", "youth", "arbor", "blimp", "carat", "cover", "dodge", "evict", "frail", "groan",
    "inept", "lodge", "mount", "patio", "purer", "rouge", "shirt", "space", "suite", "tooth", "verso", "zebra",
    "ardor", "blind", "cargo", "covet", "dodgy", "evoke", "frame", "groin", "inert", "lofty", "mourn", "patsy",
    "purge", "rough", "shoal", "spade", "sulky", "topaz", "verve", "zesty", "arena", "blink", "carol", "covey",
    "dogma", "exact", "frank", "groom", "infer", "logic", "mouse", "patty", "purse", "round", "shock", "spank",
    "sully", "topic", "vicar", "zonal", "argue", "bliss", "carry", "cower", "doing", "exalt", "fraud", "grope",
    "ingot", "login", "mouth", "pause", "pushy", "rouse", "shone", "spare", "sumac", "torch", "video", "arise",
    "blitz", "carve", "coyly", "dolly", "excel", "freak", "gross", "inlay", "loopy", "mover", "payee", "putty",
    "route", "shook", "spark", "sunny", "torso", "vigil", "armor", "bloat", "caste", "crack", "donor", "exert",
    "freed", "group", "inlet", "loose", "movie", "payer", "pygmy", "rover", "shoot", "spasm", "super", "torus",
    "vigor", "aroma", "block", "catch", "craft", "donut", "exile", "freer", "grout", "inner", "lorry", "mower",
    "peace", "quack", "rowdy", "shore", "spawn", "surer", "total", "villa", "arose", "bloke", "cater", "cramp",
    "dopey", "exist", "fresh", "grove", "input", "loser", "mucky", "peach", "quail", "rower", "shorn", "speak",
    "surge", "totem", "vinyl", "array", "blond", "catty", "crane", "doubt", "expel", "friar", "growl", "inter",
    "louse", "mucus", "pearl", "quake", "royal", "short", "spear", "surly", "touch", "viola", "arrow", "blood",
    "caulk", "crank", "dough", "extol", "fried", "grown", "intro", "lousy", "muddy", "pecan", "qualm", "ruddy",
    "shout", "speck", "sushi", "tough", "viper", "arson", "bloom", "cause", "crash", "dowdy", "extra", "frill",
    "gruel", "ionic", "lover", "mulch", "pedal", "quark", "ruder", "shove", "speed", "swami", "towel", "viral",
    "artsy", "blown", "cavil", "crass", "dowel", "exult", "frisk", "gruff", "irate", "lower", "mummy", "penal",
    "quart", "rugby", "shown", "spell", "swamp", "tower", "virus", "ascot", "bluer", "cease", "crate", "downy",
    "eying", "fritz", "grunt", "irony", "lowly", "munch", "pence", "quash", "ruler", "showy", "spelt", "swarm",
    "toxic", "visit", "ashen", "bluff", "cedar", "crave", "dowry", "fable", "frock", "guard", "islet", "loyal",
    "mural", "penne", "quasi", "rumba", "shrew", "spend", "swash", "toxin", "visor", "aside", "blunt", "cello",
    "crawl", "dozen", "facet", "frond", "guava", "issue", "lucid", "murky", "penny", "queen", "rumor", "shrub",
    "spent", "swath", "trace", "vista", "askew", "mushy"

]

possible_words = word_list
checked_words = []

y_n_list = ["yes", "no"]
user_option_list = ['1', '2', '3']

# Errors
y_n_error = "Please enter either yes or no"
user_option_error = 'Please enter either 1, 2 or 3'

# Prints title with decorations and color
title = statement_generator("Welcome to The Wonderful Wordle Solver", "*", 3)
color_text(title, 'forest_green')

# set variables for end of program
reset_words = 'no'
keep_words = 'no'

play_again = "yes"
while play_again == "yes":

    if keep_words == 'yes':
        possible_words = checked_words

    if reset_words == 'yes':
        possible_words = []
        possible_words = word_list
        checked_words = []

    checked_words = []

    wrong_letters = input("Please enter all wrong letters (grey box) separated by a space: ")
    print()

    for word in possible_words:
        if_possible = True
        for letter in wrong_letters:
            if letter in word:
                if_possible = False
                break

        if if_possible:
            checked_words.append(word)

    # reset lists
    possible_words = checked_words
    checked_words = []

    # Input for the correct letters in the wrong position (yellow box)
    yellow_letters = \
        input("Please enter the correct letters that are in the wrong place (yellow box): ")
    print()

    # Filter the words based on the input orange letters
    for word in possible_words:
        valid_word = True

        # Check if the letters in the yellow_letters match the word
        for i, letter in enumerate(yellow_letters):
            if letter != '-' and letter == word[i]:
                valid_word = False
                break

        # Check if the word contains any letters not in yellow_letters
        for letter in yellow_letters:
            if letter != '-' and letter not in word:
                valid_word = False
                break

        if valid_word:
            checked_words.append(word)

    # reset lists
    possible_words = checked_words
    checked_words = []

    # Input for correct letters
    green_letters = input("Please enter the correct letters (green box): ").lower()
    print()

    for word in possible_words:
        valid_word = True
        for i, letter in enumerate(green_letters):
            if letter != '-' and letter != word[i]:
                valid_word = False
                break
        if valid_word:
            checked_words.append(word)

    # Print the possible words
    print(checked_words)

    user_option = choice_checker('Would you like to continue (1), play again (2) or quit (3): ', user_option_list,
                                 user_option_error).lower()

    if user_option == '1':
        keep_words = 'yes'

    elif user_option == '2':
        reset_words = 'yes'

    elif user_option == '3':
        break

color_text('Thank you for using The Wonderful Wordle Solver :D', 'forest green')
