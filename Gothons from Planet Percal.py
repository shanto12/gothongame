from sys import exit
from random import randint
from textwrap import dedent




class Scene():
    def enter(self):
        pass

class Engine():
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()


class Death(Scene):

        quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud.... if she were smarter.",
            "Such a luser!",
            "I have a small puppy thats better at this.",
            "You are worse than your Dads jokes"
        ]


        def enter(self):
            print(Death.quips[randint(0, len(quit()-1))])
            exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal have invaded your ship and destroyed your entire crew.
            You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the
            bridge, and blow the ship up after getting into an escape pod.
            
            You are running down the cntral corridor to the Weapons Armory when a Gothon jumpos out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.
            He is blocking the door to the Armory and about to pull a weapon to blast you.
            """))
        action = input('> ')
        if action =='shoot!':
            print(dedent("""
            Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, hich throws off your aim. Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother bougth him. Which makes him fly into an insane rage and blast you
            repeatedly in the face until you are dead. Then he eats you.
            """))

            return 'death'

        elif action =='dodge!':
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and slide right as the Gothons blaster cranks a laser past your head.
            In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out.
            You wake up shortly after only to die as the Gothon stomps on your head and eats you.
            """))

            return 'death'
        elif action =='tell a joke':
            print(dedent("""
            Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know:
            Lbhe zsadfl asdflksjd fasdflasdlfkj . The Gothon stops, tries not to laugh, then busts out 
            laughing and cant move. While he is laughing you run up and shoot him square in the head
            putting him down, then jump through the Weapon Armory door
            """))

            return 'laser_weapon_armory'
        else:
            print('DONE NOT COMPUTE!')
            return 'central_corridor'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to
            tke control of the ship. Each of them has an even uglier clown costume than the last. They havent pulled their
            weapons out yet, as they see the active bomb under your arm and dont want to set it off.
            """))
        action = input('> ')
        if action =='throw the bomb':
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back
            killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they ill probably blow up when it goes off.
            """))

            return 'death'
        elif action =='slownly place the bomb':
            print(dedent("""
            You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing the door,
            punch the close button and blast the lock so the Gothons cant get out. Now that the bomb is placed you run to
            the escape pod to get off this tin can
            """))

            return 'escape_pod'
        else:
            print('DONE NOT COMPUTE!')
            return 'the_bridge'



class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            You rush through the ship deseperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any
            Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods,
            and now need to pick one to take. Some of them could be damaed but you dont have time to look.
            There is 5 pods. which one do you take?
            """))
        good_pod = randint(1,5)
        guess = input('> ')

        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the void of space, then implodes as the hull ruptures, crusing your body into jam jelly
            """))

            return "death"
        else:
            print(dedent("""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into the space heading to the planet below. As it flies to the planet, 
            you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!
            """))

            return 'finished'

class Finished(Scene):
    def enter(self):
        print('You won! Good job.')
        return 'finished'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, Crouch and scan the room for more Gothons that might be hiding. Its dead quiet, too quiet.
        You stand up and run to the far side of the room and find the neutron bomb in its containe.
        There is a keypad lock on the box and you need the code to get the bomb out. If you get the code rong 10 times then the lock
        closes forever and you cant get the bomb. The code is 3 digits
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input('[keypad]> ')
        guesses = 0

        while guess!= code and guesses<10:
            print('BZZZZEDDD!')
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting the gas out.
            You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot
            """))

            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together.
            You decide to sit there, and finally the Gothons blow up the ship from their ship and you die.
            """))

            return 'death'

class Map():

    scenes = {'central_corridor': CentralCorridor(),
                 'death': Death(),
                 'the_bridge': TheBridge(),
                 'escape_pod': EscapePod(),
                 'laser_weapon_armory': LaserWeaponArmory()
                 }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val =  Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene((self.start_scene))


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
