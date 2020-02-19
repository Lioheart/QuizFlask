# -*- coding: utf-8 -*-
# quiz-orm/main.py
from dane import *
from models import *
from views import *

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        baza.create_tables([Pytanie, Odpowiedz])  # Tworzymy tabele
        dodaj_pytania(pobierz_dane('pytania.csv'))
    app.run(debug=True)
