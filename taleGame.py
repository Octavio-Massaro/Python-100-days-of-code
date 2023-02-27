print('''
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
      
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
      
ejm96 /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\





ad88                                                     
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  




 .. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
print("Welcome to Dark Forest")
print("Your mission is to get out of this dark place.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input(
    "You are in a dark forest and you see two paths ahead of you. The first takes you to the left and the other to the right. Which direction would you go? Be careful or you might get hurt. Type left or right\n"
)

if direction == "left":
    decision = input(
        "The path on the left leads you to an old hut. Would you go in or stay outside in the darkness of the forest? Type enter or stay\n"
    )
    if decision == "enter":
        final_decision = input(
            "Now you are inside the hut and you can see using a torch that you found inside that there is a map with an 'X' written on one of the walls and a trapdoor just below a table. Which one would you choose to take: the map and try to go to the 'X' mark, go down through the trapdoor or go outside and try to figure out some other way to escape? type: map or trapdoor or outside\n"
        )
        if final_decision == "tap":
            print(
                "You followed the map, but without a compass it's no use and you end up lost in the woods without knowing the direction back to the hut and eventually dying of thirst. Game Over"
            )
        elif final_decision == "trapdoor":
            print(
                "You followed a trail inside the trapdoor and finally saw a ladder and when you climbed it you ended up in a shelter on the side of a road and with a heart full of hope you managed to escape. Congratulations you won the game."
            )
        else:
            print(
                "You left the hut and ended up being eaten by wolves.\nGame over."
            )
    else:
        print(
            "You stood outside and in the darkness of the night a figure looked at you and called you to come closer. You did that and the figure turned out to be a vampire and you died.Game over"
        )
elif direction == "right":
    print(
        "You are at the middle of the right path when you hear a loud howl next to you and out of the suddenly a werewolf jumps out of a bush and devours you.\nGame Over."
    )
else:
    print("Please, just type left or right")