# Used to save database for projects
from main_page.models import Project

p1 = Project(
    title = 'Ice Man',
    image = '/portfolio/iceman.png',
    github = 'https://github.com/rmiyahara/IceMan',
    technology = 'Visual Studio, C++',
    description_short = 'A desktop game which implements extensive use of object-oriented programming\'s class inheritance.',
    date = 'July 2017 - August 2017',
    description_long = 'This was my final project for UCLA\'s Computer Science 32: Introduction to Computer Science II. The objective of the game is to move the Ice Man throughout the field looking for oil barrels. He will quickly dig away any ice in his path and collect various power ups as he makes contact with them. The Ice Man is not alone however; following him are protestors who are looking to end Ice Man\'s quest. They will eat away at Ice Man\'s health until he is forced to leave. In this case, the player will lose a life and start the level over. All power ups, health, and score are kept on the top of the screen. This project\'s main obstacle was creating a useful inheritence heirarchy for the player, enemies, and power ups. I wanted to avoid rewriting code, but had to make sure everything was working properly. Once I had finilized the heirarchy, the next big issue was writing the behavior for the protestors. While some of them move randomly in straight lines, others will move towards the player if they are within a certain amount of steps away (the number of steps increases with the level). On top of that, if a protestor is defeated, they must then leave the field, taking the shortest path to their spawn point. I eventually accomplished this using a queue-based algorithm on the cleared part of the field. Overall, this project really challenged my problem solving skills as well as my familiarity with C++.'
)
p1.save()