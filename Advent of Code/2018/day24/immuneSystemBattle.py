import re #used to parse data from text file
import copy
import math

class Group():
    """Represent a group of units"""
    def take_damage(self, dmg):
        self.units = max(0, self.units - math.ceil((self.hp*self.units - dmg)/self.hp))
        
    
    def __init__(self, army, nUnits, hp, dmg, attackType, initiative, weaknesses, immunities):
        self.army = army
        self.units = nUnits
        self.hp = hp
        self.dmg = dmg
        self.atkType = attackType
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        
        self.effectivePower = self.units * self.dmg

        
    def __str__(self):
        """return readable string representation of the object"""
        output = str(self.units) + " units each with " + str(self.hp) + " hit points "
        
        if len(self.weaknesses) > 0 or len(self.immunities) > 0:
            output += "("

            if len(self.weaknesses) > 0:
                output += "weak to "
                for weakness in self.weaknesses:
                    output += weakness + ", "
                output = output[:-2]
            if len(self.immunities) > 0:
                if len(self.weaknesses) > 0:
                    output += "; "
                output += "immune to "
                for immunity in self.immunities:
                    output += immunity + ", "
                output = output[:-2]
            output += ") "

        output += "with an attack that does " + str(self.dmg) + " " + self.atkType + " damage "
        output += "at initiative " + str(self.initiative)
        
        return output
    
    def __lt__(self, other):
        if self.effectivePower < other.effectivePower:
            return True
        elif self.effectivePower > other.effectivePower:
            return False
        else:
            return self.initiative < other.initiative
    def __gt__(self, other):
        if self.effectivePower > other.effectivePower:
            return True
        elif self.effectivePower < other.effectivePower:
            return False
        else:
            return self.initiative > other.initiative
    def __eq__(self, other):
        return self.effectivePower == other.effectivePower and self.initiative == other.initiative
    def __hash__(self):
        return hash((self.army, self.units, self.hp, self.dmg, self.atkType, self.initiative, tuple(self.weaknesses), tuple(self.immunities)))

def calculate_damage(atkGroup, defGroup):
    dmgType = atkGroup.atkType
    if dmgType in defGroup.immunities:
        return 0
    elif dmgType  in defGroup.weaknesses:
        return 2*atkGroup.effectivePower;
    return atkGroup.effectivePower

def read_armies(fileName):
    """read army data from text file and parse it into lists of groups"""

    #extract text from file
    immuneSystem = []
    infection = []
    with open(fileName, "r") as f:
        for line in f:
            immuneLines, infectionLines = f.read().split("\n\n")

    #parse text
    numPattern = "(\d+) units each with (\d+) hit points( \(.+\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)"
    weakPattern = "weak to (((\w+)(, )?)+)(;|\))"
    immunePattern = "immune to (((\w+)(, )?)+)(;|\))"

    for line in immuneLines.split("\n"):

        nUnits, hp, _, dmg, attackType, initiative = re.findall(numPattern, line)[0]
        
        weakMatches = re.findall(weakPattern, line)
        if len(weakMatches) > 0:
            weaknesses = weakMatches[0][0].split(", ")
        else:
            weaknesses = []
            
        immuneMatches = re.findall(immunePattern, line)
        if len(immuneMatches) > 0:
            immunities = immuneMatches[0][0].split(", ")
        else:
            immunities = []

        #create group and add it to list
        currGroup = Group("Immune System", int(nUnits), int(hp), int(dmg), attackType, int(initiative), weaknesses, immunities)
        immuneSystem.append(currGroup)
        
    for line in infectionLines.split("\n")[1:]:

        nUnits, hp, _, dmg, attackType, initiative = re.findall(numPattern, line)[0]
        
        weakMatches = re.findall(weakPattern, line)
        if len(weakMatches) > 0:
            weaknesses = weakMatches[0][0].split(", ")
        else:
            weaknesses = []
            
        immuneMatches = re.findall(immunePattern, line)
        if len(immuneMatches) > 0:
            immunities = immuneMatches[0][0].split(", ")
        else:
            immunities = []

        #create group and add it to list
        currGroup = Group("Infection", int(nUnits), int(hp), int(dmg), attackType, int(initiative), weaknesses, immunities)
        infection.append(currGroup)

    return immuneSystem, infection;


def main():

    #load armies
    immuneArmy, infectionArmy = read_armies("test1.txt")


    #repeat battle until one army is empty
    while len(immuneArmy) > 0 and len(infectionArmy) > 0:
        
        """Phase 1: Choose Targets"""
        targets = {}
        
        #sort armies by power
        immuneArmy.sort()
        infectionArmy.sort()

        #print status
        print("==================================================")
        print("Immune System: ")
        for groupNo, group in enumerate(immuneArmy):
            print("Group " + str(groupNo) + " contains " + str(group.units) + " units")
        print("Infection: ")
        for groupNo, group in enumerate(infectionArmy):
            print("Group " + str(groupNo) + " contains " + str(group.units) + " units")
        print("\n")

        #select target by comparing expected damage
        untargetedInfection = copy.copy(infectionArmy)
        for immuneGroupNo, immuneGroup in enumerate(immuneArmy):
            maxGroup = None
            maxDmg = 0
            maxInit = 0
            for infectionGroup in untargetedInfection:
                infectionGroupNo = infectionArmy.index(infectionGroup)
                potentialDmg = calculate_damage(immuneGroup, infectionGroup)
                print("Immune System Group " + str(immuneGroupNo) + " would deal defending group " + str(infectionGroupNo) + " " + str(potentialDmg) + " damage") 
                if potentialDmg > maxDmg or (potentialDmg == maxDmg and infectionGroup.initiative > maxInit):
                    maxGroup = infectionGroup
                    maxDmg = potentialDmg
                    maxInit = infectionGroup.initiative
            targets[immuneGroup] = maxGroup
            untargetedInfection.remove(maxGroup)

        untargetedImmune = copy.copy(immuneArmy)
        for infectionGroupNo, infectionGroup in enumerate(infectionArmy):
            maxGroup = None
            maxDmg = 0
            maxInit = 0
            for immuneGroup in untargetedImmune:
                immuneGroupNo = immuneArmy.index(immuneGroup)
                potentialDmg = calculate_damage(infectionGroup, immuneGroup)
                print("Infection Group " + str(infectionGroupNo) + " would deal defending group " + str(immuneGroupNo) + " " + str(potentialDmg) + " damage")
                if potentialDmg > maxDmg or (potentialDmg == maxDmg and infectionGroup.initiative > maxInit):
                    maxGroup = immuneGroup
                    maxDmg = potentialDmg
                    maxInit = immuneGroup.initiative
            targets[infectionGroup] = maxGroup
            untargetedImmune.remove(maxGroup)


        """Phase 2: Apply Damage and Reset"""
        newImmuneArmy, newInfectionArmy = [], []

        armyDict = {"Immune System":immuneArmy, "Infection":infectionArmy}
        newArmyDict = {"Immune System":newImmuneArmy, "Infection":newInfectionArmy}
        for attacker, defender in targets.items():
            if defender is not None:
                prevUnitNum = defender.units
                defender.take_damage(calculate_damage(attacker, defender))
                print(attacker.army + " Group " + str(armyDict[attacker.army].index(attacker)) + " attacks defending group "
                      + str(armyDict[defender.army].index(defender)) + ", killing " + str(defender.units - prevUnitNum) + " units")
                if defender.units > 0:
                    newArmyDict[defender.army].append(defender)
                  
        immuneArmy, infectionArmy = newImmuneArmy, newInfectionArmy
        print("")
    
    

if __name__ == "__main__":
    main();
        

