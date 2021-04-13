# Stardew Valley Resource Tool

Live site: <https://sdv-resource-calculator.vercel.app/>

Frontend Repo: <https://github.com/kirstengreen/sdv-resource-calculator>

API Repo: <https://github.com/kirstengreen/sdv-resource-calculator-api>


## Overview

For my capstone project at General Assembly (Jan - Apr 2021), we were required to make an application that used a frontend and database while learning something new in the process. I decided to begin creating an app I have wanted to build for almost 2-years. As a builder/planner Stardew Valley player, I often visited the [Stardew Valley Wiki](https://stardewvalleywiki.com/Stardew_Valley_Wiki) page to make calculations for the items I wanted to craft. I wanted to create a tool that helped make this process easier and quicker, so I could get back to farming for all the resources I needed to build my items. As for the new technology, I decided to learn Vue.js and I couldn't be happier with that decision.


## Technologies

* HTML5
* CSS3
* JavaScript
* Vue.js
* Python
* Flask
* npm
* Fetch API
* Cors
* Vercel
* Heroku Postgress
* VS Code
* Figma - Wireframes
* Notion - Project planning


## User Stories

* As a user, I can see a list of craftable items
* As a user, I can search the crafatble items to find the item I am looking for
* As a user, I can select an item to view more about the item
* As a user, when I view an item, I can see the resources needed to build the item
* As a user, when I view an item, I can change the amount of items I need to build and see the resources dynamically change based on that number


## v1 Features

* Users can see a complete list of available craftable items on the Calculator page
* Users can search through all of the currently available craftable items to find a keyword match. In v1, search is limited to item name matches
* Search results replace the full item list with items that match the keyword typed
* Users can select a craftable item from the full list or research results list to view item details
* Users can calculate how many resources they need by inputting how many of the craftable items they would like to make. Calculations are automatic


## Future Features and Improvements

* Complete the craftable item database API to provide a full craftable items list for the app
* Improve how the resources needed for craftable items are rendered (add images of them, etc.)
* Design improvements
* Add animations and transitions
* Add filtering options so users can filter all craftable items by category (i.g., Artisan Equipment, Refining Equipment, Fences, Seeds, etc.)
* Search improvements
* Add user accounts and authentication
* Allow users to save, edit, and delete their calculations
* Allow users to create collections, so they can group craftable items and get total resource counts for all items
* Allow users to save, edit, and delete their collections
* Create additional formulas for resources that might need resources of their own to be made (i.e., you need coal and gold ore to make gold bars)
* Add other build items such as buildings


## Known Bugs

* When a user searches for a keyword that returns no results, the Results Not Found component will not render properly
* Input on item calculation pages infinitely intakes a user's input. Want to find a way to restrict this without the user having to hit enter
* Fix what renders on the calculation pages when the input field is empty
* Normalize does not seem to be working as intended, and some adjustments need to be made to improve spacing and sizing across the site. 


## Resources and Credit

### Special thanks to the Stardew Valley Wiki:
* <https://stardewvalleywiki.com/Stardew_Valley_Wiki>
* For the item data and images
* Without Stardew Valley's dedicated fanbase (and ConcernedApe of course!), obtaining the data I needed for this project would have been much harder


### Tutorials that helped me learn Vue.js:
* Vue 3 for Beginners by The Net Ninja: <https://www.youtube.com/playlist?list=PL4cUxeGkcC9hYYGbV60Vq3IXYNfDk8At1>
* Vue JS Crash Course 2021 by  Traversy Media: <https://www.youtube.com/watch?v=qZXt1Aom3Cs>