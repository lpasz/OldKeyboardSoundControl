from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

g_cmd = False
g_alt = False
g_home = False
g_end = False
g_arrow_up = False
g_arrow_down = False
g_arrow_left = False
g_arrow_right = False

def Shortcuts(_key):

    def isVerifiedKeys(key):
        isNotcmdOrAlt =  not (key is Key.alt or key is Key.alt_gr 
        or key is Key.alt_l or key is Key.alt_r 
        or key is Key.cmd_l or key is Key.cmd 
        or key is Key.cmd_r) 
        
        isMonitoresKeys =  (key is Key.home or    
        key is Key.end or key is Key.up or
        key is Key.down or key is Key.left or
        key is Key.right)

        return isMonitoresKeys and isNotcmdOrAlt

    global g_cmd 
    global g_alt 
    global g_home 
    global g_end 
    global g_arrow_up 
    global g_arrow_down 
    global g_arrow_left 
    global g_arrow_right 

    if isVerifiedKeys(_key):       
        if g_cmd and g_alt and g_home:        
            keyboard.press(Key.media_play_pause)  
            print('Pause/Play')          
        if g_cmd and g_alt and g_end:
            keyboard.press(Key.media_volume_mute)
            print('Muted') 
        if g_cmd and g_alt and g_arrow_up:
            keyboard.press(Key.media_volume_up)
            print('Volume Up') 
        if g_cmd and g_alt and g_arrow_down:
            keyboard.press(Key.media_volume_down)
            print('Volume Down') 
        if g_cmd and g_alt and g_arrow_left:
            keyboard.press(Key.media_previous)   
            print('Previous')      
        if g_cmd and g_alt and g_arrow_right:
            keyboard.press(Key.media_next)
            print('Next') 

def on_press(key):
    global g_cmd 
    global g_alt 
    global g_home 
    global g_end 
    global g_arrow_up 
    global g_arrow_down 
    global g_arrow_left 
    global g_arrow_right 

    if key is Key.alt or key is Key.alt_gr or key is Key.alt_l or key is Key.alt_r:
        g_alt = True
    elif key is Key.cmd_l or key is Key.cmd or key is Key.cmd_r:
        g_cmd = True
    elif key is Key.home:
        g_home = True
    elif key is Key.end:
        g_home = True
    elif key is Key.up:
        g_arrow_up = True
    elif key is Key.down:
        g_arrow_down = True
    elif key is Key.left:
        g_arrow_left = True
    elif key is Key.right:
        g_arrow_right = True
    Shortcuts(key)


def on_release(key):
    global g_cmd 
    global g_alt 
    global g_home 
    global g_end 
    global g_arrow_up 
    global g_arrow_down 
    global g_arrow_left 
    global g_arrow_right 

    if key is Key.alt or key is Key.alt_gr or key is Key.alt_l or key is Key.alt_r:
        g_alt = False
    elif key is Key.cmd_l or key is Key.cmd or key is Key.cmd_r:
        g_cmd = False
    elif key is Key.home:
        g_home = False
    elif key is Key.end:
        g_home = False
    elif key is Key.up:
        g_arrow_up = False
    elif key is Key.down:
        g_arrow_down = False
    elif key is Key.left:
        g_arrow_left = False
    elif key is Key.right:
        g_arrow_right = False
    Shortcuts(key)


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()




