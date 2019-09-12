# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image BBedroom = "Boy_Bedroom.png"
image SakuraPath = "Sakura_Path.jpg"

define g = Character("Girl")
define b = Character("Boy")
    

    
screen showbutton():
    textbutton "Inventory":
        action ShowMenu ("inventory_screen")
        xpos 0.8
        ypos 0.1



# The game starts here.    
label start:
    $ has_phone = False
    $ coins = 0
    $ items = []
    $ items_length = len([items])


    
    $ showitems = True
   
  

    screen inventory_screen:
        
        text "{color=#000000}Inventory" xpos 0.8 ypos 0.1
        
        imagebutton:
            xpos 1000 ypos 430
            idle "arrowborderlessright.png" 
            hover "arrowborderright.png"
            action Return()
            
        for items_length in [items]:
            $ items = '\n'.join(items) 
            text "{color=#000000}[items]" xpos 0.8 ypos 0.2
        

    
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable("time", time - 0.01), false=[Hide("countdown"), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_dissolve
        
    init:
        $ timer_range = 0
        $ timer_jump = 0
        python:
            def countdown(st, at, length=0.0):

                remaining = length - st

                if remaining > 5.0:
                    return Text("%.1f" % remaining, color="#fff", size=72), .1
                elif remaining > 0.0:
                    return Text("%.1f" % remaining, color="#f00", size=72), .1
                else:
                    return anim.Blink(Text("0.0", color="#f00", size=72)), None

        image countdown = DynamicDisplayable(countdown, length=10.0) 
    
    #Attempt at adding fade to buttons
    #transform ib_fade:
      #  on show:
        #    alpha 1
        #on idle:
          #  easein 0.2 alpha 1
        #on hover:
          #  easein 0.2 alpha 0
 
    scene BBedroom
    "Today you made 10 coins!!"
    "You found an old watch!"
    $ coins += 10
    
    $ items.append("old watch")
    $ items.append("bracelet")
    "You now have %(coins)d coins."
    
    "You have a [items[1]] in your inventory."
    $ time = 10
    $ timer_range = 10
    $ timer_jump = "timer1_slow"
    show screen countdown
    menu:
        "Call girl":
            #hide screen countdown
            jump lookforphone
        "Go to school":
            hide screen countdown
            jump walkschool1
    label lookforphone:
        scene BBedroom
        "Look for your phone"
        # if not has_phone:
        show screen toSakura
        $ renpy.pause (hard = 'True')
        jump phonecall1     
    label timer1_slow:
        "You were too slow and died."
        return
            
    label phonecall1:
        "You found your phone!"
        $ items.append ("phone")
        "You now have a [items[2]] in your inventory"
        show screen showbutton()
        #$ showitems = true

        
        g "Hello?"
        b "Hey girl."
        jump walkschool1
       
    label walkschool1:
        scene SakuraPath
        "It's a nice day outside today."
        show screen toRoom
        $ renpy.pause (hard = 'True')
        
    screen toSakura:
        modal False
 
        imagebutton:
            xpos 1000 ypos 430
            idle "arrowborderlessright.png" 
            hover "arrowborderright.png"
            action [SetVariable("has_phone", True), Hide("toSakura", transition=dissolve), Jump("phonecall1")]
    screen toRoom:
        modal False
        imagebutton:
            xpos 20 ypos 430
            idle "arrowborderlessleft.png" 
            hover "arrowborderleft.png"
            action [SetVariable("has_phone", True), Hide("toRoom", transition=dissolve), Jump("lookforphone")]
            

    
return
