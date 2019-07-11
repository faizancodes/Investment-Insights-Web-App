from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/portfolioConstruction')
def portfolioConstruction():
    return render_template('portfolioConstruction.html')

@app.route('/gs')
def gs():
    return render_template('gs.html')

@app.route('/rm')
def rm():
    return render_template('rm.html')

@app.route('/howToPickGreatStocks')
def howToPickGreatStocks():
    return render_template('howToPickGreatStocks.html')

@app.route('/bestInvestingApps')
def bestInvestingApps():
    return render_template('bestInvestingApps.html')

@app.route('/portfolioBuilder')
def portfolioBuilder():
    return render_template('portfolioBuilder.html')

if __name__ == '__main__':
    app.run(debug = True)
