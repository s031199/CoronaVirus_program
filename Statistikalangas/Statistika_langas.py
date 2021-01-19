from PySide2.QtWidgets import QVBoxLayout, QLabel, QDialog, QPushButton

from Statistikalangas.Data import *


class Second(QDialog):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

        self.setWindowTitle("Statistika")
        self.setGeometry(300, 300, 500, 400)
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)
        self.setMaximumHeight(500)
        self.setMaximumWidth(400)

        self.InitWindow()

    def InitWindow(self):
        update_status()
        vbox = QVBoxLayout()
        data_label = QLabel(f"Nacionalinio visuomenės sveikatos centro {informacija[0]['Data']} duomenimis:")
        patvirtinti_label = QLabel(f"Patvirtintų ligos atvejų skaičius: {informacija[0]['Patvirtinti']}")
        sergantis_label = QLabel(f"Sergančių žmonių skaičius: {informacija[0]['Sergantis']}")
        patvirtinti_nauji_label = QLabel(
            f"Naujų patvirtintų susirgusių skaičius: {informacija[0]['Patvirtinti nauji']}")
        mire_label = QLabel(f"Mirusių žmonių skaičius: {informacija[0]['Mire']}")
        uzsikrete_label = QLabel(
            f"Užsikrėtusieji koronavirusu, mirę dėl kitų priežasčių: {informacija[0]['Uzsikrete']}")
        pasveike_label = QLabel(f"Pasveikusių žmonių skaičius: {informacija[0]['Pasveike']}")
        izoliuoti_label = QLabel(f"Izoliacijoje esančių asmenų skaičius: {informacija[0]['Izoliuoti']}")
        iveztiniai_label = QLabel(
            f"Nuo {informacija[0]['Data iveztiniai']} įvežtinių atvejų: {informacija[0]['Iveztiniai']}")
        vbox.addWidget(data_label)
        vbox.addWidget(patvirtinti_label)
        vbox.addWidget(sergantis_label)
        vbox.addWidget(patvirtinti_nauji_label)
        vbox.addWidget(mire_label)
        vbox.addWidget(uzsikrete_label)
        vbox.addWidget(pasveike_label)
        vbox.addWidget(izoliuoti_label)
        vbox.addWidget(iveztiniai_label)

        button2 = QPushButton("Įšėjimas", self)
        vbox.addWidget(button2)
        button2.clicked.connect(self.exit_app)

        self.setLayout(vbox)

    def exit_app(self):
        self.close()
