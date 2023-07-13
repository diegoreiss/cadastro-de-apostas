from random import randint, choice
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox)
from ..infra.repository.resultado_repository import ResultadoRepository


class Apostador:
    def __init__(self, nome, aposta, placar: list, valor_aposta):
        self.nome = nome
        self.aposta = aposta
        self.placar = placar
        self.valor_aposta = valor_aposta

    def __repr__(self) -> str:
        return f"Apostador(nome={self.nome}, aposta={self.aposta}, valor_aposta={self.valor_aposta}, placar={self.placar})"


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(self.centralwidget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.top_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_titulo = QLabel(self.top_widget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.horizontalLayout.addWidget(self.lbl_titulo)

        self.verticalLayout.addWidget(self.top_widget)

        self.mid_widget = QWidget(self.centralwidget)
        self.mid_widget.setObjectName(u"mid_widget")
        self.horizontalLayout_11 = QHBoxLayout(self.mid_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_apostador = QLabel(self.mid_widget)
        self.lbl_apostador.setObjectName(u"lbl_apostador")

        self.horizontalLayout_2.addWidget(self.lbl_apostador)

        self.txt_apostador = QLineEdit(self.mid_widget)
        self.txt_apostador.setObjectName(u"txt_apostador")
        self.txt_apostador.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(35, 35, 35);\n"
                                         "border:1px solid black;")

        self.horizontalLayout_2.addWidget(self.txt_apostador)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_valor_aposta = QLabel(self.mid_widget)
        self.lbl_valor_aposta.setObjectName(u"lbl_valor_aposta")

        self.horizontalLayout_3.addWidget(self.lbl_valor_aposta)

        self.combo_valor_aposta = QComboBox(self.mid_widget)
        self.combo_valor_aposta.addItem("")
        self.combo_valor_aposta.addItem("")
        self.combo_valor_aposta.addItem("")
        self.combo_valor_aposta.addItem("")
        self.combo_valor_aposta.addItem("")
        self.combo_valor_aposta.setObjectName(u"combo_valor_aposta")
        self.combo_valor_aposta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.combo_valor_aposta)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_time_vencedor = QLabel(self.mid_widget)
        self.lbl_time_vencedor.setObjectName(u"lbl_time_vencedor")

        self.horizontalLayout_5.addWidget(self.lbl_time_vencedor)

        self.btn_casa = QRadioButton(self.mid_widget)
        self.btn_casa.setObjectName(u"btn_casa")
        self.btn_casa.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_casa)

        self.btn_visitante = QRadioButton(self.mid_widget)
        self.btn_visitante.setObjectName(u"btn_visitante")
        self.btn_visitante.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_visitante)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_placar = QLabel(self.mid_widget)
        self.lbl_placar.setObjectName(u"lbl_placar")

        self.horizontalLayout_8.addWidget(self.lbl_placar)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_casa_placar = QLabel(self.mid_widget)
        self.lbl_casa_placar.setObjectName(u"lbl_casa_placar")

        self.horizontalLayout_6.addWidget(self.lbl_casa_placar)

        self.txt_casa_placar = QLineEdit(self.mid_widget)
        self.txt_casa_placar.setObjectName(u"txt_casa_placar")
        self.txt_casa_placar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(35, 35, 35);\n"
                                           "border:1px solid black;")

        self.horizontalLayout_6.addWidget(self.txt_casa_placar)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_visitante_placar = QLabel(self.mid_widget)
        self.lbl_visitante_placar.setObjectName(u"lbl_visitante_placar")

        self.horizontalLayout_7.addWidget(self.lbl_visitante_placar)

        self.txt_visitante_placar = QLineEdit(self.mid_widget)
        self.txt_visitante_placar.setObjectName(u"txt_visitante_placar")
        self.txt_visitante_placar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(35, 35, 35);\n"
                                                "border:1px solid black;")

        self.horizontalLayout_7.addWidget(self.txt_visitante_placar)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txt_num_apostadores = QLineEdit(self.mid_widget)
        self.txt_num_apostadores.setObjectName(u"txt_num_apostadores")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_num_apostadores.sizePolicy().hasHeightForWidth())
        self.txt_num_apostadores.setSizePolicy(sizePolicy)
        self.txt_num_apostadores.setMinimumSize(QSize(40, 0))
        self.txt_num_apostadores.setMaximumSize(QSize(20, 16777215))
        self.txt_num_apostadores.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(35, 35, 35);\n"
                                               "border:1px solid black;")

        self.horizontalLayout_10.addWidget(self.txt_num_apostadores)

        self.lbl_num_apostadores = QLabel(self.mid_widget)
        self.lbl_num_apostadores.setObjectName(u"lbl_num_apostadores")

        self.horizontalLayout_10.addWidget(self.lbl_num_apostadores)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.btn_apostar = QPushButton(self.mid_widget)
        self.btn_apostar.setObjectName(u"btn_apostar")
        self.btn_apostar.setMaximumSize(QSize(100, 16777215))
        self.btn_apostar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.btn_apostar)

        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.right_widget = QFrame(self.mid_widget)
        self.right_widget.setObjectName(u"right_widget")
        self.right_widget.setMinimumSize(QSize(180, 0))
        self.right_widget.setMaximumSize(QSize(180, 16777215))
        self.right_widget.setFrameShape(QFrame.StyledPanel)
        self.right_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_gerar_resultado = QPushButton(self.right_widget)
        self.btn_gerar_resultado.setObjectName(u"btn_gerar_resultado")
        self.btn_gerar_resultado.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.btn_gerar_resultado)

        self.horizontalLayout_11.addWidget(self.right_widget)

        self.verticalLayout.addWidget(self.mid_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.bot_frame = QFrame(self.centralwidget)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setMaximumSize(QSize(16777215, 150))
        self.bot_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.bot_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.bot_frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_9.addWidget(self.tableWidget)

        self.verticalLayout.addWidget(self.bot_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.txt_casa_placar.setInputMask("000")
        self.txt_visitante_placar.setInputMask("000")

        self.apostadores = []
        self.quantidade_apostas = 0
        self.total_rodada = 0
        self.btn_apostar.clicked.connect(self.apostar)
        self.btn_gerar_resultado.clicked.connect(self.gerar_resultado)
        self.atualizar_quantidade_apostas()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#fffdfc;\">M'laze</span></p></body></html>",
                                                           None))
        self.lbl_apostador.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p><span style=\" color:#ffffff;\">Apostador: </span></p></body></html>",
                                                              None))
        self.lbl_valor_aposta.setText(QCoreApplication.translate("MainWindow",
                                                                 u"<html><head/><body><p><span style=\" color:#ffffff;\">Valor de Aposta</span></p></body></html>",
                                                                 None))
        self.combo_valor_aposta.setItemText(0, QCoreApplication.translate("MainWindow", u"$50", None))
        self.combo_valor_aposta.setItemText(1, QCoreApplication.translate("MainWindow", u"$100", None))
        self.combo_valor_aposta.setItemText(2, QCoreApplication.translate("MainWindow", u"$200", None))
        self.combo_valor_aposta.setItemText(3, QCoreApplication.translate("MainWindow", u"$500", None))
        self.combo_valor_aposta.setItemText(4, QCoreApplication.translate("MainWindow", u"$1000", None))

        self.lbl_time_vencedor.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<html><head/><body><p><span style=\" color:#ffffff;\">Vencedor:</span></p></body></html>",
                                                                  None))
        self.btn_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.btn_visitante.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.lbl_placar.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p><span style=\" color:#ffffff;\">Placar:</span></p></body></html>",
                                                           None))
        self.lbl_casa_placar.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p><span style=\" color:#ffffff;\">Casa</span></p></body></html>",
                                                                None))
        self.lbl_visitante_placar.setText(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p><span style=\" color:#ffffff;\">Visitante</span></p></body></html>",
                                                                     None))
        self.lbl_num_apostadores.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body><p><span style=\" color:#fefefe;\">Pessoa(s) ja apostaram</span></p></body></html>",
                                                                    None))
        self.btn_apostar.setText(QCoreApplication.translate("MainWindow", u"Apostar", None))
        self.btn_gerar_resultado.setText(QCoreApplication.translate("MainWindow", u"Gerar Resultado", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Apostador", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Placar", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor Ganho", None));

    # retranslateUi

    def get_campos(self):
        return {
            "apostador": self.txt_apostador.text(),
            "valor_aposta": float(self.combo_valor_aposta.currentText().replace("$", "")),
            "aposta": "casa" if self.btn_casa.isChecked() else "visitante",
            "placar": {"casa": int(self.txt_casa_placar.text()), "visitante": int(self.txt_visitante_placar.text())}
        }

    def is_campos_preenchidos(self) -> bool:
        return len(self.txt_apostador.text()) != 0 \
            and self.txt_casa_placar.text().isnumeric() \
            and self.txt_visitante_placar.text().isnumeric() \
            and (self.btn_casa.isChecked() or self.btn_visitante.isChecked())
    

    def apostar(self):
        if not self.is_campos_preenchidos():
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Preencha os Campos!!!")
            msg_box.exec()
            return 

        campos = self.get_campos()
        self.apostadores.append(Apostador(nome=campos["apostador"], aposta=campos["aposta"], valor_aposta=campos["valor_aposta"], placar=[campos["placar"]["casa"], campos["placar"]["visitante"]]))
        print(self.apostadores)
        self.quantidade_apostas += 1
        self.total_rodada += campos["valor_aposta"]
        self.atualizar_quantidade_apostas()
        self.limpar_campos()
        
    def atualizar_quantidade_apostas(self):
        self.txt_num_apostadores.setText(str(self.quantidade_apostas))

    def limpar_campos(self):
        self.txt_apostador.clear()
        self.txt_casa_placar.clear()
        self.txt_visitante_placar.clear()
        self.btn_casa.setChecked(False)
        self.btn_visitante.setChecked(False)

    def gerar_resultado(self):
        if self.quantidade_apostas == 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Não existe nenhum apostador!!!")
            msg_box.exec()
            return 

        dados = {"gols_da_casa": randint(0, 10), "gols_do_visitante": randint(0, 10)}
        dados.update({"vencedor": "casa" if dados["gols_da_casa"] > dados["gols_do_visitante"] else "visitante"})

        resultado = ResultadoRepository.insert(**dados)
        self.tableWidget.setRowCount(len(self.apostadores))

        for linha, apostador in enumerate(self.apostadores):
            print(apostador)
            obj = [apostador.nome, apostador.aposta, f"casa {apostador.placar[0]} x visitante {apostador.placar[1]}", self.get_valor_ganho(apostador, resultado)]

            for coluna, valor in enumerate(obj):
                item = QTableWidgetItem(str(valor))
                self.tableWidget.setItem(linha, coluna, item)

        self.apostadores.clear()
        self.quantidade_apostas = 0
        self.total_rodada = 0
        self.atualizar_quantidade_apostas()

    def get_valor_ganho(self, apostador, resultado):
        if apostador.aposta == str(resultado.vencedor) and (apostador.placar[0] == resultado.gols_da_casa and apostador[1] == resultado.gols_do_visitante):
            return apostador.valor_aposta + self.total_rodada
        elif apostador.aposta == str(resultado.vencedor):
            return apostador.valor_aposta + (self.total_rodada // 2)
        else:
            return 0

