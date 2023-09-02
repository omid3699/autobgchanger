# changing background automaticaly with python3 and feh

## created for i3 and awesome wm background problem

# run

    pacman  -S feh

# or

    apt-get install feh

# finaly

    #add the following line in your i3 config
    exec --no-startup-id ${path_to_app}/bg_changer.py
