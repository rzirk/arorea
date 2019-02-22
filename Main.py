import keyboard
import Process

print("1: Erkenne die 2 Hauptfarben im aufgenommen Bild")
print("2: Objekterkennung")
print("Q: Programm beenden")

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('1'):  # if key 'q' is pressed 
            Process.tellColor()
        if keyboard.is_pressed('2'):
            Process.tell_what_you_see()
        if keyboard.is_pressed('q'):
            
            break
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break  

