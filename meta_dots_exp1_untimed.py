
# imports
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray, random
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from pyglet.window import key # to detect key state, whether key is held down, to move slider on key hold
import pyglet

# Store info about the experiment session
expName = 'MetaDots'
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp


# Start Code - component code to be run before the window creation

# set up variable to track current state of key press, to move slider when keys held down

keyState = key.KeyStateHandler()

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )
win.winHandle.push_handlers(keyState)
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
  

# Set up variables for random_dots
DotStable = 50
DotDifference = 20
DotVarialble = DotStable - DotDifference

DotLeft = 1
DotRight = 1

DotLeftDict=[40, 50, 53, 35, 23]
DotRightDict=[60, 30, 58, 25, 8]
ExampleTrials = []
for x in range(5):
    ExampleTrials.append({'ExDotLeft':DotLeftDict[x], 'ExDotRight':DotRightDict[x]})

######################## COMPONENTS ##########################

#Instalize components for Routine Introduction
IntroductionClock =core.Clock()

IntroductionText =visual.TextStim(win,text='Welcome to this experiment. \n\n\nPress space to find out what the task involves!',
    units='cm', pos=(0,2.0),  height=1, wrapWidth=30)

#Instalize components for Routine "Instructions 1"
Instructions1Clock =core.Clock()

Instructions1Text =visual.TextStim(win, text='You will see two circles on the screen, each with a number of dots inside. Your task is to try to guess which circle contains the most points. Then we will ask you to rate your confidence in your decision. \n\n\nPlease press the space to see some example stimuli.',
    units='cm', pos=(0,2.0), height=1, wrapWidth=30)
    
# Initialize components for Main Experiment
ExampleClock =core.Clock()

CircleLeft = visual.Circle(win, radius=6.0, edges=64,
    lineColor=(1.0, 1.0, 1.0), fillColorSpace=u'rgb', fillColor=u'black', lineWidth=15,
    pos=(-11.0, 4.0), interpolate=True, units='cm')

CircleRight = visual.Circle(win, radius=6.0, edges=64,
    lineColor=(1.0, 1.0, 1.0), fillColorSpace=u'rgb', fillColor=u'black', lineWidth=15,
    pos=(11.0, 4.0), interpolate=True, units='cm')

DotPatchLeft =visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotLeft, fieldShape='circle', fieldPos=(-11.0, 4.0),fieldSize=11.0,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)

DotPatchLeft =visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotLeft, fieldShape='circle', fieldPos=(11.0, 4.0),fieldSize=11.0,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)

DotExampleLeft =visual.TextStim(win,text=sin, units='cm',
    pos=(-11.0,-3.0), height=1, wrapWidth=10)
    
DotExampleRight =visual.TextStim(win,text=sin, units='cm',
    pos=(11.0,-3.0), height=1, wrapWidth=10)

DotExampleInstructions =visual.TextStim(win,text="Please press space to continue",
    units='cm', pos=(0,-8.0), height=1, wrapWidth=15)
    
DotCalibrationInstructions = visual.TextStim(win,text="Which circle contains the most dots?",
    units='cm', pos=(0,-8.0), height=1, wrapWidth=20)
    
#Instalize components for Routine Instructions2
Instructions2Clock =core.Clock()

Instructions2Text =visual.TextStim(win,text=u"The first part of the task is to choose which circle contains the most points. We will next familiarise you with this part of the task. Press the left arrow key \u2190 to pick the left circle and the right arrow key \u2192 to pick the right circle. After each trial you will get feedback and there will be a star under the circle that you choose. Don't worry if some of your decisions feel like guesses - it is a hard task! \n\n\nPress the space bar to continue.",
    units='cm', pos=(0,2.0),  height=1, wrapWidth=30)

# Instalize components for Feedback trials
FeedbackCorrect = visual.TextStim(win,text="Correct!",
    units='cm', pos=(0,-8.0), height=1, color='#7FFF00', wrapWidth=15)

FeedbackIncorrect = visual.TextStim(win,text="Incorrect",
    units='cm', pos=(0,-8.0), height=1, color='#FF0000', wrapWidth=15)

FeedbackClock = core.Clock()

FeedbackStarLeft = visual.TextStim(win=win, ori=0, name='FeedbackStarLeft',
text=u'*', units='cm', pos=(-11.0,-4.5), height=3, wrapWidth=10)
    
FeedbackStarRight = visual.TextStim(win=win, ori=0, name='FeedbackStarRight',
text=u'*', units='cm', pos=(11.0,-4.5), height=3, wrapWidth=10)

#Instalize components for Routine Instructions3
Instructions3Clock =core.Clock()

Instructions3Text =visual.TextStim(win,text=u"The basic training is now complete. For the rest of the trials you won't get any feedback. Additionally, after each of the remaining trials you will be asked to rate your confidence in your choice using a sliding scale. You can move the cursor around on the scale using the left \u2190 and right \u2192 arrow keys. Press the down arrow key \u2193 to confirm your decision. The left end of the scale means that you are less confident than normal, and the right end of the scale means that you are more confident than normal. \n\nHowever, please remember that this is a difficult task - it's rare that you will be very confident! As we are interested in relative changes in confidence, we encourage you to use the whole scale. \n\nYou will now have some trials to practice using the confidence scale.\n\n\nPlease press the space bar to continue.",
    units='cm', pos=(0,2.0),  height=1, wrapWidth=30)

# Initialize components for Routine "Confidence"
ConfClock = core.Clock()
InstrConf = visual.TextStim(win=win, ori=0, name='instr_conf', text=u'How confident are you in your choice?', font=u'Arial', pos=[0, 0.6], height=0.1, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)
InstrConfKeys = visual.TextStim(win=win, ori=0, name='instr_conf_keys', text=u'Use the left \u2190 and right \u2192 arrow keys to move the triangle. \n\nWhen the triangle is in the correct place, press the down \u2193 arrow key to move on.', font=u'Arial', pos=[0, 0.15], height=0.07, wrapWidth=0.7, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)
Confidence = visual.RatingScale(win=win, name='Confidence', marker=u'triangle', markerColor=u'orange', leftKeys=None, rightKeys=None, size=1.0, pos=[0.0, -0.3], low=0, high=1, precision=100, labels=[u'Less', u'More'], scale=u'', markerStart=u'0.5', tickHeight=u'0', showAccept=False, acceptKeys=[u'down', u'return'])

#Instalize components for Routine Instructions4
Instructions4Clock =core.Clock()

Instructions4Text =visual.TextStim(win,text=u"The training is now complete and you will soon begin the main task, consisting of 200 trials that will work exactly the same as the last practice trials. You will get a chance to rest every 25 trials, please use these breaks as it is a challenging task. \n\n If you have any questions please ask the experimenter now.\n\n\nOtherwise, press the space bar to continue.",
    units='cm', pos=(0,2.0),  height=1, wrapWidth=30)
    
# Instalize components for "Rest"
RestClock = core.Clock()
RestText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'Great! Now have a rest and press spacebar when you are ready to begin the next block.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

# Instalize components for "Thank You"
ThankYouClock = core.Clock()
ThankYouText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'You have now completed this experiment. Thank you for your participation. Please inform the experimenter that you have finished.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

####################### Introduction to experiment ###########################

#------Prepare to start Routine "Introduction"-------
t = 0
IntroductionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
IntroductionResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
IntroductionResponse.status = NOT_STARTED
# keep track of which components have finished
IntroductionComponents = []
IntroductionComponents.append(IntroductionText)
IntroductionComponents.append(IntroductionResponse)
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Introduction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroductionText* updates
    if t >= 0.0 and IntroductionText.status == NOT_STARTED:
        # keep track of start time/frame for later
        IntroductionText.tStart = t  # underestimates by a little under one frame
        IntroductionText.frameNStart = frameN  # exact frame index
        IntroductionText.setAutoDraw(True)
    
    # *IntroductionResponse* updates
    if t >= 0 and IntroductionResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        IntroductionResponse.tStart = t  # underestimates by a little under one frame
        IntroductionResponse.frameNStart = frameN  # exact frame index
        IntroductionResponse.status = STARTED
        # keyboard checking is just starting
        IntroductionResponse.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if IntroductionResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            IntroductionResponse.keys = theseKeys[-1]  # just the last key pressed
            IntroductionResponse.rt = IntroductionResponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IntroductionResponse.keys in ['', [], None]:  # No response was made
   IntroductionResponse.keys=None
# Move on to next section
thisExp.nextEntry()

#------Prepare to start Routine "Instructions1"-------
t = 0
Instructions1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instructions1Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions1Response.status = NOT_STARTED
# keep track of which components have finished
Instructions1Components = []
Instructions1Components.append(Instructions1Text)
Instructions1Components.append(Instructions1Response)
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions1Text* updates
    if t >= 0.0 and Instructions1Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions1Text.tStart = t  # underestimates by a little under one frame
        Instructions1Text.frameNStart = frameN  # exact frame index
        Instructions1Text.setAutoDraw(True)
    
    # *Instructions1Response* updates
    if t >= 0 and Instructions1Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions1Response.tStart = t  # underestimates by a little under one frame
        Instructions1Response.frameNStart = frameN  # exact frame index
        Instructions1Response.status = STARTED
        # keyboard checking is just starting
        Instructions1Response.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instructions1Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instructions1Response.keys = theseKeys[-1]  # just the last key pressed
            Instructions1Response.rt = Instructions1Response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions1"-------
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructions1Response.keys in ['', [], None]:  # No response was made
   Instructions1Response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instructions1Response.keys',Instructions1Response.keys)
if Instructions1Response.keys != None:  # we had a response
    thisExp.addData('Instructions1Response.rt', Instructions1Response.rt)
thisExp.nextEntry()

############################# EXAMPLE LOOP ###############################

# set up handler to look after randomisation of conditions etc
choice_loop = data.TrialHandler(nReps=1, method=u'sequential',     extraInfo=expInfo, originPath=None,
    trialList=ExampleTrials,
    seed=None, name='choice_loop')
thisExp.addLoop(choice_loop)
thischoice_loop = choice_loop.trialList[0]
if thischoice_loop != None:
    for paramName in thischoice_loop.keys():
        exec paramName + '= thischoice_loop.' + paramName

# Set up counter to keep track of binary loop cycle, so that the rest prompt is shown only after a certain number of trials

print choice_loop.trialList

for thischoice_loop in choice_loop:
    currentLoop = choice_loop
    if thischoice_loop != None:
        for paramName in thischoice_loop.keys():
            exec paramName + '= thischoice_loop.' + paramName
            

    #------Prepare to start Routine "choice"-------
    t = 0
    ExampleClock.reset()
    frameN = -1
     # update component parameters for each repeat
    DotPatchLeft=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=ExDotLeft, fieldShape='circle', fieldPos=(-11.0, 4.0), fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    DotPatchRight=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=ExDotRight, fieldShape='circle', fieldPos=(11, 4.0),fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)

    DotExampleLeft.setText(ExDotLeft)
    DotExampleRight.setText(ExDotRight)
    event.clearEvents(eventType='keyboard')
    key_resp_choice = event.BuilderKeyResponse()
    key_resp_choice.status = NOT_STARTED
     # keep track of which components have finished
    dot_choiceComponents = []
    dot_choiceComponents.append(CircleLeft)
    dot_choiceComponents.append(CircleRight)
    dot_choiceComponents.append(DotPatchLeft)
    dot_choiceComponents.append(DotPatchRight)
    dot_choiceComponents.append(DotExampleInstructions)
    dot_choiceComponents.append(DotExampleLeft)
    dot_choiceComponents.append(DotExampleRight)
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
 #-------Start Routine "dot_choice"-------
    continueRoutine = True
    while continueRoutine:
        t = ExampleClock.getTime()
        frameN = frameN + 1
        
        # *CircleLeft* updates
        if t >= 0.2 and CircleLeft.status == NOT_STARTED:
            CircleLeft.tStart = t
            CircleLeft.frameNStart = frameN
            CircleLeft.setAutoDraw(True)

            
        # *CircleRight* updates
        if t >= 0.2 and CircleRight.status == NOT_STARTED:
            CircleRight.tStart = t
            CircleRight.frameNStart = frameN
            CircleRight.setAutoDraw(True)

            
         # *DotPatchLeft* updates
        if t >= 0.2 and DotPatchLeft.status == NOT_STARTED:
            DotPatchLeft.tStart = t
            DotPatchLeft.frameNStart = frameN
            DotPatchLeft.setAutoDraw(True)

        
        # *DotPatchRight* updates
        if t >= 0.2 and DotPatchRight.status == NOT_STARTED:
            DotPatchRight.tStart = t
            DotPatchRight.frameNStart = frameN
            DotPatchRight.setAutoDraw(True)

        
        # *DotExampleInstructions* updates
        if t >= 0.2 and DotExampleInstructions.status == NOT_STARTED:
            DotExampleInstructions.tStart = t
            DotExampleInstructions.frameNStart = frameN
            DotExampleInstructions.setAutoDraw(True)
            
                # *DotExampleLeft* updates
        if t >= 0.2 and DotExampleLeft.status == NOT_STARTED:
            DotExampleLeft.tStart = t
            DotExampleLeft.frameNStart = frameN
            DotExampleLeft.setAutoDraw(True)
            
                # *DotExampleRight* updates
        if t >= 0.2 and DotExampleRight.status == NOT_STARTED:
            DotExampleRight.tStart = t
            DotExampleRight.frameNStart = frameN
            DotExampleRight.setAutoDraw(True)

            
        # *key_resp_choice* updates
        if t >= 0.2 and key_resp_choice.status == NOT_STARTED:
            key_resp_choice.tStart = t
            key_resp_choice.frameNStart = frameN
            key_resp_choice.status = STARTED
            key_resp_choice.clock.reset()
        if key_resp_choice.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if 'escape' in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                key_resp_choice.keys = theseKeys[-1]
                key_resp_choice.rt = key_resp_choice.clock.getTime()
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in dot_choiceComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
         # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
            
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
     #-------Ending Routine "choice"-------
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_choice.keys in ['', [], None]:
        key_resp_choice.keys = None
    
    # store data for binary (TrialHandler)
    choice_loop.addData('key_resp_choice.keys', key_resp_choice.keys)
    if key_resp_choice.keys != None:
        choice_loop.addData('key_resp_choice.rt', key_resp_choice.rt)
    choice_loop.addData('DotPatchRight.nDots', DotPatchRight.nDots)
    choice_loop.addData('DotPatchLeft.nDots', DotPatchLeft.nDots)
    thisExp.nextEntry()
    
########################################### Examples Finished ###################################################

#------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instructions2Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions2Response.status = NOT_STARTED
# keep track of which components have finished
Instructions2Components = []
Instructions2Components.append(Instructions2Text)
Instructions2Components.append(Instructions2Response)
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions2Text* updates
    if t >= 0.0 and Instructions2Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions2Text.tStart = t  # underestimates by a little under one frame
        Instructions2Text.frameNStart = frameN  # exact frame index
        Instructions2Text.setAutoDraw(True)
    
    # *Instructions2Response* updates
    if t >= 0 and Instructions2Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions2Response.tStart = t  # underestimates by a little under one frame
        Instructions2Response.frameNStart = frameN  # exact frame index
        Instructions2Response.status = STARTED
        # keyboard checking is just starting
        Instructions2Response.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instructions2Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instructions2Response.keys = theseKeys[-1]  # just the last key pressed
            Instructions2Response.rt = Instructions2Response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructions2Response.keys in ['', [], None]:  # No response was made
   Instructions2Response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instructions2Response.keys',Instructions2Response.keys)
if Instructions2Response.keys != None:  # we had a response
    thisExp.addData('Instructions2Response.rt', Instructions2Response.rt)
thisExp.nextEntry()

############################# Calibration Phase ############################

#create the staircase handler
CalStaircase = data.StairHandler(startVal = 20.0,
                          stepType = 'lin', stepSizes=[4,4,3,3,2,2,1,1],
                          nUp=1, nDown=2, minVal=1, maxVal=99)  #will home in on the 70% threshold
                          
for ThisIncrement in CalStaircase:
    
    # Set dot difference for this trial
    DotDifference = ThisIncrement
    #randomise whether the stable dotarray is the smaller or the larger value
    DotDiffDenominator = np.random.choice([-1,1])
    if DotDiffDenominator == -1:
        DotVarialble = DotStable - DotDifference
    else:
        DotVarialble = DotStable + DotDifference
    #randomise the location of the fixed and variable stimuli
    StableSide= np.random.choice([-1,1])
    if StableSide == -1:
        DotLeft = DotStable
        DotRight = DotVarialble
    else:
        DotLeft =DotVarialble
        DotRight = DotStable
    # Determine the correct response for the trial
    if DotLeft > DotRight:
        CorrectKey = str('left')
    elif DotRight > DotLeft:
        CorrectKey = str('right')

    #------Prepare to start Routine "choice"-------
    t = 0
    ExampleClock.reset()
    frameN = -1
     # update component parameters for each repeat
    DotPatchLeft=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotLeft, fieldShape='circle', fieldPos=(-11.0, 4.0), fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    DotPatchRight=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotRight, fieldShape='circle', fieldPos=(11, 4.0),fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    # Update Keyboard parameters
    event.clearEvents(eventType='keyboard')
    KeyRespCal = event.BuilderKeyResponse()
    KeyRespCal.status = NOT_STARTED
     # keep track of which components have finished
    dot_choiceComponents = []
    dot_choiceComponents.append(CircleLeft)
    dot_choiceComponents.append(CircleRight)
    dot_choiceComponents.append(DotPatchLeft)
    dot_choiceComponents.append(DotPatchRight)
    dot_choiceComponents.append(DotCalibrationInstructions)
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
#-------Start Routine "dot_choice"-------
    continueRoutine = True
    while continueRoutine:
        t = ExampleClock.getTime()
        frameN = frameN + 1
        
        # *CircleLeft* updates
        if t >= 0.2 and CircleLeft.status == NOT_STARTED:
            CircleLeft.tStart = t
            CircleLeft.frameNStart = frameN
            CircleLeft.setAutoDraw(True)

            
        # *CircleRight* updates
        if t >= 0.2 and CircleRight.status == NOT_STARTED:
            CircleRight.tStart = t
            CircleRight.frameNStart = frameN
            CircleRight.setAutoDraw(True)

            
         # *DotPatchLeft* updates
        if t >= 0.2 and DotPatchLeft.status == NOT_STARTED:
            DotPatchLeft.tStart = t
            DotPatchLeft.frameNStart = frameN
            DotPatchLeft.setAutoDraw(True)

        
        # *DotPatchRight* updates
        if t >= 0.2 and DotPatchRight.status == NOT_STARTED:
            DotPatchRight.tStart = t
            DotPatchRight.frameNStart = frameN
            DotPatchRight.setAutoDraw(True)

        
        # *DotExampleInstructions* updates
        if t >= 0.2 and DotCalibrationInstructions.status == NOT_STARTED:
            DotCalibrationInstructions.tStart = t
            DotCalibrationInstructions.frameNStart = frameN
            DotCalibrationInstructions.setAutoDraw(True)
            
        # *key_resp_choice* updates
        if t >= 0.2 and KeyRespCal.status == NOT_STARTED:
            KeyRespCal.tStart = t
            KeyRespCal.frameNStart = frameN
            KeyRespCal.status = STARTED
            KeyRespCal.clock.reset()
        if KeyRespCal.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if 'escape' in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                KeyRespCal.keys = theseKeys[-1]
                KeyRespCal.rt = KeyRespCal.clock.getTime()
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in dot_choiceComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
         # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
            
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
     #-------Ending Routine "choice"-------
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyRespCal.keys in ['', [], None]:
        KeyRespCal.keys = None
        # was no response the correct answer?!
    if KeyRespCal.keys == CorrectKey: KeyRespCal.corr = 1  # correct non-response
    else: KeyRespCal.corr = 0  # failed to respond (incorrectly)
    
    # Tell the staircase if the participant is correct (TrialHandler)
    CalStaircase.addResponse(KeyRespCal.corr)
    
    # Store data for experiment:
    thisExp.addData('Correct', KeyRespCal.corr)
    thisExp.addData('CorrectKey', CorrectKey)
    thisExp.addData('Response', KeyRespCal.keys)
    if KeyRespCal.keys != None:
        thisExp.addData('RT', KeyRespCal.rt)
    thisExp.addData('DotDifference', DotDifference)
    thisExp.addData('DotNumberRight', DotPatchRight.nDots)
    thisExp.addData('DotNumberLeft', DotPatchLeft.nDots)



#------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()
    frameN = -1
    # Create Key Response Object
    FeedbackKeyResp = event.BuilderKeyResponse()
    FeedbackKeyResp.status = NOT_STARTED

     # keep track of which components have finished
    FeedbackComponents = []
    FeedbackComponents.append(CircleLeft)
    FeedbackComponents.append(CircleRight)
    FeedbackComponents.append(DotPatchLeft)
    FeedbackComponents.append(DotPatchRight)
    FeedbackComponents.append(FeedbackCorrect)
    FeedbackComponents.append(FeedbackIncorrect)
    FeedbackComponents.append(FeedbackStarLeft)
    FeedbackComponents.append(FeedbackStarRight)
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
#-------Start Routine "Feedback"-------
    continueRoutine = True
    while continueRoutine:
        t = FeedbackClock.getTime()
        frameN = frameN + 1
        
        # *CircleLeft* updates
        if t >= 0.2 and CircleLeft.status == NOT_STARTED:
            CircleLeft.tStart = t
            CircleLeft.frameNStart = frameN
            CircleLeft.setAutoDraw(True)
        elif CircleLeft.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            CircleLeft.setAutoDraw(False)
            continueRoutine = False

            
        # *CircleRight* updates
        if t >= 0.2 and CircleRight.status == NOT_STARTED:
            CircleRight.tStart = t
            CircleRight.frameNStart = frameN
            CircleRight.setAutoDraw(True)
        elif CircleRight.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            CircleRight.setAutoDraw(False)
            
         # *DotPatchLeft* updates
        if t >= 0.2 and DotPatchLeft.status == NOT_STARTED:
            DotPatchLeft.tStart = t
            DotPatchLeft.frameNStart = frameN
            DotPatchLeft.setAutoDraw(True)
        elif DotPatchLeft.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            DotPatchLeft.setAutoDraw(False)
        
        # *DotPatchRight* updates
        if t >= 0.2 and DotPatchRight.status == NOT_STARTED:
            DotPatchRight.tStart = t
            DotPatchRight.frameNStart = frameN
            DotPatchRight.setAutoDraw(True)
        elif DotPatchRight.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            DotPatchRight.setAutoDraw(False)
        
        # *FeedbackCorrect* updates
        if KeyRespCal.corr == 1:
            if t >= 0.2 and FeedbackCorrect.status == NOT_STARTED:
                FeedbackCorrect.tStart = t
                FeedbackCorrect.frameNStart = frameN
                FeedbackCorrect.setAutoDraw(True)
            elif FeedbackCorrect.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                FeedbackCorrect.setAutoDraw(False)
        
        # *FeedbackIncorrect* updates
        if KeyRespCal.corr == 0:
            if t >= 0.2 and FeedbackIncorrect.status == NOT_STARTED:
                   FeedbackIncorrect.tStart = t
                   FeedbackIncorrect.frameNStart = frameN
                   FeedbackIncorrect.setAutoDraw(True)
            elif FeedbackIncorrect.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                FeedbackIncorrect.setAutoDraw(False)

        # *FeedbackStarLeft* updates
        if KeyRespCal.keys == 'left':
            if t >= 0.2 and FeedbackStarLeft.status == NOT_STARTED:
                FeedbackStarLeft.tStart = t
                FeedbackStarLeft.frameNStart = frameN
                FeedbackStarLeft.setAutoDraw(True)
            elif FeedbackStarLeft.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                FeedbackStarLeft.setAutoDraw(False)
            
        # *FeedbackStarRight* updates
        if KeyRespCal.keys == 'right':
            if t >= 0.2 and FeedbackStarRight.status == NOT_STARTED:
                FeedbackStarRight.tStart = t
                FeedbackStarRight.frameNStart = frameN
                FeedbackStarRight.setAutoDraw(True)
            elif FeedbackStarRight.status == STARTED and t >= (0.2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                FeedbackStarRight.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
         # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
            
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
     #-------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
        
######################### End of Calibration Phase ######################### 
#------Prepare to start Routine "Instructions3"-------
t = 0
Instructions3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instructions3Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions3Response.status = NOT_STARTED
# keep track of which components have finished
Instructions3Components = []
Instructions3Components.append(Instructions3Text)
Instructions3Components.append(Instructions3Response)
for thisComponent in Instructions3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions2Text* updates
    if t >= 0.0 and Instructions3Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions3Text.tStart = t  # underestimates by a little under one frame
        Instructions3Text.frameNStart = frameN  # exact frame index
        Instructions3Text.setAutoDraw(True)
    
    # *Instructions2Response* updates
    if t >= 0 and Instructions3Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions3Response.tStart = t  # underestimates by a little under one frame
        Instructions3Response.frameNStart = frameN  # exact frame index
        Instructions3Response.status = STARTED
        # keyboard checking is just starting
        Instructions3Response.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instructions3Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instructions3Response.keys = theseKeys[-1]  # just the last key pressed
            Instructions3Response.rt = Instructions3Response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions3"-------
for thisComponent in Instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructions3Response.keys in ['', [], None]:  # No response was made
   Instructions3Response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instructions3Response.keys',Instructions3Response.keys)
if Instructions3Response.keys != None:  # we had a response
    thisExp.addData('Instructions3Response.rt', Instructions3Response.rt)
thisExp.nextEntry()
########################## Confidence Example Staircase ##################################

#create the staircase handler
ConfidenceStaircase = data.StairHandler(startVal = DotDifference,
                          stepType = 'lin', stepSizes=1, nTrials=10,
                          nUp=1, nDown=2, minVal=1, maxVal=99)  #will home in on the 80% threshold
                          

for ThisIncrement in ConfidenceStaircase:
    # Set dot difference for this trial
    DotDifference = ThisIncrement
    #randomise whether the stable dotarray is the smaller or the larger value
    DotDiffDenominator = np.random.choice([-1,1])
    if DotDiffDenominator == -1:
        DotVarialble = DotStable - DotDifference
    else:
        DotVarialble = DotStable + DotDifference
    #randomise the location of the fixed and variable stimuli
    StableSide= np.random.choice([-1,1])
    if StableSide == -1:
        DotLeft = DotStable
        DotRight = DotVarialble
    else:
        DotLeft =DotVarialble
        DotRight = DotStable
    # Determine the correct response for the trial
    if DotLeft > DotRight:
        CorrectKey = str('left')
    elif DotRight > DotLeft:
        CorrectKey = str('right')

    #------Prepare to start Routine "choice"-------
    t = 0
    ExampleClock.reset()
    frameN = -1
     # update component parameters for each repeat
    DotPatchLeft=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotLeft, fieldShape='circle', fieldPos=(-11.0, 4.0), fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    DotPatchRight=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotRight, fieldShape='circle', fieldPos=(11, 4.0),fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    # Update Keyboard parameters
    event.clearEvents(eventType='keyboard')
    KeyRespCal = event.BuilderKeyResponse()
    KeyRespCal.status = NOT_STARTED
     # keep track of which components have finished
    dot_choiceComponents = []
    dot_choiceComponents.append(CircleLeft)
    dot_choiceComponents.append(CircleRight)
    dot_choiceComponents.append(DotPatchLeft)
    dot_choiceComponents.append(DotPatchRight)
    dot_choiceComponents.append(DotCalibrationInstructions)
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
#-------Start Routine "dot_choice"-------
    continueRoutine = True
    while continueRoutine:
        t = ExampleClock.getTime()
        frameN = frameN + 1
        
        # *CircleLeft* updates
        if t >= 0.2 and CircleLeft.status == NOT_STARTED:
            CircleLeft.tStart = t
            CircleLeft.frameNStart = frameN
            CircleLeft.setAutoDraw(True)

            
        # *CircleRight* updates
        if t >= 0.2 and CircleRight.status == NOT_STARTED:
            CircleRight.tStart = t
            CircleRight.frameNStart = frameN
            CircleRight.setAutoDraw(True)

            
         # *DotPatchLeft* updates
        if t >= 0.2 and DotPatchLeft.status == NOT_STARTED:
            DotPatchLeft.tStart = t
            DotPatchLeft.frameNStart = frameN
            DotPatchLeft.setAutoDraw(True)

        
        # *DotPatchRight* updates
        if t >= 0.2 and DotPatchRight.status == NOT_STARTED:
            DotPatchRight.tStart = t
            DotPatchRight.frameNStart = frameN
            DotPatchRight.setAutoDraw(True)

        
        # *DotExampleInstructions* updates
        if t >= 0.2 and DotCalibrationInstructions.status == NOT_STARTED:
            DotCalibrationInstructions.tStart = t
            DotCalibrationInstructions.frameNStart = frameN
            DotCalibrationInstructions.setAutoDraw(True)
            
        # *key_resp_choice* updates
        if t >= 0.2 and KeyRespCal.status == NOT_STARTED:
            KeyRespCal.tStart = t
            KeyRespCal.frameNStart = frameN
            KeyRespCal.status = STARTED
            KeyRespCal.clock.reset()
        if KeyRespCal.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if 'escape' in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                KeyRespCal.keys = theseKeys[-1]
                KeyRespCal.rt = key_resp_choice.clock.getTime()
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in dot_choiceComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
         # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
            
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
     #-------Ending Routine "choice"-------
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyRespCal.keys in ['', [], None]:
        KeyRespCal.keys = None
        # was no response the correct answer?!
    if KeyRespCal.keys == CorrectKey: KeyRespCal.corr = 1  # correct non-response
    else: KeyRespCal.corr = 0  # failed to respond (incorrectly)
    
    # Tell the staircase if the participant is correct (TrialHandler)
    ConfidenceStaircase.addResponse(KeyRespCal.corr)
    
    # Store data for experiment:
    thisExp.addData('Correct', KeyRespCal.corr)
    thisExp.addData('CorrectKey', CorrectKey)
    thisExp.addData('Response', KeyRespCal.keys)
    if KeyRespCal.keys != None:
        thisExp.addData('RT', KeyRespCal.rt)
    thisExp.addData('DotDifference', DotDifference)
    thisExp.addData('DotNumberRight', DotPatchRight.nDots)
    thisExp.addData('DotNumberLeft', DotPatchLeft.nDots)
    
    #------Prepare to start Routine "conf"-------
    t = 0
    ConfClock.reset()
    frameN = -1
    # update component parameters for each repeat
    Confidence.reset()
    # keep track of which components have finished
    ConfComponents = []
    ConfComponents.append(InstrConf)
    ConfComponents.append(InstrConfKeys)
    ConfComponents.append(Confidence)
    for thisComponent in ConfComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "conf"-------
# checking to see if participants responded to the choice question
# if not,it skips this iteration of the confidence routine
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ConfClock.getTime()
        frameN = frameN + 1

        # *confidence* updates
        if t > 0.2:
            Confidence.draw()
            continueRoutine = Confidence.noResponse
            if Confidence.noResponse == False:
                Confidence.response = Confidence.getRating()
                Confidence.rt = Confidence.getRT()
            elif Confidence.noResponse == True:
                if keyState[key.LEFT] == True and Confidence.markerPlacedAt > 0.01:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt - 0.02
                    Confidence.draw()
                elif keyState[key.LEFT] == True and Confidence.markerPlacedAt == 0.01:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt - 0.01
                    Confidence.draw()
                elif keyState[key.RIGHT] == True and Confidence.markerPlacedAt < 0.99:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt + 0.02
                    Confidence.draw()
                elif keyState[key.RIGHT] == True and Confidence.markerPlacedAt == 0.99:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt + 0.01
                    Confidence.draw()
        
        # *InstrConf* updates
        if t >= 0.2 and InstrConf.status == NOT_STARTED:
            InstrConf.tStart = t
            InstrConf.frameNStart = frameN
            InstrConf.setAutoDraw(True)
        
        # *instr_conf_keys* updates
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in ConfComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
        
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
    #-------Ending Routine "conf"-------
    for thisComponent in ConfComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    # store data for binary (TrialHandler)
    thisExp.addData('Confidence', Confidence.getRating())
    thisExp.addData('Confidence.RT', Confidence.getRT())
    thisExp.nextEntry()

#################################### End of Confidence Example #####################################
#------Prepare to start Routine "Instructions4"-------
t = 0
Instructions4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instructions4Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions4Response.status = NOT_STARTED
# keep track of which components have finished
Instructions4Components = []
Instructions4Components.append(Instructions4Text)
Instructions4Components.append(Instructions4Response)
for thisComponent in Instructions4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions4Text* updates
    if t >= 0.0 and Instructions4Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions4Text.tStart = t  # underestimates by a little under one frame
        Instructions4Text.frameNStart = frameN  # exact frame index
        Instructions4Text.setAutoDraw(True)
    
    # *Instructions4Response* updates
    if t >= 0 and Instructions4Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions4Response.tStart = t  # underestimates by a little under one frame
        Instructions4Response.frameNStart = frameN  # exact frame index
        Instructions4Response.status = STARTED
        # keyboard checking is just starting
        Instructions4Response.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instructions4Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instructions4Response.keys = theseKeys[-1]  # just the last key pressed
            Instructions4Response.rt = Instructions2Response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions4"-------
for thisComponent in Instructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructions4Response.keys in ['', [], None]:  # No response was made
   Instructions4Response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instructions4Response.keys',Instructions4Response.keys)
if Instructions3Response.keys != None:  # we had a response
    thisExp.addData('Instructions4Response.rt', Instructions4Response.rt)
thisExp.nextEntry()

########################## Main Staircase ##################################
# create a counter to control the breaks within the stairhandler
RestCounter = 0
#create the staircase handler
MainStaircase = data.StairHandler(startVal = DotDifference,
                          stepType = 'lin', stepSizes=1, nTrials=200,
                          nUp=1, nDown=2, minVal=1, maxVal=99)  #will home in on the 80% threshold
                          

for ThisIncrement in MainStaircase:
    # Increase the RestCounter
    RestCounter += 1
    # Set dot difference for this trial
    DotDifference = ThisIncrement
    #randomise whether the stable dotarray is the smaller or the larger value
    DotDiffDenominator = np.random.choice([-1,1])
    if DotDiffDenominator == -1:
        DotVarialble = DotStable - DotDifference
    else:
        DotVarialble = DotStable + DotDifference
    #randomise the location of the fixed and variable stimuli
    StableSide= np.random.choice([-1,1])
    if StableSide == -1:
        DotLeft = DotStable
        DotRight = DotVarialble
    else:
        DotLeft =DotVarialble
        DotRight = DotStable
    # Determine the correct response for the trial
    if DotLeft > DotRight:
        CorrectKey = str('left')
    elif DotRight > DotLeft:
        CorrectKey = str('right')

    #------Prepare to start Routine "choice"-------
    t = 0
    ExampleClock.reset()
    frameN = -1
     # update component parameters for each repeat
    DotPatchLeft=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotLeft, fieldShape='circle', fieldPos=(-11.0, 4.0), fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    DotPatchRight=visual.DotStim(win, color=(1.0,1.0,1.0), dir=270, units='cm',
    nDots=DotRight, fieldShape='circle', fieldPos=(11, 4.0),fieldSize=11,
    dotSize= 15,
    dotLife=-1, #number of frames for each dot to be drawn
    signalDots='same', #are the signal dots the 'same' on each frame? (see Scase et al)
    noiseDots='position', #do the noise dots follow random- 'walk', 'direction', or 'position'
    speed=0.0, coherence=1.0)
    # Update Keyboard parameters
    event.clearEvents(eventType='keyboard')
    KeyRespCal = event.BuilderKeyResponse()
    KeyRespCal.status = NOT_STARTED
     # keep track of which components have finished
    dot_choiceComponents = []
    dot_choiceComponents.append(CircleLeft)
    dot_choiceComponents.append(CircleRight)
    dot_choiceComponents.append(DotPatchLeft)
    dot_choiceComponents.append(DotPatchRight)
    dot_choiceComponents.append(DotCalibrationInstructions)
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
#-------Start Routine "dot_choice"-------
    continueRoutine = True
    while continueRoutine:
        t = ExampleClock.getTime()
        frameN = frameN + 1
        
        # *CircleLeft* updates
        if t >= 0.2 and CircleLeft.status == NOT_STARTED:
            CircleLeft.tStart = t
            CircleLeft.frameNStart = frameN
            CircleLeft.setAutoDraw(True)

            
        # *CircleRight* updates
        if t >= 0.2 and CircleRight.status == NOT_STARTED:
            CircleRight.tStart = t
            CircleRight.frameNStart = frameN
            CircleRight.setAutoDraw(True)

            
         # *DotPatchLeft* updates
        if t >= 0.2 and DotPatchLeft.status == NOT_STARTED:
            DotPatchLeft.tStart = t
            DotPatchLeft.frameNStart = frameN
            DotPatchLeft.setAutoDraw(True)

        
        # *DotPatchRight* updates
        if t >= 0.2 and DotPatchRight.status == NOT_STARTED:
            DotPatchRight.tStart = t
            DotPatchRight.frameNStart = frameN
            DotPatchRight.setAutoDraw(True)

        
        # *DotExampleInstructions* updates
        if t >= 0.2 and DotCalibrationInstructions.status == NOT_STARTED:
            DotCalibrationInstructions.tStart = t
            DotCalibrationInstructions.frameNStart = frameN
            DotCalibrationInstructions.setAutoDraw(True)
            
        # *key_resp_choice* updates
        if t >= 0.2 and KeyRespCal.status == NOT_STARTED:
            KeyRespCal.tStart = t
            KeyRespCal.frameNStart = frameN
            KeyRespCal.status = STARTED
            KeyRespCal.clock.reset()
        if KeyRespCal.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if 'escape' in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                KeyRespCal.keys = theseKeys[-1]
                KeyRespCal.rt = key_resp_choice.clock.getTime()
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in dot_choiceComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break
            
         # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
            
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
     #-------Ending Routine "choice"-------
    for thisComponent in dot_choiceComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyRespCal.keys in ['', [], None]:
        KeyRespCal.keys = None
        # was no response the correct answer?!
    if KeyRespCal.keys == CorrectKey: KeyRespCal.corr = 1  # correct non-response
    else: KeyRespCal.corr = 0  # failed to respond (incorrectly)
    
    # Tell the staircase handler whether the participant responded correctly
    MainStaircase.addResponse(KeyRespCal.corr)
    
    # Store data for experiment:
    thisExp.addData('Correct', KeyRespCal.corr)
    thisExp.addData('CorrectKey', CorrectKey)
    thisExp.addData('Response', KeyRespCal.keys)
    if KeyRespCal.keys != None:
        thisExp.addData('RT', KeyRespCal.rt)
    thisExp.addData('DotDifference', DotDifference)
    thisExp.addData('DotNumberRight', DotPatchRight.nDots)
    thisExp.addData('DotNumberLeft', DotPatchLeft.nDots)
    
    
    #------Prepare to start Routine "conf"-------
    t = 0
    ConfClock.reset()
    frameN = -1
    # update component parameters for each repeat
    Confidence.reset()
    # keep track of which components have finished
    ConfComponents = []
    ConfComponents.append(InstrConf)
    ConfComponents.append(InstrConfKeys)
    ConfComponents.append(Confidence)
    for thisComponent in ConfComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "conf"-------
# checking to see if participants responded to the choice question
# if not,it skips this iteration of the confidence routine
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ConfClock.getTime()
        frameN = frameN + 1

        # *confidence* updates
        if t > 0.2:
            Confidence.draw()
            continueRoutine = Confidence.noResponse
            if Confidence.noResponse == False:
                Confidence.response = Confidence.getRating()
                Confidence.rt = Confidence.getRT()
            elif Confidence.noResponse == True:
                if keyState[key.LEFT] == True and Confidence.markerPlacedAt > 0.01:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt - 0.02
                    Confidence.draw()
                elif keyState[key.LEFT] == True and Confidence.markerPlacedAt == 0.01:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt - 0.01
                    Confidence.draw()
                elif keyState[key.RIGHT] == True and Confidence.markerPlacedAt < 0.99:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt + 0.02
                    Confidence.draw()
                elif keyState[key.RIGHT] == True and Confidence.markerPlacedAt == 0.99:
                    Confidence.markerPlacedAt = Confidence.markerPlacedAt + 0.01
                    Confidence.draw()
        
        # *InstrConf* updates
        if t >= 0.2 and InstrConf.status == NOT_STARTED:
            InstrConf.tStart = t
            InstrConf.frameNStart = frameN
            InstrConf.setAutoDraw(True)
        
        # *instr_conf_keys* updates
        if not continueRoutine:
            routineTimer.reset()
            break
        continueRoutine = False
        for thisComponent in ConfComponents:
            if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=['escape']):
            core.quit()
        
        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()
    
    #-------Ending Routine "conf"-------
    for thisComponent in ConfComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
    # store data for binary (TrialHandler)
    thisExp.addData('Confidence', Confidence.getRating())
    thisExp.addData('Confidence.RT', Confidence.getRT())
    thisExp.nextEntry()
    
    # If the trial number is divisible by 25, display the rest prompt
    if RestCounter % 25 == 0 and RestCounter != 200:
        
        #------Prepare to start Routine "Rest"-------
        t = 0
        RestClock.reset()
        frameN = -1
        # update component parameters for each repeat
        RestResponse = event.BuilderKeyResponse()
        RestResponse.status = NOT_STARTED
        # keep track of which components have finished
        RestComponents = []
        RestComponents.append(RestText)
        RestComponents.append(RestResponse)
        for thisComponent in RestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Rest"-------
        continueRoutine = True
        while continueRoutine:
            t = RestClock.getTime()
            frameN = frameN + 1
            
            # *RestText* updates
            if t >= 0.0 and RestText.status == NOT_STARTED:
                RestText.tStart = t
                RestText.frameNStart = frameN
                RestText.setAutoDraw(True)
            
            # *RestResponse* updates
            if t >= 2.0 and RestResponse.status == NOT_STARTED:
                RestResponse.tStart = t
                RestResponse.frameNStart = frameN
                RestResponse.status = STARTED
                RestResponse.clock.reset()
                event.clearEvents(eventType='keyboard')
            if RestResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if 'escape' in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:
                    RestResponse.keys = theseKeys[-1]
                    RestResponse.rt = RestResponse.clock.getTime()
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:
                routineTimer.reset()
                break
            continueRoutine = False
            for thisComponent in RestComponents:
                if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=['escape']):
                core.quit()
            
            # refresh the screen
            if continueRoutine:
                win.flip()
            else:
                routineTimer.reset()

        #-------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, 'setAutoDraw'):
                thisComponent.setAutoDraw(False)
        # check responses
        if RestResponse.keys in ['', [], None]:
            RestResponse.keys = None
        # store data for MainStaircase (ExperimentHandler)
        if RestResponse.keys != None:
            thisExp.addData('RestTime', RestResponse.rt)  
            thisExp.nextEntry()

#################################### End of main staircase #####################################
#------Prepare to start Routine "Thank You"-------
t = 0
ThankYouClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ThankYouResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
ThankYouResponse.status = NOT_STARTED
# keep track of which components have finished
ThankYouComponents = []
ThankYouComponents.append(Instructions3Text)
ThankYouComponents.append(Instructions3Response)
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ThankYou"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYouText* updates
    if t >= 0.0 and ThankYouText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouText.tStart = t  # underestimates by a little under one frame
        ThankYouText.frameNStart = frameN  # exact frame index
        ThankYouText.setAutoDraw(True)
    
    # *ThankYouResponse* updates
    if t >= 0 and ThankYouResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouResponse.tStart = t  # underestimates by a little under one frame
        ThankYouResponse.frameNStart = frameN  # exact frame index
        ThankYouResponse.status = STARTED
        # keyboard checking is just starting
        ThankYouResponse.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ThankYouResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ThankYouResponse.keys = theseKeys[-1]  # just the last key pressed
            ThankYouResponse.rt = ThankYouResponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions3"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ThankYouResponse.keys in ['', [], None]:  # No response was made
   ThankYouResponse.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('ThankYouResponse.keys',ThankYouResponse.keys)
if ThankYouResponse.keys != None:  # we had a response
    thisExp.addData('ThankYouResponse.rt', ThankYouResponse.rt)
thisExp.nextEntry()
win.close()
core.quit()