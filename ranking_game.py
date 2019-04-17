# This code is developed in Psychopy2 using python 2
#This is a piece of game from an experiment that i have programmed during my programmer job at university of cologne
# The following code is for a ranking game and each frame of the display should display 6 pie charts including 6 buttons below them and a reset button.
# User should be able to choose pie charts(lotteries) based on their interest and rank them based on how much they like each lottery. Each click on the button will allow the user to give ranking for every pie chart based on their interest 
#first click on a button under a pie chart will give it a first rank and displays the rank on the screen and the rest respectively.
# Since there was no option for buttons in psychopy in 2017, I programmed it from the scratch. 
# The basic idea for this is as follows. 
# For simple ranking button => I drew a polygon and colored it so it could be easily distingushable from the background. then i looked for the mouse movement and mouse clicks.
# The button color would change and display the ranking ( 1 to 6 numbers) if the mouse is inside the button and get clicked. 
# For a resert button => I have used while loop. the whole routine would go on until the reset button is clicked, if the reset button is clicked, the while loop will break and 
#whole ranking routine starts again which means, all the ranking will disappear and user can change their ranking and re rank all the lotteries.




def ranking_phase():

 #################################### LIST OF SUBJECT NUMBERS FOR THE EXPERIMENTS  ####################################

    subject_list1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']



    ####################################

   #################################### DIFFERENT CONDITIONS FOR DIFFERENT SUBJECTS  ####################################   

    if Subj_Number in subject_list1:

    

        trials = data.TrialHandler(nReps=1, method='sequential', 

        extraInfo=subj_info, originPath=-1,

        trialList=data.importConditions(u'sequence_lottery_rank99.xlsx'),

        seed=None, name='trials')

        thisExp8.addLoop(trials) 

                 

    ##########################################################



    else:

        pass

        thisExp8.addLoop(trials)  # add the loop to the experiment

        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values



    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)

        if thisTrial != None:

            for paramName in thisTrial.keys():

                exec(paramName + '= thisTrial.' + paramName)

    for thisTrial in trials:

            currentLoop = trials

            #mywin.flip()

            

        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)

            if thisTrial != None:

                for paramName in thisTrial.keys():

                    exec(paramName + '= thisTrial.' + paramName)


######################

###########

           #########################################################new lines#########################################        

            count = 0        

            #while count != 6:

            while True:    #################################### WHILE loop for the whole routine, all the code below this while loop runs until the break is clicked
             ####################################This is important for RESET button, if the is not under this while loop, the reset button will not work for the code
              ####################################which is not under this while loop

                while True:   #################################### this wHILE loop is for each button, so user can also use reset button for every frame       


            ######################################################### All the below lines will display all the following items on the screen for each and every frame#########################################   

         #------Prepare to start Routine "main trial"-------

                    t = 0


                    routine_1Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    text_D.setText(textPrompt)

                    probability_L1.setText(prob_left_L1)

                    probability_L2.setText(prob_left_L2)

                    probability_L3.setText(prob_left_L3)

                    probability_L4.setText(prob_left_L4)

                    probability_L5.setText(prob_left_L5)

                    probability_L6.setText(prob_left_L6)

                    outcome_L1.setText(outcome_left_L1)

                    outcome_L2.setText(outcome_left_L2)

                    outcome_L3.setText(outcome_left_L3)

                    outcome_L4.setText(outcome_left_L4)

                    outcome_L5.setText(outcome_left_L5)

                    outcome_L6.setText(outcome_left_L6)

                    euro_L1.setText(euro1)

                    euro_L2.setText(euro1)

                    euro_L3.setText(euro1)

                    euro_L4.setText(euro1)

                    euro_L5.setText(euro1)

                    euro_L6.setText(euro1)

                    circleL1.setPos([-380,220])

                    circleL2.setPos([0,220])

                    circleL3.setPos([380,220])

                    circleL4.setPos([-380,-280])

                    circleL5.setPos([0,-280])

                    circleL6.setPos([380,-280])

                    

                    sliceL1.setPos([-380,220])

                    sliceL1.setOri(probability/2)

                    sliceL1.visibleWedge = [0.0, 360-probability]

                    sliceL1.draw()

                    

                    sliceL2.setPos([0,220])

                    sliceL2.setOri(probability2/2)

                    sliceL2.visibleWedge = [0.0, 360-probability2]

                    sliceL2.draw()

                    

                    sliceL3.setPos([380,220])

                    sliceL3.setOri(probability3/2)

                    sliceL3.visibleWedge = [0.0, 360-probability3]

                    sliceL3.draw()

                    

                    sliceL4.setPos([-380,-280])

                    sliceL4.setOri(probability4/2)

                    sliceL4.visibleWedge = [0.0, 360-probability4]

                    sliceL4.draw()

                    

                    sliceL5.setPos([0,-280])

                    sliceL5.setOri(probability5/2)

                    sliceL5.visibleWedge = [0.0, 360-probability5]

                    sliceL5.draw()

                    

                    sliceL6.setPos([380,-280])

                    sliceL6.setOri(probability6/2)

                    sliceL6.visibleWedge = [0.0, 360-probability6]

                    sliceL6.draw()

 #################################### every buttons opacity is given with 0.5 to distingush it from the background ####################################

                    polygon.opacity = 0.5

                    polygon_2.opacity = 0.5

                    polygon_3.opacity = 0.5

                    polygon_4.opacity = 0.5

                    polygon_5.opacity = 0.5

                    polygon_6.opacity = 0.5

#################################### Initializing text components to display ranks  ####################################


                    text_1.text = ""

                    text_2a.text = ""

                    text_3.text = ""

                    text_4a.text = ""

                    text_5a.text = ""

                    text_6.text = ""

                    text_23.text = ""

 #################################### display the text on the scrren  ####################################

                    text_1.draw()

                    text_2a.draw()

                    text_3.draw()

                    text_4a.draw()

                    text_5a.draw()

                    text_6.draw()

                    text_23.draw()

                    #diese_lottery_1.draw()

 ####################################different conditions for different subjects, these conditions are based on experimental conditions  ####################################

                    if subj_info['Counter_Balance'] == '1':

                        circleL1.setFillColor([0, 0, 153], colorSpace="rgb255")




                    else:

                        circleL1.setFillColor('green') 



                         

                    if subj_info['Counter_Balance'] == '1':

                        circleL2.setFillColor([0, 0, 153], colorSpace="rgb255")

                    else:

                        circleL2.setFillColor('green') 

                        


                        

                    if subj_info['Counter_Balance'] == '1':

                        circleL3.setFillColor([0, 0, 153], colorSpace="rgb255")

                    else:

                        circleL3.setFillColor('green') 

                         

                    if subj_info['Counter_Balance'] == '1':

                        circleL4.setFillColor([0, 0, 153], colorSpace="rgb255")

                    else:

                        circleL4.setFillColor('green') 

                        


                    if subj_info['Counter_Balance'] == '1':

                        circleL5.setFillColor([0, 0, 153], colorSpace="rgb255")

                    else:

                        circleL5.setFillColor('green') 

                         

                    if subj_info['Counter_Balance'] == '1':

                        circleL6.setFillColor([0, 0, 153], colorSpace="rgb255")

                    else:

                        circleL6.setFillColor('green') 

          


                    key_resp_2 = event.BuilderKeyResponse()



 #################################### Initializing different componenets  ####################################                    

                    pol_1 = 0

                    pol_2 = 0

                    pol_3 = 0

                    pol_4 = 0

                    pol_5 = 0

                    pol_6 = 0

                    

                    button_1= 0

                    button_2= 0

                    button_3= 0

                    button_4= 0      

                    button_5= 0

                    button_6= 0

                    

                    
 #################################### ALL the below items will be displayed on the screen ####################################
                    # -------Start Routine "main trial"-------

                    while continueRoutine:

                        # get current time

                        t = routine_1Clock.getTime()

                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)



                        text21.draw()

                        text_weiter.draw()


                        text_1.draw()

                        text_2a.draw()

                        text_3.draw()

                        text_4a.draw()

                        text_5a.draw()

                        text_6.draw()

                        text_23.draw()

                        #round_text_22.draw()

                        #text_lottery.draw()

                        polygon_7.draw() 


                        if t >= 0.0 and mouse.status == NOT_STARTED:

                            # keep track of start time/frame for later

                            mouse.tStart = t

                            mouse.frameNStart = frameN  # exact frame index

                            mouse.status = STARTED

                            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

 #################################### once the mouse movements starts  ####################################





                        # check if all components have finished

                        if not continueRoutine:  # a component has requested a forced-end of Routine

                            break

                        continueRoutine = False  # will revert to True if at least one component still running

                        for thisComponent in sentenceComponents:

                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                continueRoutine = True

                                break  # at least one component has not yet finished

                        # refresh the screen

                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                            mywin.flip()

                            

                    # -------Ending Routine "sentence"-------

                    for thisComponent in sentenceComponents:

                        if hasattr(thisComponent, "setAutoDraw"):

                             thisComponent.setAutoDraw(False)

                             

                    x, y = mouse.getPos()

                    buttons = mouse.getPressed()

                    

        

                    if mouse.isPressedIn(polygon): ######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################

                        polygon.opacity = 0.2

                        #text21.text = "ciao"

                        text_1.text = "1."

                        text_23.text = "Bitte"



                        button_1= 1

                        f.write("1" + '\t') ####################### write the use choice in the text file##################################

                        pol_1 = pol_1+1

                        count = count + 1 

                        #diese_lottery_1.draw()



                    if mouse.isPressedIn(polygon_2): ######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################

                        polygon_2.opacity = 0.2

                        text_2a.text = "1."

                        f.write("2" + '\t')

                        pol_2 = pol_2+1

                        button_1= 2

                        text_23.text = "Bitte"

                        count = count + 1 #iteration for the rank for all the six buttons

        
######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################

                    if mouse.isPressedIn(polygon_3):

                        polygon_3.opacity = 0.2

                        text_3.text = "1."

                        f.write("3" + '\t')

                        pol_3 = pol_3+1

                        button_1= 3 

                        text_23.text = "Bitte"

                        count = count + 1#########################################################new lines#########################################

 ######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################
                   

                    if mouse.isPressedIn(polygon_4):

                        polygon_4.opacity = 0.2

                        

                        text_4a.text = "1."

                        f.write("4" + '\t')

                        pol_4 = pol_4+1

                        button_1= 4

                        text_23.text = "Bitte"

                        count = count + 1#########################################################new lines#########################################

 ######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################
                       

                    if mouse.isPressedIn(polygon_5):

                        polygon_5.opacity = 0.2

                        

                        text_5a.text = "1."

                        f.write("5" + '\t')

                        pol_5 = pol_5+1

                        button_1= 5

                        text_23.text = "Bitte"

                        count = count + 1#########################################################new lines#########################################

                                
######################### IF the mouse is pressed in a polygon, the color changes and give the text "1" for the rank################################


                    if mouse.isPressedIn(polygon_6):

                        polygon_6.opacity = 0.2



                        f.write("6" + '\t')

                        text_6.text = "1."

                        pol_6 = pol_6+1

                        button_1= 6

                        text_23.text = "Bitte"

                        count = count + 1#########################################################new lines#########################################

                                


                    thisExp8.addData('button_1', button_1)

                    #thisExp.nextEntry()

                    # the Routine "trial" was not non-slip safe, so reset the non-slip timer

                    routineTimer.reset()

        #################

        #################

        ####         ####

        ####    2  rank  ####

        ####         ####

        #################

        #################

        

        
######################### for the second rank, next routine starts and  for a new frame, every is as follows as for the first rank################################

                                

                    # ------Prepare to start Routine "routine_12"-------

                    t = 0

                    routine_2Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    

        

                    key_resp_2 = event.BuilderKeyResponse()

                    # keep track of which components have finished

                    routine_12Components = [text_D, mouse_2, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]

                    

                    for thisComponent in routine_12Components:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED

                    

                    # -------Start Routine "routine_12"-------

                        

                    while continueRoutine:

######################### While loop for the second ranking routine ################################


                        # get current time

                            t = routine_2Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

########################## update/draw components on each frame#########################

                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()



                            text_reset.draw()

                            text_weiter.draw()

                            polygon_7.draw() 

                            polygon_8.draw()

                            #diese_lottery_1.draw()


                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()



                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

                            #msg.text = 'inside'
######################### the below lines are to display the ranking from the previous frame. if it was already clicked, the color of the button and rank should not change #########################
######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################
######################### this change only occurs, if it was clicked in the before frame #########################
                            
                            if polygon.opacity == 0.2: 
                                text_1.draw()

  
  ######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################


                            if polygon_2.opacity == 0.2:

                                    

                                text_2a.draw()


######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################

                            #msg.text = 'inside'

                            if polygon_3.opacity == 0.2:


                                text_3.draw()
######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################

                            if polygon_4.opacity == 0.2:

                                

                                text_4a.draw()

 ######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################                               #text_7.text = "aas"

                            if polygon_5.opacity == 0.2:


                                text_5a.draw()
######################### since we changed the opacity already, based on that condition, we can display the rank text for that lottery #########################
                                

                            if polygon_6.opacity == 0.2:

                                
                                text_6.draw()
######################### This is a reset button, if the mouse is pressed in polygon 8, the whole routine will break and the ranked can be done from the beginning #########################

                            if mouse_2.isPressedIn(polygon_8):

                                            continueRoutine = True

                                            break

 #########################################################new lines#########################################                               

                                

                            if mouse.isPressedIn(polygon) :# only update if started and not stopped!

                                    if pol_1 == 0:

                                       

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_2):# only update if started and not stopped!

                                    if pol_2 == 0: 

                                        

                                        continueRoutine = False

                            

                                if mouse.isPressedIn(polygon_3):# only update if started and not stopped!

                                    if pol_3 == 0 :

                                        

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_4) :# only update if started and not stopped!

                                    if pol_4 == 0 :

                                       

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_5) :# only update if started and not stopped!

                                    if pol_5 == 0 :

                                        

                                        continueRoutine = False


                            

                                if mouse.isPressedIn(polygon_6):# only update if started and not stopped!

                                    if  pol_6 == 0:

                                        

                                        continueRoutine = False

                            


                            if not continueRoutine:  # a component has requested a forced-end of Routine

                                break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in routine_12Components:

                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                    continueRoutine = True

                                    break  # at least one component has not yet finished
                        

                        # refresh the screen

                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()

                    

                    # -------Ending Routine "trial"-------

                    for thisComponent in routine_12Components:

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                    # store data for thisExp (ExperimentHandler)

                    x, y = mouse_2.getPos()

                    buttons = mouse_2.getPressed()

                    #######################################new line####################################

                    if mouse_2.isPressedIn(polygon_8):

                        #continueRoutine = False

                            break


 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################
                    if not polygon.opacity == 0.2: 

                    

                        if polygon.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon.opacity = 0.2

                            text_1.text = "2."

                            #text_44.draw

                            f.write("1" + '\t')

                            pol_1 = pol_1+1

                            button_2= 1

                            count = count + 1 
                            
######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################
                    if not polygon_2.opacity == 0.2:        

                        if polygon_2.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon_2.opacity = 0.2

                            button_2= 2

                            text_2a.text = "2."

                            f.write("2" + '\t')

                            pol_2 = pol_2+1

                            count = count + 1 #########################################################new lines#########################################

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################                       

                    if not polygon_3.opacity == 0.2:

                        if polygon_3.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon_3.opacity = 0.2

                            button_2= 3

                            text_3.text = "2."        

                            f.write("3" + '\t')

                            pol_3 = pol_3+1

                            count = count + 1 #########################################################new lines#########################################

                            
######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################
                                                        

                    if not polygon_4.opacity == 0.2:

                        if polygon_4.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon_4.opacity = 0.2

                            button_2= 4

                            text_4a.text = "2."        

                            f.write("4" + '\t')

                            pol_4 = pol_4+1

                            count = count + 1 #########################################################new lines#########################################

######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################
                    if not polygon_5.opacity == 0.2:

                        if polygon_5.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon_5.opacity = 0.2

                            button_2= 5

                            text_5a.text = "2."        

                            f.write("5" + '\t')

                            pol_5 = pol_5+1

                            count = count + 1 #########################################################new lines#########################################

######################### IF the mouse is pressed in a polygon, the color (opacity) changes and give the text "2" for the rank################################

                    if not polygon_6.opacity == 0.2:

                        if polygon_6.contains(mouse_2) and mouse_2.getPressed():

                            #msg.text = 'inside'

                            polygon_6.opacity = 0.2

                            button_2= 6

                            text_6.text = "2."        

                            f.write("6" + '\t')

                            pol_6 =pol_6+1

                            count = count + 1 #########################################################new lines#########################################



                    thisExp8.addData('button_2', button_2)

                    routineTimer.reset()
        

        #################

        #################

        ####         ####

        ####    3    ####

        ####         ####

        #################

        #################


                    # ------Prepare to start Routine "routine_12"-------

                    t = 0

                    routine_3Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    key_resp_2 = event.BuilderKeyResponse()

                    # keep track of which components have finished

                    routine_2Components = [text_1,mouse_3, text_D, mouse_2, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]

                    for thisComponent in routine_2Components:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED

                    

                    # -------Start Routine "routine_12"-------

                        

                    while continueRoutine:

                           
                            # get current time

                            t = routine_3Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

                        # update/draw components on each frame

                        

                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()

                            

                            text_reset.draw()

                            text_weiter.draw()

                            polygon_7.draw()

                            polygon_8.draw()



                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()



                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

        

                            text21.draw()



                            if t >= 0.0 and mouse_3.status == NOT_STARTED:

                            # keep track of start time/frame for later

                                mouse_3.tStart = t

                                mouse_3.frameNStart = frameN  # exact frame index

                                mouse_3.status = STARTED

                                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

                            if mouse_3.status == STARTED:  # only update if started and not stopped!

                                #buttons = mouse_3.getPressed()

                                ###############################Check every polygon values and it helps to know that the ranking is not done and user does not skip any round#########################################

                                if mouse.isPressedIn(polygon_8):

                                            continueRoutine = True

                                            break

                                if mouse.isPressedIn(polygon) :# only update if started and not stopped!

                                    if pol_1 == 0:

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_2):# only update if started and not stopped!

                                    if pol_2 == 0: 

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_3):# only update if started and not stopped!

                                    if pol_3 == 0 :

                                        continueRoutine = False


# only update if started and not stopped!
                                if mouse.isPressedIn(polygon_4) :# only update if started and not stopped!

                                    if pol_4 == 0 :

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_5) :# only update if started and not stopped!

                                    if pol_5 == 0 :

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_6):# only update if started and not stopped!

                                    if  pol_6 == 0:



                            if not continueRoutine:  # a component has requested a forced-end of Routine

                                break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in routine_2Components:

                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                    continueRoutine = True

                                    break  # at least one component has not yet finished


                        # refresh the screen

                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()

                    

                    # -------Ending Routine "rank3"-------

                    for thisComponent in routine_2Components:

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                    # store data for thisExp (ExperimentHandler)

                    x, y = mouse_3.getPos()

                    buttons = mouse_3.getPressed()

                    

                    

                    if mouse_3.isPressedIn(polygon_8):

                        #continueRoutine = False

                            break

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################
                    if not polygon.opacity == 0.2: 

                    

                        if polygon.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon.opacity = 0.2

                            text_1.text = "3."

                            f.write("2" + '\t')

                            pol_1 = pol_1+1

                            button_3= 1

                            count = count + 1 

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################                            

                    if not polygon_2.opacity == 0.2:        

                        if polygon_2.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon_2.opacity = 0.2

                            button_3= 2

                            text_2a.text = "3."

                            f.write("1" + '\t')

                            pol_2 = pol_2+1

                            count = count + 1 

                        

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################
                    if not polygon_3.opacity == 0.2:

                        if polygon_3.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon_3.opacity = 0.2

                            button_3= 3

                            text_3.text = "3."

                            f.write("3" + '\t')

                            pol_3 = pol_3+1

                            count = count + 1 


######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################
                    if not polygon_4.opacity == 0.2:

                        if polygon_4.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon_4.opacity = 0.2

                            button_3= 4

                            text_4a.text = "3."

                            f.write("4" + '\t')

                            pol_4 = pol_4+1

                            count = count + 1
                            

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################                            

                    if not polygon_5.opacity == 0.2:

                        if polygon_5.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon_5.opacity = 0.2

                            button_3= 5

                            text_5a.text = "3."

                            f.write("5" + '\t')

                            pol_5 = pol_5+1

                            count = count + 1 


######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "3" for the rank################################
                    if not polygon_6.opacity == 0.2:

                        if polygon_6.contains(mouse_3) and mouse_3.getPressed():

                            #msg.text = 'inside'

                            polygon_6.opacity = 0.2

                            button_3= 6

                            text_6.text = "3."

                            f.write("6" + '\t')

                            pol_6 = pol_6+1

                            count = count + 1 


                    thisExp8.addData('button_3', button_3)

                    routineTimer.reset()

        

        #################

        #################

        #### rank     ####

        ####    4    ####

        ####         ####

        #################

        #################

                    # ------Prepare to start Routine "rank3"-------

                    t = 0

                    routine_4Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    # setup some python lists for storing info about the mouse_3

                    # keep track of which components have finished

                    rank3Components = [mouse_4, text_D, mouse_2, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]

                    

                    for thisComponent in rank3Components:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED


                        

                    while continueRoutine:

                    
           

                        # get current time

                            t = t = routine_4Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

                        # update/draw components on each frame

                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()

                            

                            text_reset.draw()

                            text_weiter.draw()

                            polygon_7.draw()

                            polygon_8.draw()

                            

                             

                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()
                            

                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

        

                            text21.draw()


                            if t >= 0.0 and mouse_4.status == NOT_STARTED:

                                    # keep track of start time/frame for later

                                    mouse_4.tStart = t

                                    mouse_4.frameNStart = frameN  # exact frame index

                                    mouse_4.status = STARTED

                                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

                            if mouse_4.status == STARTED:  # only update if started and not stopped!
      # only update if started and not stopped!

                                if mouse.isPressedIn(polygon_8):

                                            continueRoutine = True

                                            break

                                if mouse.isPressedIn(polygon) : # only update if started and not stopped!

                                    if pol_1 == 0:

                                        continueRoutine = False
                                

                                if mouse.isPressedIn(polygon_2):# only update if started and not stopped!

                                    if pol_2 == 0: 

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_3):# only update if started and not stopped!

                                    if pol_3 == 0 :

                                        continueRoutine = False


                                if mouse.isPressedIn(polygon_4) :# only update if started and not stopped!

                                    if pol_4 == 0 :

                                        continueRoutine = False

                                if mouse.isPressedIn(polygon_5) :# only update if started and not stopped!

                                    if pol_5 == 0 :

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_6):# only update if started and not stopped!

                                    if  pol_6 == 0:

                                        continueRoutine = False

                                 

                            if not continueRoutine:  # a component has requested a forced-end of Routine

                               break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in rank3Components:

                               if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                   continueRoutine = True

                                   break  # at least one component has not yet finished


                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()



                    # -------Ending Routine "trial"-------

                    for thisComponent in rank3Components :

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                    # store data for thisExp (ExperimentHandler)

                    x, y = mouse_4.getPos()

                    buttons = mouse_4.getPressed()


                    if mouse_4.isPressedIn(polygon_8):

                        #continueRoutine = False

                            break

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################


                    if not polygon.opacity == 0.2: 

                    

                        if polygon.contains(mouse_4) and mouse_4.getPressed():

                            #msg.text = 'inside'

                            polygon.opacity = 0.2

                            text_1.text = "4."

                            f.write("2" + '\t')

                            pol_1 = pol_1+1

                            button_4= 1

                            count = count + 1 
                            

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################
                           

                    if not polygon_2.opacity == 0.2:        

                        if polygon_2.contains(mouse_4) and mouse_4.getPressed():

                            #msg.text = 'inside'

                            polygon_2.opacity = 0.2

                            button_4= 2

                            text_2a.text = "4."

                            f.write("1" + '\t')

                            pol_2 = pol_2+1

                            count = count + 1 
######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################
                        

                    if not polygon_3.opacity == 0.2:

                        if polygon_3.contains(mouse_4) and mouse_4.getPressed():

                            #msg.text = 'inside'

                            polygon_3.opacity = 0.2

                            button_4= 3

                            text_3.text = "4."        

                            f.write("3" + '\t')

                            pol_3 = pol_3+1

                            count = count + 1 
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################
                           


                    if not polygon_4.opacity == 0.2:


                        if polygon_4.contains(mouse_4) and mouse_4.getPressed():


                            polygon_4.opacity = 0.2

                            button_4= 4

                            text_4a.text = "4."        

                            f.write("4" + '\t')

                            pol_4 = pol_4+1

                            count = count + 1 
######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################

                    if not polygon_5.opacity == 0.2:

                       
                        if polygon_5.contains(mouse_4) and mouse_4.getPressed():


                            polygon_5.opacity = 0.2

                            button_4= 5

                            text_5a.text = "4."        

                            f.write("5" + '\t')

                            pol_5 = pol_5+1

                            count = count + 1 

######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "4" for the rank################################

                    if not polygon_6.opacity == 0.2:

                        if polygon_6.contains(mouse_4) and mouse_4.getPressed():

                            polygon_6.opacity = 0.2

                            button_4= 6

                            text_6.text = "4."        

                            f.write("6" + '\t')

                            pol_6 = pol_6+1

                            count = count + 1 #########################################################new lines#########################################



                    thisExp8.addData('button_4', button_4) 

                    routineTimer.reset()



        #################

        #################

        #### rank    ####

        ####    5    ####

        ####         ####

        #################

        #################

                    # ------Prepare to start Routine "routine_12"-------

                    t = 0

                    routine_5Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    key_resp_2 = event.BuilderKeyResponse()

                    # keep track of which components have finished

                    clock4Components = [text_1,mouse_5, text_D, mouse_2, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]


                    for thisComponent in clock4Components:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED



                    while continueRoutine:



                            t = routine_5Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)


                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()

                            

                            text_weiter.draw()

                            text_reset.draw()

                            polygon_7.draw()

                            polygon_8.draw()



                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()



                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

        

                            text21.draw()


                            if t >= 0.0 and mouse_5.status == NOT_STARTED:         

                                # keep track of start time/frame for later

                                mouse_5.tStart = t

                                mouse_5.frameNStart = frameN  # exact frame index

                                mouse_5.status = STARTED

                                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

                                         

                            if mouse_5.status == STARTED:  # only update if started and not stopped!


                                if mouse.isPressedIn(polygon_8):

                                            continueRoutine = True

                                            break

                                if mouse.isPressedIn(polygon) :# only update if started and not stopped!

                                    if pol_1 == 0:

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_2):# only update if started and not stopped!

                                    if pol_2 == 0: 

                                        continueRoutine = False


                                if mouse.isPressedIn(polygon_3):# only update if started and not stopped!

                                    if pol_3 == 0 :

                                        continueRoutine = False



                                if mouse.isPressedIn(polygon_4) :# only update if started and not stopped!

                                    if pol_4 == 0 :

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_5) :# only update if started and not stopped!

                                    if pol_5 == 0 :

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_6):# only update if started and not stopped!

                                    if  pol_6 == 0:

                                        continueRoutine = False



                            if not continueRoutine:  # a component has requested a forced-end of Routine

                                break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in clock4Components:

                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                    continueRoutine = True

                                    break  # at least one component has not yet finished



                        # refresh the screen

                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()

                    # -------Ending Routine "trial"-------

                    for thisComponent in clock4Components:

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                            # store data for thisExp (ExperimentHandler)

                    x, y = mouse_5.getPos()

                    buttons = mouse_5.getPressed()

                    

                    if mouse_5.isPressedIn(polygon_8):

                        #continueRoutine = True

                               break
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################

                    if not polygon.opacity == 0.2: 

                    
                        if polygon.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon.opacity = 0.2

                            text_1.text = "5."

                            f.write("2" + '\t')

                            pol_1 = pol_1+1

                            button_5= 1

                            count = count + 1 
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################                            

                    if not polygon_2.opacity == 0.2:        

                        if polygon_2.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon_2.opacity = 0.2

                            button_5= 2

                            text_2a.text = "5."

                            f.write("1" + '\t')

                            pol_2 = pol_2+1

                            count = count + 1 
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################                        

                    if not polygon_3.opacity == 0.2:

                        if polygon_3.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon_3.opacity = 0.2

                            button_5= 3

                            text_3.text = "5."        

                            f.write("3" + '\t')

                            pol_3 = pol_3+1

                            count = count + 1 
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################

                    if not polygon_4.opacity == 0.2:

                        if polygon_4.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon_4.opacity = 0.2

                            button_5= 4

                            text_4a.text = "5."        

                            f.write("4" + '\t')

                            pol_4 = pol_4+1

                            count = count + 1 

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################
                    if not polygon_5.opacity == 0.2:

                        if polygon_5.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon_5.opacity = 0.2

                            button_5= 5

                            text_5a.text = "5."        

                            f.write("5" + '\t')

                            pol_5 = pol_5+1

                            count = count + 1 

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "5" for the rank################################

                    if not polygon_6.opacity == 0.2:

                        if polygon_6.contains(mouse_5) and mouse_5.getPressed():

                            #msg.text = 'inside'

                            polygon_6.opacity = 0.2

                            button_5= 6

                            text_6.text = "5."        

                            f.write("6" + '\t')

                            pol_6 = pol_6+1

                            count = count + 1 

                    thisExp8.addData('button_5', button_5) 

                    routineTimer.reset()

        

        

        #################

        #################

        #### rank    ####

        ####    6    ####

        ####         ####

        #################

        #################

                    # ------Prepare to start Routine "routine_12"-------

                    t = 0

                    routine_6Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    # keep track of which components have finished

                    clock5Components = [text_1,mouse_6, text_D, mouse_2, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]

                    

                    for thisComponent in clock5Components:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED

                    

                    # -------Start Routine "routine_12"-------

                        

                    while continueRoutine:

                          

                            # get current time

                            t = routine_6Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

                        # update/draw components on each frame

                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()

                            

                            text_weiter.draw()

                            text_reset.draw()

                            polygon_7.draw()

                            polygon_8.draw()

                             

                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()


                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

        

                            text21.draw()

        

                            if t >= 0.0 and mouse_6.status == NOT_STARTED:

                                    # keep track of start time/frame for later

                                mouse_6.tStart = t

                                mouse_6.frameNStart = frameN  # exact frame index

                                mouse_6.status = STARTED

                                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

                            if mouse_6.status == STARTED:# only update if started and not stopped!


                                if mouse.isPressedIn(polygon_8):

                                            continueRoutine = True

                                            break



                                if mouse.isPressedIn(polygon) :# only update if started and not stopped!

                                    if pol_1 == 0:

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_2):# only update if started and not stopped!

                                    if pol_2 == 0: 

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_3):# only update if started and not stopped!

                                    if pol_3 == 0 :

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_4) :# only update if started and not stopped!
# only update if started and not stopped!
                                    if pol_4 == 0 :

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_5) :# only update if started and not stopped!

                                    if pol_5 == 0 :

                                        continueRoutine = False

                            

                            

                                if mouse.isPressedIn(polygon_6):# only update if started and not stopped!

                                    if  pol_6 == 0:

                                        continueRoutine = False

                    

                            if not continueRoutine:  # a component has requested a forced-end of Routine

                                break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in clock5Components:

                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                    continueRoutine = True

                                    break  # at least one component has not yet finished


                        # refresh the screen

                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()

      

                    # -------Ending Routine "trial"-------

                    for thisComponent in clock5Components:

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                    # store data for thisExp (ExperimentHandler)

                    x, y = mouse_6.getPos()

                    buttons = mouse_6.getPressed()



                    if mouse_6.isPressedIn(polygon_8):

                        #continueRoutine = False

                            break
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################


                    if not polygon.opacity == 0.2: 

                    

                        if polygon.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon.opacity = 0.2

                            text_1.text = "6."

                            f.write("2" + '\t')

                            pol_1 = pol_1+1

                            button_6= 1

                            count = count + 1 
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################
                            

                    if not polygon_2.opacity == 0.2:        

                        if polygon_2.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon_2.opacity = 0.2

                            button_6= 2

                            text_2a.text = "6."

                            f.write("1" + '\t')

                            pol_2 = pol_2+1

                            count = count + 1 
                        
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################

                    if not polygon_3.opacity == 0.2:

                        if polygon_3.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon_3.opacity = 0.2

                            button_6= 3

                            text_3.text = "6."        

                            f.write("3" + '\t')

                            pol_3 = pol_3+1

                            count = count + 1 

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################


                    if not polygon_4.opacity == 0.2:

                        if polygon_4.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon_4.opacity = 0.2

                            button_6= 4

                            text_4a.text = "6."        

                            f.write("4" + '\t')

                            pol_4 = pol_4+1

                            count = count + 1 

 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################

                    if not polygon_5.opacity == 0.2:

                        if polygon_5.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon_5.opacity = 0.2

                            button_6= 5

                            text_5a.text = "6."        

                            f.write("5" + '\t')

                            pol_5 = pol_5+1

                            count = count + 1
 ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################


                    if not polygon_6.opacity == 0.2:

                        if polygon_6.contains(mouse_6) and mouse_6.getPressed():

                            #msg.text = 'inside'

                            polygon_6.opacity = 0.2

                            button_6= 6

                            text_6.text = "6."        

                            f.write("6" + '\t')

                            pol_6 = pol_6+1

                            count = count + 1 

  ######################### IF the mouse is pressed in a polygon, the color (opacity) changes (only if the polygon color is different and it was not pressed )
#and give the text "6" for the rank################################
                   


                    routineTimer.reset()

                    thisExp8.addData('button_6', button_6) 

                    

        

        #################

        #################

        ####  button ####

        ####  next   ####

        ####  button ####

        #################

        #################

        # ------Prepare to start Routine "routine_12"-------

                    t = 0 

                    routine_7Clock.reset()  # clock

                    frameN = -1

                    continueRoutine = True

                    # update component parameters for each repeat

                    # keep track of which components have finished

                    routine_nextComponents = [text_1, mouse_7, text_D, sliceL1, sliceL2, sliceL3, sliceL4, sliceL5, sliceL6,

                    probability_L1, probability_L2 ,probability_L3 ,probability_L4 ,probability_L5, probability_L6,

                    outcome_L1, outcome_L2, outcome_L3, outcome_L4, outcome_L5, outcome_L6, round_text_22]

                    for thisComponent in routine_nextComponents:

                        if hasattr(thisComponent, 'status'):

                            thisComponent.status = NOT_STARTED

                    

                    # -------Start Routine "routine_12"-------

                        

                    while continueRoutine:                            

                            # get current time

                            t = routine_7Clock.getTime()

                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

                        # update/draw components on each frame

                        

                            polygon.draw()

                            polygon_2.draw()

                            polygon_3.draw()

                            polygon_4.draw()

                            polygon_5.draw()

                            polygon_6.draw()

                            polygon_7.draw()

                            

                            text_1.draw()

                            text_2a.draw()

                            text_3.draw()

                            text_4a.draw()

                            text_5a.draw()

                            text_6.draw()

                            

                            text_weiter.draw()

                            text_reset.draw()

                            polygon_7.draw()

                            polygon_8.draw()

                            

                             

                            percentage_L1.draw()

                            percentage_L2.draw()

                            percentage_L3.draw()

                            percentage_L4.draw()

                            percentage_L5.draw()

                            percentage_L6.draw()

                            

                            euro_L1.draw()

                            euro_L2.draw()

                            euro_L3.draw()

                            euro_L4.draw()

                            euro_L5.draw()

                            euro_L6.draw()

                                                
                            

                            circleL1.draw()

                            circleL2.draw()

                            circleL3.draw()

                            circleL4.draw()

                            circleL5.draw()

                            circleL6.draw()

                            

                            round_text_22.draw()

        

                            text21.draw()

        
                            if t >= 0.0 and mouse_7.status == NOT_STARTED:

                                    # keep track of start time/frame for later

                                mouse_7.tStart = t

                                mouse_7.frameNStart = frameN  # exact frame index

                                mouse_7.status = STARTED

                                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'

                            if mouse_7.status == STARTED:  # only update if started and not stopped!

                                 #########################################################new lines#########################################        

                                if mouse_7.isPressedIn(polygon_8):

                                    break



                                if mouse.isPressedIn(polygon_7) :

                                    if (pol_1 == 1 and pol_2 == 1 and pol_3 == 1 and pol_4 == 1 and pol_5 == 1 and pol_6 == 1):

                                        

                                            continueRoutine = True

                                            thisExp8.nextEntry()

                                            break


#                                   continueRoutine = False

                            if not continueRoutine:  # a component has requested a forced-end of Routine

                                break

                            continueRoutine = False  # will revert to True if at least one component still running

                            for thisComponent in routine_nextComponents:

                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                                    continueRoutine = True

                                    break  # at least one component has not yet finished



                        # refresh the screen

                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

                                mywin.flip()

                            

        

            # -------Ending Routine "trial"-------

                    for thisComponent in routine_nextComponents:

                        if hasattr(thisComponent, "setAutoDraw"):

                            thisComponent.setAutoDraw(False)

                    # store data for thisExp (ExperimentHandler)

                    x, y = mouse_7.getPos()

                    buttons = mouse_7.getPressed()

                    

                    if mouse_7.isPressedIn(polygon_8):

                        break

                



                #########################################################new lines#########################################

                #break    

                    if (polygon.opacity == 0.2 and polygon_2.opacity == 0.2 and polygon_3.opacity == 0.2 and polygon_4.opacity == 0.2 and polygon_5.opacity == 0.2 and polygon_6.opacity == 0.2):

                        if mouse_7.isPressedIn(polygon_7):

                            break    

                #else:

                    #pass

                if (polygon.opacity == 0.2 and polygon_2.opacity == 0.2 and polygon_3.opacity == 0.2 and polygon_4.opacity == 0.2 and polygon_5.opacity == 0.2 and polygon_6.opacity == 0.2):

                    if mouse_7.isPressedIn(polygon_7):

                        break
        


