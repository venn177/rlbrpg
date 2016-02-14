from random import randint
import random

#declare boss encounters false
bossflags = dict.fromkeys(["rusty", "brodie", "serafino", "davephillips", "crayon", "marty", "g-rey", "terror", "bye-bye", "thunder", "spoon"], False)

class Character:
	def __init__(self):
		self.name = ""
		self.playerclass = ""
		self.health = 1
		self.health_max = 1
		self.MP = 1
		self.MP_max = 1
		self.value = 0
	def do_damage(self, enemy):
		damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
		enemy.health = enemy.health - damage
		if damage == 0: 
			possibilities = ["%s evades %s's attack.", "%s blocks %s's attack.", "%s will have none of what %s is giving out."]
			print random.choice(possibilities) % (enemy.name, self.name) + " [%d/%d]" % (enemy.health, enemy.health_max)
		else: 
			print "%s deals %d damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.health, enemy.health_max)
		return enemy.health <= 0

class Enemy(Character):
	def __init__(self, player):
		Character.__init__(self)
		title = ["SP", "RP", "CL", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"]
		firstName = ["Jose", "Raul", "Javier", "Tim", "Rich", "Carlos", "Lewis", "Chris", "Steve", "George", "Garland", "Leland", "Gregg", "Bob", "Matt", "Rodrigo", "Freek", "John", "Mariano", "Stanley", "Jerry", "Romel", "Esteban"]
		lastName = ["Harris", "Bell", "Rodriguez", "Rangel", "Taylor", "Ware", "Moore", "George", "Harrington", "Reynolds", "Stewart", "King", "Jenkins", "Moser", "Lloyd", "Zapata", "Mateo", "Fleming", "Trout", "Bass"]
		self.name = random.choice(title) + " " + random.choice(firstName) + " " + random.choice(lastName)
		encounterrand = randint(1,50)
		self.value = randint(1,5)
		if p.level <= 3:
			self.health_max = randint(1,6)
		elif p.level <= 5:
			self.health_max = randint(3,8)
		elif p.level <= 7:
			self.health_max = randint(5,12)
		elif p.level <= 9:
			self.health_max = randint(5,15)
		elif p.level <= 11:
			self.health_max = randint(5,20)
		else:
			self.health_max = randint(7,30)
		if encounterrand <= 5:
			if bossflags['rusty'] != True:
				bossflags['rusty'] = True
				self.name = "Team Leader Rusty 'The Rusty One' Nasution"
				self.value = 10
				self.health_max = 10
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 7:
			if bossflags['davephillips'] != True:
				bossflags['davephillips'] = True
				self.name = "The Mayor, Dave Phillips"
				self.value = 10
				self.health_max = 15
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 8:
			if bossflags['crayon'] != True:
				bossflags['crayon'] = True
				self.name = "The Crayon, Bonifazio Geccerelli"
				self.value = 10
				self.health_max = 15
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 15:
			if bossflags['marty'] != True:
				bossflags['marty'] = True
				self.name = "The one who takes you to lunch, Martin Bunch"
				self.value = 10
				self.health_max = 5
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 16:
			if bossflags['g-rey'] != True:
				bossflags['g-rey'] = True
				self.name = "The original prospect, Gary Reynolds"
				self.value = 10
				self.health_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 17:
			if bossflags['terror'] != True:
				bossflags['terror'] = True
				self.name = "The terror, Steve Dillard"
				self.value = 10
				self.health_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 18:
			if bossflags['bye-bye'] != True:
				bossflags['bye-bye'] = True
				self.name = "Bye-bye himself-- Antonio Pujals"
				self.value = 10
				self.health_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 19:
			if bossflags['thunder'] != True:
				bossflags['thunder'] = True
				self.name = "The never-ending offense, Thunder, Juan Munoz"
				self.value = 10
				self.health_max = 35
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 20:
			if bossflags['spoon'] != True:
				bossflags['spoon]'] = True
				self.name = "The Spoonman Rafael Diaz" # he should do more damage once that's set up
				self.value = 10
				self.health_max = 20
			else:
				self.enemy = Enemy(self)
		if encounterrand == 50:
			if bossflags['serafino'] != True:
				bossflags['serafino'] = True		
				self.name = "True Grit, Serafino De Mesquites"
				self.value = 1000
				self.health_max = 100
			else:
				self.enemy = Enemy(self)
		self.health = self.health_max

class Player(Character):
	def __init__(self):
		Character.__init__(self)
		self.state = 'normal'
		self.level = 1
		self.experience = 0
		self.xpNext = 20
	def quit(self):
		print "%s gives up, allowing the dankness to overtake them." % self.name
		self.health = 0
	def help(self): 
		print Commands.keys()
	def status(self): 
		print "HP: %d/%d, MP: %d/%d, Lvl: %d, XP: %d/%d" % (self.health, self.health_max, self.MP, self.MP_max, self.level, self.experience, self.xpNext)
	def tired(self):
		self.health = max(1, self.health - 1)
		print "%s is getting tired of wandering..." % self.name
	def rest(self):
		if self.state != 'normal':
			print "%s can't rest now!" % self.name; self.enemy_attacks()
		else:
			print "%s rests." % self.name
		if randint(0, 1):
			self.enemy = Enemy(self)
			print "%s is rudely interrupted by %s! [%d/%d]" % (self.name, self.enemy.name, self.enemy.health, self.enemy.health_max)
			self.state = 'fight'
			self.enemy_attacks()
		else:
			if self.health < self.health_max:
				self.health += p.level
				self.MP += p.level
				if self.MP > self.MP_max:
					self.MP = self.MP_max
			else: 
				print "%s has much too much energy to sleep!" % self.name
	def explore(self):
		if self.state != 'normal':
			print "%s is too busy right now!" % self.name
			self.enemy_attacks()
		else:
			possibilities = ["heads toward the infield", "stops at a beer stand", "goes to the bleachers", "heads to the away-team dugout", "goes behind home plate", "wanders towards the parking lot", "goes to will call", "heads over to the press box", "investigates a fight at the home team dugout", "rounds third base", "makes a call to the bullpen", "heads over to take a leak", "meanders toward the VIP area", "heads down the foul line", "heads back to the locker room"]
			print "%s " % self.name + random.choice(possibilities) + "..."
		if randint(0, 1):
			self.enemy = Enemy(self)
			print "%s encounters %s! [%d/%d]" % (self.name, self.enemy.name, self.enemy.health, self.enemy.health_max)
			self.state = 'fight'
		else:
			if randint(0, 1): 
				self.tired()
	def flee(self):
		if self.state != 'fight': 
			print "%s has no reason to run right now." % self.name
		else:
			if randint(1, self.health + 5) > randint(1, self.enemy.health):
				print "%s pulls himself, abandoning %s." % (self.name, self.enemy.name)
				self.enemy = None
				self.state = 'normal'
			else: 
				print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()
	def attack(self):
		if self.state != 'fight': 
			print "%s can't attack, there's nothing around!" % self.name; self.tired()
		else:
			if self.do_damage(self.enemy):
				announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
				print announce.upper()
				self.experience = self.experience + self.enemy.value
				self.level_up()
				self.enemy = None
				self.state = 'normal'
#			if randint(0, self.health) < 10:
#				self.health = self.health + 1
#				self.health_max = self.health_max + 1
#				print "%s feels stronger!" % self.name
			else: 
				self.enemy_attacks()
	def enemy_attacks(self):
		if self.enemy.do_damage(self): 
			print "%s got got by %s!!!\nR.I.P." %(self.name, self.enemy.name)
	def level_up(self):
		if self.experience >= self.xpNext:
			self.level += 1
			self.experience = self.experience - self.xpNext
			if p.playerclass == "batter":
				randhp = randint(1,6)
				randmp = randint(1,2)
				self.health_max += randhp
				self.MP_max += randmp
				self.health += randhp
				self.MP += randmp
			if p.playerclass == "pitcher":
				randhp = randint(1,3)
				randmp = randint(1,6)
				self.health_max += randhp
				self.MP_max += randmp
				self.health += randhp
				self.MP += randmp
			if self.health > self.health_max:
				self.health = self.health_max
			if self.MP > self.MP_max:
				self.MP = self.MP_max
			print "%s leveled up! HP is now %d and MP is now %d!" % (self.name, self.health_max, self.MP_max)
			

Commands = {
	'quit': Player.quit,
	'help': Player.help,
	'status': Player.status,
	'rest': Player.rest,
	'explore': Player.explore,
	'flee': Player.flee,
	'attack': Player.attack,
	}

p = Player()
p.name = raw_input("What is your character's name? ")
p.playerclass = raw_input("What class do you want to be? [Batter/Pitcher] ")
while p.playerclass not in ['pitcher', 'batter', 'Batter', 'Pitcher']:
	print "You can only be a pitcher or batter!"
	p.playerclass = raw_input("What class do you want to be? [Batter/Pitcher] ")
p.playerclass = p.playerclass.lower()
if p.playerclass == "batter":
	p.health = 10
	p.health_max = 10
	p.MP = 4
	p.MP_max = 4
elif p.playerclass == "pitcher":
	p.health = 6
	p.health_max = 6
	p.MP = 10
	p.MP_max = 10
print "(type help to get a list of actions)\n"
print "%s enters a dark stadium full of putrid, overused jokes and out-of-date memes." % p.name

while(p.health > 0):
	line = raw_input("> ")
	args = line.split()
	if len(args) > 0:
		commandFound = False
		for c in Commands.keys():
			if args[0] == c[:len(args[0])]:
				Commands[c](p)
				commandFound = True
				break
		if not commandFound:
			print "%s doesn't understand the suggestion." % p.name
