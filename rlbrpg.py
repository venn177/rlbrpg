from random import randint
import random

#declare boss encounters false
bossflags = dict.fromkeys(["rusty", "brodie", "serafino", "davephillips", "crayon", "marty", "g-rey", "terror", "bye-bye", "thunder", "spoon"], False)

class Character:
	def __init__(self):
		self.name = ""
		self.playerclass = ""
		self.HP = 1
		self.HP_max = 1
		self.MP = 1
		self.MP_max = 1
		self.offense = 1
		self.defense = 1
		self.value = 0
	def do_damage(self, enemy):
		damage = int(self.offense + randint(0,(self.HP/2)) - enemy.defense)
		if damage < 1:
			damage = 0
		enemy.HP = enemy.HP - damage
		if damage < 1: 
			possibilities = ["%s evades %s's attack.", "%s blocks %s's attack.", "%s will have none of what %s is giving out."]
			print random.choice(possibilities) % (enemy.name, self.name) + " [%d/%d]" % (enemy.HP, enemy.HP_max) + "\n[Battle] [Status] [Flee]"
		else: 
			print "%s deals %d damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max) 
		return enemy.HP <= 0
	def do_fastball(self, enemy):
		self.MP -= 3
		damage = randint(1,self.HP)
		enemy.HP -= damage
		print "Fastball! %s deals %d true damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0
	def do_powerswing(self, enemy):
		self.MP -= 2
		damage = self.offense * 2 + randint(1,self.HP/2) - enemy.defense
		enemy.HP -= damage
		print "Power swing! %s deals %d damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0
	def do_killerheat(self, enemy):
		self.MP -= 15
		damage = randint(6,50) - enemy.defense
		enemy.HP -= damage
		print "Throwing killer heat! %s deals %d damage to %s! Broke 100 on the gun! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0
	def do_eephus(self, enemy):
		self.MP -= 6
		damage = randint(5,10)
		enemy.HP -= damage
		print "An eephus?! %s deals %d true damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0
	def do_contact(self, enemy):
		self.MP -= 6
		damage = randint(5,10)
		enemy.HP -= damage
		print "A great contact swing by %s deals %d true damage to %s! [%d/%d]" % (self.name, damage, enemy.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0
	def do_fences(self, enemy):
		self.MP -= 15
		damage = randint(6,50)
		selfdamage = randint(3,20)
		enemy.HP -= damage
		self.HP -= selfdamage
		print "%s swings for the fences! It deals %d damage to %s, but %d to %s, too! Home run! [%d/%d]" % (self.name, damage, enemy.name, selfdamage, self.name, enemy.HP, enemy.HP_max)
		return enemy.HP <= 0

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
			self.HP_max = randint(1,6)
			self.offense = randint(1,3)
			self.defense = randint(1,3)
		elif p.level <= 5:
			self.HP_max = randint(3,8)
			self.offense = randint(1,5)
			self.defense = randint(1,3)
		elif p.level <= 7:
			self.HP_max = randint(5,12)
			self.offense = randint(1,5)
			self.defense = randint(1,5)
		elif p.level <= 9:
			self.HP_max = randint(5,15)
			self.offense = randint(2,6)
			self.defense = randint(2,6)
		elif p.level <= 11:
			self.HP_max = randint(5,20)
			self.offense = randint(2,7)
			self.defense = randint(2,7)
		else:
			self.HP_max = randint(7,30)
			self.offense = randint(3,10)
			self.defense = randint(3,10)
		if encounterrand == 5:
			if bossflags['rusty'] != True:
				bossflags['rusty'] = True
				self.name = "Team Leader Rusty 'The Rusty One' Nasution"
				self.value = 10
				self.HP_max = 10
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 7:
			if bossflags['davephillips'] != True:
				bossflags['davephillips'] = True
				self.name = "the Mayor, Dave Phillips"
				self.value = 10
				self.HP_max = 15
			else:
				self.enemy = Enemy(self)
		if encounterrand == 8:
			if bossflags['crayon'] != True:
				bossflags['crayon'] = True
				self.name = "the Crayon, Bonifazio Geccerelli"
				self.value = 10
				self.HP_max = 15
			else:
				self.enemy = Enemy(self)
		if encounterrand <= 15:
			if bossflags['marty'] != True:
				bossflags['marty'] = True
				self.name = "the one who takes you to lunch, Martin Bunch"
				self.value = 10
				self.HP_max = 5
			else:
				self.enemy = Enemy(self)
		if encounterrand == 16:
			if bossflags['g-rey'] != True:
				bossflags['g-rey'] = True
				self.name = "the original prospect, Gary Reynolds"
				self.value = 10
				self.HP_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand == 17:
			if bossflags['terror'] != True:
				bossflags['terror'] = True
				self.name = "the terror, Steve Dillard"
				self.value = 10
				self.HP_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand == 18:
			if bossflags['bye-bye'] != True:
				bossflags['bye-bye'] = True
				self.name = "Bye-Bye himself-- Antonio Pujals"
				self.value = 10
				self.HP_max = 25
			else:
				self.enemy = Enemy(self)
		if encounterrand == 19:
			if bossflags['thunder'] != True:
				bossflags['thunder'] = True
				self.name = "the never-ending offense, Thunder, Juan Munoz"
				self.value = 10
				self.HP_max = 35
			else:
				self.enemy = Enemy(self)
		if encounterrand == 20:
			if bossflags['spoon'] != True:
				bossflags['spoon]'] = True
				self.name = "the Spoonman Rafael Diaz" # he should do more damage once that's set up
				self.value = 10
				self.HP_max = 20
			else:
				self.enemy = Enemy(self)
		if encounterrand == 50:
			if bossflags['serafino'] != True:
				bossflags['serafino'] = True		
				self.name = "TRUE GRIT, Serafino De Mesquites"
				self.value = 1000
				self.HP_max = 100
			else:
				self.enemy = Enemy(self)
		self.HP = self.HP_max

class Player(Character):
	def __init__(self):
		Character.__init__(self)
		self.state = 'normal'
		self.level = 1
		self.experience = 0
		self.xpNext = 20
	def quit(self):
		print "%s gives up, allowing the dankness to overtake them." % self.name
		self.HP = 0
	def help(self): 
		print Commands.keys()
	def status(self): 
		print "HP: %d/%d, MP: %d/%d, Lvl: %d, Off: %d, Def: %d, XP: %d/%d" % (self.HP, self.HP_max, self.MP, self.MP_max, self.level, self.offense, self.defense, self.experience, self.xpNext)
	def tired(self):
		self.HP = max(1, self.HP - 1)
		print "%s is getting tired of wandering..." % self.name
	def rest(self):
		if self.state != 'normal':
			print "%s can't rest now!" % self.name; self.enemy_attacks()
		else:
			print "%s rests." % self.name
		if randint(0, 1):
			self.enemy = Enemy(self)
			print "%s is rudely interrupted by %s! [%d/%d]" % (self.name, self.enemy.name, self.enemy.HP, self.enemy.HP_max)
			self.state = 'fight'
			self.enemy_attacks()
		else:
			if self.HP < self.HP_max:
				self.HP += p.level
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
			print "%s encounters %s! [%d/%d]\n[Battle] [Status] [Flee]" % (self.name, self.enemy.name, self.enemy.HP, self.enemy.HP_max)
			self.state = 'fight'
		else:
			if randint(0, 1): 
				self.tired()
	def flee(self):
		if self.state != 'fight': 
			print "%s has no reason to run right now." % self.name
		else:
			if randint(1, self.HP + 5) > randint(1, self.enemy.HP):
				print "%s pulls himself, abandoning %s." % (self.name, self.enemy.name)
				self.enemy = None
				self.state = 'normal'
			else: 
				print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()
	def battle(self):
		if self.state != 'fight': 
			print "%s can't attack, there's nothing around!" % self.name; self.tired()
		else:
			attackchoiceoutput = "[Attack] "
			for x in range(0, len(skillList)):
				if skillList[x][1] == 1:
					attackchoiceoutput += "[" + str(skillList[x][0]) + "] "
			attackchoiceoutput += "\n> "
			attackchoice = raw_input(attackchoiceoutput)
			attackchoice = attackchoice.lower()
			if attackchoice == "attack":
				if self.do_damage(self.enemy):
					announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
					print announce.upper()
					self.experience = self.experience + self.enemy.value
					self.level_up()
					self.enemy = None
					self.state = 'normal'
				else: 
					self.enemy_attacks()
			else:
				if attackchoice == "fastball" and skillList[0][1] == 1:
					if self.MP >= 3:
						if self.do_fastball(self.enemy):
							announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
							print announce.upper()
							self.experience = self.experience + self.enemy.value
							self.level_up()
							self.enemy = None
							self.state = 'normal'
						else:
							self.enemy_attacks()
					else:
						print "You don't have enough MP to use that skill.\n[Battle] [Status] [Flee]"
				elif attackchoice == "power swing" and skillList[1][1] == 1:
					if self.MP >= 2:
						if self.do_powerswing(self.enemy):
							announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
							print announce.upper()
							self.experience = self.experience + self.enemy.value
							self.level_up()
							self.enemy = None
							self.state = 'normal'
						else:
							self.enemy_attacks()
					else:
						print "You don't have enough MP to use that skill.\n[Battle] [Status] [Flee]"
				elif attackchoice == "killer heat" and skillList[2][1] == 1:
					if self.MP >= 15:
						if self.do_killerheat(self.enemy):
							announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
							print announce.upper()
							self.experience = self.experience + self.enemy.value
							self.level_up()
							self.enemy = None
							self.state = 'normal'
						else:
							self.enemy_attacks()
					else:
						print "You don't have enough MP to use that skill.\n[Battle] [Status] [Flee]"
				elif attackchoice == "eephus" and skillList[3][1] == 1:
					if self.MP >= 6:
						if self.do_eephus(self.enemy):
							announce = "%s defeats %s, gaining %d XP!" % (self.name, self.enemy.name, self.enemy.value)
							print announce.upper()
							self.experience = self.experience + self.enemy.value
							self.level_up()
							self.enemy = None
							self.state = 'normal'
						else:
							self.enemy_attacks()
					else:
						print "You don't have enough MP to use that skill.\n[Battle] [Status] [Flee]"
				else:
						print "That's not a skill.\n[Battle] [Status] [Flee]"
									
					
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
				self.HP_max += randhp
				self.MP_max += randmp
				self.HP += randhp
				self.MP += randmp
				if self.level == 2:
					skillList[0][1] = 1
					print "%s learned Power Swing!" % self.name
				if self.level == 5:
					skillList[4][1] = 1
					print "%s learned Swing for Contact!" % self.name
				if self.level == 9:
					skillList[5][1] = 1
					print "%s learned Swing for the Fences!" % self.name
			if p.playerclass == "pitcher":
				randhp = randint(1,3)
				randmp = randint(1,6)
				self.HP_max += randhp
				self.MP_max += randmp
				self.HP += randhp
				self.MP += randmp
				if self.level == 5:
					skillList[3][1] = 1
					print "%s learned Eephus!" % self.name
				if self.level == 9:
					skillList[2][1] = 1
					print "%s learned Killer Heat!" % self.name
			print "%s leveled up! HP is now %d and MP is now %d!" % (self.name, self.HP_max, self.MP_max)
			upgradechoice = raw_input("Increase offense or defense? [Offense/Defense] ")
			while upgradechoice not in ['offense', 'defense', 'offense', 'defense']:
				upgradechoice = raw_input("Increase offense or defense? [Offense/Defense] ")
			upgradechoice = upgradechoice.lower()
			if self.HP > self.HP_max:
				self.HP = self.HP_max
			if self.MP > self.MP_max:
				self.MP = self.MP_max
			if upgradechoice == "offense":
				self.offense += 1
			elif upgradechoice == "defense":
				self.defense += 1
			


skillList = []
skillList.append(["Fastball",0])
skillList.append(["Power Swing",0])
skillList.append(["Killer Heat",0])
skillList.append(["Eephus",0])
skillList.append(["Swing for Contact",0])
skillList.append(["Swing for the Fences",0])
			
Commands = {
	'battle': Player.battle,
	'explore': Player.explore,
	'rest': Player.rest,
	'status': Player.status,
	'flee': Player.flee,
	'help': Player.help,
	'quit': Player.quit,
	}

p = Player()
p.name = raw_input("What is your character's name?\n> ")
p.playerclass = raw_input("What class do you want to be? [Batter/Pitcher]\n> ")
while p.playerclass not in ['pitcher', 'batter', 'Batter', 'Pitcher']:
	print "You can only be a pitcher or batter!"
	p.playerclass = raw_input("What class do you want to be? [Batter/Pitcher]\n> ")
p.playerclass = p.playerclass.lower()
if p.playerclass == "batter":
	p.HP = 10
	p.HP_max = 10
	p.MP = 4
	p.MP_max = 4
	p.offense = 3
	p.defense = 2
elif p.playerclass == "pitcher":
	p.HP = 6
	p.HP_max = 6
	p.MP = 10
	p.MP_max = 10
	p.offense = 1
	p.defense = 1
	skillList[0][1] = 1
print "(type help to get a list of actions)"
print "%s enters a dark stadium full of putrid, overused jokes and out-of-date memes." % p.name
while(p.HP > 0):
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
