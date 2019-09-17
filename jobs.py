# Used to save database for Jobs
from main_page.models import Job

j1 = Job(
    company = 'Workday',
    position = 'Software Development Engineer Intern',
    description1 = 'Developed an API for VMWare tools using Flask, uWSGI, and NGINX.',
    description2 = 'Implemented logging system for API using MongoDB.',
    description3 = 'Refactored Python scripts for use with the API.',
    description4 = 'Documented unit tests, usage, and results in detail.'
)
j1.save()