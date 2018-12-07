DESIGN.MD

EasyDonor - an app built in Django that will make it easier for non-profits to track donations and send thank you letters.

I built the project in my mac terminal with Atom as my editor. While I tried many, many different things that you will see evidence of in my git commits, ultimately I gave up trying to use Heroku and MySql in order to save time. I consider this project to still be in the very early stages, and will move into something better when I am further along.

That being said, it does lots of stuff already! Granted, most of it is in the admin tools, but I built those models and came up with the structure.

Easydonor has 3 apps built into it:

The users app deals with registration, login and authentication, and also user profiles (future).

The contacts app deals with contact lists, their forms, and their tables.
* Contacts
* Donors
* Vendors

The easydonorapp deals with the function of the project.
* deposit slip
* layout
* home page
*anything else I decided I need to add to this.

I made a Trello board for the project. The first column has links to all of the files associated with this project. https://trello.com/b/i8mKALZ5/easy-donor-build

You can see the things I did and did not do yet in the trello. I was able to make the database almost to my liking. There are a few things I need to make required or make not required and many little fixes I will eventually get around to.

It works like this:
Registration/Login creates an authorized user that can only see things while logged in. My current dilemma is that ANY authorized user can see ALL of the content, even if it belongs to another user. The entire internet told me that a thing called Allauth was the solution to my problems, but it actually ate about two of my days because, ultimately, it has two init.py files in separate directories, and my computer wanted to only acknowledge one of them even if I typed out the entire file path. Why? I will never know. My workaround was to begrudgingly change all of the imports to import ..otherinit.py, which was tricky, because both files had the same name. DID NOT SAVE ME TIME. And it didn’t fix my little authentication issue. But now you can log in with google, so that’s pretty cool.  I temporarily disabled the feature while I am doing the rest of the site, because it was getting in the way.
The users will have their own profile as well as a company profile to eventually use for reports and tax id info to go on the tax letters.
Contacts is just a really fancy address book made up of one Contact model with several listviews. With the javascript on the contact-list.html template I was able to make buttons that change the view. Rumor has it that there is an easier way to do this, but I haven’t had time yet to do that research. Each contact is going to have their own profile, which will link their “pledges” both paid and unpaid, payments, and contact information.
The main app contains my layout file, home page, error code template and things like that. But it also contains the main functions of this app. The deposit slip doesn’t exist yet because of one major reason. I was unable (yet!) to figure out how to make individual profile pages in a details view. For some reason none of the detailview, URL, get_absolute_url tutorials on the internet could get my urls to work. Honestly I can’t code another thing until they do. If I can’t separate users, how can I actually do anything with them?
Answer: The django admin page! But that wasn’t working for me for the longest time. I had to install this thing called Admin Tools and then totally restructure the TEMPLATE = part of my settings.py.

Side Note: You’d think some of these things would just be default. Why in the world was it this difficult?

From the admin page you can see how a donor makes a pledge. Then they pay that pledge. The pledge will be deposited in the bank alone or with others, and all at once on one deposit slip (which doesn’t exist yet) the user will be able to add in donations, payments, and even edit the contact information.

I have high hopes for this. It was a great time. I will continue to do this project, but I will sleep at night now.

Link to repository  https://github.com/TammyLaforest/donor-track
