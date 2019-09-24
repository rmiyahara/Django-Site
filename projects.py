# Used to save database for projects
from main_page.models import Project

p1 = Project(
    title = 'Ice Man',
    image = '/portfolio/iceman.png',
    github = 'https://github.com/rmiyahara/IceMan',
    technology = 'Visual Studio, C++',
    description_short = 'A desktop game which implements extensive use of object-oriented programming\'s class inheritance.',
    date = 'July 2017 - August 2017',
    description_long = 'This was my final project for UCLA\'s Computer Science 32: Introduction to Computer Science II. The objective of the game is to move the Ice Man throughout the field looking for oil barrels. He will quickly dig away any ice in his path and collect various power ups as he makes contact with them.\nThe Ice Man is not alone however; following him are protestors who are looking to end Ice Man\'s quest. They will eat away at Ice Man\'s health until he is forced to leave. In this case, the player will lose a life and start the level over.\nAll power ups, health, and score are kept on the top of the screen.\nThis project\'s main obstacle was creating a useful inheritence heirarchy for the player, enemies, and power ups. I wanted to avoid rewriting code, but had to make sure everything was working properly. Once I had finilized the heirarchy, the next big issue was writing the behavior for the protestors. While some of them move randomly in straight lines, others will move towards the player if they are within a certain amount of steps away (the number of steps increases with the level). On top of that, if a protestor is defeated, they must then leave the field, taking the shortest path to their spawn point. I eventually accomplished this using a queue-based algorithm on the cleared part of the field. Overall, this project really challenged my problem solving skills as well as my familiarity with C++.'
)
p1.save()

p1 = Project(
    title = 'One Call Away',
    image = '/portfolio/workday.jpg',
    github = 'https://github.com/Workday',
    technology = 'Python, Flask, uWSGI, NGINX, VMWare Products, MongoDB',
    description_short = 'An API project assigned to me during my 2019 summer internship with Workday.',
    date = 'June 2019 - September 2019',
    description_long = 'During the summer of 2019, I had the opportunity to Intern with Workday, Inc. I was stationed in Pleasanton, CA and put onto the Virtualization as a Service (VaaS) team. This team was in charge of communicating with companies like VMWare and Pure Storage to provide infrastructure to the company. My summer project was to convert our Python tool scripts into an easily accessible API.\nThis was accomplished leveraging the Flask API. I then hosted my API through a virtual server on one of Workday’s data centers. To handle requests, I learned about uWSGI and NGINX and implemented them onto the virtual server.\nLastly, for security and tracking purposes, I added a logging database to the API using MongoDB. This way, all calls made to the server could easily be tracked in one place in the case of a bug or error being found.',
)
p1.save()

p1 = Project(
    title = 'No Duines',
    image = '/portfolio/noduines.png',
    github = 'https://github.com/rmiyahara/NoDuines',
    technology = 'Arduino Software, C, Basic circuit reworking',
    description_short = 'Combining the technical mechanics of Super Smash Bros. Melee with the power of an Arduino!',
    date = 'February 2018 - March 2018',
    description_long = 'Despite being more than 15 years old, Nintendo\'s Super Smash Bros. Melee still thrives as a game with an active fanbase. Melee had the highest viewer count during Evolution 2018, the most prestigious fighting game tournament of the year outliving all other fighting games matching its age. One of its defining factors would be its demanding techniques, something the competitive community dubbes "Tech Skill".\nEach of these techniques has a unique name such as Wavedashing, L-Cancelling, and Multishining. While some of these are regularly used during competitive play, some of these techniques have an execution barrier that is too high for humans. These are discovered using tool assisted speedruns (TAS) where the game can be played out frame by frame. While the execution may be too high for humans, an Arduino has no such limits.\nBy soldering an Arduino to the motherboard of a controller, I am able to have my character perform these high-precision techniques at the push of a button. Examples of these can be seen in the video above. This modification is not meant for tournament play as it provides clear, unfair advantages. While this project is finished, I occasionally come back and add a few new macros.',
)
p1.save()

p1 = Project(
    title = 'Do Not Disturb',
    image = '/portfolio/android.png',
    github = 'https://github.com/rmiyahara/DoNotDisturb',
    technology = 'ReactNative, Android Studio, Java, HTML',
    description_short = 'An Android application that allows roommates to communicate through the use of a simple UI.',
    date = 'August 2018 - Present',
    description_long = 'As a student at UCLA where nearly everyone has a roommate or two, I noticed a major problem when it came to roommate communication. Often times, issues would stem from having overnight guests over. Communicating this can be uncomfortable for some, but when it isn\'t communicated at all, awkward walk-ins are bound to happen. The goal of this application is to provide roommates with a discrete way to tell their roommates when the room is occupied and when they are free to come back in.\nThis is implemented by using a simple homescreen which highlights one button that starts a timer and sends a push notification to connected roommates. The timer length is agreed upon by all roommates beforehand and will notify roommates with another push notification when the timer reaches zero. Roommates can easily be added in the "Roommates" tab on the left and various settings, such as timer length, can be toggled in the "Settings" tab.\nDevelopment for this application is currently ongoing with an expected completion date by the end of the year.',
)
p1.save()

p1 = Project(
    title = 'Birthday Tracker',
    image = '/portfolio/kyodo.png',
    github = 'https://github.com/rmiyahara/BirthdayTracker',
    technology = 'Python, Batch scripting',
    description_short = 'A short Python script which reminds the user which of their friend\'s birthdays are today or coming soon.',
    date = 'January 2018 - February 2018',
    description_long = 'This is a short Python script which includes a list of birthdays and corresponding names. When the script is run, it notifies the user which birthday is either today or coming soon. The idea for this program came to me while I was learning Python over winter break. During this time, I held a leadership position for UCLA\'s Kyodo Taiko, a cultural  performance group. One of the responsibilities of this position was to acknowledge each individual member\'s birthday. At the time, I didn\'t have an efficient system to do this. I would check the roster everyday which became very tedious over the course of the year. I used this as an oppertunity to apply Python to my everyday life.\nWhile this solution worked, I still had to remember to run it everyday. Luckily for me, I had just finished my unit in Linux Bash Scripting in class. I applied what I had learned with a few changes, since I was working with Windows this time around, to get the script to run each time I booted my computer. After I got this to work, I could finally stop worrying about missing a birthday for the rest of my term.',
)
p1.save()

p1 = Project(
    title = 'Health Tracker',
    image = '/portfolio/healthtracker.png',
    github = 'https://github.com/rmiyahara/Health-Tracker',
    technology = 'Android Studio, React Native, SciKit Learn, HTML, JavaScript, Python',
    description_short = 'An Android application which utilizes machine learning to track and predict eating habits on The Hill at UCLA.',
    date = 'November 2017',
    description_long = 'This project was made for UCLA\'s Hack on the Hill. The hackathon lasted for 16 hours where teams began working on various projects. This one was my first hackathon and really opened to my eyes to taking coding beyond the classroom. This project\'s main objective was to use the Hill\'s extensive dining menu and the user\'s eating habits to construct a suggested diet. As the user continues to log their foods, the application could continuously suggest meals which would be healthier and more enjoyable to the user.\nThe biggest issue we ran into during our development was time. Since development was only a day long, we had to cut a few features as well as exclude certain dining halls. On top of this, we were all working with technology we had little to no experience with at the time which made everything take longer than expected. While I was working on the front-end, we eventually all had to input nutritional values manually due to the values being saved in a picture on the dining menu site. Without the time to figure out image recognition, each item on the menu had to be added by hand making this process quite tedious.\nIn the end, our team was able to present the application with limited functionality. While very stressful, the entire hackathon experience was enlightening and helped spark my love for coding.',
)
p1.save()