#run this program in order to initate html sites and scraping.py functionalities
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
