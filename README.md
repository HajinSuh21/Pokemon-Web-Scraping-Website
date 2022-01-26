# Pokemon-Web-Scraping-Website
- My first personal project
- Scrapes tcgplayer.com for updated prices on Pokemon cards
- Displays the data in a user friendly website

# Skills:
HTML, CSS, Python, Web Scraping

# Background:
This website takes data from an external Pokemon Price website that constantly updates due to supply and demand.  For my first project, I wanted a way to simply choose which Pokemon set I would like to view prices for an individual card for and search for the specific card in a search bar.  I also wanted to create this functionality in a form of a website.  The resulting project is a website that is styled using HTML and CSS and has functionalities that were created with Python and Web Scraping.

# Get Started:
## Prerequisites:
- Python
- pip

## pip Installs:
```
pip install bs4
pip install flask
pip install requests
```
## Running the Site/Program
Run the
```
main.py
```
program and it will create a http port.  Click and open the port on browser.

# Home Page
The home page looks like this...
![image](https://user-images.githubusercontent.com/97658524/149619199-c66202d3-02ad-4026-a602-a155bbe05ffa.png)
![image](https://user-images.githubusercontent.com/97658524/149619205-55f6fde3-10d8-406c-9766-04ff95cd97e9.png)
The Pokeball is clickable and returns to the home page.
Each set (Celebrations, Fusion Strike, and Evolving Skies) are clickable and will lead to their respective html pages.

# Example Page - Celebrations Page
![image](https://user-images.githubusercontent.com/97658524/149619283-3001c801-5757-4a4b-9c9d-2bcd2c63d3cc.png)

The search bar takes user input and is expandable when the user's mouse hovers it.
![image](https://user-images.githubusercontent.com/97658524/149619328-44173204-d93b-494e-a728-8c5d4620578d.png)

The menu is also expandable and takes the user to different pages.
![image](https://user-images.githubusercontent.com/97658524/149619390-b5e28ff9-549d-4316-83dd-5752ff38b184.png)

# Example Output - Celebrations Page
The search bar will return the input's desired Pokemon's name, number in the set, and its current updated price.  Prices always change so it's important that my site reflects the current data (which it fulfills through Web Scraping).

For example, since Charizard is in the Celebrations Set, it is a valid input and returns as of 1/15/2022 @ 1:06am...
![image](https://user-images.githubusercontent.com/97658524/149619466-17bc4405-7b7b-405f-b9d0-086e349bb2f0.png)

However, if a Pokemon is not included in the particular set, it will return something like...
![image](https://user-images.githubusercontent.com/97658524/149619639-5e470ebe-e967-4aae-8711-6992603ecdd6.png)

# What I Enjoyed About This Project
- I got to learn so many new things-I've never worked with HTML, CSS, Python, and BeautifulSoup4 before.
- I found myself always trying to add new things like hover capabilities on the search/navigation bars to make the website look cooler.
- It was more than HTML/CSS design, I got to use problem-solving in figuring out how to get data from another website and only output it under certain conditions (whenever I figured something out, it felt refreshing).
- I used what I learned from CS courses at Vanderbilt to aid me in solving these problems (booleans, for-loops, lists, if-statements, and even debugging).
- Although this may seem simple for many others, I feel very proud of myself for being able to complete my vision-I've always wanted to try create something like this.
- Overall, this was an awesome project because I combined two things I love (Pokemon + Coding).

# Problems/Solutions:
- In Flask, it is necessary for CSS and images to go into a folder named "static".  I did not know this and for 3 hours, I was stuck figuring out why my CSS wasn't applying to my HTML pages.
- I had to figure out a way to check if the input Pokemon was in the set.  So, I used lists and appended to store the Pokemon's name, number, and price from the tcgplayer.com site.  Then, I used a for-loop to check if the Pokemon was in the set.
- At one point, the error message: "___ was not found in this set, please try again" popped up even though I hadn't inputted anything in the search bar.  In order to fix this, I used a boolean to keep track of whether or not the Pokemon was found.  I used a second boolean to keep track of whether or not the Pokemon was not found.  Then, I only printed the error message when both booleans were set to True.
- Many more problems...

# Future Aspirations:
Since there is no written database and the data is taken externally, it was difficult to figure out a way to put pictures along with each output (looks kind of boring as of now!).  In the future, I'd like to find a way to add pictures and make the website more fun.
