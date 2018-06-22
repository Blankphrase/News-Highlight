from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():

    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    science_news = get_sources('science')
    sports_news = get_sources('sport')
    technology_news = get_sources('technology')
    health_news = get_sources('health')
    

    title = 'NEWS'
    return render_template('index.html', title = title, general = general_news, business = business_news, entertainment = entertainment_news,
    science = science_news, sport = sports_news, technology = technology_news, health = health_news)


@main.route('/source/<id>')
def articles(id):
    '''
    returns source with it's articles
    '''
    article = get_articles(id)
    print(article)
    title = f'{id}'

    return render_template('source.html', title = title, article = article)
