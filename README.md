# RockPaperScissors
A basic Rock Paper Scissors game built using Python, Tkinter UI

## Table of Contents
 - [How the game works](#Howthegameworks)
 - [Features](##Features)
 - [Images](##ImagesoftheGame)
 - [Technologies Used](##Technologiesused)

## How the game works
 - Once the game starts, you choose between Rock, Paper, Scissors to win a game to 3 with the computer
  - The goal of the game is to beat the computer by 3

## Features
 - User Friendly GUI 
 - Shows User, AI score
    - Ability to choose between Scissors, Rock and Paper with Buttons
    - Exit out of Game with Button
 - AI Components


## Images of the Game
![Screenshot1](https://private-user-images.githubusercontent.com/52137719/371736865-43fa8e5e-a9bb-4b92-885b-8b46893bd8be.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc1MDU4MTAsIm5iZiI6MTcyNzUwNTUxMCwicGF0aCI6Ii81MjEzNzcxOS8zNzE3MzY4NjUtNDNmYThlNWUtYTliYi00YjkyLTg4NWItOGI0Njg5M2JkOGJlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTI4VDA2MzgzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkyYWNkMDFiNzZhYWVlZDBjZDUwNzk0YzYwNGVkZGFjOTE3OGYwMzJmNzBhZTZlYzUxNDgyNDVjYzVhMTBkNTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.uIMT5imTiUkp_sUIa3viPA_IuZeLWgN700CYheXduEE)

![Screenshot2](https://private-user-images.githubusercontent.com/52137719/371736956-13bc30cf-c13d-4134-9858-dce14819e926.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc1MDU4MTAsIm5iZiI6MTcyNzUwNTUxMCwicGF0aCI6Ii81MjEzNzcxOS8zNzE3MzY5NTYtMTNiYzMwY2YtYzEzZC00MTM0LTk4NTgtZGNlMTQ4MTllOTI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTI4VDA2MzgzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBiYzg3OWQ2ZmZmMmU4NTI4NGFmYzM5NWI3ZDljMDc0NTA1YTAyNWNmZjhjYTk2NjQ0ZTcwYWE0NzhiN2UxNzAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.db_99lxzvfo61UJ7ltenTRnE-E9nvn-eT2o3NxkCmHE)

![Screenshot3](https://private-user-images.githubusercontent.com/52137719/371737039-9ffb48ab-e9e4-4a87-9bfd-81525fcb0c94.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc1MDU4MTAsIm5iZiI6MTcyNzUwNTUxMCwicGF0aCI6Ii81MjEzNzcxOS8zNzE3MzcwMzktOWZmYjQ4YWItZTllNC00YTg3LTliZmQtODE1MjVmY2IwYzk0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTI4VDA2MzgzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYzMWY2MWZhNzQ2M2VlNDJhNGZmZDViZGIyZWQ1YmUzZDYxYzY2M2YxMTEyYzU4MzE0MDU3ZTFhZWRkNGQyZGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.dyOjfPGFe6nFaEbhaV44NR8-h1pVH4Ff7X3Lb3Dy4dk)

## Technologies and Resources used 
 - [Python3](https://www.python.org/)
 - [Tkinter](https://docs.python.org/3/library/tkinter.html)
 - [Rock_Paper_Scissors_Wiki](https://en.wikipedia.org/wiki/Rock_paper_scissors)


## Authors

- [@TrenyceCodes](https://github.com/TrenyceCodes)



