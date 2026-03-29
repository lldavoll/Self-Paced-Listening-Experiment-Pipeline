#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.2),
    on marzo 26, 2026, at 18:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from list
from psychopy import gui, core

# Which list to use?
dlg = gui.Dlg(title="Select List")
dlg.addField("List number (1–2):")
ok_data = dlg.show()

if dlg.OK:
    list_num = ok_data[0]
else:
    core.quit()  # closes the experiment if Cancel is pressed

# --- Build the filename dynamically ---
conditions_file = f"spl_stim_exp1_{list_num}.csv"
print(f"Using condition file: {conditions_file}")
# Run 'Before Experiment' code from code_bio


# Run 'Before Experiment' code from code_historial


# Run 'Before Experiment' code from code_historial_2


# Run 'Before Experiment' code from code_uso


# Run 'Before Experiment' code from code_uso_2


# Run 'Before Experiment' code from code_uso_3


# Run 'Before Experiment' code from code_competencia


# Run 'Before Experiment' code from code_actitud


# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.2'
expName = 'spl_exp'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\ateni\\Desktop\\U of A\\EXPERIMENTOS\\SPL\\SPL_Gabi\\exp_1\\spl_exp_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[-0.6314, -0.3804, -0.3804], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.6314, -0.3804, -0.3804]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Tarea cargando, por favor espere...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "list_setup" ---
    # Run 'Begin Experiment' code from list
    import pandas as pd
    import random
    
    # Load condition file for this list
    df = pd.read_csv(conditions_file)
    
    # Extract unique item_ids
    items = df["item_id"].unique().tolist()
    
    # Separate items by type (ending in d or p)
    items_d = [it for it in items if it.endswith("d")]
    items_p = [it for it in items if it.endswith("p")]
    
    random.shuffle(items_d)
    random.shuffle(items_p)
    
    final_order = []
    
    # Pick items one by one while ensuring no 3 in a row
    while items_d or items_p:
        
        # Determine which list to draw from
        if len(final_order) >= 2:
            last1 = final_order[-1][-1]
            last2 = final_order[-2][-1]
    
            # If last two end in d → must choose p
            if last1 == last2 == "d" and items_p:
                choice = "p"
    
            # If last two end in p → must choose d
            elif last1 == last2 == "p" and items_d:
                choice = "d"
    
            else:
                # Otherwise choose whichever has more remaining items
                choice = "d" if len(items_d) >= len(items_p) else "p"
    
        else:
            # First two items: choose from whichever has more
            choice = "d" if len(items_d) >= len(items_p) else "p"
    
        # Draw the item
        if choice == "d" and items_d:
            final_order.append(items_d.pop())
        elif choice == "p" and items_p:
            final_order.append(items_p.pop())
        else:
            # fallback if one list empties
            if items_d:
                final_order.append(items_d.pop())
            else:
                final_order.append(items_p.pop())
    
    print("Randomized item order:", final_order)
    
    # ---- Convert item order into row indices ----
    new_order = []
    for it in final_order:
        rows = df.index[df["item_id"] == it].tolist()
        new_order.extend(rows)
    
    trial_list = new_order
    
    
    # --- Initialize components for Routine "blp_bio" ---
    # Run 'Begin Experiment' code from code_bio
    from psychopy import core
    boton_bio = visual.ButtonStim(win, 
        text='Siguiente (1/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_bio',
        depth=-1
    )
    boton_bio.buttonClock = core.Clock()
    indicaciones_bio = visual.TextStim(win=win, name='indicaciones_bio',
        text='1. Información Biográfica  \nPor favor complete los campos y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.45), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_nombre = visual.TextStim(win=win, name='text_nombre',
        text='Nombre ',
        font='Arial',
        pos=(-0.38, 0.30), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    nombre = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, 0.30), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='nombre',
         depth=-4, autoLog=False,
    )
    text_edad = visual.TextStim(win=win, name='text_edad',
        text='Edad',
        font='Arial',
        pos=(-0.38, 0.20), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    edad = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, 0.20), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='edad',
         depth=-6, autoLog=False,
    )
    text_genero = visual.TextStim(win=win, name='text_genero',
        text='Género (Hombre / Mujer / Otro)\n',
        font='Arial',
        pos=(-0.38, 0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    genero = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, 0.10), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='genero',
         depth=-8, autoLog=False,
    )
    text_nacimiento = visual.TextStim(win=win, name='text_nacimiento',
        text='Lugar donde nació',
        font='Arial',
        pos=(-0.38, 0.0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    nacimiento = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, 0.0), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='nacimiento',
         depth=-10, autoLog=False,
    )
    text_vive = visual.TextStim(win=win, name='text_vive',
        text='Lugar donde vive ahora (ciudad/barrio)\n',
        font='Arial',
        pos=(-0.38, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    vive = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, -0.10), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='vive',
         depth=-12, autoLog=False,
    )
    text_mama = visual.TextStim(win=win, name='text_mama',
        text='¿Lengua(s) que habla su mamá?',
        font='Arial',
        pos=(-0.38, -0.20), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    mama = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, -0.20), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='mama',
         depth=-14, autoLog=False,
    )
    text_papa = visual.TextStim(win=win, name='text_papa',
        text='¿Lengua(s) que habla su papá? ',
        font='Arial',
        pos=(-0.38, -0.30), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    papa = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, -0.30), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='papa',
         depth=-16, autoLog=False,
    )
    text_educacion = visual.TextStim(win=win, name='text_educacion',
        text='¿Nivel más alto de educación?\n',
        font='Arial',
        pos=(-0.38, -0.40), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    educacion = visual.TextBox2(
         win, text=None, placeholder='Escriba aquí… / Qillqay kaypi…', font='Arial',
         ori=0.0, pos=(0.38, -0.40), draggable=False,      letterHeight=0.04,
         size=(0.8, 0.08), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='educacion',
         depth=-18, autoLog=False,
    )
    
    # --- Initialize components for Routine "blp_historial_1" ---
    # Run 'Begin Experiment' code from code_historial
    from psychopy import core
    boton_historial = visual.ButtonStim(win, 
        text='Siguiente (2/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_historial',
        depth=-1
    )
    boton_historial.buttonClock = core.Clock()
    indicaciones_historial = visual.TextStim(win=win, name='indicaciones_historial',
        text='2. Historial lingüístico\nPor favor marque la casilla que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_edad_q = visual.TextStim(win=win, name='text_edad_q',
        text='¿A qué edad empezó a aprender el quechua?',
        font='Arial',
        pos=(-0.5, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    edad_aprender_que = visual.Slider(win=win, name='edad_aprender_que',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.30), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_edad_esp = visual.TextStim(win=win, name='text_edad_esp',
        text='¿A qué edad empezó a aprender el español?  \n',
        font='Arial',
        pos=(-0.5, 0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    edad_aprender_esp = visual.Slider(win=win, name='edad_aprender_esp',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.15), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_comodidad_que = visual.TextStim(win=win, name='text_comodidad_que',
        text='¿A qué edad empezó a usar el Quechua con comodidad?\n',
        font='Arial',
        pos=(-0.5, -0.03), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    edad_comodidad_que = visual.Slider(win=win, name='edad_comodidad_que',
        startValue=None, size=(0.8, 0.05), pos=(0.35, 0), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    text_comodidad_esp = visual.TextStim(win=win, name='text_comodidad_esp',
        text='¿A qué edad empezó a usar el Español con comodidad?',
        font='Arial',
        pos=(-0.5, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    edad_comodidad_esp = visual.Slider(win=win, name='edad_comodidad_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.10), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    text_clases_que = visual.TextStim(win=win, name='text_clases_que',
        text='¿Cuántos años de clases (gramática, historia, matemáticas, etc.) \nha tenido en Quechua (desde la escuela a la universidad)?\n',
        font='Arial',
        pos=(-0.48, -0.22), draggable=False, height=0.027, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    años_clases_que = visual.Slider(win=win, name='años_clases_que',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.20), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    text_clases_esp = visual.TextStim(win=win, name='text_clases_esp',
        text='¿Cuántos años de clases (gramática, historia, matemáticas, etc.) \nha tenido en Castellano(desde la escuela a la universidad)?\n',
        font='Arial',
        pos=(-0.48, -0.32), draggable=False, height=0.027, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    años_clases_esp = visual.Slider(win=win, name='años_clases_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.30), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    
    # --- Initialize components for Routine "blp_historial_2" ---
    # Run 'Begin Experiment' code from code_historial_2
    from psychopy import core
    boton_historial_2 = visual.ButtonStim(win, 
        text='Siguiente (3/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_historial_2',
        depth=-1
    )
    boton_historial_2.buttonClock = core.Clock()
    indicaciones_historial_2 = visual.TextStim(win=win, name='indicaciones_historial_2',
        text='2. Historial lingüístico\nPor favor marque la casilla que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_comunidad_que = visual.TextStim(win=win, name='text_comunidad_que',
        text='¿Cuántos años ha vivido en una comunidad \ndonde se habla Quechua?',
        font='Arial',
        pos=(-0.5, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    años_comunidad_que = visual.Slider(win=win, name='años_comunidad_que',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.30), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_comunidad_esp = visual.TextStim(win=win, name='text_comunidad_esp',
        text='¿Cuántos años ha vivido en una comunidad \ndonde se habla Castellano?',
        font='Arial',
        pos=(-0.5, 0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    años_comunidad_esp = visual.Slider(win=win, name='años_comunidad_esp',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.15), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_familia_que = visual.TextStim(win=win, name='text_familia_que',
        text='¿Cuántos años ha pasado hablando Quechua \ncon su familia?',
        font='Arial',
        pos=(-0.5, -0.025), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    años_familia_que = visual.Slider(win=win, name='años_familia_que',
        startValue=None, size=(0.8, 0.05), pos=(0.35, 0), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    text_familia_esp = visual.TextStim(win=win, name='text_familia_esp',
        text='¿Cuántos años ha pasado hablando Castellano \ncon su familia?',
        font='Arial',
        pos=(-0.5, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    años_familia_esp = visual.Slider(win=win, name='años_familia_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.10), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    text_trabajo_que = visual.TextStim(win=win, name='text_trabajo_que',
        text='¿Cuántos años ha trabajado en un ambiente \ndonde se habla Quechua?',
        font='Arial',
        pos=(-0.48, -0.22), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    años_trabajo_que = visual.Slider(win=win, name='años_trabajo_que',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.20), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    text_trabajo_esp = visual.TextStim(win=win, name='text_trabajo_esp',
        text='¿Cuántos años ha trabajado en un ambiente \ndonde se habla Castellano?\n',
        font='Arial',
        pos=(-0.48, -0.32), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    años_trabajo_esp = visual.Slider(win=win, name='años_trabajo_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.30), units=win.units,
        labels=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20+'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.021,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    
    # --- Initialize components for Routine "blp_uso_1" ---
    # Run 'Begin Experiment' code from code_uso
    from psychopy import core
    boton_uso = visual.ButtonStim(win, 
        text='Siguiente (4/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_uso',
        depth=-1
    )
    boton_uso.buttonClock = core.Clock()
    indicaciones_uso = visual.TextStim(win=win, name='indicaciones_uso',
        text='3. El uso de lenguas\nPor favor eleccione la opcion que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_amigos_que = visual.TextStim(win=win, name='text_amigos_que',
        text='\nPorcentaje del tiempo que usa Quechua \ncon sus amigos\n',
        font='Arial',
        pos=(-0.5, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    porc_amigos_que = visual.Slider(win=win, name='porc_amigos_que',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_amigos_esp = visual.TextStim(win=win, name='text_amigos_esp',
        text='\nPorcentaje del tiempo que usa Castellano \ncon sus amigos\n',
        font='Arial',
        pos=(-0.5, 0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    porc_amigos_esp = visual.Slider(win=win, name='porc_amigos_esp',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.15), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_amigos_otr = visual.TextStim(win=win, name='text_amigos_otr',
        text='Porcentaje del tiempo que usa Otras Lenguas\ncon sus amigos\n',
        font='Arial',
        pos=(-0.5, -0.03), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    porc_amigos_otr = visual.Slider(win=win, name='porc_amigos_otr',
        startValue=None, size=(0.8, 0.05), pos=(0.35, 0), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    porcent_familia_que = visual.TextStim(win=win, name='porcent_familia_que',
        text='\n\nPorcentaje del tiempo que usa Quechua \ncon su familia\n',
        font='Arial',
        pos=(-0.5, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    porc_familia_que = visual.Slider(win=win, name='porc_familia_que',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.10), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    porcent_familia_esp = visual.TextStim(win=win, name='porcent_familia_esp',
        text='Porcentaje del tiempo que usa Castellano \ncon su familia\n',
        font='Arial',
        pos=(-0.48, -0.22), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    porc_familia_esp = visual.Slider(win=win, name='porc_familia_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.20), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    porcent_familia_otr = visual.TextStim(win=win, name='porcent_familia_otr',
        text='Porcentaje del tiempo que usa \nOtras Lenguas con su familia\n',
        font='Arial',
        pos=(-0.48, -0.32), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    porc_familia_otr = visual.Slider(win=win, name='porc_familia_otr',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    
    # --- Initialize components for Routine "blp_uso_2" ---
    # Run 'Begin Experiment' code from code_uso_2
    from psychopy import core
    boton_uso_2 = visual.ButtonStim(win, 
        text='Siguiente (5/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_uso_2',
        depth=-1
    )
    boton_uso_2.buttonClock = core.Clock()
    indicaciones_uso_2 = visual.TextStim(win=win, name='indicaciones_uso_2',
        text='3. El uso de lenguas\nPor favor eleccione la opcion que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_formal_que = visual.TextStim(win=win, name='text_formal_que',
        text='Porcentaje del tiempo que usa Quechua \nen ambientes formales (educación, alcaldía)\n',
        font='Arial',
        pos=(-0.5, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    porc_formal_que = visual.Slider(win=win, name='porc_formal_que',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_formal_esp = visual.TextStim(win=win, name='text_formal_esp',
        text='Porcentaje del tiempo que usa Castellano \nen ambientes formales (educación, alcaldía)\n',
        font='Arial',
        pos=(-0.5, 0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    porc_formal_esp = visual.Slider(win=win, name='porc_formal_esp',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.15), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_formal_otr = visual.TextStim(win=win, name='text_formal_otr',
        text='Porcentaje del tiempo que usa \nOtras Lenguas en ambientes formales \n(educación, alcaldía)\n',
        font='Arial',
        pos=(-0.5, -0.03), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    porc_formal_otr = visual.Slider(win=win, name='porc_formal_otr',
        startValue=None, size=(0.8, 0.05), pos=(0.35, 0), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    porct_trabajo_que = visual.TextStim(win=win, name='porct_trabajo_que',
        text='\n\nPorcentaje del tiempo que usa Quechua \nen el trabajo\n',
        font='Arial',
        pos=(-0.5, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    porc_trabajo_que = visual.Slider(win=win, name='porc_trabajo_que',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.10), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    porct_trabajo_esp = visual.TextStim(win=win, name='porct_trabajo_esp',
        text='Porcentaje del tiempo que usa Castellano \nen el trabajo\n',
        font='Arial',
        pos=(-0.48, -0.22), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    porc_trabajo_esp = visual.Slider(win=win, name='porc_trabajo_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.20), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    porct_trabajo_otr = visual.TextStim(win=win, name='porct_trabajo_otr',
        text='Porcentaje del tiempo que usa \nOtras Lenguas en el trabajo\n',
        font='Arial',
        pos=(-0.48, -0.32), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    porc_trabajo_otr = visual.Slider(win=win, name='porc_trabajo_otr',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    
    # --- Initialize components for Routine "blp_uso_3" ---
    # Run 'Begin Experiment' code from code_uso_3
    from psychopy import core
    boton_uso_3 = visual.ButtonStim(win, 
        text='Siguiente (6/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_uso_3',
        depth=-1
    )
    boton_uso_3.buttonClock = core.Clock()
    indicaciones_uso_3 = visual.TextStim(win=win, name='indicaciones_uso_3',
        text='3. El uso de lenguas\nPor favor eleccione la opcion que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_mismo_que = visual.TextStim(win=win, name='text_mismo_que',
        text='Porcentaje del tiempo que se habla\na sí mismo en Quechua\n',
        font='Arial',
        pos=(-0.5, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    porc_mismo_que = visual.Slider(win=win, name='porc_mismo_que',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_mismo_esp = visual.TextStim(win=win, name='text_mismo_esp',
        text='Porcentaje del tiempo que se habla\na sí mismo en Castellano\n',
        font='Arial',
        pos=(-0.5, 0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    porc_mismo_esp = visual.Slider(win=win, name='porc_mismo_esp',
        startValue=None, size=(0.8, 0.05), pos=(0.25, 0.15), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_mismo_otr = visual.TextStim(win=win, name='text_mismo_otr',
        text='Porcentaje del tiempo que se habla\na sí mismo en Otras Lenguas\n',
        font='Arial',
        pos=(-0.5, -0.03), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    porc_mismo_otr = visual.Slider(win=win, name='porc_mismo_otr',
        startValue=None, size=(0.8, 0.05), pos=(0.35, 0), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    text_calculos_que = visual.TextStim(win=win, name='text_calculos_que',
        text='\n\nPorcentaje del tiempo que cuenta\no calcula en Quechua\n',
        font='Arial',
        pos=(-0.5, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    porc_calculos_que = visual.Slider(win=win, name='porc_calculos_que',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.10), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    text_calculos_esp = visual.TextStim(win=win, name='text_calculos_esp',
        text='\n\nPorcentaje del tiempo que cuenta\no calcula en Castellano\n\n',
        font='Arial',
        pos=(-0.48, -0.22), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    porc_calculos_esp = visual.Slider(win=win, name='porc_calculos_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.20), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    text_calculos_otr = visual.TextStim(win=win, name='text_calculos_otr',
        text='Porcentaje del tiempo que cuenta\no calcula en Otras Lenguas\n',
        font='Arial',
        pos=(-0.48, -0.32), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    porc_calculos_otr = visual.Slider(win=win, name='porc_calculos_otr',
        startValue=None, size=(0.8, -0.05), pos=(0.35, -0.30), units=win.units,
        labels=('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'),ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    
    # --- Initialize components for Routine "blp_competencia" ---
    # Run 'Begin Experiment' code from code_competencia
    from psychopy import core
    boton_competencia = visual.ButtonStim(win, 
        text='Siguiente (7/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_competencia',
        depth=-1
    )
    boton_competencia.buttonClock = core.Clock()
    indicaciones_competencia = visual.TextStim(win=win, name='indicaciones_competencia',
        text='4. Competencia Lingüística\nPor favor eleccione la opcion que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_habla_que = visual.TextStim(win=win, name='text_habla_que',
        text='\n\n¿Habla bien en Quechua?\n',
        font='Arial',
        pos=(-0.7, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    habla_bien_que = visual.Slider(win=win, name='habla_bien_que',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.30), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_habla_esp = visual.TextStim(win=win, name='text_habla_esp',
        text='¿Habla bien en Castellano?',
        font='Arial',
        pos=(-0.7, 0.20), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    habla_bien_esp = visual.Slider(win=win, name='habla_bien_esp',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.20), units=win.units,
        labels=('0=may mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_entiende_que = visual.TextStim(win=win, name='text_entiende_que',
        text='\n   ¿Entiende bien en Quechua?\n',
        font='Arial',
        pos=(-0.7, 0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    entiende_bien_que = visual.Slider(win=win, name='entiende_bien_que',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.10), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    text_entiende_esp = visual.TextStim(win=win, name='text_entiende_esp',
        text='\n    ¿Entiende bien en Castellano?\n',
        font='Arial',
        pos=(-0.7, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    entiende_bien_esp = visual.Slider(win=win, name='entiende_bien_esp',
        startValue=None, size=(0.8, -0.05), pos=(0, 0), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    text_lee_que = visual.TextStim(win=win, name='text_lee_que',
        text='\n\n¿Lee bien en Quechua?\n\n',
        font='Arial',
        pos=(-0.7, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    lee_bien_que = visual.Slider(win=win, name='lee_bien_que',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.10), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    text_lee_esp = visual.TextStim(win=win, name='text_lee_esp',
        text='¿Lee bien en Castellano?',
        font='Arial',
        pos=(-0.7, -0.20), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    lee_bien_esp = visual.Slider(win=win, name='lee_bien_esp',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.20), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    text_escribe_que = visual.TextStim(win=win, name='text_escribe_que',
        text='¿Escribe bien en Quechua?',
        font='Arial',
        pos=(-0.7, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    escribe_bien_que = visual.Slider(win=win, name='escribe_bien_que',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.3), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-16, readOnly=False)
    text_escribe_esp = visual.TextStim(win=win, name='text_escribe_esp',
        text='¿Escribe bien en Castellano?',
        font='Arial',
        pos=(-0.7, -0.40), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    escribe_bien_esp = visual.Slider(win=win, name='escribe_bien_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.0, -0.40), units=win.units,
        labels=('0=muy mal','1','2','3','4','5','6=muy bien'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.02,
        flip=False, ori=0.0, depth=-18, readOnly=False)
    
    # --- Initialize components for Routine "blp_actitud" ---
    # Run 'Begin Experiment' code from code_actitud
    from psychopy import core
    boton_actitud = visual.ButtonStim(win, 
        text='Siguiente (8/8)', font='Arvo',
        pos=(0.75, -0.45),
        letterHeight=0.035,
        size=(0.3, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='gray', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='boton_actitud',
        depth=-1
    )
    boton_actitud.buttonClock = core.Clock()
    indicaciones_actitud = visual.TextStim(win=win, name='indicaciones_actitud',
        text='5. Actitudes Lingüísticas\nPor favor eleccione la opcion que cosidere apropiada y haga clic en Siguiente.',
        font='Arial',
        pos=(0, 0.40), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_yomismo_que = visual.TextStim(win=win, name='text_yomismo_que',
        text='\n  Me siento "yo mismo" cuando \nhablo en Quechua\n',
        font='Arial',
        pos=(-0.7, 0.30), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    yo_mismo_que = visual.Slider(win=win, name='yo_mismo_que',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.30), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    text_yomismo_esp = visual.TextStim(win=win, name='text_yomismo_esp',
        text='\n  Me siento "yo mismo" cuando \nhablo en Castellano\n',
        font='Arial',
        pos=(-0.7, 0.20), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    yo_mismo_esp = visual.Slider(win=win, name='yo_mismo_esp',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.20), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    text_cultura_que = visual.TextStim(win=win, name='text_cultura_que',
        text='\n   Me identifico con la cultura \n   de los que hablan Quechua\n',
        font='Arial',
        pos=(-0.7, 0.10), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    cultura_que = visual.Slider(win=win, name='cultura_que',
        startValue=None, size=(0.8, 0.05), pos=(0, 0.10), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    text_cultura_esp = visual.TextStim(win=win, name='text_cultura_esp',
        text='\n\n\n  Me identifico con la cultura\n  de los que hablan Castellano\n\n',
        font='Arial',
        pos=(-0.7, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    cultura_esp = visual.Slider(win=win, name='cultura_esp',
        startValue=None, size=(0.8, -0.05), pos=(0, 0), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    text_uso_nativo_que = visual.TextStim(win=win, name='text_uso_nativo_que',
        text='\n\n\n               Es importante para mí usar el Quechua\n como hablante nativo\n\n\n',
        font='Arial',
        pos=(-0.7, -0.10), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    uso_nativo_que = visual.Slider(win=win, name='uso_nativo_que',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.10), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    text_uso_nativo_esp = visual.TextStim(win=win, name='text_uso_nativo_esp',
        text='\n\n               Es importante para mí usar el Castellano\n como hablante nativo\n',
        font='Arial',
        pos=(-0.7, -0.20), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    uso_nativo_esp = visual.Slider(win=win, name='uso_nativo_esp',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.20), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    text_habalnte_nativo_que = visual.TextStim(win=win, name='text_habalnte_nativo_que',
        text='\n     Quiero que los demás piensen que \nsoy hablante nativo de Quechua\n',
        font='Arial',
        pos=(-0.7, -0.3), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    hablante_nativo_que = visual.Slider(win=win, name='hablante_nativo_que',
        startValue=None, size=(0.8, -0.05), pos=(0, -0.3), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-16, readOnly=False)
    text_hablante_nativo_esp = visual.TextStim(win=win, name='text_hablante_nativo_esp',
        text='\n     Quiero que los demás piensen que\n     soy hablante nativo de Castellano\n',
        font='Arial',
        pos=(-0.7, -0.40), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    hablante_nativo_esp = visual.Slider(win=win, name='hablante_nativo_esp',
        startValue=None, size=(0.8, -0.05), pos=(0.0, -0.40), units=win.units,
        labels=('0=para nada','1','2','3','4','5','6=de acuerdo'), ticks=None, granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-18, readOnly=False)
    
    # --- Initialize components for Routine "delay_trial" ---
    cross_q_5 = visual.TextStim(win=win, name='cross_q_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.8, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_delay_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instruction_prueba" ---
    intructions_2 = visual.TextStim(win=win, name='intructions_2',
        text='Primero escucharemos las instrucciones.  \n\nCuando termine el audio presione el boton marcado para continuar.',
        font='Arial',
        pos=(0, 0.15), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_continuar_2 = visual.TextStim(win=win, name='text_continuar_2',
        text='[Presione el boton marcado para comenzar la prueba]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instructions_space_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    # set audio backend
    sound.Sound.backend = 'ptb'
    prueba = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='prueba'
    )
    prueba.setVolume(1.0)
    
    # --- Initialize components for Routine "trial_prueba" ---
    audios_2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='audios_2'
    )
    audios_2.setVolume(1.0)
    cross_2 = visual.TextStim(win=win, name='cross_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_prueba = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "questions_prueba" ---
    question_sound_2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='question_sound_2'
    )
    question_sound_2.setVolume(1.0)
    resp_q_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Para responder la pregunta presione:\n\n"F" = Sí\n\n"J" = No',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    cross_q_2 = visual.TextStim(win=win, name='cross_q_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "delay_prueba" ---
    cross_q_3 = visual.TextStim(win=win, name='cross_q_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.8, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_delay = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions" ---
    intructions = visual.TextStim(win=win, name='intructions',
        text='¡Muy bien! A continuación, haremos la tarea en limpio. \n\nRecuerde presionar el boton marcado para seguir escuchando las oraciones. \n\nDespues de cada oracion, recuerde responder la pregunta presionando uno de los botones marcados. ',
        font='Arial',
        pos=(0, 0.15), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_continuar = visual.TextStim(win=win, name='text_continuar',
        text='[Presione el boton marcado para comenzar la prueba]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instructions_space = keyboard.Keyboard(deviceName='defaultKeyboard')
    intro_prueba = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='intro_prueba'
    )
    intro_prueba.setVolume(1.0)
    
    # --- Initialize components for Routine "trial" ---
    audios = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='audios'
    )
    audios.setVolume(1.0)
    # Run 'Begin Experiment' code from main_code
    from psychopy import event, core
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "question" ---
    question_sound = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='question_sound'
    )
    question_sound.setVolume(1.0)
    resp_q = keyboard.Keyboard(deviceName='defaultKeyboard')
    text = visual.TextStim(win=win, name='text',
        text='Para responder la pregunta presione:\n\n"F" = Sí\n\n"J" = No',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    cross_q = visual.TextStim(win=win, name='cross_q',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "delay_trial" ---
    cross_q_5 = visual.TextStim(win=win, name='cross_q_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.8, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_delay_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "end_routine" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='\n¡Gracias por participar! \n\nTinkunakama masiy.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "list_setup" ---
    # create an object to store info about Routine list_setup
    list_setup = data.Routine(
        name='list_setup',
        components=[],
    )
    list_setup.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from list
    
    
    
    
    # store start times for list_setup
    list_setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    list_setup.tStart = globalClock.getTime(format='float')
    list_setup.status = STARTED
    list_setup.maxDuration = None
    # keep track of which components have finished
    list_setupComponents = list_setup.components
    for thisComponent in list_setup.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "list_setup" ---
    thisExp.currentRoutine = list_setup
    list_setup.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=list_setup,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            list_setup.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if list_setup.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in list_setup.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "list_setup" ---
    for thisComponent in list_setup.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for list_setup
    list_setup.tStop = globalClock.getTime(format='float')
    list_setup.tStopRefresh = tThisFlipGlobal
    # Run 'End Routine' code from list
    # Compute which row to read from the question file
    question_row = [int(list_num) - 1]
    thisExp.nextEntry()
    # the Routine "list_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_bio" ---
    # create an object to store info about Routine blp_bio
    blp_bio = data.Routine(
        name='blp_bio',
        components=[boton_bio, indicaciones_bio, text_nombre, nombre, text_edad, edad, text_genero, genero, text_nacimiento, nacimiento, text_vive, vive, text_mama, mama, text_papa, papa, text_educacion, educacion],
    )
    blp_bio.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_bio
    # Start with Siguiente disabled
    canContinue = False
    boton_bio.opacity = 0.5  # make it look disabled
    boton_bio.color = 'gray'
    # reset boton_bio to account for continued clicks & clear times on/off
    boton_bio.reset()
    nombre.reset()
    edad.reset()
    genero.reset()
    nacimiento.reset()
    vive.reset()
    mama.reset()
    papa.reset()
    educacion.reset()
    # store start times for blp_bio
    blp_bio.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_bio.tStart = globalClock.getTime(format='float')
    blp_bio.status = STARTED
    blp_bio.maxDuration = None
    # keep track of which components have finished
    blp_bioComponents = blp_bio.components
    for thisComponent in blp_bio.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_bio" ---
    thisExp.currentRoutine = blp_bio
    blp_bio.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_bio
        # Check if all fields are filled (no empty textboxes)
        textboxes = [nombre, edad, genero, nacimiento, vive, mama, papa, educacion]  # adapt to your routine
        
        filled = all(len(tb.text.strip()) > 0 for tb in textboxes)
        
        # Enable Siguiente only when all are filled
        if filled and not canContinue:
            canContinue = True
            boton_bio.opacity = 1
            boton_bio.color = 'white'
        elif not filled:
            canContinue = False
            boton_bio.opacity = 0.5
            boton_bio.color = 'gray'
        
        # Only allow clicking Siguiente if validated
        if boton_bio.isClicked and canContinue:
            continueRoutine = False
        # *boton_bio* updates
        
        # if boton_bio is starting this frame...
        if boton_bio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_bio.frameNStart = frameN  # exact frame index
            boton_bio.tStart = t  # local t and not account for scr refresh
            boton_bio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_bio, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_bio.status = STARTED
            win.callOnFlip(boton_bio.buttonClock.reset)
            boton_bio.setAutoDraw(True)
        
        # if boton_bio is active this frame...
        if boton_bio.status == STARTED:
            # update params
            pass
            # check whether boton_bio has been pressed
            if boton_bio.isClicked:
                if not boton_bio.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_bio.timesOn.append(boton_bio.buttonClock.getTime())
                    boton_bio.timesOff.append(boton_bio.buttonClock.getTime())
                elif len(boton_bio.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_bio.timesOff[-1] = boton_bio.buttonClock.getTime()
                # run callback code when boton_bio is clicked
                pass
        # take note of whether boton_bio was clicked, so that next frame we know if clicks are new
        boton_bio.wasClicked = boton_bio.isClicked and boton_bio.status == STARTED
        
        # *indicaciones_bio* updates
        
        # if indicaciones_bio is starting this frame...
        if indicaciones_bio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_bio.frameNStart = frameN  # exact frame index
            indicaciones_bio.tStart = t  # local t and not account for scr refresh
            indicaciones_bio.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_bio, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_bio.status = STARTED
            indicaciones_bio.setAutoDraw(True)
        
        # if indicaciones_bio is active this frame...
        if indicaciones_bio.status == STARTED:
            # update params
            pass
        
        # *text_nombre* updates
        
        # if text_nombre is starting this frame...
        if text_nombre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_nombre.frameNStart = frameN  # exact frame index
            text_nombre.tStart = t  # local t and not account for scr refresh
            text_nombre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_nombre, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_nombre.status = STARTED
            text_nombre.setAutoDraw(True)
        
        # if text_nombre is active this frame...
        if text_nombre.status == STARTED:
            # update params
            pass
        
        # *nombre* updates
        
        # if nombre is starting this frame...
        if nombre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nombre.frameNStart = frameN  # exact frame index
            nombre.tStart = t  # local t and not account for scr refresh
            nombre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nombre, 'tStartRefresh')  # time at next scr refresh
            # update status
            nombre.status = STARTED
            nombre.setAutoDraw(True)
        
        # if nombre is active this frame...
        if nombre.status == STARTED:
            # update params
            pass
        
        # *text_edad* updates
        
        # if text_edad is starting this frame...
        if text_edad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_edad.frameNStart = frameN  # exact frame index
            text_edad.tStart = t  # local t and not account for scr refresh
            text_edad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_edad, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_edad.status = STARTED
            text_edad.setAutoDraw(True)
        
        # if text_edad is active this frame...
        if text_edad.status == STARTED:
            # update params
            pass
        
        # *edad* updates
        
        # if edad is starting this frame...
        if edad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            edad.frameNStart = frameN  # exact frame index
            edad.tStart = t  # local t and not account for scr refresh
            edad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edad, 'tStartRefresh')  # time at next scr refresh
            # update status
            edad.status = STARTED
            edad.setAutoDraw(True)
        
        # if edad is active this frame...
        if edad.status == STARTED:
            # update params
            pass
        
        # *text_genero* updates
        
        # if text_genero is starting this frame...
        if text_genero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_genero.frameNStart = frameN  # exact frame index
            text_genero.tStart = t  # local t and not account for scr refresh
            text_genero.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_genero, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_genero.status = STARTED
            text_genero.setAutoDraw(True)
        
        # if text_genero is active this frame...
        if text_genero.status == STARTED:
            # update params
            pass
        
        # *genero* updates
        
        # if genero is starting this frame...
        if genero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            genero.frameNStart = frameN  # exact frame index
            genero.tStart = t  # local t and not account for scr refresh
            genero.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(genero, 'tStartRefresh')  # time at next scr refresh
            # update status
            genero.status = STARTED
            genero.setAutoDraw(True)
        
        # if genero is active this frame...
        if genero.status == STARTED:
            # update params
            pass
        
        # *text_nacimiento* updates
        
        # if text_nacimiento is starting this frame...
        if text_nacimiento.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_nacimiento.frameNStart = frameN  # exact frame index
            text_nacimiento.tStart = t  # local t and not account for scr refresh
            text_nacimiento.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_nacimiento, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_nacimiento.status = STARTED
            text_nacimiento.setAutoDraw(True)
        
        # if text_nacimiento is active this frame...
        if text_nacimiento.status == STARTED:
            # update params
            pass
        
        # *nacimiento* updates
        
        # if nacimiento is starting this frame...
        if nacimiento.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nacimiento.frameNStart = frameN  # exact frame index
            nacimiento.tStart = t  # local t and not account for scr refresh
            nacimiento.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nacimiento, 'tStartRefresh')  # time at next scr refresh
            # update status
            nacimiento.status = STARTED
            nacimiento.setAutoDraw(True)
        
        # if nacimiento is active this frame...
        if nacimiento.status == STARTED:
            # update params
            pass
        
        # *text_vive* updates
        
        # if text_vive is starting this frame...
        if text_vive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_vive.frameNStart = frameN  # exact frame index
            text_vive.tStart = t  # local t and not account for scr refresh
            text_vive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_vive, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_vive.status = STARTED
            text_vive.setAutoDraw(True)
        
        # if text_vive is active this frame...
        if text_vive.status == STARTED:
            # update params
            pass
        
        # *vive* updates
        
        # if vive is starting this frame...
        if vive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vive.frameNStart = frameN  # exact frame index
            vive.tStart = t  # local t and not account for scr refresh
            vive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vive, 'tStartRefresh')  # time at next scr refresh
            # update status
            vive.status = STARTED
            vive.setAutoDraw(True)
        
        # if vive is active this frame...
        if vive.status == STARTED:
            # update params
            pass
        
        # *text_mama* updates
        
        # if text_mama is starting this frame...
        if text_mama.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mama.frameNStart = frameN  # exact frame index
            text_mama.tStart = t  # local t and not account for scr refresh
            text_mama.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mama, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_mama.status = STARTED
            text_mama.setAutoDraw(True)
        
        # if text_mama is active this frame...
        if text_mama.status == STARTED:
            # update params
            pass
        
        # *mama* updates
        
        # if mama is starting this frame...
        if mama.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mama.frameNStart = frameN  # exact frame index
            mama.tStart = t  # local t and not account for scr refresh
            mama.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mama, 'tStartRefresh')  # time at next scr refresh
            # update status
            mama.status = STARTED
            mama.setAutoDraw(True)
        
        # if mama is active this frame...
        if mama.status == STARTED:
            # update params
            pass
        
        # *text_papa* updates
        
        # if text_papa is starting this frame...
        if text_papa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_papa.frameNStart = frameN  # exact frame index
            text_papa.tStart = t  # local t and not account for scr refresh
            text_papa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_papa, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_papa.status = STARTED
            text_papa.setAutoDraw(True)
        
        # if text_papa is active this frame...
        if text_papa.status == STARTED:
            # update params
            pass
        
        # *papa* updates
        
        # if papa is starting this frame...
        if papa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            papa.frameNStart = frameN  # exact frame index
            papa.tStart = t  # local t and not account for scr refresh
            papa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(papa, 'tStartRefresh')  # time at next scr refresh
            # update status
            papa.status = STARTED
            papa.setAutoDraw(True)
        
        # if papa is active this frame...
        if papa.status == STARTED:
            # update params
            pass
        
        # *text_educacion* updates
        
        # if text_educacion is starting this frame...
        if text_educacion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_educacion.frameNStart = frameN  # exact frame index
            text_educacion.tStart = t  # local t and not account for scr refresh
            text_educacion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_educacion, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_educacion.status = STARTED
            text_educacion.setAutoDraw(True)
        
        # if text_educacion is active this frame...
        if text_educacion.status == STARTED:
            # update params
            pass
        
        # *educacion* updates
        
        # if educacion is starting this frame...
        if educacion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            educacion.frameNStart = frameN  # exact frame index
            educacion.tStart = t  # local t and not account for scr refresh
            educacion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(educacion, 'tStartRefresh')  # time at next scr refresh
            # update status
            educacion.status = STARTED
            educacion.setAutoDraw(True)
        
        # if educacion is active this frame...
        if educacion.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_bio,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_bio.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_bio.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_bio.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_bio" ---
    for thisComponent in blp_bio.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_bio
    blp_bio.tStop = globalClock.getTime(format='float')
    blp_bio.tStopRefresh = tThisFlipGlobal
    thisExp.addData('nombre.text',nombre.text)
    thisExp.addData('edad.text',edad.text)
    thisExp.addData('genero.text',genero.text)
    thisExp.addData('nacimiento.text',nacimiento.text)
    thisExp.addData('vive.text',vive.text)
    thisExp.addData('mama.text',mama.text)
    thisExp.addData('papa.text',papa.text)
    thisExp.addData('educacion.text',educacion.text)
    thisExp.nextEntry()
    # the Routine "blp_bio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_historial_1" ---
    # create an object to store info about Routine blp_historial_1
    blp_historial_1 = data.Routine(
        name='blp_historial_1',
        components=[boton_historial, indicaciones_historial, text_edad_q, edad_aprender_que, text_edad_esp, edad_aprender_esp, text_comodidad_que, edad_comodidad_que, text_comodidad_esp, edad_comodidad_esp, text_clases_que, años_clases_que, text_clases_esp, años_clases_esp],
    )
    blp_historial_1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset boton_historial to account for continued clicks & clear times on/off
    boton_historial.reset()
    edad_aprender_que.reset()
    edad_aprender_esp.reset()
    edad_comodidad_que.reset()
    edad_comodidad_esp.reset()
    años_clases_que.reset()
    años_clases_esp.reset()
    # store start times for blp_historial_1
    blp_historial_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_historial_1.tStart = globalClock.getTime(format='float')
    blp_historial_1.status = STARTED
    blp_historial_1.maxDuration = None
    # keep track of which components have finished
    blp_historial_1Components = blp_historial_1.components
    for thisComponent in blp_historial_1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_historial_1" ---
    thisExp.currentRoutine = blp_historial_1
    blp_historial_1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_historial
        # List of all slider components in this routine
        sliders = [
            edad_aprender_que,
            edad_aprender_esp,
            edad_comodidad_que,
            edad_comodidad_esp,
            años_clases_que,
            años_clases_esp
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_historial.opacity = 1
            boton_historial.color = 'white'
        elif not filled:
            canContinue = False
            boton_historial.opacity = 0.5
            boton_historial.color = 'gray'
        
        # Only allow "Siguiente" to continue if all answered
        if boton_historial.isClicked and canContinue:
            continueRoutine = False
        # *boton_historial* updates
        
        # if boton_historial is starting this frame...
        if boton_historial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_historial.frameNStart = frameN  # exact frame index
            boton_historial.tStart = t  # local t and not account for scr refresh
            boton_historial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_historial, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_historial.status = STARTED
            win.callOnFlip(boton_historial.buttonClock.reset)
            boton_historial.setAutoDraw(True)
        
        # if boton_historial is active this frame...
        if boton_historial.status == STARTED:
            # update params
            pass
            # check whether boton_historial has been pressed
            if boton_historial.isClicked:
                if not boton_historial.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_historial.timesOn.append(boton_historial.buttonClock.getTime())
                    boton_historial.timesOff.append(boton_historial.buttonClock.getTime())
                elif len(boton_historial.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_historial.timesOff[-1] = boton_historial.buttonClock.getTime()
                # run callback code when boton_historial is clicked
                pass
        # take note of whether boton_historial was clicked, so that next frame we know if clicks are new
        boton_historial.wasClicked = boton_historial.isClicked and boton_historial.status == STARTED
        
        # *indicaciones_historial* updates
        
        # if indicaciones_historial is starting this frame...
        if indicaciones_historial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_historial.frameNStart = frameN  # exact frame index
            indicaciones_historial.tStart = t  # local t and not account for scr refresh
            indicaciones_historial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_historial, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_historial.status = STARTED
            indicaciones_historial.setAutoDraw(True)
        
        # if indicaciones_historial is active this frame...
        if indicaciones_historial.status == STARTED:
            # update params
            pass
        
        # *text_edad_q* updates
        
        # if text_edad_q is starting this frame...
        if text_edad_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_edad_q.frameNStart = frameN  # exact frame index
            text_edad_q.tStart = t  # local t and not account for scr refresh
            text_edad_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_edad_q, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_edad_q.status = STARTED
            text_edad_q.setAutoDraw(True)
        
        # if text_edad_q is active this frame...
        if text_edad_q.status == STARTED:
            # update params
            pass
        
        # *edad_aprender_que* updates
        
        # if edad_aprender_que is starting this frame...
        if edad_aprender_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            edad_aprender_que.frameNStart = frameN  # exact frame index
            edad_aprender_que.tStart = t  # local t and not account for scr refresh
            edad_aprender_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edad_aprender_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            edad_aprender_que.status = STARTED
            edad_aprender_que.setAutoDraw(True)
        
        # if edad_aprender_que is active this frame...
        if edad_aprender_que.status == STARTED:
            # update params
            pass
        
        # *text_edad_esp* updates
        
        # if text_edad_esp is starting this frame...
        if text_edad_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_edad_esp.frameNStart = frameN  # exact frame index
            text_edad_esp.tStart = t  # local t and not account for scr refresh
            text_edad_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_edad_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_edad_esp.status = STARTED
            text_edad_esp.setAutoDraw(True)
        
        # if text_edad_esp is active this frame...
        if text_edad_esp.status == STARTED:
            # update params
            pass
        
        # *edad_aprender_esp* updates
        
        # if edad_aprender_esp is starting this frame...
        if edad_aprender_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            edad_aprender_esp.frameNStart = frameN  # exact frame index
            edad_aprender_esp.tStart = t  # local t and not account for scr refresh
            edad_aprender_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edad_aprender_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            edad_aprender_esp.status = STARTED
            edad_aprender_esp.setAutoDraw(True)
        
        # if edad_aprender_esp is active this frame...
        if edad_aprender_esp.status == STARTED:
            # update params
            pass
        
        # *text_comodidad_que* updates
        
        # if text_comodidad_que is starting this frame...
        if text_comodidad_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_comodidad_que.frameNStart = frameN  # exact frame index
            text_comodidad_que.tStart = t  # local t and not account for scr refresh
            text_comodidad_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_comodidad_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_comodidad_que.status = STARTED
            text_comodidad_que.setAutoDraw(True)
        
        # if text_comodidad_que is active this frame...
        if text_comodidad_que.status == STARTED:
            # update params
            pass
        
        # *edad_comodidad_que* updates
        
        # if edad_comodidad_que is starting this frame...
        if edad_comodidad_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            edad_comodidad_que.frameNStart = frameN  # exact frame index
            edad_comodidad_que.tStart = t  # local t and not account for scr refresh
            edad_comodidad_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edad_comodidad_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            edad_comodidad_que.status = STARTED
            edad_comodidad_que.setAutoDraw(True)
        
        # if edad_comodidad_que is active this frame...
        if edad_comodidad_que.status == STARTED:
            # update params
            pass
        
        # *text_comodidad_esp* updates
        
        # if text_comodidad_esp is starting this frame...
        if text_comodidad_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_comodidad_esp.frameNStart = frameN  # exact frame index
            text_comodidad_esp.tStart = t  # local t and not account for scr refresh
            text_comodidad_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_comodidad_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_comodidad_esp.status = STARTED
            text_comodidad_esp.setAutoDraw(True)
        
        # if text_comodidad_esp is active this frame...
        if text_comodidad_esp.status == STARTED:
            # update params
            pass
        
        # *edad_comodidad_esp* updates
        
        # if edad_comodidad_esp is starting this frame...
        if edad_comodidad_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            edad_comodidad_esp.frameNStart = frameN  # exact frame index
            edad_comodidad_esp.tStart = t  # local t and not account for scr refresh
            edad_comodidad_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(edad_comodidad_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            edad_comodidad_esp.status = STARTED
            edad_comodidad_esp.setAutoDraw(True)
        
        # if edad_comodidad_esp is active this frame...
        if edad_comodidad_esp.status == STARTED:
            # update params
            pass
        
        # *text_clases_que* updates
        
        # if text_clases_que is starting this frame...
        if text_clases_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_clases_que.frameNStart = frameN  # exact frame index
            text_clases_que.tStart = t  # local t and not account for scr refresh
            text_clases_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_clases_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_clases_que.status = STARTED
            text_clases_que.setAutoDraw(True)
        
        # if text_clases_que is active this frame...
        if text_clases_que.status == STARTED:
            # update params
            pass
        
        # *años_clases_que* updates
        
        # if años_clases_que is starting this frame...
        if años_clases_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_clases_que.frameNStart = frameN  # exact frame index
            años_clases_que.tStart = t  # local t and not account for scr refresh
            años_clases_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_clases_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_clases_que.status = STARTED
            años_clases_que.setAutoDraw(True)
        
        # if años_clases_que is active this frame...
        if años_clases_que.status == STARTED:
            # update params
            pass
        
        # *text_clases_esp* updates
        
        # if text_clases_esp is starting this frame...
        if text_clases_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_clases_esp.frameNStart = frameN  # exact frame index
            text_clases_esp.tStart = t  # local t and not account for scr refresh
            text_clases_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_clases_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_clases_esp.status = STARTED
            text_clases_esp.setAutoDraw(True)
        
        # if text_clases_esp is active this frame...
        if text_clases_esp.status == STARTED:
            # update params
            pass
        
        # *años_clases_esp* updates
        
        # if años_clases_esp is starting this frame...
        if años_clases_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_clases_esp.frameNStart = frameN  # exact frame index
            años_clases_esp.tStart = t  # local t and not account for scr refresh
            años_clases_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_clases_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_clases_esp.status = STARTED
            años_clases_esp.setAutoDraw(True)
        
        # if años_clases_esp is active this frame...
        if años_clases_esp.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_historial_1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_historial_1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_historial_1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_historial_1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_historial_1" ---
    for thisComponent in blp_historial_1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_historial_1
    blp_historial_1.tStop = globalClock.getTime(format='float')
    blp_historial_1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('edad_aprender_que.response', edad_aprender_que.getRating())
    thisExp.addData('edad_aprender_esp.response', edad_aprender_esp.getRating())
    thisExp.addData('edad_comodidad_que.response', edad_comodidad_que.getRating())
    thisExp.addData('edad_comodidad_esp.response', edad_comodidad_esp.getRating())
    thisExp.addData('años_clases_que.response', años_clases_que.getRating())
    thisExp.addData('años_clases_esp.response', años_clases_esp.getRating())
    thisExp.nextEntry()
    # the Routine "blp_historial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_historial_2" ---
    # create an object to store info about Routine blp_historial_2
    blp_historial_2 = data.Routine(
        name='blp_historial_2',
        components=[boton_historial_2, indicaciones_historial_2, text_comunidad_que, años_comunidad_que, text_comunidad_esp, años_comunidad_esp, text_familia_que, años_familia_que, text_familia_esp, años_familia_esp, text_trabajo_que, años_trabajo_que, text_trabajo_esp, años_trabajo_esp],
    )
    blp_historial_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_historial_2
    # Disable "Siguiente" at start
    canContinue = False
    boton_historial_2.opacity = 0.5
    boton_historial_2.color = 'gray'
    
    # reset boton_historial_2 to account for continued clicks & clear times on/off
    boton_historial_2.reset()
    años_comunidad_que.reset()
    años_comunidad_esp.reset()
    años_familia_que.reset()
    años_familia_esp.reset()
    años_trabajo_que.reset()
    años_trabajo_esp.reset()
    # store start times for blp_historial_2
    blp_historial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_historial_2.tStart = globalClock.getTime(format='float')
    blp_historial_2.status = STARTED
    blp_historial_2.maxDuration = None
    # keep track of which components have finished
    blp_historial_2Components = blp_historial_2.components
    for thisComponent in blp_historial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_historial_2" ---
    thisExp.currentRoutine = blp_historial_2
    blp_historial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_historial_2
        # List of all slider components in this routine
        sliders = [
            años_comunidad_que,
            años_comunidad_esp,
            años_familia_que,
            años_familia_esp,
            años_trabajo_que,
            años_trabajo_esp
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" once all sliders have responses
        if filled and not canContinue:
            canContinue = True
            boton_historial_2.opacity = 1
            boton_historial_2.color = 'white'
        elif not filled:
            canContinue = False
            boton_historial_2.opacity = 0.5
            boton_historial_2.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_historial_2.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_historial_2* updates
        
        # if boton_historial_2 is starting this frame...
        if boton_historial_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_historial_2.frameNStart = frameN  # exact frame index
            boton_historial_2.tStart = t  # local t and not account for scr refresh
            boton_historial_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_historial_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_historial_2.status = STARTED
            win.callOnFlip(boton_historial_2.buttonClock.reset)
            boton_historial_2.setAutoDraw(True)
        
        # if boton_historial_2 is active this frame...
        if boton_historial_2.status == STARTED:
            # update params
            pass
            # check whether boton_historial_2 has been pressed
            if boton_historial_2.isClicked:
                if not boton_historial_2.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_historial_2.timesOn.append(boton_historial_2.buttonClock.getTime())
                    boton_historial_2.timesOff.append(boton_historial_2.buttonClock.getTime())
                elif len(boton_historial_2.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_historial_2.timesOff[-1] = boton_historial_2.buttonClock.getTime()
                # run callback code when boton_historial_2 is clicked
                pass
        # take note of whether boton_historial_2 was clicked, so that next frame we know if clicks are new
        boton_historial_2.wasClicked = boton_historial_2.isClicked and boton_historial_2.status == STARTED
        
        # *indicaciones_historial_2* updates
        
        # if indicaciones_historial_2 is starting this frame...
        if indicaciones_historial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_historial_2.frameNStart = frameN  # exact frame index
            indicaciones_historial_2.tStart = t  # local t and not account for scr refresh
            indicaciones_historial_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_historial_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_historial_2.status = STARTED
            indicaciones_historial_2.setAutoDraw(True)
        
        # if indicaciones_historial_2 is active this frame...
        if indicaciones_historial_2.status == STARTED:
            # update params
            pass
        
        # *text_comunidad_que* updates
        
        # if text_comunidad_que is starting this frame...
        if text_comunidad_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_comunidad_que.frameNStart = frameN  # exact frame index
            text_comunidad_que.tStart = t  # local t and not account for scr refresh
            text_comunidad_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_comunidad_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_comunidad_que.status = STARTED
            text_comunidad_que.setAutoDraw(True)
        
        # if text_comunidad_que is active this frame...
        if text_comunidad_que.status == STARTED:
            # update params
            pass
        
        # *años_comunidad_que* updates
        
        # if años_comunidad_que is starting this frame...
        if años_comunidad_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_comunidad_que.frameNStart = frameN  # exact frame index
            años_comunidad_que.tStart = t  # local t and not account for scr refresh
            años_comunidad_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_comunidad_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_comunidad_que.status = STARTED
            años_comunidad_que.setAutoDraw(True)
        
        # if años_comunidad_que is active this frame...
        if años_comunidad_que.status == STARTED:
            # update params
            pass
        
        # *text_comunidad_esp* updates
        
        # if text_comunidad_esp is starting this frame...
        if text_comunidad_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_comunidad_esp.frameNStart = frameN  # exact frame index
            text_comunidad_esp.tStart = t  # local t and not account for scr refresh
            text_comunidad_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_comunidad_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_comunidad_esp.status = STARTED
            text_comunidad_esp.setAutoDraw(True)
        
        # if text_comunidad_esp is active this frame...
        if text_comunidad_esp.status == STARTED:
            # update params
            pass
        
        # *años_comunidad_esp* updates
        
        # if años_comunidad_esp is starting this frame...
        if años_comunidad_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_comunidad_esp.frameNStart = frameN  # exact frame index
            años_comunidad_esp.tStart = t  # local t and not account for scr refresh
            años_comunidad_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_comunidad_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_comunidad_esp.status = STARTED
            años_comunidad_esp.setAutoDraw(True)
        
        # if años_comunidad_esp is active this frame...
        if años_comunidad_esp.status == STARTED:
            # update params
            pass
        
        # *text_familia_que* updates
        
        # if text_familia_que is starting this frame...
        if text_familia_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_familia_que.frameNStart = frameN  # exact frame index
            text_familia_que.tStart = t  # local t and not account for scr refresh
            text_familia_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_familia_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_familia_que.status = STARTED
            text_familia_que.setAutoDraw(True)
        
        # if text_familia_que is active this frame...
        if text_familia_que.status == STARTED:
            # update params
            pass
        
        # *años_familia_que* updates
        
        # if años_familia_que is starting this frame...
        if años_familia_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_familia_que.frameNStart = frameN  # exact frame index
            años_familia_que.tStart = t  # local t and not account for scr refresh
            años_familia_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_familia_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_familia_que.status = STARTED
            años_familia_que.setAutoDraw(True)
        
        # if años_familia_que is active this frame...
        if años_familia_que.status == STARTED:
            # update params
            pass
        
        # *text_familia_esp* updates
        
        # if text_familia_esp is starting this frame...
        if text_familia_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_familia_esp.frameNStart = frameN  # exact frame index
            text_familia_esp.tStart = t  # local t and not account for scr refresh
            text_familia_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_familia_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_familia_esp.status = STARTED
            text_familia_esp.setAutoDraw(True)
        
        # if text_familia_esp is active this frame...
        if text_familia_esp.status == STARTED:
            # update params
            pass
        
        # *años_familia_esp* updates
        
        # if años_familia_esp is starting this frame...
        if años_familia_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_familia_esp.frameNStart = frameN  # exact frame index
            años_familia_esp.tStart = t  # local t and not account for scr refresh
            años_familia_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_familia_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_familia_esp.status = STARTED
            años_familia_esp.setAutoDraw(True)
        
        # if años_familia_esp is active this frame...
        if años_familia_esp.status == STARTED:
            # update params
            pass
        
        # *text_trabajo_que* updates
        
        # if text_trabajo_que is starting this frame...
        if text_trabajo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_trabajo_que.frameNStart = frameN  # exact frame index
            text_trabajo_que.tStart = t  # local t and not account for scr refresh
            text_trabajo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_trabajo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_trabajo_que.status = STARTED
            text_trabajo_que.setAutoDraw(True)
        
        # if text_trabajo_que is active this frame...
        if text_trabajo_que.status == STARTED:
            # update params
            pass
        
        # *años_trabajo_que* updates
        
        # if años_trabajo_que is starting this frame...
        if años_trabajo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_trabajo_que.frameNStart = frameN  # exact frame index
            años_trabajo_que.tStart = t  # local t and not account for scr refresh
            años_trabajo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_trabajo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_trabajo_que.status = STARTED
            años_trabajo_que.setAutoDraw(True)
        
        # if años_trabajo_que is active this frame...
        if años_trabajo_que.status == STARTED:
            # update params
            pass
        
        # *text_trabajo_esp* updates
        
        # if text_trabajo_esp is starting this frame...
        if text_trabajo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_trabajo_esp.frameNStart = frameN  # exact frame index
            text_trabajo_esp.tStart = t  # local t and not account for scr refresh
            text_trabajo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_trabajo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_trabajo_esp.status = STARTED
            text_trabajo_esp.setAutoDraw(True)
        
        # if text_trabajo_esp is active this frame...
        if text_trabajo_esp.status == STARTED:
            # update params
            pass
        
        # *años_trabajo_esp* updates
        
        # if años_trabajo_esp is starting this frame...
        if años_trabajo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            años_trabajo_esp.frameNStart = frameN  # exact frame index
            años_trabajo_esp.tStart = t  # local t and not account for scr refresh
            años_trabajo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(años_trabajo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            años_trabajo_esp.status = STARTED
            años_trabajo_esp.setAutoDraw(True)
        
        # if años_trabajo_esp is active this frame...
        if años_trabajo_esp.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_historial_2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_historial_2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_historial_2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_historial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_historial_2" ---
    for thisComponent in blp_historial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_historial_2
    blp_historial_2.tStop = globalClock.getTime(format='float')
    blp_historial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('años_comunidad_que.response', años_comunidad_que.getRating())
    thisExp.addData('años_comunidad_esp.response', años_comunidad_esp.getRating())
    thisExp.addData('años_familia_que.response', años_familia_que.getRating())
    thisExp.addData('años_familia_esp.response', años_familia_esp.getRating())
    thisExp.addData('años_trabajo_que.response', años_trabajo_que.getRating())
    thisExp.addData('años_trabajo_esp.response', años_trabajo_esp.getRating())
    thisExp.nextEntry()
    # the Routine "blp_historial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_uso_1" ---
    # create an object to store info about Routine blp_uso_1
    blp_uso_1 = data.Routine(
        name='blp_uso_1',
        components=[boton_uso, indicaciones_uso, text_amigos_que, porc_amigos_que, text_amigos_esp, porc_amigos_esp, text_amigos_otr, porc_amigos_otr, porcent_familia_que, porc_familia_que, porcent_familia_esp, porc_familia_esp, porcent_familia_otr, porc_familia_otr],
    )
    blp_uso_1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_uso
    # Disable "Siguiente" at start
    canContinue = False
    boton_uso.opacity = 0.5
    boton_uso.color = 'gray'
    
    # reset boton_uso to account for continued clicks & clear times on/off
    boton_uso.reset()
    porc_amigos_que.reset()
    porc_amigos_esp.reset()
    porc_amigos_otr.reset()
    porc_familia_que.reset()
    porc_familia_esp.reset()
    porc_familia_otr.reset()
    # store start times for blp_uso_1
    blp_uso_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_uso_1.tStart = globalClock.getTime(format='float')
    blp_uso_1.status = STARTED
    blp_uso_1.maxDuration = None
    # keep track of which components have finished
    blp_uso_1Components = blp_uso_1.components
    for thisComponent in blp_uso_1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_uso_1" ---
    thisExp.currentRoutine = blp_uso_1
    blp_uso_1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_uso
        # List of all slider components in this routine
        sliders = [
            porc_amigos_que,
            porc_amigos_esp,
            porc_amigos_otr,
            porc_familia_que,
            porc_familia_esp,
            porc_familia_otr
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_uso.opacity = 1
            boton_uso.color = 'white'
        elif not filled:
            canContinue = False
            boton_uso.opacity = 0.5
            boton_uso.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_uso.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_uso* updates
        
        # if boton_uso is starting this frame...
        if boton_uso.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_uso.frameNStart = frameN  # exact frame index
            boton_uso.tStart = t  # local t and not account for scr refresh
            boton_uso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_uso, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_uso.status = STARTED
            win.callOnFlip(boton_uso.buttonClock.reset)
            boton_uso.setAutoDraw(True)
        
        # if boton_uso is active this frame...
        if boton_uso.status == STARTED:
            # update params
            pass
            # check whether boton_uso has been pressed
            if boton_uso.isClicked:
                if not boton_uso.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_uso.timesOn.append(boton_uso.buttonClock.getTime())
                    boton_uso.timesOff.append(boton_uso.buttonClock.getTime())
                elif len(boton_uso.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_uso.timesOff[-1] = boton_uso.buttonClock.getTime()
                # run callback code when boton_uso is clicked
                pass
        # take note of whether boton_uso was clicked, so that next frame we know if clicks are new
        boton_uso.wasClicked = boton_uso.isClicked and boton_uso.status == STARTED
        
        # *indicaciones_uso* updates
        
        # if indicaciones_uso is starting this frame...
        if indicaciones_uso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_uso.frameNStart = frameN  # exact frame index
            indicaciones_uso.tStart = t  # local t and not account for scr refresh
            indicaciones_uso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_uso, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_uso.status = STARTED
            indicaciones_uso.setAutoDraw(True)
        
        # if indicaciones_uso is active this frame...
        if indicaciones_uso.status == STARTED:
            # update params
            pass
        
        # *text_amigos_que* updates
        
        # if text_amigos_que is starting this frame...
        if text_amigos_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_amigos_que.frameNStart = frameN  # exact frame index
            text_amigos_que.tStart = t  # local t and not account for scr refresh
            text_amigos_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_amigos_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_amigos_que.status = STARTED
            text_amigos_que.setAutoDraw(True)
        
        # if text_amigos_que is active this frame...
        if text_amigos_que.status == STARTED:
            # update params
            pass
        
        # *porc_amigos_que* updates
        
        # if porc_amigos_que is starting this frame...
        if porc_amigos_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_amigos_que.frameNStart = frameN  # exact frame index
            porc_amigos_que.tStart = t  # local t and not account for scr refresh
            porc_amigos_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_amigos_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_amigos_que.status = STARTED
            porc_amigos_que.setAutoDraw(True)
        
        # if porc_amigos_que is active this frame...
        if porc_amigos_que.status == STARTED:
            # update params
            pass
        
        # *text_amigos_esp* updates
        
        # if text_amigos_esp is starting this frame...
        if text_amigos_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_amigos_esp.frameNStart = frameN  # exact frame index
            text_amigos_esp.tStart = t  # local t and not account for scr refresh
            text_amigos_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_amigos_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_amigos_esp.status = STARTED
            text_amigos_esp.setAutoDraw(True)
        
        # if text_amigos_esp is active this frame...
        if text_amigos_esp.status == STARTED:
            # update params
            pass
        
        # *porc_amigos_esp* updates
        
        # if porc_amigos_esp is starting this frame...
        if porc_amigos_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_amigos_esp.frameNStart = frameN  # exact frame index
            porc_amigos_esp.tStart = t  # local t and not account for scr refresh
            porc_amigos_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_amigos_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_amigos_esp.status = STARTED
            porc_amigos_esp.setAutoDraw(True)
        
        # if porc_amigos_esp is active this frame...
        if porc_amigos_esp.status == STARTED:
            # update params
            pass
        
        # *text_amigos_otr* updates
        
        # if text_amigos_otr is starting this frame...
        if text_amigos_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_amigos_otr.frameNStart = frameN  # exact frame index
            text_amigos_otr.tStart = t  # local t and not account for scr refresh
            text_amigos_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_amigos_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_amigos_otr.status = STARTED
            text_amigos_otr.setAutoDraw(True)
        
        # if text_amigos_otr is active this frame...
        if text_amigos_otr.status == STARTED:
            # update params
            pass
        
        # *porc_amigos_otr* updates
        
        # if porc_amigos_otr is starting this frame...
        if porc_amigos_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_amigos_otr.frameNStart = frameN  # exact frame index
            porc_amigos_otr.tStart = t  # local t and not account for scr refresh
            porc_amigos_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_amigos_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_amigos_otr.status = STARTED
            porc_amigos_otr.setAutoDraw(True)
        
        # if porc_amigos_otr is active this frame...
        if porc_amigos_otr.status == STARTED:
            # update params
            pass
        
        # *porcent_familia_que* updates
        
        # if porcent_familia_que is starting this frame...
        if porcent_familia_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porcent_familia_que.frameNStart = frameN  # exact frame index
            porcent_familia_que.tStart = t  # local t and not account for scr refresh
            porcent_familia_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porcent_familia_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porcent_familia_que.status = STARTED
            porcent_familia_que.setAutoDraw(True)
        
        # if porcent_familia_que is active this frame...
        if porcent_familia_que.status == STARTED:
            # update params
            pass
        
        # *porc_familia_que* updates
        
        # if porc_familia_que is starting this frame...
        if porc_familia_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_familia_que.frameNStart = frameN  # exact frame index
            porc_familia_que.tStart = t  # local t and not account for scr refresh
            porc_familia_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_familia_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_familia_que.status = STARTED
            porc_familia_que.setAutoDraw(True)
        
        # if porc_familia_que is active this frame...
        if porc_familia_que.status == STARTED:
            # update params
            pass
        
        # *porcent_familia_esp* updates
        
        # if porcent_familia_esp is starting this frame...
        if porcent_familia_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porcent_familia_esp.frameNStart = frameN  # exact frame index
            porcent_familia_esp.tStart = t  # local t and not account for scr refresh
            porcent_familia_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porcent_familia_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porcent_familia_esp.status = STARTED
            porcent_familia_esp.setAutoDraw(True)
        
        # if porcent_familia_esp is active this frame...
        if porcent_familia_esp.status == STARTED:
            # update params
            pass
        
        # *porc_familia_esp* updates
        
        # if porc_familia_esp is starting this frame...
        if porc_familia_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_familia_esp.frameNStart = frameN  # exact frame index
            porc_familia_esp.tStart = t  # local t and not account for scr refresh
            porc_familia_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_familia_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_familia_esp.status = STARTED
            porc_familia_esp.setAutoDraw(True)
        
        # if porc_familia_esp is active this frame...
        if porc_familia_esp.status == STARTED:
            # update params
            pass
        
        # *porcent_familia_otr* updates
        
        # if porcent_familia_otr is starting this frame...
        if porcent_familia_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porcent_familia_otr.frameNStart = frameN  # exact frame index
            porcent_familia_otr.tStart = t  # local t and not account for scr refresh
            porcent_familia_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porcent_familia_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porcent_familia_otr.status = STARTED
            porcent_familia_otr.setAutoDraw(True)
        
        # if porcent_familia_otr is active this frame...
        if porcent_familia_otr.status == STARTED:
            # update params
            pass
        
        # *porc_familia_otr* updates
        
        # if porc_familia_otr is starting this frame...
        if porc_familia_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_familia_otr.frameNStart = frameN  # exact frame index
            porc_familia_otr.tStart = t  # local t and not account for scr refresh
            porc_familia_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_familia_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_familia_otr.status = STARTED
            porc_familia_otr.setAutoDraw(True)
        
        # if porc_familia_otr is active this frame...
        if porc_familia_otr.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_uso_1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_uso_1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_uso_1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_uso_1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_uso_1" ---
    for thisComponent in blp_uso_1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_uso_1
    blp_uso_1.tStop = globalClock.getTime(format='float')
    blp_uso_1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('porc_amigos_que.response', porc_amigos_que.getRating())
    thisExp.addData('porc_amigos_esp.response', porc_amigos_esp.getRating())
    thisExp.addData('porc_amigos_otr.response', porc_amigos_otr.getRating())
    thisExp.addData('porc_familia_que.response', porc_familia_que.getRating())
    thisExp.addData('porc_familia_esp.response', porc_familia_esp.getRating())
    thisExp.addData('porc_familia_otr.response', porc_familia_otr.getRating())
    thisExp.nextEntry()
    # the Routine "blp_uso_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_uso_2" ---
    # create an object to store info about Routine blp_uso_2
    blp_uso_2 = data.Routine(
        name='blp_uso_2',
        components=[boton_uso_2, indicaciones_uso_2, text_formal_que, porc_formal_que, text_formal_esp, porc_formal_esp, text_formal_otr, porc_formal_otr, porct_trabajo_que, porc_trabajo_que, porct_trabajo_esp, porc_trabajo_esp, porct_trabajo_otr, porc_trabajo_otr],
    )
    blp_uso_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_uso_2
    # Disable "Siguiente" at start
    canContinue = False
    boton_uso_2.opacity = 0.5
    boton_uso_2.color = 'gray'
    
    # reset boton_uso_2 to account for continued clicks & clear times on/off
    boton_uso_2.reset()
    porc_formal_que.reset()
    porc_formal_esp.reset()
    porc_formal_otr.reset()
    porc_trabajo_que.reset()
    porc_trabajo_esp.reset()
    porc_trabajo_otr.reset()
    # store start times for blp_uso_2
    blp_uso_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_uso_2.tStart = globalClock.getTime(format='float')
    blp_uso_2.status = STARTED
    blp_uso_2.maxDuration = None
    # keep track of which components have finished
    blp_uso_2Components = blp_uso_2.components
    for thisComponent in blp_uso_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_uso_2" ---
    thisExp.currentRoutine = blp_uso_2
    blp_uso_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_uso_2
        # List of all slider components in this routine
        sliders = [
            porc_formal_que,
            porc_formal_esp,
            porc_formal_otr,
            porc_trabajo_que,
            porc_trabajo_esp,
            porc_trabajo_otr
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_uso_2.opacity = 1
            boton_uso_2.color = 'white'
        elif not filled:
            canContinue = False
            boton_uso_2.opacity = 0.5
            boton_uso_2.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_uso_2.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_uso_2* updates
        
        # if boton_uso_2 is starting this frame...
        if boton_uso_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_uso_2.frameNStart = frameN  # exact frame index
            boton_uso_2.tStart = t  # local t and not account for scr refresh
            boton_uso_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_uso_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_uso_2.status = STARTED
            win.callOnFlip(boton_uso_2.buttonClock.reset)
            boton_uso_2.setAutoDraw(True)
        
        # if boton_uso_2 is active this frame...
        if boton_uso_2.status == STARTED:
            # update params
            pass
            # check whether boton_uso_2 has been pressed
            if boton_uso_2.isClicked:
                if not boton_uso_2.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_uso_2.timesOn.append(boton_uso_2.buttonClock.getTime())
                    boton_uso_2.timesOff.append(boton_uso_2.buttonClock.getTime())
                elif len(boton_uso_2.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_uso_2.timesOff[-1] = boton_uso_2.buttonClock.getTime()
                # run callback code when boton_uso_2 is clicked
                pass
        # take note of whether boton_uso_2 was clicked, so that next frame we know if clicks are new
        boton_uso_2.wasClicked = boton_uso_2.isClicked and boton_uso_2.status == STARTED
        
        # *indicaciones_uso_2* updates
        
        # if indicaciones_uso_2 is starting this frame...
        if indicaciones_uso_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_uso_2.frameNStart = frameN  # exact frame index
            indicaciones_uso_2.tStart = t  # local t and not account for scr refresh
            indicaciones_uso_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_uso_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_uso_2.status = STARTED
            indicaciones_uso_2.setAutoDraw(True)
        
        # if indicaciones_uso_2 is active this frame...
        if indicaciones_uso_2.status == STARTED:
            # update params
            pass
        
        # *text_formal_que* updates
        
        # if text_formal_que is starting this frame...
        if text_formal_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_formal_que.frameNStart = frameN  # exact frame index
            text_formal_que.tStart = t  # local t and not account for scr refresh
            text_formal_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_formal_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_formal_que.status = STARTED
            text_formal_que.setAutoDraw(True)
        
        # if text_formal_que is active this frame...
        if text_formal_que.status == STARTED:
            # update params
            pass
        
        # *porc_formal_que* updates
        
        # if porc_formal_que is starting this frame...
        if porc_formal_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_formal_que.frameNStart = frameN  # exact frame index
            porc_formal_que.tStart = t  # local t and not account for scr refresh
            porc_formal_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_formal_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_formal_que.status = STARTED
            porc_formal_que.setAutoDraw(True)
        
        # if porc_formal_que is active this frame...
        if porc_formal_que.status == STARTED:
            # update params
            pass
        
        # *text_formal_esp* updates
        
        # if text_formal_esp is starting this frame...
        if text_formal_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_formal_esp.frameNStart = frameN  # exact frame index
            text_formal_esp.tStart = t  # local t and not account for scr refresh
            text_formal_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_formal_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_formal_esp.status = STARTED
            text_formal_esp.setAutoDraw(True)
        
        # if text_formal_esp is active this frame...
        if text_formal_esp.status == STARTED:
            # update params
            pass
        
        # *porc_formal_esp* updates
        
        # if porc_formal_esp is starting this frame...
        if porc_formal_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_formal_esp.frameNStart = frameN  # exact frame index
            porc_formal_esp.tStart = t  # local t and not account for scr refresh
            porc_formal_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_formal_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_formal_esp.status = STARTED
            porc_formal_esp.setAutoDraw(True)
        
        # if porc_formal_esp is active this frame...
        if porc_formal_esp.status == STARTED:
            # update params
            pass
        
        # *text_formal_otr* updates
        
        # if text_formal_otr is starting this frame...
        if text_formal_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_formal_otr.frameNStart = frameN  # exact frame index
            text_formal_otr.tStart = t  # local t and not account for scr refresh
            text_formal_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_formal_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_formal_otr.status = STARTED
            text_formal_otr.setAutoDraw(True)
        
        # if text_formal_otr is active this frame...
        if text_formal_otr.status == STARTED:
            # update params
            pass
        
        # *porc_formal_otr* updates
        
        # if porc_formal_otr is starting this frame...
        if porc_formal_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_formal_otr.frameNStart = frameN  # exact frame index
            porc_formal_otr.tStart = t  # local t and not account for scr refresh
            porc_formal_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_formal_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_formal_otr.status = STARTED
            porc_formal_otr.setAutoDraw(True)
        
        # if porc_formal_otr is active this frame...
        if porc_formal_otr.status == STARTED:
            # update params
            pass
        
        # *porct_trabajo_que* updates
        
        # if porct_trabajo_que is starting this frame...
        if porct_trabajo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porct_trabajo_que.frameNStart = frameN  # exact frame index
            porct_trabajo_que.tStart = t  # local t and not account for scr refresh
            porct_trabajo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porct_trabajo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porct_trabajo_que.status = STARTED
            porct_trabajo_que.setAutoDraw(True)
        
        # if porct_trabajo_que is active this frame...
        if porct_trabajo_que.status == STARTED:
            # update params
            pass
        
        # *porc_trabajo_que* updates
        
        # if porc_trabajo_que is starting this frame...
        if porc_trabajo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_trabajo_que.frameNStart = frameN  # exact frame index
            porc_trabajo_que.tStart = t  # local t and not account for scr refresh
            porc_trabajo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_trabajo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_trabajo_que.status = STARTED
            porc_trabajo_que.setAutoDraw(True)
        
        # if porc_trabajo_que is active this frame...
        if porc_trabajo_que.status == STARTED:
            # update params
            pass
        
        # *porct_trabajo_esp* updates
        
        # if porct_trabajo_esp is starting this frame...
        if porct_trabajo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porct_trabajo_esp.frameNStart = frameN  # exact frame index
            porct_trabajo_esp.tStart = t  # local t and not account for scr refresh
            porct_trabajo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porct_trabajo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porct_trabajo_esp.status = STARTED
            porct_trabajo_esp.setAutoDraw(True)
        
        # if porct_trabajo_esp is active this frame...
        if porct_trabajo_esp.status == STARTED:
            # update params
            pass
        
        # *porc_trabajo_esp* updates
        
        # if porc_trabajo_esp is starting this frame...
        if porc_trabajo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_trabajo_esp.frameNStart = frameN  # exact frame index
            porc_trabajo_esp.tStart = t  # local t and not account for scr refresh
            porc_trabajo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_trabajo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_trabajo_esp.status = STARTED
            porc_trabajo_esp.setAutoDraw(True)
        
        # if porc_trabajo_esp is active this frame...
        if porc_trabajo_esp.status == STARTED:
            # update params
            pass
        
        # *porct_trabajo_otr* updates
        
        # if porct_trabajo_otr is starting this frame...
        if porct_trabajo_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porct_trabajo_otr.frameNStart = frameN  # exact frame index
            porct_trabajo_otr.tStart = t  # local t and not account for scr refresh
            porct_trabajo_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porct_trabajo_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porct_trabajo_otr.status = STARTED
            porct_trabajo_otr.setAutoDraw(True)
        
        # if porct_trabajo_otr is active this frame...
        if porct_trabajo_otr.status == STARTED:
            # update params
            pass
        
        # *porc_trabajo_otr* updates
        
        # if porc_trabajo_otr is starting this frame...
        if porc_trabajo_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_trabajo_otr.frameNStart = frameN  # exact frame index
            porc_trabajo_otr.tStart = t  # local t and not account for scr refresh
            porc_trabajo_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_trabajo_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_trabajo_otr.status = STARTED
            porc_trabajo_otr.setAutoDraw(True)
        
        # if porc_trabajo_otr is active this frame...
        if porc_trabajo_otr.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_uso_2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_uso_2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_uso_2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_uso_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_uso_2" ---
    for thisComponent in blp_uso_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_uso_2
    blp_uso_2.tStop = globalClock.getTime(format='float')
    blp_uso_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('porc_formal_que.response', porc_formal_que.getRating())
    thisExp.addData('porc_formal_esp.response', porc_formal_esp.getRating())
    thisExp.addData('porc_formal_otr.response', porc_formal_otr.getRating())
    thisExp.addData('porc_trabajo_que.response', porc_trabajo_que.getRating())
    thisExp.addData('porc_trabajo_esp.response', porc_trabajo_esp.getRating())
    thisExp.addData('porc_trabajo_otr.response', porc_trabajo_otr.getRating())
    thisExp.nextEntry()
    # the Routine "blp_uso_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_uso_3" ---
    # create an object to store info about Routine blp_uso_3
    blp_uso_3 = data.Routine(
        name='blp_uso_3',
        components=[boton_uso_3, indicaciones_uso_3, text_mismo_que, porc_mismo_que, text_mismo_esp, porc_mismo_esp, text_mismo_otr, porc_mismo_otr, text_calculos_que, porc_calculos_que, text_calculos_esp, porc_calculos_esp, text_calculos_otr, porc_calculos_otr],
    )
    blp_uso_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_uso_3
    # Disable "Siguiente" at start
    canContinue = False
    boton_uso_3.opacity = 0.5
    boton_uso_3.color = 'gray'
    
    # reset boton_uso_3 to account for continued clicks & clear times on/off
    boton_uso_3.reset()
    porc_mismo_que.reset()
    porc_mismo_esp.reset()
    porc_mismo_otr.reset()
    porc_calculos_que.reset()
    porc_calculos_esp.reset()
    porc_calculos_otr.reset()
    # store start times for blp_uso_3
    blp_uso_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_uso_3.tStart = globalClock.getTime(format='float')
    blp_uso_3.status = STARTED
    blp_uso_3.maxDuration = None
    # keep track of which components have finished
    blp_uso_3Components = blp_uso_3.components
    for thisComponent in blp_uso_3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_uso_3" ---
    thisExp.currentRoutine = blp_uso_3
    blp_uso_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_uso_3
        # List of all slider components in this routine
        sliders = [
            porc_mismo_que,
            porc_mismo_esp,
            porc_mismo_otr,
            porc_calculos_que,
            porc_calculos_esp,
            porc_calculos_otr
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_uso_3.opacity = 1
            boton_uso_3.color = 'white'
        elif not filled:
            canContinue = False
            boton_uso_3.opacity = 0.5
            boton_uso_3.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_uso_3.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_uso_3* updates
        
        # if boton_uso_3 is starting this frame...
        if boton_uso_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_uso_3.frameNStart = frameN  # exact frame index
            boton_uso_3.tStart = t  # local t and not account for scr refresh
            boton_uso_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_uso_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_uso_3.status = STARTED
            win.callOnFlip(boton_uso_3.buttonClock.reset)
            boton_uso_3.setAutoDraw(True)
        
        # if boton_uso_3 is active this frame...
        if boton_uso_3.status == STARTED:
            # update params
            pass
            # check whether boton_uso_3 has been pressed
            if boton_uso_3.isClicked:
                if not boton_uso_3.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_uso_3.timesOn.append(boton_uso_3.buttonClock.getTime())
                    boton_uso_3.timesOff.append(boton_uso_3.buttonClock.getTime())
                elif len(boton_uso_3.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_uso_3.timesOff[-1] = boton_uso_3.buttonClock.getTime()
                # run callback code when boton_uso_3 is clicked
                pass
        # take note of whether boton_uso_3 was clicked, so that next frame we know if clicks are new
        boton_uso_3.wasClicked = boton_uso_3.isClicked and boton_uso_3.status == STARTED
        
        # *indicaciones_uso_3* updates
        
        # if indicaciones_uso_3 is starting this frame...
        if indicaciones_uso_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_uso_3.frameNStart = frameN  # exact frame index
            indicaciones_uso_3.tStart = t  # local t and not account for scr refresh
            indicaciones_uso_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_uso_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_uso_3.status = STARTED
            indicaciones_uso_3.setAutoDraw(True)
        
        # if indicaciones_uso_3 is active this frame...
        if indicaciones_uso_3.status == STARTED:
            # update params
            pass
        
        # *text_mismo_que* updates
        
        # if text_mismo_que is starting this frame...
        if text_mismo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mismo_que.frameNStart = frameN  # exact frame index
            text_mismo_que.tStart = t  # local t and not account for scr refresh
            text_mismo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mismo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_mismo_que.status = STARTED
            text_mismo_que.setAutoDraw(True)
        
        # if text_mismo_que is active this frame...
        if text_mismo_que.status == STARTED:
            # update params
            pass
        
        # *porc_mismo_que* updates
        
        # if porc_mismo_que is starting this frame...
        if porc_mismo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_mismo_que.frameNStart = frameN  # exact frame index
            porc_mismo_que.tStart = t  # local t and not account for scr refresh
            porc_mismo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_mismo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_mismo_que.status = STARTED
            porc_mismo_que.setAutoDraw(True)
        
        # if porc_mismo_que is active this frame...
        if porc_mismo_que.status == STARTED:
            # update params
            pass
        
        # *text_mismo_esp* updates
        
        # if text_mismo_esp is starting this frame...
        if text_mismo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mismo_esp.frameNStart = frameN  # exact frame index
            text_mismo_esp.tStart = t  # local t and not account for scr refresh
            text_mismo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mismo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_mismo_esp.status = STARTED
            text_mismo_esp.setAutoDraw(True)
        
        # if text_mismo_esp is active this frame...
        if text_mismo_esp.status == STARTED:
            # update params
            pass
        
        # *porc_mismo_esp* updates
        
        # if porc_mismo_esp is starting this frame...
        if porc_mismo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_mismo_esp.frameNStart = frameN  # exact frame index
            porc_mismo_esp.tStart = t  # local t and not account for scr refresh
            porc_mismo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_mismo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_mismo_esp.status = STARTED
            porc_mismo_esp.setAutoDraw(True)
        
        # if porc_mismo_esp is active this frame...
        if porc_mismo_esp.status == STARTED:
            # update params
            pass
        
        # *text_mismo_otr* updates
        
        # if text_mismo_otr is starting this frame...
        if text_mismo_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mismo_otr.frameNStart = frameN  # exact frame index
            text_mismo_otr.tStart = t  # local t and not account for scr refresh
            text_mismo_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mismo_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_mismo_otr.status = STARTED
            text_mismo_otr.setAutoDraw(True)
        
        # if text_mismo_otr is active this frame...
        if text_mismo_otr.status == STARTED:
            # update params
            pass
        
        # *porc_mismo_otr* updates
        
        # if porc_mismo_otr is starting this frame...
        if porc_mismo_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_mismo_otr.frameNStart = frameN  # exact frame index
            porc_mismo_otr.tStart = t  # local t and not account for scr refresh
            porc_mismo_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_mismo_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_mismo_otr.status = STARTED
            porc_mismo_otr.setAutoDraw(True)
        
        # if porc_mismo_otr is active this frame...
        if porc_mismo_otr.status == STARTED:
            # update params
            pass
        
        # *text_calculos_que* updates
        
        # if text_calculos_que is starting this frame...
        if text_calculos_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_calculos_que.frameNStart = frameN  # exact frame index
            text_calculos_que.tStart = t  # local t and not account for scr refresh
            text_calculos_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_calculos_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_calculos_que.status = STARTED
            text_calculos_que.setAutoDraw(True)
        
        # if text_calculos_que is active this frame...
        if text_calculos_que.status == STARTED:
            # update params
            pass
        
        # *porc_calculos_que* updates
        
        # if porc_calculos_que is starting this frame...
        if porc_calculos_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_calculos_que.frameNStart = frameN  # exact frame index
            porc_calculos_que.tStart = t  # local t and not account for scr refresh
            porc_calculos_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_calculos_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_calculos_que.status = STARTED
            porc_calculos_que.setAutoDraw(True)
        
        # if porc_calculos_que is active this frame...
        if porc_calculos_que.status == STARTED:
            # update params
            pass
        
        # *text_calculos_esp* updates
        
        # if text_calculos_esp is starting this frame...
        if text_calculos_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_calculos_esp.frameNStart = frameN  # exact frame index
            text_calculos_esp.tStart = t  # local t and not account for scr refresh
            text_calculos_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_calculos_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_calculos_esp.status = STARTED
            text_calculos_esp.setAutoDraw(True)
        
        # if text_calculos_esp is active this frame...
        if text_calculos_esp.status == STARTED:
            # update params
            pass
        
        # *porc_calculos_esp* updates
        
        # if porc_calculos_esp is starting this frame...
        if porc_calculos_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_calculos_esp.frameNStart = frameN  # exact frame index
            porc_calculos_esp.tStart = t  # local t and not account for scr refresh
            porc_calculos_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_calculos_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_calculos_esp.status = STARTED
            porc_calculos_esp.setAutoDraw(True)
        
        # if porc_calculos_esp is active this frame...
        if porc_calculos_esp.status == STARTED:
            # update params
            pass
        
        # *text_calculos_otr* updates
        
        # if text_calculos_otr is starting this frame...
        if text_calculos_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_calculos_otr.frameNStart = frameN  # exact frame index
            text_calculos_otr.tStart = t  # local t and not account for scr refresh
            text_calculos_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_calculos_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_calculos_otr.status = STARTED
            text_calculos_otr.setAutoDraw(True)
        
        # if text_calculos_otr is active this frame...
        if text_calculos_otr.status == STARTED:
            # update params
            pass
        
        # *porc_calculos_otr* updates
        
        # if porc_calculos_otr is starting this frame...
        if porc_calculos_otr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            porc_calculos_otr.frameNStart = frameN  # exact frame index
            porc_calculos_otr.tStart = t  # local t and not account for scr refresh
            porc_calculos_otr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(porc_calculos_otr, 'tStartRefresh')  # time at next scr refresh
            # update status
            porc_calculos_otr.status = STARTED
            porc_calculos_otr.setAutoDraw(True)
        
        # if porc_calculos_otr is active this frame...
        if porc_calculos_otr.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_uso_3,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_uso_3.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_uso_3.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_uso_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_uso_3" ---
    for thisComponent in blp_uso_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_uso_3
    blp_uso_3.tStop = globalClock.getTime(format='float')
    blp_uso_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('porc_mismo_que.response', porc_mismo_que.getRating())
    thisExp.addData('porc_mismo_esp.response', porc_mismo_esp.getRating())
    thisExp.addData('porc_mismo_otr.response', porc_mismo_otr.getRating())
    thisExp.addData('porc_calculos_que.response', porc_calculos_que.getRating())
    thisExp.addData('porc_calculos_esp.response', porc_calculos_esp.getRating())
    thisExp.addData('porc_calculos_otr.response', porc_calculos_otr.getRating())
    thisExp.nextEntry()
    # the Routine "blp_uso_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_competencia" ---
    # create an object to store info about Routine blp_competencia
    blp_competencia = data.Routine(
        name='blp_competencia',
        components=[boton_competencia, indicaciones_competencia, text_habla_que, habla_bien_que, text_habla_esp, habla_bien_esp, text_entiende_que, entiende_bien_que, text_entiende_esp, entiende_bien_esp, text_lee_que, lee_bien_que, text_lee_esp, lee_bien_esp, text_escribe_que, escribe_bien_que, text_escribe_esp, escribe_bien_esp],
    )
    blp_competencia.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_competencia
    # Disable "Siguiente" at start
    canContinue = False
    boton_competencia.opacity = 0.5
    boton_competencia.color = 'gray'
    
    # reset boton_competencia to account for continued clicks & clear times on/off
    boton_competencia.reset()
    habla_bien_que.reset()
    habla_bien_esp.reset()
    entiende_bien_que.reset()
    entiende_bien_esp.reset()
    lee_bien_que.reset()
    lee_bien_esp.reset()
    escribe_bien_que.reset()
    escribe_bien_esp.reset()
    # store start times for blp_competencia
    blp_competencia.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_competencia.tStart = globalClock.getTime(format='float')
    blp_competencia.status = STARTED
    blp_competencia.maxDuration = None
    # keep track of which components have finished
    blp_competenciaComponents = blp_competencia.components
    for thisComponent in blp_competencia.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_competencia" ---
    thisExp.currentRoutine = blp_competencia
    blp_competencia.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_competencia
        # List of all slider components in this routine
        sliders = [
            habla_bien_que,
            habla_bien_esp,
            entiende_bien_que,
            entiende_bien_esp,
            lee_bien_que,
            lee_bien_esp,
            escribe_bien_que,
            escribe_bien_esp
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_competencia.opacity = 1
            boton_competencia.color = 'white'
        elif not filled:
            canContinue = False
            boton_competencia.opacity = 0.5
            boton_competencia.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_competencia.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_competencia* updates
        
        # if boton_competencia is starting this frame...
        if boton_competencia.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_competencia.frameNStart = frameN  # exact frame index
            boton_competencia.tStart = t  # local t and not account for scr refresh
            boton_competencia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_competencia, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_competencia.status = STARTED
            win.callOnFlip(boton_competencia.buttonClock.reset)
            boton_competencia.setAutoDraw(True)
        
        # if boton_competencia is active this frame...
        if boton_competencia.status == STARTED:
            # update params
            pass
            # check whether boton_competencia has been pressed
            if boton_competencia.isClicked:
                if not boton_competencia.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_competencia.timesOn.append(boton_competencia.buttonClock.getTime())
                    boton_competencia.timesOff.append(boton_competencia.buttonClock.getTime())
                elif len(boton_competencia.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_competencia.timesOff[-1] = boton_competencia.buttonClock.getTime()
                # run callback code when boton_competencia is clicked
                pass
        # take note of whether boton_competencia was clicked, so that next frame we know if clicks are new
        boton_competencia.wasClicked = boton_competencia.isClicked and boton_competencia.status == STARTED
        
        # *indicaciones_competencia* updates
        
        # if indicaciones_competencia is starting this frame...
        if indicaciones_competencia.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_competencia.frameNStart = frameN  # exact frame index
            indicaciones_competencia.tStart = t  # local t and not account for scr refresh
            indicaciones_competencia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_competencia, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_competencia.status = STARTED
            indicaciones_competencia.setAutoDraw(True)
        
        # if indicaciones_competencia is active this frame...
        if indicaciones_competencia.status == STARTED:
            # update params
            pass
        
        # *text_habla_que* updates
        
        # if text_habla_que is starting this frame...
        if text_habla_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_habla_que.frameNStart = frameN  # exact frame index
            text_habla_que.tStart = t  # local t and not account for scr refresh
            text_habla_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_habla_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_habla_que.status = STARTED
            text_habla_que.setAutoDraw(True)
        
        # if text_habla_que is active this frame...
        if text_habla_que.status == STARTED:
            # update params
            pass
        
        # *habla_bien_que* updates
        
        # if habla_bien_que is starting this frame...
        if habla_bien_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            habla_bien_que.frameNStart = frameN  # exact frame index
            habla_bien_que.tStart = t  # local t and not account for scr refresh
            habla_bien_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(habla_bien_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            habla_bien_que.status = STARTED
            habla_bien_que.setAutoDraw(True)
        
        # if habla_bien_que is active this frame...
        if habla_bien_que.status == STARTED:
            # update params
            pass
        
        # *text_habla_esp* updates
        
        # if text_habla_esp is starting this frame...
        if text_habla_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_habla_esp.frameNStart = frameN  # exact frame index
            text_habla_esp.tStart = t  # local t and not account for scr refresh
            text_habla_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_habla_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_habla_esp.status = STARTED
            text_habla_esp.setAutoDraw(True)
        
        # if text_habla_esp is active this frame...
        if text_habla_esp.status == STARTED:
            # update params
            pass
        
        # *habla_bien_esp* updates
        
        # if habla_bien_esp is starting this frame...
        if habla_bien_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            habla_bien_esp.frameNStart = frameN  # exact frame index
            habla_bien_esp.tStart = t  # local t and not account for scr refresh
            habla_bien_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(habla_bien_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            habla_bien_esp.status = STARTED
            habla_bien_esp.setAutoDraw(True)
        
        # if habla_bien_esp is active this frame...
        if habla_bien_esp.status == STARTED:
            # update params
            pass
        
        # *text_entiende_que* updates
        
        # if text_entiende_que is starting this frame...
        if text_entiende_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_entiende_que.frameNStart = frameN  # exact frame index
            text_entiende_que.tStart = t  # local t and not account for scr refresh
            text_entiende_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_entiende_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_entiende_que.status = STARTED
            text_entiende_que.setAutoDraw(True)
        
        # if text_entiende_que is active this frame...
        if text_entiende_que.status == STARTED:
            # update params
            pass
        
        # *entiende_bien_que* updates
        
        # if entiende_bien_que is starting this frame...
        if entiende_bien_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            entiende_bien_que.frameNStart = frameN  # exact frame index
            entiende_bien_que.tStart = t  # local t and not account for scr refresh
            entiende_bien_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(entiende_bien_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            entiende_bien_que.status = STARTED
            entiende_bien_que.setAutoDraw(True)
        
        # if entiende_bien_que is active this frame...
        if entiende_bien_que.status == STARTED:
            # update params
            pass
        
        # *text_entiende_esp* updates
        
        # if text_entiende_esp is starting this frame...
        if text_entiende_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_entiende_esp.frameNStart = frameN  # exact frame index
            text_entiende_esp.tStart = t  # local t and not account for scr refresh
            text_entiende_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_entiende_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_entiende_esp.status = STARTED
            text_entiende_esp.setAutoDraw(True)
        
        # if text_entiende_esp is active this frame...
        if text_entiende_esp.status == STARTED:
            # update params
            pass
        
        # *entiende_bien_esp* updates
        
        # if entiende_bien_esp is starting this frame...
        if entiende_bien_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            entiende_bien_esp.frameNStart = frameN  # exact frame index
            entiende_bien_esp.tStart = t  # local t and not account for scr refresh
            entiende_bien_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(entiende_bien_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            entiende_bien_esp.status = STARTED
            entiende_bien_esp.setAutoDraw(True)
        
        # if entiende_bien_esp is active this frame...
        if entiende_bien_esp.status == STARTED:
            # update params
            pass
        
        # *text_lee_que* updates
        
        # if text_lee_que is starting this frame...
        if text_lee_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lee_que.frameNStart = frameN  # exact frame index
            text_lee_que.tStart = t  # local t and not account for scr refresh
            text_lee_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lee_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_lee_que.status = STARTED
            text_lee_que.setAutoDraw(True)
        
        # if text_lee_que is active this frame...
        if text_lee_que.status == STARTED:
            # update params
            pass
        
        # *lee_bien_que* updates
        
        # if lee_bien_que is starting this frame...
        if lee_bien_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lee_bien_que.frameNStart = frameN  # exact frame index
            lee_bien_que.tStart = t  # local t and not account for scr refresh
            lee_bien_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lee_bien_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            lee_bien_que.status = STARTED
            lee_bien_que.setAutoDraw(True)
        
        # if lee_bien_que is active this frame...
        if lee_bien_que.status == STARTED:
            # update params
            pass
        
        # *text_lee_esp* updates
        
        # if text_lee_esp is starting this frame...
        if text_lee_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lee_esp.frameNStart = frameN  # exact frame index
            text_lee_esp.tStart = t  # local t and not account for scr refresh
            text_lee_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lee_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_lee_esp.status = STARTED
            text_lee_esp.setAutoDraw(True)
        
        # if text_lee_esp is active this frame...
        if text_lee_esp.status == STARTED:
            # update params
            pass
        
        # *lee_bien_esp* updates
        
        # if lee_bien_esp is starting this frame...
        if lee_bien_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lee_bien_esp.frameNStart = frameN  # exact frame index
            lee_bien_esp.tStart = t  # local t and not account for scr refresh
            lee_bien_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lee_bien_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            lee_bien_esp.status = STARTED
            lee_bien_esp.setAutoDraw(True)
        
        # if lee_bien_esp is active this frame...
        if lee_bien_esp.status == STARTED:
            # update params
            pass
        
        # *text_escribe_que* updates
        
        # if text_escribe_que is starting this frame...
        if text_escribe_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_escribe_que.frameNStart = frameN  # exact frame index
            text_escribe_que.tStart = t  # local t and not account for scr refresh
            text_escribe_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_escribe_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_escribe_que.status = STARTED
            text_escribe_que.setAutoDraw(True)
        
        # if text_escribe_que is active this frame...
        if text_escribe_que.status == STARTED:
            # update params
            pass
        
        # *escribe_bien_que* updates
        
        # if escribe_bien_que is starting this frame...
        if escribe_bien_que.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            escribe_bien_que.frameNStart = frameN  # exact frame index
            escribe_bien_que.tStart = t  # local t and not account for scr refresh
            escribe_bien_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(escribe_bien_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            escribe_bien_que.status = STARTED
            escribe_bien_que.setAutoDraw(True)
        
        # if escribe_bien_que is active this frame...
        if escribe_bien_que.status == STARTED:
            # update params
            pass
        
        # *text_escribe_esp* updates
        
        # if text_escribe_esp is starting this frame...
        if text_escribe_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_escribe_esp.frameNStart = frameN  # exact frame index
            text_escribe_esp.tStart = t  # local t and not account for scr refresh
            text_escribe_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_escribe_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_escribe_esp.status = STARTED
            text_escribe_esp.setAutoDraw(True)
        
        # if text_escribe_esp is active this frame...
        if text_escribe_esp.status == STARTED:
            # update params
            pass
        
        # *escribe_bien_esp* updates
        
        # if escribe_bien_esp is starting this frame...
        if escribe_bien_esp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            escribe_bien_esp.frameNStart = frameN  # exact frame index
            escribe_bien_esp.tStart = t  # local t and not account for scr refresh
            escribe_bien_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(escribe_bien_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            escribe_bien_esp.status = STARTED
            escribe_bien_esp.setAutoDraw(True)
        
        # if escribe_bien_esp is active this frame...
        if escribe_bien_esp.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_competencia,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_competencia.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_competencia.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_competencia.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_competencia" ---
    for thisComponent in blp_competencia.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_competencia
    blp_competencia.tStop = globalClock.getTime(format='float')
    blp_competencia.tStopRefresh = tThisFlipGlobal
    thisExp.addData('habla_bien_que.response', habla_bien_que.getRating())
    thisExp.addData('habla_bien_esp.response', habla_bien_esp.getRating())
    thisExp.addData('entiende_bien_que.response', entiende_bien_que.getRating())
    thisExp.addData('entiende_bien_esp.response', entiende_bien_esp.getRating())
    thisExp.addData('lee_bien_que.response', lee_bien_que.getRating())
    thisExp.addData('lee_bien_esp.response', lee_bien_esp.getRating())
    thisExp.addData('escribe_bien_que.response', escribe_bien_que.getRating())
    thisExp.addData('escribe_bien_esp.response', escribe_bien_esp.getRating())
    thisExp.nextEntry()
    # the Routine "blp_competencia" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blp_actitud" ---
    # create an object to store info about Routine blp_actitud
    blp_actitud = data.Routine(
        name='blp_actitud',
        components=[boton_actitud, indicaciones_actitud, text_yomismo_que, yo_mismo_que, text_yomismo_esp, yo_mismo_esp, text_cultura_que, cultura_que, text_cultura_esp, cultura_esp, text_uso_nativo_que, uso_nativo_que, text_uso_nativo_esp, uso_nativo_esp, text_habalnte_nativo_que, hablante_nativo_que, text_hablante_nativo_esp, hablante_nativo_esp],
    )
    blp_actitud.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_actitud
    # Disable "Siguiente" at start
    canContinue = False
    boton_actitud.opacity = 0.5
    boton_actitud.color = 'gray'
    
    # reset boton_actitud to account for continued clicks & clear times on/off
    boton_actitud.reset()
    yo_mismo_que.reset()
    yo_mismo_esp.reset()
    cultura_que.reset()
    cultura_esp.reset()
    uso_nativo_que.reset()
    uso_nativo_esp.reset()
    hablante_nativo_que.reset()
    hablante_nativo_esp.reset()
    # store start times for blp_actitud
    blp_actitud.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blp_actitud.tStart = globalClock.getTime(format='float')
    blp_actitud.status = STARTED
    blp_actitud.maxDuration = None
    # keep track of which components have finished
    blp_actitudComponents = blp_actitud.components
    for thisComponent in blp_actitud.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blp_actitud" ---
    thisExp.currentRoutine = blp_actitud
    blp_actitud.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_actitud
        # List of all slider components in this routine
        sliders = [
            yo_mismo_que,
            yo_mismo_esp,
            cultura_que,
            cultura_esp,
            uso_nativo_que,
            uso_nativo_esp,
            hablante_nativo_que,
            hablante_nativo_esp
        ]
        
        # Check if all sliders have a response
        filled = all(sl.getRating() is not None for sl in sliders)
        
        # Enable "Siguiente" button once all are filled
        if filled and not canContinue:
            canContinue = True
            boton_actitud.opacity = 1
            boton_actitud.color = 'white'
        elif not filled:
            canContinue = False
            boton_actitud.opacity = 0.5
            boton_actitud.color = 'gray'
        
        # Allow next only when all responses are made
        if boton_actitud.isClicked and canContinue:
            continueRoutine = False
        
        # *boton_actitud* updates
        
        # if boton_actitud is starting this frame...
        if boton_actitud.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            boton_actitud.frameNStart = frameN  # exact frame index
            boton_actitud.tStart = t  # local t and not account for scr refresh
            boton_actitud.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(boton_actitud, 'tStartRefresh')  # time at next scr refresh
            # update status
            boton_actitud.status = STARTED
            win.callOnFlip(boton_actitud.buttonClock.reset)
            boton_actitud.setAutoDraw(True)
        
        # if boton_actitud is active this frame...
        if boton_actitud.status == STARTED:
            # update params
            pass
            # check whether boton_actitud has been pressed
            if boton_actitud.isClicked:
                if not boton_actitud.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    boton_actitud.timesOn.append(boton_actitud.buttonClock.getTime())
                    boton_actitud.timesOff.append(boton_actitud.buttonClock.getTime())
                elif len(boton_actitud.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    boton_actitud.timesOff[-1] = boton_actitud.buttonClock.getTime()
                # run callback code when boton_actitud is clicked
                pass
        # take note of whether boton_actitud was clicked, so that next frame we know if clicks are new
        boton_actitud.wasClicked = boton_actitud.isClicked and boton_actitud.status == STARTED
        
        # *indicaciones_actitud* updates
        
        # if indicaciones_actitud is starting this frame...
        if indicaciones_actitud.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicaciones_actitud.frameNStart = frameN  # exact frame index
            indicaciones_actitud.tStart = t  # local t and not account for scr refresh
            indicaciones_actitud.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicaciones_actitud, 'tStartRefresh')  # time at next scr refresh
            # update status
            indicaciones_actitud.status = STARTED
            indicaciones_actitud.setAutoDraw(True)
        
        # if indicaciones_actitud is active this frame...
        if indicaciones_actitud.status == STARTED:
            # update params
            pass
        
        # *text_yomismo_que* updates
        
        # if text_yomismo_que is starting this frame...
        if text_yomismo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_yomismo_que.frameNStart = frameN  # exact frame index
            text_yomismo_que.tStart = t  # local t and not account for scr refresh
            text_yomismo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_yomismo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_yomismo_que.status = STARTED
            text_yomismo_que.setAutoDraw(True)
        
        # if text_yomismo_que is active this frame...
        if text_yomismo_que.status == STARTED:
            # update params
            pass
        
        # *yo_mismo_que* updates
        
        # if yo_mismo_que is starting this frame...
        if yo_mismo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yo_mismo_que.frameNStart = frameN  # exact frame index
            yo_mismo_que.tStart = t  # local t and not account for scr refresh
            yo_mismo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yo_mismo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            yo_mismo_que.status = STARTED
            yo_mismo_que.setAutoDraw(True)
        
        # if yo_mismo_que is active this frame...
        if yo_mismo_que.status == STARTED:
            # update params
            pass
        
        # *text_yomismo_esp* updates
        
        # if text_yomismo_esp is starting this frame...
        if text_yomismo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_yomismo_esp.frameNStart = frameN  # exact frame index
            text_yomismo_esp.tStart = t  # local t and not account for scr refresh
            text_yomismo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_yomismo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_yomismo_esp.status = STARTED
            text_yomismo_esp.setAutoDraw(True)
        
        # if text_yomismo_esp is active this frame...
        if text_yomismo_esp.status == STARTED:
            # update params
            pass
        
        # *yo_mismo_esp* updates
        
        # if yo_mismo_esp is starting this frame...
        if yo_mismo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yo_mismo_esp.frameNStart = frameN  # exact frame index
            yo_mismo_esp.tStart = t  # local t and not account for scr refresh
            yo_mismo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yo_mismo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            yo_mismo_esp.status = STARTED
            yo_mismo_esp.setAutoDraw(True)
        
        # if yo_mismo_esp is active this frame...
        if yo_mismo_esp.status == STARTED:
            # update params
            pass
        
        # *text_cultura_que* updates
        
        # if text_cultura_que is starting this frame...
        if text_cultura_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_cultura_que.frameNStart = frameN  # exact frame index
            text_cultura_que.tStart = t  # local t and not account for scr refresh
            text_cultura_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_cultura_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_cultura_que.status = STARTED
            text_cultura_que.setAutoDraw(True)
        
        # if text_cultura_que is active this frame...
        if text_cultura_que.status == STARTED:
            # update params
            pass
        
        # *cultura_que* updates
        
        # if cultura_que is starting this frame...
        if cultura_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cultura_que.frameNStart = frameN  # exact frame index
            cultura_que.tStart = t  # local t and not account for scr refresh
            cultura_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cultura_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            cultura_que.status = STARTED
            cultura_que.setAutoDraw(True)
        
        # if cultura_que is active this frame...
        if cultura_que.status == STARTED:
            # update params
            pass
        
        # *text_cultura_esp* updates
        
        # if text_cultura_esp is starting this frame...
        if text_cultura_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_cultura_esp.frameNStart = frameN  # exact frame index
            text_cultura_esp.tStart = t  # local t and not account for scr refresh
            text_cultura_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_cultura_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_cultura_esp.status = STARTED
            text_cultura_esp.setAutoDraw(True)
        
        # if text_cultura_esp is active this frame...
        if text_cultura_esp.status == STARTED:
            # update params
            pass
        
        # *cultura_esp* updates
        
        # if cultura_esp is starting this frame...
        if cultura_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cultura_esp.frameNStart = frameN  # exact frame index
            cultura_esp.tStart = t  # local t and not account for scr refresh
            cultura_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cultura_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            cultura_esp.status = STARTED
            cultura_esp.setAutoDraw(True)
        
        # if cultura_esp is active this frame...
        if cultura_esp.status == STARTED:
            # update params
            pass
        
        # *text_uso_nativo_que* updates
        
        # if text_uso_nativo_que is starting this frame...
        if text_uso_nativo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_uso_nativo_que.frameNStart = frameN  # exact frame index
            text_uso_nativo_que.tStart = t  # local t and not account for scr refresh
            text_uso_nativo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_uso_nativo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_uso_nativo_que.status = STARTED
            text_uso_nativo_que.setAutoDraw(True)
        
        # if text_uso_nativo_que is active this frame...
        if text_uso_nativo_que.status == STARTED:
            # update params
            pass
        
        # *uso_nativo_que* updates
        
        # if uso_nativo_que is starting this frame...
        if uso_nativo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            uso_nativo_que.frameNStart = frameN  # exact frame index
            uso_nativo_que.tStart = t  # local t and not account for scr refresh
            uso_nativo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(uso_nativo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            uso_nativo_que.status = STARTED
            uso_nativo_que.setAutoDraw(True)
        
        # if uso_nativo_que is active this frame...
        if uso_nativo_que.status == STARTED:
            # update params
            pass
        
        # *text_uso_nativo_esp* updates
        
        # if text_uso_nativo_esp is starting this frame...
        if text_uso_nativo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_uso_nativo_esp.frameNStart = frameN  # exact frame index
            text_uso_nativo_esp.tStart = t  # local t and not account for scr refresh
            text_uso_nativo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_uso_nativo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_uso_nativo_esp.status = STARTED
            text_uso_nativo_esp.setAutoDraw(True)
        
        # if text_uso_nativo_esp is active this frame...
        if text_uso_nativo_esp.status == STARTED:
            # update params
            pass
        
        # *uso_nativo_esp* updates
        
        # if uso_nativo_esp is starting this frame...
        if uso_nativo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            uso_nativo_esp.frameNStart = frameN  # exact frame index
            uso_nativo_esp.tStart = t  # local t and not account for scr refresh
            uso_nativo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(uso_nativo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            uso_nativo_esp.status = STARTED
            uso_nativo_esp.setAutoDraw(True)
        
        # if uso_nativo_esp is active this frame...
        if uso_nativo_esp.status == STARTED:
            # update params
            pass
        
        # *text_habalnte_nativo_que* updates
        
        # if text_habalnte_nativo_que is starting this frame...
        if text_habalnte_nativo_que.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_habalnte_nativo_que.frameNStart = frameN  # exact frame index
            text_habalnte_nativo_que.tStart = t  # local t and not account for scr refresh
            text_habalnte_nativo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_habalnte_nativo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_habalnte_nativo_que.status = STARTED
            text_habalnte_nativo_que.setAutoDraw(True)
        
        # if text_habalnte_nativo_que is active this frame...
        if text_habalnte_nativo_que.status == STARTED:
            # update params
            pass
        
        # *hablante_nativo_que* updates
        
        # if hablante_nativo_que is starting this frame...
        if hablante_nativo_que.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hablante_nativo_que.frameNStart = frameN  # exact frame index
            hablante_nativo_que.tStart = t  # local t and not account for scr refresh
            hablante_nativo_que.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hablante_nativo_que, 'tStartRefresh')  # time at next scr refresh
            # update status
            hablante_nativo_que.status = STARTED
            hablante_nativo_que.setAutoDraw(True)
        
        # if hablante_nativo_que is active this frame...
        if hablante_nativo_que.status == STARTED:
            # update params
            pass
        
        # *text_hablante_nativo_esp* updates
        
        # if text_hablante_nativo_esp is starting this frame...
        if text_hablante_nativo_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_hablante_nativo_esp.frameNStart = frameN  # exact frame index
            text_hablante_nativo_esp.tStart = t  # local t and not account for scr refresh
            text_hablante_nativo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_hablante_nativo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_hablante_nativo_esp.status = STARTED
            text_hablante_nativo_esp.setAutoDraw(True)
        
        # if text_hablante_nativo_esp is active this frame...
        if text_hablante_nativo_esp.status == STARTED:
            # update params
            pass
        
        # *hablante_nativo_esp* updates
        
        # if hablante_nativo_esp is starting this frame...
        if hablante_nativo_esp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hablante_nativo_esp.frameNStart = frameN  # exact frame index
            hablante_nativo_esp.tStart = t  # local t and not account for scr refresh
            hablante_nativo_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hablante_nativo_esp, 'tStartRefresh')  # time at next scr refresh
            # update status
            hablante_nativo_esp.status = STARTED
            hablante_nativo_esp.setAutoDraw(True)
        
        # if hablante_nativo_esp is active this frame...
        if hablante_nativo_esp.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blp_actitud,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blp_actitud.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blp_actitud.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blp_actitud.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blp_actitud" ---
    for thisComponent in blp_actitud.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blp_actitud
    blp_actitud.tStop = globalClock.getTime(format='float')
    blp_actitud.tStopRefresh = tThisFlipGlobal
    thisExp.addData('yo_mismo_que.response', yo_mismo_que.getRating())
    thisExp.addData('yo_mismo_esp.response', yo_mismo_esp.getRating())
    thisExp.addData('cultura_que.response', cultura_que.getRating())
    thisExp.addData('cultura_esp.response', cultura_esp.getRating())
    thisExp.addData('uso_nativo_que.response', uso_nativo_que.getRating())
    thisExp.addData('uso_nativo_esp.response', uso_nativo_esp.getRating())
    thisExp.addData('hablante_nativo_que.response', hablante_nativo_que.getRating())
    thisExp.addData('hablante_nativo_esp.response', hablante_nativo_esp.getRating())
    thisExp.nextEntry()
    # the Routine "blp_actitud" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "delay_trial" ---
    # create an object to store info about Routine delay_trial
    delay_trial = data.Routine(
        name='delay_trial',
        components=[cross_q_5, space_delay_3],
    )
    delay_trial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for space_delay_3
    space_delay_3.keys = []
    space_delay_3.rt = []
    _space_delay_3_allKeys = []
    # store start times for delay_trial
    delay_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    delay_trial.tStart = globalClock.getTime(format='float')
    delay_trial.status = STARTED
    delay_trial.maxDuration = None
    # keep track of which components have finished
    delay_trialComponents = delay_trial.components
    for thisComponent in delay_trial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "delay_trial" ---
    thisExp.currentRoutine = delay_trial
    delay_trial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_q_5* updates
        
        # if cross_q_5 is starting this frame...
        if cross_q_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_q_5.frameNStart = frameN  # exact frame index
            cross_q_5.tStart = t  # local t and not account for scr refresh
            cross_q_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_q_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            cross_q_5.status = STARTED
            cross_q_5.setAutoDraw(True)
        
        # if cross_q_5 is active this frame...
        if cross_q_5.status == STARTED:
            # update params
            pass
        
        # *space_delay_3* updates
        
        # if space_delay_3 is starting this frame...
        if space_delay_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_delay_3.frameNStart = frameN  # exact frame index
            space_delay_3.tStart = t  # local t and not account for scr refresh
            space_delay_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_delay_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            space_delay_3.status = STARTED
            # keyboard checking is just starting
            space_delay_3.clock.reset()  # now t=0
        if space_delay_3.status == STARTED:
            theseKeys = space_delay_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_delay_3_allKeys.extend(theseKeys)
            if len(_space_delay_3_allKeys):
                space_delay_3.keys = _space_delay_3_allKeys[-1].name  # just the last key pressed
                space_delay_3.rt = _space_delay_3_allKeys[-1].rt
                space_delay_3.duration = _space_delay_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=delay_trial,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            delay_trial.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if delay_trial.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in delay_trial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "delay_trial" ---
    for thisComponent in delay_trial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for delay_trial
    delay_trial.tStop = globalClock.getTime(format='float')
    delay_trial.tStopRefresh = tThisFlipGlobal
    # check responses
    if space_delay_3.keys in ['', [], None]:  # No response was made
        space_delay_3.keys = None
    thisExp.addData('space_delay_3.keys',space_delay_3.keys)
    if space_delay_3.keys != None:  # we had a response
        thisExp.addData('space_delay_3.rt', space_delay_3.rt)
        thisExp.addData('space_delay_3.duration', space_delay_3.duration)
    thisExp.nextEntry()
    # the Routine "delay_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_prueba" ---
    # create an object to store info about Routine instruction_prueba
    instruction_prueba = data.Routine(
        name='instruction_prueba',
        components=[intructions_2, text_continuar_2, instructions_space_2, prueba],
    )
    instruction_prueba.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instructions_space_2
    instructions_space_2.keys = []
    instructions_space_2.rt = []
    _instructions_space_2_allKeys = []
    prueba.setSound('audio/intro_seg1.wav', hamming=True)
    prueba.setVolume(1.0, log=False)
    prueba.seek(0)
    # store start times for instruction_prueba
    instruction_prueba.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_prueba.tStart = globalClock.getTime(format='float')
    instruction_prueba.status = STARTED
    instruction_prueba.maxDuration = None
    # keep track of which components have finished
    instruction_pruebaComponents = instruction_prueba.components
    for thisComponent in instruction_prueba.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_prueba" ---
    thisExp.currentRoutine = instruction_prueba
    instruction_prueba.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intructions_2* updates
        
        # if intructions_2 is starting this frame...
        if intructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intructions_2.frameNStart = frameN  # exact frame index
            intructions_2.tStart = t  # local t and not account for scr refresh
            intructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intructions_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            intructions_2.status = STARTED
            intructions_2.setAutoDraw(True)
        
        # if intructions_2 is active this frame...
        if intructions_2.status == STARTED:
            # update params
            pass
        
        # *text_continuar_2* updates
        
        # if text_continuar_2 is starting this frame...
        if text_continuar_2.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
            # keep track of start time/frame for later
            text_continuar_2.frameNStart = frameN  # exact frame index
            text_continuar_2.tStart = t  # local t and not account for scr refresh
            text_continuar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_continuar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_continuar_2.status = STARTED
            text_continuar_2.setAutoDraw(True)
        
        # if text_continuar_2 is active this frame...
        if text_continuar_2.status == STARTED:
            # update params
            pass
        
        # *instructions_space_2* updates
        waitOnFlip = False
        
        # if instructions_space_2 is starting this frame...
        if instructions_space_2.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            instructions_space_2.frameNStart = frameN  # exact frame index
            instructions_space_2.tStart = t  # local t and not account for scr refresh
            instructions_space_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_space_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions_space_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_space_2.clock.reset)  # t=0 on next screen flip
        if instructions_space_2.status == STARTED and not waitOnFlip:
            theseKeys = instructions_space_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instructions_space_2_allKeys.extend(theseKeys)
            if len(_instructions_space_2_allKeys):
                instructions_space_2.keys = _instructions_space_2_allKeys[-1].name  # just the last key pressed
                instructions_space_2.rt = _instructions_space_2_allKeys[-1].rt
                instructions_space_2.duration = _instructions_space_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *prueba* updates
        
        # if prueba is starting this frame...
        if prueba.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prueba.frameNStart = frameN  # exact frame index
            prueba.tStart = t  # local t and not account for scr refresh
            prueba.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            prueba.status = STARTED
            prueba.play(when=win)  # sync with win flip
        
        # if prueba is stopping this frame...
        if prueba.status == STARTED:
            if bool(False) or prueba.isFinished:
                # keep track of stop time/frame for later
                prueba.tStop = t  # not accounting for scr refresh
                prueba.tStopRefresh = tThisFlipGlobal  # on global time
                prueba.frameNStop = frameN  # exact frame index
                # update status
                prueba.status = FINISHED
                prueba.stop()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_prueba,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instruction_prueba.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instruction_prueba.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instruction_prueba.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_prueba" ---
    for thisComponent in instruction_prueba.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_prueba
    instruction_prueba.tStop = globalClock.getTime(format='float')
    instruction_prueba.tStopRefresh = tThisFlipGlobal
    prueba.pause()  # ensure sound has stopped at end of Routine
    thisExp.nextEntry()
    # the Routine "instruction_prueba" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_prueba = data.TrialHandler2(
        name='trials_prueba',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('spl_stim_prueba.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_prueba)  # add the loop to the experiment
    thisTrials_prueba = trials_prueba.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prueba.rgb)
    if thisTrials_prueba != None:
        for paramName in thisTrials_prueba:
            globals()[paramName] = thisTrials_prueba[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_prueba in trials_prueba:
        trials_prueba.status = STARTED
        if hasattr(thisTrials_prueba, 'status'):
            thisTrials_prueba.status = STARTED
        currentLoop = trials_prueba
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_prueba.rgb)
        if thisTrials_prueba != None:
            for paramName in thisTrials_prueba:
                globals()[paramName] = thisTrials_prueba[paramName]
        
        # --- Prepare to start Routine "trial_prueba" ---
        # create an object to store info about Routine trial_prueba
        trial_prueba = data.Routine(
            name='trial_prueba',
            components=[audios_2, cross_2, key_prueba],
        )
        trial_prueba.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        audios_2.setSound('C:/Users/AAPL/Desktop/SPL_Gabi/exp_1/audio/' + audio_file, hamming=True)
        audios_2.setVolume(1.0, log=False)
        audios_2.seek(0)
        # create starting attributes for key_prueba
        key_prueba.keys = []
        key_prueba.rt = []
        _key_prueba_allKeys = []
        # store start times for trial_prueba
        trial_prueba.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_prueba.tStart = globalClock.getTime(format='float')
        trial_prueba.status = STARTED
        trial_prueba.maxDuration = None
        # skip Routine trial_prueba if its 'Skip if' condition is True
        trial_prueba.skipped = continueRoutine and not (segment_number == 7)
        continueRoutine = trial_prueba.skipped
        # keep track of which components have finished
        trial_pruebaComponents = trial_prueba.components
        for thisComponent in trial_prueba.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_prueba" ---
        thisExp.currentRoutine = trial_prueba
        trial_prueba.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_prueba, 'status') and thisTrials_prueba.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *audios_2* updates
            
            # if audios_2 is starting this frame...
            if audios_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                audios_2.frameNStart = frameN  # exact frame index
                audios_2.tStart = t  # local t and not account for scr refresh
                audios_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                audios_2.status = STARTED
                audios_2.play(when=win)  # sync with win flip
            
            # if audios_2 is stopping this frame...
            if audios_2.status == STARTED:
                if bool(False) or audios_2.isFinished:
                    # keep track of stop time/frame for later
                    audios_2.tStop = t  # not accounting for scr refresh
                    audios_2.tStopRefresh = tThisFlipGlobal  # on global time
                    audios_2.frameNStop = frameN  # exact frame index
                    # update status
                    audios_2.status = FINISHED
                    audios_2.stop()
            
            # *cross_2* updates
            
            # if cross_2 is starting this frame...
            if cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_2.frameNStart = frameN  # exact frame index
                cross_2.tStart = t  # local t and not account for scr refresh
                cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_2.status = STARTED
                cross_2.setAutoDraw(True)
            
            # if cross_2 is active this frame...
            if cross_2.status == STARTED:
                # update params
                pass
            
            # *key_prueba* updates
            
            # if key_prueba is starting this frame...
            if key_prueba.status == NOT_STARTED and t >= duration_ms / 1000-frameTolerance:
                # keep track of start time/frame for later
                key_prueba.frameNStart = frameN  # exact frame index
                key_prueba.tStart = t  # local t and not account for scr refresh
                key_prueba.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_prueba, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_prueba.status = STARTED
                # keyboard checking is just starting
                key_prueba.clock.reset()  # now t=0
            if key_prueba.status == STARTED:
                theseKeys = key_prueba.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_prueba_allKeys.extend(theseKeys)
                if len(_key_prueba_allKeys):
                    key_prueba.keys = _key_prueba_allKeys[-1].name  # just the last key pressed
                    key_prueba.rt = _key_prueba_allKeys[-1].rt
                    key_prueba.duration = _key_prueba_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial_prueba,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial_prueba.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial_prueba.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial_prueba.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_prueba" ---
        for thisComponent in trial_prueba.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_prueba
        trial_prueba.tStop = globalClock.getTime(format='float')
        trial_prueba.tStopRefresh = tThisFlipGlobal
        audios_2.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_prueba.keys in ['', [], None]:  # No response was made
            key_prueba.keys = None
        trials_prueba.addData('key_prueba.keys',key_prueba.keys)
        if key_prueba.keys != None:  # we had a response
            trials_prueba.addData('key_prueba.rt', key_prueba.rt)
            trials_prueba.addData('key_prueba.duration', key_prueba.duration)
        # the Routine "trial_prueba" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "questions_prueba" ---
        # create an object to store info about Routine questions_prueba
        questions_prueba = data.Routine(
            name='questions_prueba',
            components=[question_sound_2, resp_q_2, text_2, cross_q_2],
        )
        questions_prueba.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if segment_number != 7:
            continueRoutine = False
        question_sound_2.setSound("audio/" + audio_file, hamming=True)
        question_sound_2.setVolume(1.0, log=False)
        question_sound_2.seek(0)
        # create starting attributes for resp_q_2
        resp_q_2.keys = []
        resp_q_2.rt = []
        _resp_q_2_allKeys = []
        # store start times for questions_prueba
        questions_prueba.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        questions_prueba.tStart = globalClock.getTime(format='float')
        questions_prueba.status = STARTED
        questions_prueba.maxDuration = None
        # skip Routine questions_prueba if its 'Skip if' condition is True
        questions_prueba.skipped = continueRoutine and not (segment_number != 7)
        continueRoutine = questions_prueba.skipped
        # keep track of which components have finished
        questions_pruebaComponents = questions_prueba.components
        for thisComponent in questions_prueba.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "questions_prueba" ---
        thisExp.currentRoutine = questions_prueba
        questions_prueba.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_prueba, 'status') and thisTrials_prueba.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_sound_2* updates
            
            # if question_sound_2 is starting this frame...
            if question_sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sound_2.frameNStart = frameN  # exact frame index
                question_sound_2.tStart = t  # local t and not account for scr refresh
                question_sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                question_sound_2.status = STARTED
                question_sound_2.play(when=win)  # sync with win flip
            
            # if question_sound_2 is stopping this frame...
            if question_sound_2.status == STARTED:
                if bool(False) or question_sound_2.isFinished:
                    # keep track of stop time/frame for later
                    question_sound_2.tStop = t  # not accounting for scr refresh
                    question_sound_2.tStopRefresh = tThisFlipGlobal  # on global time
                    question_sound_2.frameNStop = frameN  # exact frame index
                    # update status
                    question_sound_2.status = FINISHED
                    question_sound_2.stop()
            
            # *resp_q_2* updates
            waitOnFlip = False
            
            # if resp_q_2 is starting this frame...
            if resp_q_2.status == NOT_STARTED and tThisFlip >= duration_ms / 1000-frameTolerance:
                # keep track of start time/frame for later
                resp_q_2.frameNStart = frameN  # exact frame index
                resp_q_2.tStart = t  # local t and not account for scr refresh
                resp_q_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_q_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                resp_q_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_q_2.clock.reset)  # t=0 on next screen flip
            if resp_q_2.status == STARTED and not waitOnFlip:
                theseKeys = resp_q_2.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _resp_q_2_allKeys.extend(theseKeys)
                if len(_resp_q_2_allKeys):
                    resp_q_2.keys = _resp_q_2_allKeys[-1].name  # just the last key pressed
                    resp_q_2.rt = _resp_q_2_allKeys[-1].rt
                    resp_q_2.duration = _resp_q_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *cross_q_2* updates
            
            # if cross_q_2 is starting this frame...
            if cross_q_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_q_2.frameNStart = frameN  # exact frame index
                cross_q_2.tStart = t  # local t and not account for scr refresh
                cross_q_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_q_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_q_2.status = STARTED
                cross_q_2.setAutoDraw(True)
            
            # if cross_q_2 is active this frame...
            if cross_q_2.status == STARTED:
                # update params
                pass
            
            # if cross_q_2 is stopping this frame...
            if cross_q_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_q_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_q_2.tStop = t  # not accounting for scr refresh
                    cross_q_2.tStopRefresh = tThisFlipGlobal  # on global time
                    cross_q_2.frameNStop = frameN  # exact frame index
                    # update status
                    cross_q_2.status = FINISHED
                    cross_q_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=questions_prueba,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                questions_prueba.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if questions_prueba.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in questions_prueba.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "questions_prueba" ---
        for thisComponent in questions_prueba.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for questions_prueba
        questions_prueba.tStop = globalClock.getTime(format='float')
        questions_prueba.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code_2
        # Convert response time from seconds to milliseconds
        if resp_q.rt is not None:
            resp_q_rt_ms = resp_q.rt * 1000
        else:
            resp_q_rt_ms = None
        
        # Label the F/J response as Sí/No
        if resp_q.keys == 'f':
            resp_label = 'Sí'
        elif resp_q.keys == 'j':
            resp_label = 'No'
        else:
            resp_label = 'Sin respuesta'
        
        # Add data to the PsychoPy output file
        thisExp.addData('resp_key', resp_q.keys)
        thisExp.addData('resp_label', resp_label)
        thisExp.addData('resp_q_rt_ms', resp_q_rt_ms)
        question_sound_2.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if resp_q_2.keys in ['', [], None]:  # No response was made
            resp_q_2.keys = None
        trials_prueba.addData('resp_q_2.keys',resp_q_2.keys)
        if resp_q_2.keys != None:  # we had a response
            trials_prueba.addData('resp_q_2.rt', resp_q_2.rt)
            trials_prueba.addData('resp_q_2.duration', resp_q_2.duration)
        # the Routine "questions_prueba" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "delay_prueba" ---
        # create an object to store info about Routine delay_prueba
        delay_prueba = data.Routine(
            name='delay_prueba',
            components=[cross_q_3, space_delay],
        )
        delay_prueba.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for space_delay
        space_delay.keys = []
        space_delay.rt = []
        _space_delay_allKeys = []
        # store start times for delay_prueba
        delay_prueba.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        delay_prueba.tStart = globalClock.getTime(format='float')
        delay_prueba.status = STARTED
        delay_prueba.maxDuration = None
        # skip Routine delay_prueba if its 'Skip if' condition is True
        delay_prueba.skipped = continueRoutine and not (segment_number != 7)
        continueRoutine = delay_prueba.skipped
        # keep track of which components have finished
        delay_pruebaComponents = delay_prueba.components
        for thisComponent in delay_prueba.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "delay_prueba" ---
        thisExp.currentRoutine = delay_prueba
        delay_prueba.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_prueba, 'status') and thisTrials_prueba.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_q_3* updates
            
            # if cross_q_3 is starting this frame...
            if cross_q_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_q_3.frameNStart = frameN  # exact frame index
                cross_q_3.tStart = t  # local t and not account for scr refresh
                cross_q_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_q_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_q_3.status = STARTED
                cross_q_3.setAutoDraw(True)
            
            # if cross_q_3 is active this frame...
            if cross_q_3.status == STARTED:
                # update params
                pass
            
            # *space_delay* updates
            
            # if space_delay is starting this frame...
            if space_delay.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space_delay.frameNStart = frameN  # exact frame index
                space_delay.tStart = t  # local t and not account for scr refresh
                space_delay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_delay, 'tStartRefresh')  # time at next scr refresh
                # update status
                space_delay.status = STARTED
                # keyboard checking is just starting
                space_delay.clock.reset()  # now t=0
            if space_delay.status == STARTED:
                theseKeys = space_delay.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _space_delay_allKeys.extend(theseKeys)
                if len(_space_delay_allKeys):
                    space_delay.keys = _space_delay_allKeys[-1].name  # just the last key pressed
                    space_delay.rt = _space_delay_allKeys[-1].rt
                    space_delay.duration = _space_delay_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=delay_prueba,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                delay_prueba.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if delay_prueba.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in delay_prueba.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "delay_prueba" ---
        for thisComponent in delay_prueba.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for delay_prueba
        delay_prueba.tStop = globalClock.getTime(format='float')
        delay_prueba.tStopRefresh = tThisFlipGlobal
        # check responses
        if space_delay.keys in ['', [], None]:  # No response was made
            space_delay.keys = None
        trials_prueba.addData('space_delay.keys',space_delay.keys)
        if space_delay.keys != None:  # we had a response
            trials_prueba.addData('space_delay.rt', space_delay.rt)
            trials_prueba.addData('space_delay.duration', space_delay.duration)
        # the Routine "delay_prueba" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrials_prueba as finished
        if hasattr(thisTrials_prueba, 'status'):
            thisTrials_prueba.status = FINISHED
        # if awaiting a pause, pause now
        if trials_prueba.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_prueba.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_prueba'
    trials_prueba.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[intructions, text_continuar, instructions_space, intro_prueba],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instructions_space
    instructions_space.keys = []
    instructions_space.rt = []
    _instructions_space_allKeys = []
    intro_prueba.setSound('audio/intro_seg2.wav', hamming=True)
    intro_prueba.setVolume(1.0, log=False)
    intro_prueba.seek(0)
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    thisExp.currentRoutine = instructions
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intructions* updates
        
        # if intructions is starting this frame...
        if intructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intructions.frameNStart = frameN  # exact frame index
            intructions.tStart = t  # local t and not account for scr refresh
            intructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            intructions.status = STARTED
            intructions.setAutoDraw(True)
        
        # if intructions is active this frame...
        if intructions.status == STARTED:
            # update params
            pass
        
        # *text_continuar* updates
        
        # if text_continuar is starting this frame...
        if text_continuar.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
            # keep track of start time/frame for later
            text_continuar.frameNStart = frameN  # exact frame index
            text_continuar.tStart = t  # local t and not account for scr refresh
            text_continuar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_continuar, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_continuar.status = STARTED
            text_continuar.setAutoDraw(True)
        
        # if text_continuar is active this frame...
        if text_continuar.status == STARTED:
            # update params
            pass
        
        # *instructions_space* updates
        waitOnFlip = False
        
        # if instructions_space is starting this frame...
        if instructions_space.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_space.frameNStart = frameN  # exact frame index
            instructions_space.tStart = t  # local t and not account for scr refresh
            instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_space, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_space.clock.reset)  # t=0 on next screen flip
        if instructions_space.status == STARTED and not waitOnFlip:
            theseKeys = instructions_space.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instructions_space_allKeys.extend(theseKeys)
            if len(_instructions_space_allKeys):
                instructions_space.keys = _instructions_space_allKeys[-1].name  # just the last key pressed
                instructions_space.rt = _instructions_space_allKeys[-1].rt
                instructions_space.duration = _instructions_space_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *intro_prueba* updates
        
        # if intro_prueba is starting this frame...
        if intro_prueba.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_prueba.frameNStart = frameN  # exact frame index
            intro_prueba.tStart = t  # local t and not account for scr refresh
            intro_prueba.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            intro_prueba.status = STARTED
            intro_prueba.play(when=win)  # sync with win flip
        
        # if intro_prueba is stopping this frame...
        if intro_prueba.status == STARTED:
            if bool(False) or intro_prueba.isFinished:
                # keep track of stop time/frame for later
                intro_prueba.tStop = t  # not accounting for scr refresh
                intro_prueba.tStopRefresh = tThisFlipGlobal  # on global time
                intro_prueba.frameNStop = frameN  # exact frame index
                # update status
                intro_prueba.status = FINISHED
                intro_prueba.stop()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    intro_prueba.pause()  # ensure sound has stopped at end of Routine
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        conditions_file, 
        selection=trial_list
    )
    , 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[audios, cross],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        audios.setSound('C:/Users/AAPL/Desktop/SPL_Gabi/exp_1/audio/' + audio_file, hamming=True)
        audios.setVolume(1.0, log=False)
        audios.seek(0)
        # Run 'Begin Routine' code from main_code
        if segment_number == 8:
            continueRoutine = False
            
        # Get audio duration in seconds from CSV
        min_wait_time = duration_ms / 1000
        
        # Start a clock for the trial
        routine_clock = core.Clock()
        
        # Prevent spacebar presses before the audio finishes
        event.clearEvents(eventType='keyboard')
        
        # Variables to track spacebar press
        space_pressed = False
        spacebar_rt = None
        audio_finished = False
        
        
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        thisExp.currentRoutine = trial
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *audios* updates
            
            # if audios is starting this frame...
            if audios.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                audios.frameNStart = frameN  # exact frame index
                audios.tStart = t  # local t and not account for scr refresh
                audios.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                audios.status = STARTED
                audios.play(when=win)  # sync with win flip
            
            # if audios is stopping this frame...
            if audios.status == STARTED:
                if bool(False) or audios.isFinished:
                    # keep track of stop time/frame for later
                    audios.tStop = t  # not accounting for scr refresh
                    audios.tStopRefresh = tThisFlipGlobal  # on global time
                    audios.frameNStop = frameN  # exact frame index
                    # update status
                    audios.status = FINISHED
                    audios.stop()
            # Run 'Each Frame' code from main_code
            current_time = routine_clock.getTime()
            
            # Mark when audio has finished playing
            if current_time >= min_wait_time and not audio_finished:
                audio_finished = True
                event.clearEvents(eventType='keyboard')
                print(f"Audio finished at: {current_time:.3f}s, now accepting spacebar.")
            
            # Allow spacebar only after audio ends
            if audio_finished and not space_pressed:
                keys = event.getKeys(keyList=['space'], timeStamped=routine_clock)
                if keys:
                    space_pressed = True
                    spacebar_rt = keys[0][1]  # in seconds
            
                    # Calculate timing
                    spacebar_rt_ms = spacebar_rt * 1000
                    reaction_time_ms = spacebar_rt_ms - duration_ms
            
                    print(f"Pressed SPACE at {spacebar_rt:.3f}s ({reaction_time_ms:.2f} ms after audio).")
            
                    # Save to PsychoPy's data file
                    thisExp.addData('spacebar_rt_ms', spacebar_rt_ms)
                    thisExp.addData('reaction_time_ms', reaction_time_ms)
                    continueRoutine = False
            
            
            # *cross* updates
            
            # if cross is starting this frame...
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross.status = STARTED
                cross.setAutoDraw(True)
            
            # if cross is active this frame...
            if cross.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        audios.pause()  # ensure sound has stopped at end of Routine
        # Run 'End Routine' code from main_code
        event.clearEvents(eventType='keyboard')
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "question" ---
        # create an object to store info about Routine question
        question = data.Routine(
            name='question',
            components=[question_sound, resp_q, text, cross_q],
        )
        question.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if segment_number != 8:
            continueRoutine = False
        question_sound.setSound("audio/" + audio_file, hamming=True)
        question_sound.setVolume(1.0, log=False)
        question_sound.seek(0)
        # create starting attributes for resp_q
        resp_q.keys = []
        resp_q.rt = []
        _resp_q_allKeys = []
        # store start times for question
        question.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        question.tStart = globalClock.getTime(format='float')
        question.status = STARTED
        question.maxDuration = None
        # keep track of which components have finished
        questionComponents = question.components
        for thisComponent in question.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "question" ---
        thisExp.currentRoutine = question
        question.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_sound* updates
            
            # if question_sound is starting this frame...
            if question_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_sound.frameNStart = frameN  # exact frame index
                question_sound.tStart = t  # local t and not account for scr refresh
                question_sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                question_sound.status = STARTED
                question_sound.play(when=win)  # sync with win flip
            
            # if question_sound is stopping this frame...
            if question_sound.status == STARTED:
                if bool(False) or question_sound.isFinished:
                    # keep track of stop time/frame for later
                    question_sound.tStop = t  # not accounting for scr refresh
                    question_sound.tStopRefresh = tThisFlipGlobal  # on global time
                    question_sound.frameNStop = frameN  # exact frame index
                    # update status
                    question_sound.status = FINISHED
                    question_sound.stop()
            
            # *resp_q* updates
            waitOnFlip = False
            
            # if resp_q is starting this frame...
            if resp_q.status == NOT_STARTED and tThisFlip >= duration_ms / 1000-frameTolerance:
                # keep track of start time/frame for later
                resp_q.frameNStart = frameN  # exact frame index
                resp_q.tStart = t  # local t and not account for scr refresh
                resp_q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_q, 'tStartRefresh')  # time at next scr refresh
                # update status
                resp_q.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_q.clock.reset)  # t=0 on next screen flip
            if resp_q.status == STARTED and not waitOnFlip:
                theseKeys = resp_q.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _resp_q_allKeys.extend(theseKeys)
                if len(_resp_q_allKeys):
                    resp_q.keys = _resp_q_allKeys[-1].name  # just the last key pressed
                    resp_q.rt = _resp_q_allKeys[-1].rt
                    resp_q.duration = _resp_q_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *cross_q* updates
            
            # if cross_q is starting this frame...
            if cross_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_q.frameNStart = frameN  # exact frame index
                cross_q.tStart = t  # local t and not account for scr refresh
                cross_q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_q, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_q.status = STARTED
                cross_q.setAutoDraw(True)
            
            # if cross_q is active this frame...
            if cross_q.status == STARTED:
                # update params
                pass
            
            # if cross_q is stopping this frame...
            if cross_q.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_q.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_q.tStop = t  # not accounting for scr refresh
                    cross_q.tStopRefresh = tThisFlipGlobal  # on global time
                    cross_q.frameNStop = frameN  # exact frame index
                    # update status
                    cross_q.status = FINISHED
                    cross_q.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=question,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                question.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if question.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in question.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "question" ---
        for thisComponent in question.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for question
        question.tStop = globalClock.getTime(format='float')
        question.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code
        # Convert response time from seconds to milliseconds
        if resp_q.rt is not None:
            resp_q_rt_ms = resp_q.rt * 1000
        else:
            resp_q_rt_ms = None
        
        # Label the F/J response as Sí/No
        if resp_q.keys == 'f':
            resp_label = 'Sí'
        elif resp_q.keys == 'j':
            resp_label = 'No'
        else:
            resp_label = 'Sin respuesta'
        
        # Add data to the PsychoPy output file
        thisExp.addData('resp_key', resp_q.keys)
        thisExp.addData('resp_label', resp_label)
        thisExp.addData('resp_q_rt_ms', resp_q_rt_ms)
        question_sound.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if resp_q.keys in ['', [], None]:  # No response was made
            resp_q.keys = None
        trials.addData('resp_q.keys',resp_q.keys)
        if resp_q.keys != None:  # we had a response
            trials.addData('resp_q.rt', resp_q.rt)
            trials.addData('resp_q.duration', resp_q.duration)
        # the Routine "question" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "delay_trial" ---
        # create an object to store info about Routine delay_trial
        delay_trial = data.Routine(
            name='delay_trial',
            components=[cross_q_5, space_delay_3],
        )
        delay_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for space_delay_3
        space_delay_3.keys = []
        space_delay_3.rt = []
        _space_delay_3_allKeys = []
        # store start times for delay_trial
        delay_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        delay_trial.tStart = globalClock.getTime(format='float')
        delay_trial.status = STARTED
        delay_trial.maxDuration = None
        # keep track of which components have finished
        delay_trialComponents = delay_trial.components
        for thisComponent in delay_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "delay_trial" ---
        thisExp.currentRoutine = delay_trial
        delay_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_q_5* updates
            
            # if cross_q_5 is starting this frame...
            if cross_q_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_q_5.frameNStart = frameN  # exact frame index
                cross_q_5.tStart = t  # local t and not account for scr refresh
                cross_q_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_q_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_q_5.status = STARTED
                cross_q_5.setAutoDraw(True)
            
            # if cross_q_5 is active this frame...
            if cross_q_5.status == STARTED:
                # update params
                pass
            
            # *space_delay_3* updates
            
            # if space_delay_3 is starting this frame...
            if space_delay_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space_delay_3.frameNStart = frameN  # exact frame index
                space_delay_3.tStart = t  # local t and not account for scr refresh
                space_delay_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_delay_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                space_delay_3.status = STARTED
                # keyboard checking is just starting
                space_delay_3.clock.reset()  # now t=0
            if space_delay_3.status == STARTED:
                theseKeys = space_delay_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _space_delay_3_allKeys.extend(theseKeys)
                if len(_space_delay_3_allKeys):
                    space_delay_3.keys = _space_delay_3_allKeys[-1].name  # just the last key pressed
                    space_delay_3.rt = _space_delay_3_allKeys[-1].rt
                    space_delay_3.duration = _space_delay_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=delay_trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                delay_trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if delay_trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in delay_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "delay_trial" ---
        for thisComponent in delay_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for delay_trial
        delay_trial.tStop = globalClock.getTime(format='float')
        delay_trial.tStopRefresh = tThisFlipGlobal
        # check responses
        if space_delay_3.keys in ['', [], None]:  # No response was made
            space_delay_3.keys = None
        trials.addData('space_delay_3.keys',space_delay_3.keys)
        if space_delay_3.keys != None:  # we had a response
            trials.addData('space_delay_3.rt', space_delay_3.rt)
            trials.addData('space_delay_3.duration', space_delay_3.duration)
        # the Routine "delay_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_routine" ---
    # create an object to store info about Routine end_routine
    end_routine = data.Routine(
        name='end_routine',
        components=[end_text],
    )
    end_routine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_routine
    end_routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_routine.tStart = globalClock.getTime(format='float')
    end_routine.status = STARTED
    end_routine.maxDuration = 5.0
    # keep track of which components have finished
    end_routineComponents = end_routine.components
    for thisComponent in end_routine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_routine" ---
    thisExp.currentRoutine = end_routine
    end_routine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > end_routine.maxDuration-frameTolerance:
            end_routine.maxDurationReached = True
            continueRoutine = False
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # if end_text is stopping this frame...
        if end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.tStopRefresh = tThisFlipGlobal  # on global time
                end_text.frameNStop = frameN  # exact frame index
                # update status
                end_text.status = FINISHED
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end_routine,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            end_routine.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if end_routine.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in end_routine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_routine" ---
    for thisComponent in end_routine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_routine
    end_routine.tStop = globalClock.getTime(format='float')
    end_routine.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end_routine.maxDurationReached:
        routineTimer.addTime(-end_routine.maxDuration)
    elif end_routine.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
