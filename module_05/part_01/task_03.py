from random import randint


class Warrior:

    def __init__(self, name, health):

        self.name = name
        self.health = health

    def get_damage(self):

        self.health -= 20

    def is_alive(self):

        alive = True

        if self.health < 1:
            alive = False

        return alive


class WarriorAdvanced(Warrior):

    def __init__(self, name, health, armor, stamina):

        super().__init__(name, health)

        self.armor = armor
        self.stamina = stamina

    def f_attack(self, enemy_action, enemy_stamina):

        if self.stamina > 10:
            self.stamina -= 10
        else:
            self.stamina = 0

        if enemy_action == 1:

            if enemy_stamina > 0:
                self.health -= randint(10, 30)
            else:
                self.health -= randint(0, 10)

        if self.health < 0:
            self.health = 0

        print(f'{self.name} \033[91mattacks\033[0m')

    def f_defend(self, enemy_action, enemy_stamina):

        if enemy_action == 1:

            if self.armor > 0:

                self.armor -= randint(0, 10)

                if self.armor < 0:

                    self.health += self.armor
                    self.armor = 0

                if enemy_stamina > 0:
                    self.health -= randint(0, 20)
                else:
                    self.health -= randint(0, 10)
            else:
                if enemy_stamina > 0:
                    self.health -= randint(10, 30)
                else:
                    self.health -= randint(0, 10)

        if self.health < 0:
            self.health = 0

        print(f'{self.name} \033[94mdefends\033[0m')

    def f_print_status(self):

        print(f'{self.name} health: {self.health} armor: {self.armor} stamina: {self.stamina}')


def f_fight_simple(name1, name2):

    warrior1 = Warrior(name1, 100)
    warrior2 = Warrior(name2, 100)

    fight_not_finished = True

    while fight_not_finished:

        turn = randint(1, 2)

        if turn == 1:

            warrior2.get_damage()

            print(f'{warrior1.name} hits {warrior2.name} . {warrior2.name} health left {warrior2.health}')

            if not warrior2.is_alive():

                print(warrior1.name, 'WINS !')
                fight_not_finished = False

        else:

            warrior1.get_damage()

            print(f'{warrior2.name} hits {warrior1.name} . {warrior1.name} health left {warrior1.health}')

            if not warrior1.is_alive():

                print(f'{warrior2.name} WINS !')
                fight_not_finished = False


def f_fight_round(warrior1, warrior2):

    action1 = randint(0, 1)
    action2 = randint(0, 1)

    stamina1 = warrior1.stamina
    stamina2 = warrior2.stamina

    print('\033[93m-= Round =-\033[0m')

    if action1 == 1:
        warrior1.f_attack(action2, stamina2)
    else:
        warrior1.f_defend(action2, stamina2)

    if action2 == 1:
        warrior2.f_attack(action1, stamina1)
    else:
        warrior2.f_defend(action1, stamina1)

    warrior1.f_print_status()
    warrior2.f_print_status()

    if warrior1.health > 10 and warrior2.health > 10:

        f_fight_round(warrior1, warrior2)


def f_fight_advanced(name1, name2):

    warrior1 = WarriorAdvanced(name1, randint(180, 230), randint(30, 50), randint(90, 110))
    warrior2 = WarriorAdvanced(name2, randint(180, 230), randint(30, 50), randint(90, 110))

    warrior1.f_print_status()
    warrior2.f_print_status()

    f_fight_round(warrior1, warrior2)

    if warrior1.is_alive() and warrior2.is_alive():

        if warrior1.health == warrior2.health:
            print('Both are too tired, draw declared')

        elif warrior1.health > warrior2.health:
            decision = input(str('Do you want to kill ' + warrior2.name + ' y or n ?:'))
            if decision == 'y':
                print(warrior1.name, 'kills', warrior2.name, '.', warrior1.name, 'wins!')
            else:
                print(warrior1.name, 'release', warrior2.name, '.', warrior1.name, 'wins!')
        elif warrior1.health < warrior2.health:
            decision = input(str('Do you want to kill ' + warrior1.name + ' y or n ?:'))
            if decision == 'y':
                print(warrior2.name, 'kills', warrior1.name, '.', warrior2.name, 'wins!')
            else:
                print(warrior2.name, 'release', warrior1.name, '.', warrior2.name, 'wins!')

    elif warrior1.is_alive() and not warrior2.is_alive():

        print(warrior2.name, "is dead.", warrior1.name, 'wins!')

    elif warrior2.is_alive() and not warrior1.is_alive():

        print(warrior1.name, "is dead.", warrior2.name, 'wins!')
    else:

        print('Both warriors are dead')


if input('Enter 1 for simple fight, 2 for advanced fight : ') == '1':

    f_fight_simple('Spartacus', 'Crixus')

else:

    f_fight_advanced('Spartacus', 'Crixus')
