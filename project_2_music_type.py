from random import  choice

music_type = [['rock','motivated','angry','excited'],
              ['pop','happy','moody','energized'],
              ['rnb','calm','happy','in-love'],
              ['metal','angry','sad','powerful'],
              ['house','energized','chill','joyful']]

print('What mood are you in?')
mood = input()

for item in music_type:
    if item[1] == mood:
        print(mood + ' music: ' + item[0])
    elif item[2] == mood:
        print(mood + ' music: ' + item[0])
    elif item[3] == mood:
        print(mood + ' music: ' + item[0])

