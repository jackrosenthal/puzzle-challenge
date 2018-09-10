How to organize the Puzzle Challenge
====================================

This document covers what tasks need done to run the CS@Mines Puzzle Challenge.
If you're looking for the actual challenge itself, go to our website:

https://puzzles.mines.edu

Theme Selection
---------------

In Fall 2017, we did not have a general theme. Things felt more "fun" when we
had a theme in Fall 2018 (time/clocks).

It's pretty easy to adapt puzzles to fit within a theme, so this can be
something you think about while designing random puzzles, or something that you
decide on at start.

Puzzle Creation
---------------

* Create 6-10 puzzles
* Ask if they want to contribute a puzzle or two: Tom Williams, contacts at
  Google. I also think it would be cool to reach out to some CS@Mines Alumni
  and see if this is something they would want to do too!
* Proofread puzzles and send to Tom or other helpers on this project
* Try and rank the puzzles by: **obscurity** and **work effort**

  - Obscurity: how hard it is to find the answer because it is hidden
  - Work effort: the amount of effort that will be required to solve the
    puzzle, *not counting effort to defeat obscurities*

For example, here is how I would rank some past puzzles:

* **Hopskotch:** Obscurity: 2/5, Effort: 2/5
* **Master Mind:** Obscurity: 2/5, Effort: 3/5
* **Nono-cheating:** Obscurity: 2/5, Effort: 4/5
* **It's a Trap:** Obscurity: 4/5, Effort: 2/5
* **Color Coded:** Obscurity: 5/5, Effort: 2/5
* **f(f(...f(n))):** Obscurity: 5/5, Effort: 1/5
* **Time for what:** Obscurity: 2/5, Effort: 3/5
* **Clock Tower:** Obscurity: 1/5, Effort: 2/5
* **Time Acrostic:** Obscurity: 1/5, Effort: 3/5
* **Time-Travel Tour:** Obscurity: 5/5, Effort: 2/5
* **The Hunt:** Obscurity: 2/5, Effort: 4/5
* **Spin Like a Clock:** Obscurity: 3/5, Effort: 4/5
* **Movies:** Obscurity: 6/5, Effort: 1/5
* **Secret Puzzle:** Obscurity: 6/5, Effort: 2/5

Generally, it's good to start the competition with some low-obscurity,
medium-effort puzzles, and put the high-obscurity puzzles near the end. This
will keep solvers engaged when they are first starting.

You're going to want to make sure the competition has a good balance of
obscurity and effort-based puzzles. Too much effort-based puzzles, and you'll
just get the people who dedicate a lot of time who win, and if too much
obscurity-based puzzles, people will loose engagement.

Considerations
~~~~~~~~~~~~~~

* People often print puzzles to work on them. Make sure the puzzles are still
  solvable even when printed in monochrome. This also means your puzzles will
  be friendly to the colorblind too!
* You can always lead to answer that is off-the-page (e.g., webpage, telephone
  number, have been used in the past).
* Cutting things out of the page is fun!
* Don't give advantage to people who have knowledge of some non-universal but
  pretty well known knowledge (for example, needing to have taken a certain
  Mines course). It is OK to use *really* domain-specific knowledge, as almost
  everyone will have to look that up. (for example A-traps in "It's a Trap" or
  EBCDIC in "Color Coded").

Tooling
~~~~~~~

I had used XeTeX to produce the puzzles in the past. I did this because it was
a good workflow for me, and made it easy to keep formatting consistent across
puzzles. If you choose to use this workflow, see the examples from prior years
on how to use.

You, of course, could use any tool you want. The puzzle challenge website just
needs PDF files.

Setting up the Website
----------------------

The puzzles website is located at https://puzzles.mines.edu. As of this time of
writing, this is hosted on *mastergo*, Tracy's web server. Conveniently, I was
also the sysadmin of mastergo. But this may be different in the future.

In particular, you may find it worthy to move the website to its own server,
especially if the future sysadmin of mastergo is not involved in the Puzzle
Challenge (reduce the risk of puzzles or solutions being leaked).

On that note, it's probably advisable to try and involve the sysadmin (give
them responsibilities related to the website) as that way you don't have to
worry about it running on their server.

Tasks:

* Promote involved people to admin group in database:

  - Existing admin (Jack, Tracy, or Tom) must go to ``Admin Panel > Group >
    admin`` and edit. Add involved users to the group.

* Create a competition:

  - ``Admin Panel > Competition > New Competition``
  - Fill out relevant details (name, dates, prize, etc.)
  - Do not need to add puzzles in select box, you can do later

* Upload puzzles, for each puzzle:

  - ``Admin Panel > Puzzle > New Puzzle``
  - Fill out relevant details (name, upload PDF, solution, etc.)
  - Assign correct author
  - You do not need to select any answers: this gets done by grader interface

Hacking
~~~~~~~

The website codebase is at:

https://github.com/jackrosenthal/puzzle-challenge-website

It is written in Python using TurboGears 2.3. I think it should be fairly easy
to hack upon for someone who has seen an MVC-style web application and Python
before.

Advertising
-----------

* Make flyer and slide and give to both Tracy and Shannon
* Put two postings in daily blast: one for a few days before, and one for the
  day it starts.
* Advertise on ACM and LUG mailing lists
* Send an email the night before it starts to all users registered on the site.
  I find this easy to get a list using a SQL query::

   SELECT STRING_AGG(CONCAT(user_name, "@mines.edu"), ",") FROM tg_user;

  Paste into BCC field of an email.

Running the challenge
---------------------

* Morning it starts: monitor site closely, monitor email closely, have someone
  ready to put out a fire.
* Assign someone to grading answers. This is easiest to do by checking in every
  few hours and marking as correct/incorrect. If you keep up on it (and don't
  leave till end), you can watch the leaderboard (which is fun!) and you'll be
  ready to release the leaderboard as soon as the challenge ends.
* 24-hours left: send a reminder to the list of users on the site

After the Challenge
-------------------

* Make sure there are no answers left to grade.
* Send an email to everyone with a link to the leaderboard and solutions.
* Contact Google for potential date options for top-ten lunch.
* Organize cash prizes with winners and Tracy/Shannon.
