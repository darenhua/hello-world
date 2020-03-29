def wordcount(string):
    count = 0
    for i in string.split():
        count += 1
    return count

words = wordcount('''My first passion was animation. Watching animated stick-men beat each other up on YouTube
and beautiful stories in anime motivated me to create animations of my own. I greatly enjoyed practicing animating,
even as I struggled to draw with a mouse on pirated Macromedia Flash 7 software. When I finally became able to draw fluid stick-man motion,
rather than its past limp and unnatural staggering, I was overjoyed.But as time passed, I realized that animation was what I wanted to do forever. ''')

print(words)
