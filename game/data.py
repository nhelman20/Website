
worldRooms = {
    'Home Room': {
        DESC: 'Your home room is MS 302, it is creepy, your teacher is sleeping. You want to escape.',
        NORTH: 'Studio',
        GROUND: ['Sock']},
    'Studio': {
        DESC: 'The studio is the passage way to almost every room in the building. Your friend calls you "try to go to an e..........?" Your cell phone turns off...... ',
        NORTH: 'PAC',
        EAST: 'SC Room',
        SOUTH: 'Home Room',
        WEST: 'Death',
        GROUND: ['MacBook', 'Audio Recorder']},
    'PAC': {
        DESC: 'The PAC... You see actors... They are practicing...',
        SOUTH: 'Studio',
        WEST: 'Deli',
        EAST: 'GYM',
        GROUND: ['Paper Clip', 'Knife']},
    'Deli': {
        DESC: 'The delightful smell of junk fills the air, making you hungry. You drool... The baker has a knife in his hand, he drops it',
        EAST: 'PAC',
        SHOP: ['Brownie', 'Hot Dog', 'Pizza'],
        GROUND: ['Shop Howto', 'Knife']},
    'SC Room': {
        DESC: 'The student government of the school.. You think they are mean and selfish. Screw them!',
        NORTH: 'GYM',
        WEST: 'Studio',
        EAST: 'Death',
        GROUND: ['Paper', 'Pencil', 'Sign']},
    'GYM': {
        DESC: 'Your phone rings, you have a message. "YOU ARE ALMOST THERE BUT BEWARE I AM GOING TO GET YOU!!" You start to hurry.',
        NORTH: 'Elevator',
        GROUND: ['Key', 'Soccer Ball']},
    'Elevator': {
        DESC: 'There is a sign "t_iselev_t_r_etsyo_outoft_esc_ool" It seems like some words got erased. You see another sign. "You need a key to escape".....',
        DOWN: 'Outside',
        UP: '2nd Floor Lobby',
        SOUTH: 'GYM',
        GROUND: []},
    'Outside': {
        DESC: 'You are out of the school, but still inside the gate. You are still not done...',
        SOUTH: 'Elevator',
        NORTH: 'Front Gate',
        GROUND: []},
    'Front Gate': {
        DESC: 'YOU MADE IT TO THE FRONT YOU ARE FREE YOU RUN BACK HOME. HOPE YOU DONT GET CAUGHT!!',
        GROUND: []},
    'Death': {
	    DESC: 'YOU WALK IN TO A ROOM.... YOUR EYESIGHT GETS BLURRY....YOU DIE...',
	    NORTH: 'Home Room',
	    GROUND: []},
    '2nd Floor Lobby': {
	    DESC: 'You are on the 2nd floor',
	    NORTH: 'Art Room',
	    SOUTH: 'Elevator',
	    EAST: 'Library',
	    GROUND: []},
	'Art Room': {
		DESC: 'The brightest place at the school...Disgusting...',
		NORTH: 'Computer Room',
		SOUTH: '2nd Floor Lobby',
		GROUND: ['Paint Brush']},
	'Computer Room': {
		DESC: 'You can hear a video playing inside.',
		WEST: 'Death',
		SOUTH: 'Art Room',
		EAST: 'CCT',
		GROUND: ['Charger']},
	'CCT': {
		DESC: 'The main "MANAGER" of the school. They are lazy...',
		WEST: 'Computer Room',
		SOUTH: 'Office',
		NORTH: 'Death',
		GROUND: ['SD CARD']},

	'Office': {
		DESC: 'You can hear the people typing away on there computers.',
		NORTH: 'CCT',
		EAST: 'Pool',
		SOUTH: 'Spanish',
		GROUND: ['Coins']},
	
        
    'Pool': {
	    DESC: 'The place where there used to be water.',
	    WEST: 'Office',
	    EAST: 'Locker Room',
	    NORTH: 'Death',
	    GROUND: ['Goggles']},
   
    'Locker Room': {
	    DESC: 'SMELLS LIKE SWEAT',
	    WEST: 'Pool',
	    NORTH: 'Death',
	    GROUND: []},
	    
	'Spanish': {
		DESC: 'THE PLACE EVERYONE HATES',
		NORTH: 'Office',
		SOUTH: 'Library',
		GROUND: []},
    
    'Library': {
    	DESC: 'THE BOOKS OF "KNOWLEDGE" SIT THERE UNTOUCHED.',
    	NORTH: 'Spanish',
    	SOUTH: 'Death',
    	WEST: 'Lobby',
    	EAST: 'Hall Way',
    	GROUND: ['BOOK']},
    	
    'Hallway': {
    	DESC: 'A Long and spooky hallway stands before you',
    	NORTH: 'Death',
    	SOUTH: 'Death',
    	EAST: 'Secret Door',
    	WEST: 'Library',
    	GROUND: []},
    	
    'Secret Door': {	
	    DESC: "YOU OPEN OUT THER DOOR YOU ESCAPED!!!"
    	

worldItems = {
    'Key': {
        GROUNDDESC: 'An important Key',
        SHORTDESC: 'A Key',
        LONGDESC: 'The Key seem to be very important. I has a lot of dust on it',
        TAKEABLE: True,
        DESCWORDS: ['key', 'important']},
    'Sock': {
        GROUNDDESC: 'A Smelly sock lays on the ground',
        SHORTDESC: 'a sock',
        LONGDESC: 'A Smelly sock lays on the ground.. It looks like yours."',
        TAKEABLE: True,
        DESCWORDS: ['sock']},
    'Paper Clip': {
        GROUNDDESC: 'A silvery clip. Might come in handy',
        SHORTDESC: 'A clip',
        LONGDESC: 'A silvery clip. Might come in handy... Maybe as a.....key?',
        TAKEABLE: True,
        DESCWORDS: ['clip']},
    'Pencil': {
        GROUNDDESC: 'A pencil lies on the ground.',
        SHORTDESC: 'a pencil',
        LONGDESC: 'A pencil, engraved with the word, "DANNY"',
        TAKEABLE: True,
        DESCWORDS: ['pencil']},
    'Paper': {
        GROUNDDESC: 'A piece of paper lying on the ground',
        SHORTDESC: 'A piece of paper',
        LONGDESC: 'A piece of paper lying on the ground. Does not really seem useful.',
        TAKEABLE: True,
        DESCWORDS: ['paper', 'piece']},
    'Knife': {
        GROUNDDESC: 'The knife that the baker dropped is on the ground.',
        SHORTDESC: 'The knife',
        LONGDESC: 'The knife that the baker dropped is on the ground (Maybe on purpose). Engraved on the front: "You\'re Stupid and FAT! You ignore it."',
        TAKEABLE: True,
        DESCWORDS: ['knife', 'baker', 'stupid']},
    'Sign': {
        GROUNDDESC: 'On the sign: "WORK IN PROGRESS',
        SHORTDESC: 'a sign',
        LONGDESC: 'On the sign: "WORK IN PROGRESS... It sound like a lie...',
        TAKEABLE: False,
        DESCWORDS: ['sign']},
    'Audio Recorder': {
        GROUNDDESC: 'An Audio Recorder lies on the ground.',
        SHORTDESC: 'An Audio Recorder',
        LONGDESC: 'An Audio Recorder lies on the ground... Maybe it had a clue??',
        TAKEABLE: True,
        DESCWORDS: ['audio', 'recorder', 'clue']},
    'MacBook': {
        GROUNDDESC: 'Everyones favorite device.. A MacBook is on the ground. Your hand want to touch it.',
        SHORTDESC: 'A MacBook is on the ground',
        LONGDESC: 'The battery is dead but you still have hope you are eager to get out of this place.',
        TAKEABLE: True,
        DESCWORDS: ['macbook', 'dead', 'hope', 'device']},
    'Hot dog': {
        GROUNDDESC: 'A suspicious Hot dog rests on the ground.',
        SHORTDESC: 'a Hot dog',
        LONGDESC: 'A Hot dog. It tastes like a normal hot dog.',
        EDIBLE: True,
        DESCWORDS: ['hot', 'dog']},
    'Pizza': {
        GROUNDDESC: 'A pizza rests on the ground. (Gross.)',
        SHORTDESC: 'a pizza',
        LONGDESC: 'It is a pizza. Looks like someone dropped it.',
        EDIBLE: True,
        DESCWORDS: ['pizza']},
    'Brownie': {
        GROUNDDESC: 'A Brownie rests on the ground. (Gross.)',
        SHORTDESC: 'a brownie',
        LONGDESC: 'It is a chocolate brownie.',
        EDIBLE: True,
        DESCWORDS: ['brownie']},
    'Charger': {
        GROUNDDESC: 'A Charger rests on the bleachers',
        SHORTDESC: 'a charger',
        LONGDESC: 'YOU FOUND THE CHARGER.. YOU ARE EXCITED... YOU TURN THE COMPUTER ON YOU SEE A VIDEO MESSAGE. "You have to get out of there till 12!!!!!! OR ELSE!!!!"',
        TAKEABLE: True,
        DESCWORDS: ['charger']},
    'Soccer Ball': {
        GROUNDDESC: 'A soccer ball lies on the ground',
        SHORTDESC: 'a soccer ball',
        LONGDESC: 'The soccer ball does not look useful, You kick it around.',
        DESCWORDS: ['soccer', 'ball']},
    'Paint Brush': {
        GROUNDDESC: 'A Paint Brush lies on the ground',
        SHORTDESC: 'a Paint Brush',
        LONGDESC: 'The Paint Brush does not look useful.',
        TAKEABLE: True,
        DESCWORDS: ['paint', 'brush']},
    'SD CARD': {
        GROUNDDESC: 'A SD CARD lies on the ground',
        SHORTDESC: 'a SD CARD',
        LONGDESC: 'The SD CARD might have something in it. You are closer to the end.',
        TAKEABLE: True,
        DESCWORDS: ['SD', 'CARD']},
        
    'Coins': {
        GROUNDDESC: 'A coin is shinning on the ground',
        SHORTDESC: 'Coins',
        LONGDESC: 'Maybe You can get something with the money you just picked up',
        TAKEABLE: True,
        DESCWORDS: ['coin', 'money']},
        
    'Goggles': {
        GROUNDDESC: 'A Goggle???',
        SHORTDESC: 'A Goggle',
        LONGDESC: 'A GOGGLE??????? DEFIANTLY NOT NEEDED.',
        TAKEABLE: True,
        DESCWORDS: ['goggle']},
        
    'BOOK': {
        GROUNDDESC: 'A Book is laying on the ground',
        SHORTDESC: 'A Book',
        LONGDESC: 'The book seem to be very important. I has a lot of dust on it.... You open it "YOU ARE ALMOST THERE"',
        TAKEABLE: False,
        DESCWORDS: ['book', 'important']},


        
    'README Note': {
        GROUNDDESC: 'A note titled "README" rests on the ground.',
        SHORTDESC: 'a README note',
        LONGDESC: 'The README note reads, "Welcome to the text adventure demo. Be sure to check out the source code to see how this game is put together."',
        EDIBLE: True,
        DESCWORDS: ['readme', 'note']},
        
    'Shop Howto': {
        GROUNDDESC: 'A "Shopping HOWTO" note rests on the ground.',
        SHORTDESC: 'a shopping howto',
        LONGDESC: 'The note reads, "When you are at a shop, you can type "list" to show what is for sale. "buy <item>" will add it to your inventory, or you can sell an item in your inventory with "sell <item>". (Currently, money is not implemented in this program.)',
        EDIBLE: True,
        DESCWORDS: ['howto', 'note', 'shop']},
    }

