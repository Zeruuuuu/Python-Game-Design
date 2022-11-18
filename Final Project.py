#
# CS 17700-Project 3.py
# {Zeru Zhou, Carlos Emmanuel Santiago Estrada, Allison Deborah Plumadore}
# This program aimed to further develop the game base on project2. In this project,
#   players can not only move Pete horizontally and vertically, but also diagonally.
#   What's more, there are two 'warp points' in the game, which means players are able to
#   go to one warp point without changing score by moving to the other warp point. In addition,
#   we designed 'Hidden Hoosier Bummers', which are three hidden traps. If players first step
#   on that, the score would plus 20. If the players step on second time, the game would over.

#   At last, we still have three custom creative features, demonstrating as follows:
#   1. Night Mood. We design a button on the game panel. If players click on the 'Night mood' button,
#      the game panel would become black, and a huge text'Darkness is coming' would shown up on the panel
#      and last for 3 seconds(we imported time and use sleep).After that, the style of both panel and play field
#      changes: The background becomes indigo, all the texts become gold and the sensors and frozen area(custom #2)
#      also changes color. To achieve that, I create a new play field, and adjust everything in the new field to makes
#      the new field Night Mood. 
#      How I did this: I created a new field function for night mood first, and then we wrote a if statement in my panel function: if player choose night mood, call the new field;
#      else, call the original field. I also adjust the panel function to make sure every part of the panel and play field has its style changed


#   2. Frozen area. We draw up to 9 pink squares(actually random 0-9) in the play field(if player choose night mood,
#      the pink squares becomes dark red). if Pete step on the pink frozen area, it has 70% possibility to become blue
#      , which means it got frozen. If Pete becomes blue, every single movement he makes will be counted for double points
#      (which means that if the movement counts for 3 point normally,it counts for 6 points if Pete is blue.). So, if you want a good score,
#      TRY TO AVOID THE FROZEN ZONES!  
#      If blue Pete steps on Hoosier, it still plus 20 points. If blue Pete steps on warp zone, score will not change, just like normal case.
#      How I did this: I draw those pink squares in the frozen() function, and then call frozen() in field function. I suppose blue=False,
#      if Pete becomes blue, bule=True. Then I adjust score system depends on whether Pete is blue or not.

#   3. Gold food. We draw three Gold bubbles on play field. If Pete 'eats' the bubble, one of the followings would happen:
#      25 points minused by total score, 10% Possibility
#      10 points minused by total score, 40% Possibility
#      15 points plused by total score, 20% Possibility
#      5 points plused by total score, 30% Possibility
#      The change of total score would be -25,-10,5,or 15, no matter how Pete moves in this movement!
#      After Pete eats one bubble, the bubble eaten by Pete will disappear(undraw, and I used a True/False statement to make sure eaten bubbles
#      will not be counted again)
#      How I did this: I draw the bubbles in field function and operate them in Animating function. I undraw them after Pete eating them, and I used a True/False statement to make sure eaten bubbles
#      will not be counted again)
# 
#


# Create the panel
from graphics import * #import libraries 
import random
import time

def panel():      # Separate function creates the Game Panel window
    win=GraphWin('win',300,200)   
    win.setBackground('grey')    #set background color
    White=Rectangle(Point(0,0),Point(300,40))
    White.draw(win)
    White.setFill('white')   # draw the white rectangle for title
    text=Text(Point(150,20),'Pete-A-Maze')
    text.draw(win)    # Title
    Rec=Rectangle(Point(50,60),Point(250,160))
    Rec.draw(win)
    Rec.setFill('white')  #Place for Top scores
    text0=Text(Point(150,70),'TOP SCORES')
    text0.draw(win)
    text1=Text(Point(150,82),'==========')
    text1.draw(win)   #draw required texts
    NightMode= Rectangle(Point(0,0),Point(60,40))
    NightMode.setFill("Indigo")
    NightMode.draw(win)
    NightText= Text(Point(30,20),"Night Mode")
    NightText.setStyle("bold")
    NightText.setTextColor("gold")
    NightText.setSize(8)
    NightText.draw(win)
    def take(elem):
        k=elem.split(',')
        return int(k[1])  #use sort() function aimed to get the four best scores for initial state
    top=open('top_scores.txt','r')
    TS=top.readlines()
    TS.sort(key=take)
    STR0=''
    for i in range(4):
        STR0+=TS[i]    #convert the sorted score list into Strings in order to draw
        
    TS0=Text(Point(150,130),STR0)
    TS0.draw(win)    #Draw the top 4 scores
    Rec0=Rectangle(Point(95,170),Point(205,200))
    Rec0.draw(win)
    Rec0.setFill('light green')
    text2=Text(Point(150,185),'NEW PLAYER')
    text2.draw(win)  #create NEW PLAYER button
    Rec1=Rectangle(Point(250,170),Point(300,200))
    Rec1.draw(win)
    Rec1.setFill('red')
    text3=Text(Point(275,185),'EXIT')
    text3.draw(win) #create EXIT button
    x=0
    y=0
    Night=0  #Prepare for night mood. if night>=1, Start Night mood
    
    while not (x>250 and y>170):  # if click 'EXIT',close the window
        click=win.getMouse()    #let player click the window
        x=click.getX()
        y=click.getY()
        if (0<x<60 and 0<y<40):   #detect if player click on 'night mood' button 
            Night+=1    #if clicked on the button,the game panel would become black, then Night>=1,start night mood
            Black=Rectangle(Point(0,0),Point(300,200))
            Black.setFill('Black')
            Black.draw(win)
            TT=Text(Point(150,100),'DARKNESS IS COMING')  #a huge text'Darkness is coming' would shown up on the panel
            TT.setStyle("bold")
            TT.setSize(18)
            TT.setTextColor('red')
            TT.draw(win)
            time.sleep(2)    #here I use imported time.sleep() to make sure the scene above last for 2 seconds
            Black.undraw()
            TT.undraw()
            win.setBackground('Indigo')  #change color of panel window's background
            White.undraw()
            Rec.undraw()
            text.setTextColor('gold')   # change color of all texts into gold  (Because night mood)
            text0.setTextColor('gold')
            TS0.setTextColor('gold')
            text1.setTextColor('gold')
            
            
        if (x>95 and x<205 and y>170 and Night<1):  #if 'NEW PLAYER'button is clicked, and Night<1 means normal case(not night mood):
            text2.undraw()      #undraw items in the initial state
            Rec.undraw()
            TS0.undraw()
            text0.undraw()
            text1.undraw()
            text4=Text(Point(150,185),'START!')
            text4.draw(win)     #draw 'START'button
            text11=Text(Point(100,75),'Player Name:')
            text11.draw(win)    #draw 'Player Name'button
            inputBox = Entry(Point(220,75), 10)
            inputBox.draw(win)
            inputBox.setFill('white')  #create input box                   
            m=0
            n=0
            while not (m>250 and n>170):  # if click 'EXIT',close the window
                click=win.getMouse()  #let player click the window after filling in box
                m=click.getX()
                n=click.getY()
                if (m>95 and m<205 and n>170):  #START is clicked:Program is activated
                    T=inputBox.getText()  #get the text from inputbox
                    if T!='':   #program makes sense only if player fill something in the box
                        inputBox.undraw()
                        text4.undraw()
                        text13=Text(Point(150,185),'NEW PLAYER') #draw required items for the activated game
                        text13.draw(win)
                        text5=Text(Point(220,75),T) #Draw the player's name
                        text5.draw(win)
                        text6=Text(Point(120,140),'Score:')
                        text6.draw(win)
                        R=Rectangle(Point(0,170),Point(50,200))
                        R.draw(win)
                        R.setFill('Yellow')
                        text7=Text(Point(25,185),'RESET')
                        text7.draw(win)
                        text9=Text(Point(160,140),0) #initial score is 0
                        text9.draw(win)
                        Field,Pete,Trigger=field()  #call field() function which defined later
                        
                        sensor=sensitive(Field)  #call sensitive() function which defined later
                        trace,count,text12,COUNT=Animating(Field,Pete,sensor,win,text9,Night,Trigger) #call Animating() function which defined later
                        if COUNT<2:  #record the score only when there are less than 2 hidden hoosier bummers hit last game.
                            scoreOut(count,T) #call scoreOut() function in order to add recent score to top_scores.txt

                        win.close()

                        win=panel() #call main() in order to start a new round
                        break
                               
                        
                        
            win.close()
            break


        if(x>95 and x<205 and y>170 and Night>=1):   # Night>=1 means Night mood starts. We need to call different field function here(night mood field) 
            text2.undraw()      #undraw items in the initial state
            Rec.undraw()
            TS0.undraw()
            text0.undraw()
            text1.undraw()
            text4=Text(Point(150,185),'START!')
            text4.draw(win)     #draw 'START'button
            text11=Text(Point(100,75),'Player Name:')
            text11.setTextColor('gold')   #Here, set all the color 'gold' for night mood
            text11.draw(win)    #draw 'Player Name'button
            inputBox = Entry(Point(220,75), 10)
            inputBox.draw(win)
            inputBox.setFill('gold')  #create input box                   
            m=0
            n=0
            while not (m>250 and n>170):  # if click 'EXIT',close the window
                click=win.getMouse()  #let player click the window after filling in box
                m=click.getX()
                n=click.getY()
                if (m>95 and m<205 and n>170):  #START is clicked:Program is activated
                    T=inputBox.getText()  #get the text from inputbox
                    if T!='':   #program makes sense only if player fill something in the box
                        inputBox.undraw()
                        text4.undraw()
                        text13=Text(Point(150,185),'NEW PLAYER') #draw required items for the activated game
                        text13.draw(win)
                        text5=Text(Point(220,75),T) #Draw the player's name
                        text5.setTextColor('gold')
                        text5.draw(win)
                        text6=Text(Point(120,140),'Score:')
                        text6.setTextColor('gold')
                        text6.draw(win)
                        R=Rectangle(Point(0,170),Point(50,200))
                        R.draw(win)
                        R.setFill('Yellow')
                        text7=Text(Point(25,185),'RESET')
                        text7.draw(win)
                        text9=Text(Point(160,140),0) #initial score is 0
                        text9.setTextColor('gold')
                        text9.draw(win)
                          #call field() function which defined later
                        Field,Pete,Trigger=field1()  #call night mood field (field1 is night mood field)
                        
                        sensor=List_sensors(Field)  #call sensitive() function which defined later
                        trace,count,text12,COUNT=Animating(Field,Pete,sensor,win,text9,Night,Trigger) #call Animating() function which defined later
                        if COUNT<2: #record the score only when there are less than 2 hidden hoosier bummers hit last game.
                            scoreOut(count,T) #call scoreOut() function in order to add recent score to top_scores.txt

                        win.close()    #close the window
                        win=panel() #call main() in order to start a new round
                        break
                        
            win.close()
            break
    win.close()
    
    return(win)  #return values
      




def field():   #Separate function creates the Field Graphics window as specified
    Field=[]
    win=GraphWin('win',400,400)
    Field.append(win)
    centerList=[]    
    for i in range(10):     # draw field includes 10 x 10 grid of light-grey lines, and each grid is a 40x40 Rectangle
        for j in range(10):
            m=Rectangle(Point(i*40,j*40),Point((i+1)*40,(j+1)*40))
            m.draw(win)
            m.setFill('white')
            m.setOutline('light grey')
            Field.append(m)
    for i in range(2,100):
        p=Field[i].getCenter()
        centerList.append(p)    #create a list of white square's center(Use these centers to draw warp zones, hoosiers and gold bubbles)

    


    a=random.randint(0,97)      # a and b are random centers for warp zones; Hidden1-3 are points for Hidden hoosiers; Gold1-3 are centers for gold bubbles 
    b=random.randint(0,97) 
    Hidden1=random.randint(0,97)   #centerList[random.randint(0,97)] means random center of the 98 white squares except for the green one and red one. I need the center to draw Warp zones/gold bubble/Hoosier Bummer
    Hidden2=random.randint(0,97)
    Hidden3=random.randint(0,97)
    Gold1=random.randint(0,97)
    Gold2=random.randint(0,97)
    Gold3=random.randint(0,97)

    while not ((a != b) and (Hidden1 != Hidden2) and (Hidden2 != Hidden3) and (Hidden1 != Hidden3) and (Gold1 != a) and (Gold1 != b) and (Gold2 !=a) and (Gold2 != b) and (Gold3 !=a) and (Gold3 !=b) and (Gold1 != Gold2) and (Gold1 != Gold3) and (Gold2 != Gold3)): # Make sure that those items above will not drawn in the same place
        a=random.randint(0,97)
        b=random.randint(0,97) 
        Hidden1=random.randint(0,97)
        Hidden2=random.randint(0,97)
        Hidden3=random.randint(0,97)
        Gold1=random.randint(0,97)
        Gold2=random.randint(0,97)
        Gold3=random.randint(0,97)
        

    P1=centerList[Hidden1]     #get the center for warp and Gold bubbles objects
    P2=centerList[Hidden2]
    P3=centerList[Hidden3]
    Trigger=frozen(win)
    C1=Circle(centerList[a],5)  #draw warp zones
    C1.draw(win)
    C1.setFill('black')
    Field.append(C1)
    C2=Circle(centerList[b],5)
    C2.draw(win)
    C2.setFill('black')
    Field.append(C2)

    Field.append(P1)
    Field.append(P2)
    Field.append(P3)
    G1=Circle(centerList[Gold1],5)
    G1.draw(win)               #draw gold bubbles
    G1.setFill('Gold')
    G2=Circle(centerList[Gold2],5)
    G2.draw(win)
    G2.setFill('Gold')
    G3=Circle(centerList[Gold3],5)
    G3.draw(win)
    G3.setFill('Gold')
    Field.append(G1)
    Field.append(G2)
    Field.append(G3)    

    
    R=Rectangle(Point(0,0),Point(40,40))
    R.draw(win)
    R.setFill('green') #draw a 40x40 green Rectangle with a light-grey outline in the top-left grid
    R.setOutline('green')
    Field.append(R)
    R0=Rectangle(Point(360,360),Point(400,400))
    R0.draw(win)
    R0.setFill('red')
    R0.setOutline('red') #draw a 40x40 red Rectangle with a light-grey outline in the bottom-right grid
    Field.append(R0)
    Pete=Rectangle(Point(2,2),Point(38,38))
    Pete.draw(win)
    Pete.setFill('gold')#draw Pete 
    return(Field,Pete,Trigger) # Field and Pete are returned


def field1():   #New field function design for Night Mood
    Field=[]    
    win=GraphWin('win',400,400)
    win.setBackground("indigo")  # Set the background of the night mood as 'indigo'
    Field.append(win)
    centerList=[]
    for i in range(10):     # draw field includes 10 x 10 grid of light-grey lines, and each grid is a 40x40 Rectangle
        for j in range(10):
            m=Rectangle(Point(i*40,j*40),Point((i+1)*40,(j+1)*40))
            m.draw(win)
            m.setFill("indigo")
            m.setOutline('dark red')  # Set the background of the night mood as 'indigo'
            Field.append(m)
    for i in range(2,100):
        p=Field[i].getCenter()
        centerList.append(p)  # get the center of white squares and store them in a list


    a=random.randint(0,97)  # a and b are random centers for warp zones; Hidden1-3 are points for Hidden hoosiers; Gold1-3 are centers for gold bubbles 
    b=random.randint(0,97) 
    Hidden1=random.randint(0,97)  #centerList[random.randint(0,97)] means random center of the 98 white squares except for the green one and red one. I need the center to draw Warp zones/gold bubble/Hoosier Bummer
    Hidden2=random.randint(0,97)
    Hidden3=random.randint(0,97)
    Gold1=random.randint(0,97)
    Gold2=random.randint(0,97)
    Gold3=random.randint(0,97)

    while not ((a != b) and (Hidden1 != Hidden2) and (Hidden2 != Hidden3) and (Hidden1 != Hidden3) and (Gold1 != a) and (Gold1 != b) and (Gold2 !=a) and (Gold2 != b) and (Gold3 !=a) and (Gold3 !=b) and (Gold1 != Gold2) and (Gold1 != Gold3) and (Gold2 != Gold3)): # Make sure that those items above will not drawn in the same place
        a=random.randint(0,97)
        b=random.randint(0,97) 
        Hidden1=random.randint(0,97)
        Hidden2=random.randint(0,97)
        Hidden3=random.randint(0,97)
        Gold1=random.randint(0,97)
        Gold2=random.randint(0,97)
        Gold3=random.randint(0,97)

  
        

    P1=centerList[Hidden1]  #get the center for warp and Gold bubbles objects
    P2=centerList[Hidden2]
    P3=centerList[Hidden3]
    Trigger=frozen(win)     #Call frozen() function
    for i in Trigger:
        i.setFill('dark red')   #Pink frozen Zones becomes dark red in NIght Mood
        i.setOutline('dark red')
    C1=Circle(centerList[a],5)    #draw warp zones
    C1.draw(win)
    C1.setFill('black')
    Field.append(C1)
    C2=Circle(centerList[b],5)
    C2.draw(win)
    C2.setFill('black')
    Field.append(C2)

    Field.append(P1)
    Field.append(P2)
    Field.append(P3)
    G1=Circle(centerList[Gold1],5)  #draw gold bubbles
    G1.draw(win)
    G1.setFill('Gold')
    G2=Circle(centerList[Gold2],5)
    G2.draw(win)
    G2.setFill('Gold')
    G3=Circle(centerList[Gold3],5)
    G3.draw(win)
    G3.setFill('Gold')
    Field.append(G1)
    Field.append(G2)
    Field.append(G3)    

    R=Rectangle(Point(0,0),Point(40,40))
    R.draw(win)
    R.setFill('green') #draw a 40x40 green Rectangle with a light-grey outline in the top-left grid
    R.setOutline('green')
    Field.append(R)
    R0=Rectangle(Point(360,360),Point(400,400))
    R0.draw(win)
    R0.setFill('red')
    R0.setOutline('red') #draw a 40x40 red Rectangle with a light-grey outline in the bottom-right grid
    Field.append(R0)
    Pete=Rectangle(Point(2,2),Point(38,38))
    Pete.draw(win)
    Pete.setFill('gold')#draw Pete 
    return(Field,Pete,Trigger) # Field and Pete are returned


def Animating(Field,Pete,sensor,win,text9,Night,Trigger):   #Separate function written to move Pete
    isVertical = False #judge if Pete move vertically
    
    L='ABCDEFGHIJKL'
    S='abcdefghijkl'
    trace=[] #list of Pete's trace(Border locations )
    count=0 #count equals to score
    Judge=False #used to judge whether Pete pass sensor
    x=0
    y=0
    COUNT=0   #This COUNT is the number of Hoosier Bummer
    blue=False  #This is whether Pete is blue or gold(for frozen areas)

    G1=Field[106] #call field() or field1() to get gold bubbles
    G2=Field[107]
    G3=Field[108]
    Exist1=0      #That's the method to make sure gold bubbles can only be eaten once
    Exist2=0
    Exist3=0

    
    

    while not (x>=360 and y>=360):#Game ends when Pete is in the same cell as the red
        Num=random.randint(0,100)  # This Num is used to decided which result will happen when Pete eats gold bubble(Possibility)
        startcount=count        #The Score before new movement
        Minus10=False           # Followings are used to determine which result will happen when Pete eats gold bubble
        Plus5=False
        Minus25=False
        Plus15=False
        isVertical=False        # Detect whether Pete moves vertically or horizontally
        Judge=False             # If Pete does not move diagonally, detect whether it pass a sensor
        nosense=False           # If click at somewhere Pete moves diagonally but score only added by one, that's nosense
        Dia=False               # Detect whether Pete moves diagonally
        Real=False              # If moves diagonally, detect whether there are sensors in the middle of the cross            
        Hoosier=False           # Detect whether Pete steps on hoosier bummer
        Notmove=False           # If click at somewhere Pete does not move, that is Notmove
        Reach1=False            # If Pete eats gold1, Reach1 = True
        Reach2=False
        Reach3=False
        sensors=0               # This is used to count how many sensors in the cross when moving diagonally
        P=Pete.getCenter()
        x,y=P.getX(),P.getY()
        if (x==380 and y==380):  # if Pete reach the red square, end the game
            break
        click=Field[0].getMouse()  #mouse clicked 
        m,n=click.getX(),click.getY()
        Start=[]
        finish=[]
        
        
        for i in range(10):                      #if pete is in Field[i][j] rectangle (figure out what rectangle pete is in)
                                                        #Once  figure out what rectangle he is in, store that rectangle as starting rectangle (store the i and j that you used)
            for j in range(10):
                if i*40<=x<=i*40+40 and j*40 <=y <=j*40+40:
                    Start.append(i)
                    Start.append(j)   #store the started i and j
        
        if (y-20<=n<=y+20 and m>=x+20): #compare the clicked x and y to the center of Pete, then makes Pete move in the correct direction
            Pete.move(40,0)
                
        elif (x-20<=m<=x+20 and n>y+20):
            Pete.move(0,40)
            isVertical=True   #move vertically
            
        elif (y-20<=n<=y+20 and m<=x-20):
            Pete.move(-40,0)
               

        elif (x-20<=m<=x+20 and n<y-20):
            Pete.move(0,-40)
            isVertical=True  #move vertically

        elif  (m-20>x and n-20>y): #If Pete reach the requirements of diagonal movement, move Pete diagonally
            Pete.move(40,40)
            Dia=True

        elif  (x-20>m and y-20>n): # anyclick that up and left of the Pete
            Pete.move(-40,-40)
            Dia=True

        elif  (m-20>x and y-20>n): #anyclick that up and right of the Pete
            Pete.move(40,-40)
            Dia=True

        elif  (x-20>m and n-20>y): #anyclick that down and left of the Pete
            Pete.move(-40,40)
            Dia=True

        

        else:
            nosense=True
            Notmove=True
            

        
        

        P0=Pete.getCenter()          #if pete is in Field[i][j] rectangle (figure out what rectangle pete is in)
                                            #Once  figure out what rectangle he is in, store that in ending rectangle (store the i and j that you used)
        a,b=P0.getX(),P0.getY()

        for i in Trigger:
            Trigger_Center=i.getCenter() # find center of Tigger
            xC,yC=Trigger_Center.getX(),Trigger_Center.getY()

            if (a==xC and b==yC and random.random()<0.7): #if Pete steps on Trigger give frozen debuff 
                Pete.setFill('blue')
                blue=True

        for i in range(10):
            for j in range(10):
                if i*40<=a<=i*40+40 and j*40 <=b <=j*40+40:
                    finish.append(i)
                    finish.append(j)   #store the finished i and j

        if isVertical==True:  #store the Border locations as Pete moves vertically
            Str=L[Start[0]]+str(Start[1]+1)  #calculate the border location and use String in list'L' and 'S' to represent the location(Such as A1,B1)
            trace.append(Str)  #store border locations in list 'trace'
            P1=Point(Start[0]*40+20,finish[1]*40) #get the point which is located at the midpoint of the border line that Pete just passed(in order to calculate the score)
            
            
        else:  #Store the border locations as Pete moves horizontally
            Str1=S[finish[1]]+str(finish[0])#calculate the border location and use String in list'L' and 'S' to represent the location(Such as a1,b1)
            trace.append(Str1)  #store border locations in list 'trace'
            P1=Point(finish[0]*40,Start[1]*40+20)#get the point which is located at the midpoint of the border line that Pete just passed(in order to calculate the score)
            

        for i in range(len(sensor)):#sensor is the list of sensor rectangle's midpoint(defined later), im going to calculate the score
           
            if ((Dia==False) and (x<=sensor[i].getX()<=a) and (y==b==sensor[i].getY())): # if not move diagonally and compare Pete's previous center and current center with the center of sensors, if reach requirement,the
                                                                                        #   that means Pete moves horizontally or vertically and passed a sensor
                                                                                    
                Judge=True  #Pete passed sensor

            if ((Dia==False) and (a<=sensor[i].getX()<=x) and (y==b==sensor[i].getY())):
                Judge=True

            if ((Dia==False) and (a==x==sensor[i].getX()) and (y<=sensor[i].getY()<=b)):
                Judge=True

            if ((Dia==False) and (a==x==sensor[i].getX()) and (b<=sensor[i].getY()<=y)):
                Judge=True
            
            

                
            if (Dia==True and x<=sensor[i].getX()<=a and y<=sensor[i].getY()<=b):  # If Pete moved diagonally, then we need to count the number of sensors in the cross. Here we detect sensors from 4 directions
                                                                                   #    and thus we get the number of sensors in the cross
                sensors+=1  # Number of sensors in the middle cross
                Real=True    # There are sensors in the cross

            if (Dia==True and a<=sensor[i].getX()<=x and y<=sensor[i].getY()<=b):
                sensors+=1
                Real=True


            if (Dia==True and x<=sensor[i].getX()<=a and b<=sensor[i].getY()<=y):
                sensors+=1
                Real=True


            if (Dia==True and a<=sensor[i].getX()<=x and b<=sensor[i].getY()<=y):
                sensors+=1
                Real=True

                
            if (sensors==0 and Dia==True):
                nosense=True
            
        

        c1=Field[101]  #Call field() to operate warp zones, hidden hossier bummers  here
        c2=Field[102]
        
        P1=Field[103]
        P2=Field[104]
        P3=Field[105]

        if (G1.getCenter().getX()==a and G1.getCenter().getY()==b):  #Cases if Pete eats gold bubbles
            G1.undraw()    #undraw bubbles that are eaten by Pete
            if 0<=Num<=10:   #10% possibility: score minus 25
                Minus25=True 
                Exist1+=1    #times arrive at gold 1(make sure the effect would only count by once)
                Reach1=True #Gold1 has been eaten
            elif 10<Num<=30: #20% possibility: score plus 15
                Plus15=True
                Exist1+=1
                Reach1=True
            elif 30<Num<=60: #30% possibility: score plus 5
                Plus5=True
                Exist1+=1
                Reach1=True
            else:            #40% possibility: score minus 10
                Minus10=True
                Exist1+=1
                Reach1=True


        if (G2.getCenter().getX()==a and G2.getCenter().getY()==b): # Same method as Gold1 (codes above)
            G2.undraw()
            if 0<=Num<=10:
                Minus25=True
                Exist2+=1
                Reach2=True
            elif 10<Num<=30:
                Plus15=True
                Exist2+=1
                Reach2=True
            elif 30<Num<=60:
                Plus5=True
                Exist2+=1
                Reach2=True
            else:
                Minus10=True
                Exist2+=1
                Reach2=True

        if (G3.getCenter().getX()==a and G3.getCenter().getY()==b): # Same method as Gold1 (codes above)
            G3.undraw()
            if 0<=Num<=10:
                Minus25=True
                Exist3+=1
                Reach3=True
            elif 10<Num<=30:
                Plus15=True
                Exist3+=1
                Reach3=True
            elif 30<Num<=60:
                Plus5=True
                Exist3+=1
                Reach3=True
            else:
                Minus10=True
                Exist3+=1
                Reach3=True

            
        
        if (c1.getCenter().getX()==P0.getX() and c1.getCenter().getY()==P0.getY()):  # if Pete steps on Warp Zone (from c1 to c2)
            if Notmove==False:
           
                Pete.undraw()  # undraw Pete and draw it on another Warp point
                Pete=Rectangle(Point(c2.getCenter().getX()-18,c2.getCenter().getY()+18),Point(c2.getCenter().getX()+18,c2.getCenter().getY()-18)) #draw Pete on the other warp zone
                Pete.draw(Field[0])
                if blue==False:     # if Pete is gold before movement, it will still be gold; if it is blue, it will still be blue
                    Pete.setFill('gold')
                else:
                    Pete.setFill('blue')
            if blue == False:       # Cases that Pete is not frozen(blue)
                if  (Judge==True and nosense==False):  # Due to the fact that warp zone does not change score, we minus the score that will add later.(This is the case that only pass a sensor)
                    count=count-3
                elif (Judge==False and nosense==False):  #not pass sensor, horizontal or vertical
                    count=count-1
                elif (Dia==True and nosense==True and Real==False): #no sensor in the middle cross when moving diagonally
                    count=count-1
                elif(Dia==True and Real==True):  #have sensors in the middle cross when moving diagonally
                    count=count-3*sensors

                else:
                    count=count-0

            else:
                if  (Judge==True and nosense==False):  # Due to the fact that warp zone does not change score, we minus the score that will add later.(If Pete is frozen, the score add latr will double, so we minus double points.)
                    count=count-6
                elif (Judge==False and nosense==False):
                    count=count-2
                elif (Dia==True and nosense==True and Real==False):
                    count=count-2
                elif(Dia==True and Real==True):
                    count=count-6*sensors

                else:
                    count=count-0     

        if (c2.getCenter().getX()==P0.getX() and c2.getCenter().getY()==P0.getY()): # if Pete steps on Warp Zone (from c2 to c1), just the same as code above, This time is from c2 to c1 instead of from c1 to c2
            if Notmove==False:
                Pete.undraw()   # undraw Pete and draw it on another Warp point
                Pete=Rectangle(Point(c1.getCenter().getX()-18,c1.getCenter().getY()+18),Point(c1.getCenter().getX()+18,c1.getCenter().getY()-18))
                Pete.draw(Field[0])
                if blue==False:   # if Pete is gold before movement, it will still be gold; if it is blue, it will still be blue
                    Pete.setFill('gold')
                else:
                    Pete.setFill('blue')
            if blue== False:      # Cases that Pete is not frozen(blue)
                if  (Judge==True and nosense==False):   # Due to the fact that warp zone does not change score, we minus the score that will add later.
                    count=count-3
 
                elif (Judge==False and nosense==False): #not pass sensor, horizontal or vertical
                    count=count-1
                elif (Dia==True and nosense==True and Real==False): #no sensor in the middle cross when moving diagonally
                    count=count-1
                elif(Dia==True and Real==True): #have sensors in the middle cross when moving diagonally
                    count=count-3*sensors

                else:
                    count=count-0
            else:
                if  (Judge==True and nosense==False):  # Due to the fact that warp zone does not change score, we minus the score that will add later.(If Pete has been frozen)
                    count=count-6

                elif (Judge==False and nosense==False):
                    count=count-2
                elif (Dia==True and nosense==True and Real==False):
                    count=count-2
                elif(Dia==True and Real==True):
                    count=count-6*sensors

                else:
                    count=count-0     

 
        if ((P1.getX()==a and P1.getY()==b) or (P2.getX()==a and P2.getY()==b) or (P3.getX()==a and P3.getY()==b)):  #Case if Pete steps on Hidden Hoosier Bummers
            COUNT+=1  #Number of Bummers plus one
            Hoosier=True  # No matter how players move this round, score will plus 20 (this part of code will appear later)
            if COUNT <2:  # only make sense if this is the first time players step on Hidden hoosier Bummers
                Tx=Text(Point(200,200),'You’ve hit a Hidden Hoosier Bummer!')   # draw required texts
                Tx.draw(Field[0])
                if Night>=1:
                    Tx.setTextColor("gold")   #condition for night moood(text is gold)
                time.sleep(3) # sleep for 3 seconds
                Tx.undraw()

               

            if COUNT>=2:  #Case if players step on the hidden hoosier Bummers twice
                Tx1=Text(Point(200,200), 'That’s two Hoosier Bummers. Game Over' )  # draw required text
                Tx1.draw(Field[0])
                if Night>=1:   #change for night mood
                    Tx1.setTextColor("gold")
                time.sleep(2)  #sleep for two seconds
                Tx1.undraw()
                Field[0].close()  # to end the game, we need to close the play field
                break

        if blue==False:  #count the points added each step if Pete is not frozen
            if  (Judge==True and nosense==False and Dia==False ): # when Pete not move diagonally and pass a sensor
                count=count+3
            elif (Judge==False and nosense==False and Dia==False ): # when Pete not move diagonally and does not pass a sensor
                count=count+1
            elif (Dia==True and nosense==True and Real==False ): #no sensors in the middle cross when moving diagonally
                count=count+1
            elif (Dia==True and Real==True ):    #have sensors in the middle cross when moving diagonally
                count=count+3*sensors

            else:
                count=count+0
        else:            # cases when Pete is frozen(all score counting double)
            if  (Judge==True and nosense==False and Dia==False ):
                count=count+6
            elif (Judge==False and nosense==False and Dia==False ):
                count=count+2
            elif (Dia==True and nosense==True and Real==False):
                count=count+2
            elif (Dia==True and Real==True ):
                count=count+6*sensors

            else:
                count=count+0


        if Minus10==True and ((Exist1<=1 and Reach1==True) or (Exist2<=1 and Reach2==True) or( Exist3<=1 and Reach3==True)) and Hoosier==False: #If it is the first time Pete eats Gold1/Gold2/Gold3(you cant eat the same bubble twice)
            Tx2=Text(Point(200,200), 'Great! 10 points has been minused by your score.' )  #Text on playfield                                                     # and the random result is Minus 10
            Tx2.draw(Field[0])
            if Night>=1:
                Tx2.setTextColor("gold")  #Nightmood
            time.sleep(3) #Text stays for 3 seconds
            Tx2.undraw()
            count=startcount-10 #the final count of this step is -10 no matter how Pete moves

        if Minus25==True and ((Exist1<=1 and Reach1==True) or (Exist2<=1 and Reach2==True) or( Exist3<=1 and Reach3==True)) and Hoosier==False : #If it is the first time Pete eats Gold1/Gold2/Gold3(you cant eat the same bubble twice)
            Tx3=Text(Point(200,200), 'Great! 25 points has been minused by your score.' )                                                           # and the random result is Minus 25
            Tx3.draw(Field[0])
            if Night>=1:
                Tx3.setTextColor("gold")
            time.sleep(3)
            Tx3.undraw()
            count=startcount-25   #the final count of this step is -25 no matter how Pete moves

        if Plus5==True and ((Exist1<=1 and Reach1==True) or (Exist2<=1 and Reach2==True) or( Exist3<=1 and Reach3==True)) and Hoosier==False:  #If it is the first time Pete eats Gold1/Gold2/Gold3(you cant eat the same bubble twice)
            Tx4=Text(Point(200,200), 'Sorry! 5 points has been added by your score.' )                                                      # and the random result is Plus 5
            Tx4.draw(Field[0])
            if Night>=1:
                Tx4.setTextColor("gold")
            time.sleep(3)
            Tx4.undraw()
            count=startcount+5   #the final count of this step is 5 no matter how Pete moves

        if Plus15==True and ((Exist1<=1 and Reach1==True) or (Exist2<=1 and Reach2==True) or( Exist3<=1 and Reach3==True)) and Hoosier==False:  #If it is the first time Pete eats Gold1/Gold2/Gold3(you cant eat the same bubble twice)
            Tx5=Text(Point(200,200), 'Sorry! 15 points has been added by your score.' )                                                     # and the random result is Plus 15
            Tx5.draw(Field[0])
            if Night>=1:
                Tx5.setTextColor("gold")
            time.sleep(3)
            Tx5.undraw()
            count=startcount+15    #the final count of this step is 15 no matter how Pete moves

        if Hoosier==True:
            count=startcount+20  # The Hidden Hoosier Bummer is the most importent, so if players hit this, no matter what happened before, 20 is plused by total score.(Not conflict with Project 3)

        if count<0:
            count=0    #make sure the total score cannot be lower than 0


            

        
        text9.undraw() # undraw the initial score
        text9=Text(Point(160,140),count) #draw the new score
        if Night>=1:
            text9.setTextColor('gold')
        text9.draw(win)
        
    
           


    if COUNT<=1:  #Following will be drawn only when players step on 0 or 1 Hidden Hoosier Bummer
        text8=Text(Point(200,200),'Finished! Click to Close')#game over text
        text8.draw(Field[0])
        if Night>=1:
            text8.setTextColor("gold")


        Field[0].getMouse() #click anywhere to close
    
        Field[0].close()
    return(trace,count,text9,COUNT) #return the border locations Pete passed through;score(count);and score's text version that is drawn on win





def frozen(Window): # Separate function that adds a tile Trigger with chance of being a cold front
    Trigger=[]
    for j in  range(1,9,3): # create tile Trigger
        for i in range(1,9,3):
            randomInt=random.randint(0,100)
            if(randomInt <50):
                Trigger1=Rectangle(Point(0+40*i,0+40*j),Point(40+40*i,40+40*j))
                Trigger1.draw(Window)
                Trigger1.setFill("pink")
                Trigger1.setOutline("light gray")
                Trigger.append(Trigger1)
    return Trigger  #return the Trigger list, the ready to be called in field()



#Modified Field Function

def List_sensors(Field):  # This function prepare sensors for Night Mood
    row=[]      #midpoint list of the vertical borders
    col=[]      #midpoint list of the horizontal borders
    sensor=[]   #sensor location list
    for i in range(40,400,40):
        for j in range(20,400,40):
            P=Point(i,j)
            row.append(P) #apend midpoints 
    for i in range(20,400,40):
        for j in range(40,400,40):
            P0=Point(i,j)
            col.append(P0) ##apend midpoints 
    for i in range(len(row)):
        if random.random()<0.4: #for all vertical midpoints, only 40% of them is chose to be the center of sensor Rectangle
            P=row[i]
            x,y=P.getX(),P.getY()
            rec=Rectangle(Point(x-2.5,y+18),Point(x+2.5,y-18))
            rec.draw(Field[0])   
            rec.setFill('dark red') #draw the sensor rectangle and set their color to Night Mood color
            sensor.append(P)
    for i in range(len(col)):
        if random.random()<0.4:#for all horizontal midpoints, only 40% of them is chose to be the center of sensor Rectangle
            P=col[i]
            x,y=P.getX(),P.getY()
            Rec=Rectangle(Point(x-18,y+2.5),Point(x+18,y-2.5))
            Rec.draw(Field[0])
            Rec.setFill('dark red')#draw the sensor rectangle and set their color to Night Mood color
            sensor.append(P)
    return(sensor)#return the location of sensor(we use list of sensor rectangles' center points to represent their location)







def sensitive(Field):   #Separate function draws sensors as specified
    row=[]      #midpoint list of the vertical borders
    col=[]      #midpoint list of the horizontal borders
    sensor=[]   #sensor location list
    for i in range(40,400,40):
        for j in range(20,400,40):
            P=Point(i,j)
            row.append(P) #apend midpoints 
    for i in range(20,400,40):
        for j in range(40,400,40):
            P0=Point(i,j)
            col.append(P0) ##apend midpoints 
    for i in range(len(row)):
        if random.random()<0.4: #for all vertical midpoints, only 40% of them is chose to be the center of sensor Rectangle
            P=row[i]
            x,y=P.getX(),P.getY()
            rec=Rectangle(Point(x-2.5,y+18),Point(x+2.5,y-18))
            rec.draw(Field[0])   
            rec.setFill('orange') #draw the sensor rectangle and set their color to orange
            sensor.append(P)
    for i in range(len(col)):
        if random.random()<0.4:#for all horizontal midpoints, only 40% of them is chose to be the center of sensor Rectangle
            P=col[i]
            x,y=P.getX(),P.getY()
            Rec=Rectangle(Point(x-18,y+2.5),Point(x+18,y-2.5))
            Rec.draw(Field[0])
            Rec.setFill('orange')#draw the sensor rectangle and set their color to orange
            sensor.append(P)
    return(sensor)#return the location of sensor(we use list of sensor rectangles' center points to represent their location)

   
def scoreOut(count,T):
    f=open('top_scores.txt','a')
    m=str(count)
    var=T+','+m #var equals most recent player and score
    f.write(var+'\n') #scoresOut() function adds most recent player and score to top_scores.txt
    f.close()
                

def scoreIn():
    
    best=[]
    def take(elem):
        k=elem.split(',')
        return int(k[1])
    read=open('top_scores.txt','r')
    g=read.readlines() #scoresIn() function reads values from top_scores.txt file
    g.sort(key=take)   #sort() function is able to get the best 4 scores(key= int(score))
    for i in range(4): #scoresIn() only returns the best 4 scores
        best.append(g[i])
    return best
    
        
def main():
    win=panel()
    # I called everything in panel()function. If I call panel() here,the whole program will run

main()
    
