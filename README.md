# Overview
I created a relatively simple UI that lets a user select from a slate of classes and store that selection serverside. Signing up for courses is a big part of learning, so I decided that this was a good start to incorporate.

The homepage is at `localhost:8000/app/` (or whatever port the Django app decides to throw you). You can start the server by running `python3 manage.py runserver` from the `takehome` directory.

## Design Decisions Made

- Centering the pages. The default for web pages is left-aligned, but it makes the website a little lopsided. It feels a lot more natural to read down the middle.
- Modifying the form used on the class selection page. I used large divs contained inside labels to toggle invisible checkboxes. This way, it's a lot easier to make a selection; instead of having to click the small checkbox or its label, clicking anywhere inside of the big rectangle works.
 - In the same vein, using a background color to denote both mouseover and selection. With the checkbox invisible, there needed to be a way to tell if a course was selected. Using the same shade of color at different intensities makes logical sense for a user.
- I set the grid of classes to choose from to be 3 wide so that the user wouldn't have to scroll as much; there's not a lot of data presented, so it made sense to condense the UI to allow for an easier viewing experience.
- If a user didn't select any classes, there's a notice that tells them that when they submit.

## Development Decisions Made

- Class time data is stored in a JSON blob. This makes it easy to have a variable number of timeslots, since the JSON array can hold as many objects as needed.
- Time data is stored in integers: day 1-5 for day of the week and starttime/endtime stored in minutes since midnight that day. Although it takes a little bit more time to read for a human, it's easier to parse for the computer, and makes it easy to shift a class over by 30 minutes or a day if needed.
- I used a learner id system to store schedule data. Although the current implementation generates a new learner id for each submission, in general we'd like the learner id to be consistent with whoever's logged in at the time. That way, a user can overwrite their previous class submissions. You can also use the learner id to toggle the courses that were previously picked on if the learner revisits the page.

# Future Improvement
One thing that I ran out of time to implement was a check for if two classes overlapped. Ideally, if two classes overlapped, there'd be a warning that popped up notifying of that.

The logic would go as follows:
````
- When a class is toggled, run through the following checks.
- For each pair of classes, check to see if any of their timeslots fall on the same day.
- If they do, check those timeslots. If both timeslots' start times come before both end times, then the classes overlap.
  Record the pair of classes as a timing conflict, ideally with the conflicting timeslots as well.
- Keep going until all pairs are exhausted. If there are any timing conflicts, display all of them, otherwise don't display anything
  (nothing is wrong).
````

This logic is extensible to checking if two classes fall back-to-back, as well.

I set up the context delivered to the template to account for this implementation, which is why the context delivered preserves the numerical representation of the timeslots.

Other ideas:

- Setting up toggles to display different course info. Courses usually have a lot of info associated: credit hours, instructor, requirement-related. Displaying all of them at all times might be a little messy, so having toggles to display this info would be useful.
- Creating a graphical representation of the schedule to display both during and after selection. This way, it's easier to see what times are free, when certain days are taken up, etc. Such a visual being automatically updated with each selection would be best.

# Final Note
This project was written in Django. I think it's important to note that when I started this project, I did not know Django; I did have minor experience from a course I took in college with Flask, but they are not totally identical.

In fact, coming into the project, I realized that I did not have much experience with any of the technologies suggested. I think I misunderstood during the prior interview when answering this question; I have experience with the Wordpress.com interface but not the development kit provided by Wordpress.org, and I completely mixed up React.js and Node.js. Apologies for this; I'm not very good at remembering the names of software I've learned about, just how to use them, which resulted in some miscommunication.

I know that this project falls short in several ways, but I hope that it's able to show a bit of what I can do, especially given a somewhat protracted schedule and a new technology. Thank you for the consideration!

~ Kenny Wang