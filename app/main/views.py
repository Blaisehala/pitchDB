
from flask import render_template, url_for
from . import main 
from .. models import Pitch





@main.route('/')
@main.route('/home')
def home():
  title= 'Pitch'
  business_pitches = Pitch.get_pitches('business')
  entertainment_pitches = Pitch.get_pitches('entertainment')
  music_pitches = Pitch.get_pitches('music')
  sport_pitches = Pitch.get_pitches('sport')
  return render_template('home.html',title=title, business=business_pitches,entertainment=entertainment_pitches,music=music_pitches,sport=sport_pitches)



@main.route('/pitches/business_pitches')
def business_pitches():

    pitches = Pitch.get_pitches('business')

    return render_template("business_pitches.html", pitches = pitches)



@main.route('/pitches/entertainment_pitches')
def entertainment_pitches():

    pitches = Pitch.get_pitches('entertainment')

    return render_template("entertainment_pitches.html", pitches = pitches)


@main.route('/pitches/music_pitches')
def music_pitches():

    pitches = Pitch.get_pitches('music')

    return render_template("music_pitches.html", pitches = pitches)


@main.route('/pitches/sport_pitches')
def sport_pitches():

    pitches = Pitch.get_pitches('sport')

    return render_template("sport_pitches.html", pitches = pitches)
