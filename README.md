# Yousician

A tool to search string from Yousician portal

# Scope
As an assignment work, this tool tries to search the given string and return a sorted list of all songs and their artist names.

# Environment
The tool is using Python, Playwright and urllib.

Try to install or update to newest python, and Playwright on your PC so that the app can be run.

`pip install playwright urllib`

`playwright install`

or: `python -m playwright install`

* NOTE   Playwright requires Python 3.7+

# Usage
If the string including spaces, the string must be closed by a pair of "

`python search.py ["footprints in the sand"]`
`python search.py [Tonight]`

# Output sample

The output is a list with tuples (song and artist)

  - example 1

`python search.py "footprints in the sand"`

Searching: footprints in the sand

Corazon Partio, Alejandro Sanz

In The Hall Of The Mountain King, Edvard Grieg

I Stand Alone, Godsmack

Castles Made Of Sand, Jimi Hendrix

In The End, Linkin Park

Ride Of The Valkyries (in Am), Richard Wagner

Seasons In The Abyss (E), Slayer

Seasons In The Abyss (Eb), Slayer

Eye In The Sky, The Alan Parsons Project

Anarchy In The AI, The Yousicians

Back In The App, The Yousicians

Chilling In The Sun, The Yousicians

Feel The Beat (in C), The Yousicians

Hand Clapper, The Yousicians

In Her Majesty's Secret Band, The Yousicians

In The Horizon, The Yousicians

Jammin' In The Barrio, The Yousicians

Lost In The Wilderness, The Yousicians

Milk & Honey Land, The Yousicians

One Man Band, The Yousicians

Playing In The Park, The Yousicians

Sad Android, The Yousicians

The Great Pig In The Sky, The Yousicians

The Land of Harmony, The Yousicians

Up In The Air, The Yousicians

Wishing In The Night, The Yousicians

Black Velvet Band, Traditional

Brown Girl In The Ring, Traditional

When The Saints Go Marching In (count-in), Traditional

Whiskey In The Jar, Traditional

Cats In The Cradle, Ugly Kid Joe




  - example 2
  
`python search.py Tonight`

Searching: Tonight

Vincent (Starry Starry Night), Don McLean

Wonderful Tonight, Eric Clapton

Midnight Train To Georgia, Gladys Knight & The Pips

Night On Bald Mountain, Modest Mussorgsky

A Night To Rewind, The Yousicians

A Night To Rewind (short), The Yousicians

Flying Through The Night, The Yousicians

Open All Night, The Yousicians

Waltz Into The Night, The Yousicians

Wishing In The Night, The Yousicians

Wizard Knight, The Yousicians

O Holy Night, Traditional

Silent Night, Traditional

Silent Night (in G), Traditional

Queen Of The Night, Wolfgang Amadeus Mozart

Queen Of The Night (short), Wolfgang Amadeus Mozart


