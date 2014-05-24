Finance
=======

This is a suite of Python modules containing functionality for
analysing personal finances.

This README is very high level currently. It will be updated...

Feature List
------------

- Nada. Zip. Nil.
- Income model [TODO]
- Accomodation and bills cost model [TODO]
- Vehicle cost model [TODO]
- Bank statement chomper [TODO]
- Speculative budgets [TODO]
- "Live" budget [TODO]

Usage
-----

Of what..?

Rationale
---------

I'm creating this primarily because I'm looking at jobs; it started
out as a tool for looking at the feasibility of relocation, commuting,
and general "is this salary right for me". In practice, I found most
of this to be actually developing a speculative budget and useful in a
more general sense.

Everyone manages personal finances in different ways, but usually when
push comes to shove it involves sitting down with a calculator (or
spreadsheet) to make some sort of budget, or assess a decision/option
which has some kind of significant impact. This is fine but it's error
prone and therefore repetitive and laborious when taking an
appropriate amount of care. Looking at things properly can be as
involved as you want to make it and some advice out there on
budgeting is actually pretty decent in this respect. On the other
hand, even decent budget templates suffer from broad categories and
(justifiably) simple models (e.g. "Petrol cost per annum.") which
still leaves you doing (unnecessary) and often repetitive, inaccurate
sums. You better hope you got it right if you want to rely on it..!

A final caveat. I don't care too much about money and I'm content to
just tick along within my means. I'm not bad at this but I find myself
in a situation where this is pretty risky, which is why I'm writing
this.

Design Goals
------------

This is intended to

- Provide a mechanism for creating an accurate budget from little
  information.
- Structure and present information for analysis "at a glance".
- Model more complex aspects of personal finances in a sensible way
  (e.g. "How much will it cost me to commute to this job, with X 
  pretax salary?").

It is *not* intended to replace the user as the architect and decision
maker. It is also *not* intended to provide 

Roadmap
-------

Not in strict order.

1. Base framework for modelling budget items and transactions.
2. (Python) user-friendly budget creation mechanism.
3. Mechanism for comparing budgets to real spending (e.g. from bank
   statements/transaction sheets).
4. Models for multi-variable elements (e.g. fuel cost) with room for
   extension.
5. A mechanism for presenting aggregated information to the user with
   an appropriate degree of transparency.
6. Visualisation (graphs, charts).
7. Some sort of UI (this is very much least-concern at this point)
