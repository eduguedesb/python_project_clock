import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCalendarWidget
from PyQt5.QtCore import QTimer, QTime

class DigitalClockApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout principal
        layout = QVBoxLayout()

        # Relógio Digital
        self.clock_label = QLabel(self)
        self.clock_label.setStyleSheet("font-size: 25px;")
        layout.addWidget(self.clock_label)

        # Calendário
        self.calendar = QCalendarWidget(self)
        layout.addWidget(self.calendar)

        # Cronômetro
        self.timer_label = QLabel('00:00:00', self)
        self.timer_label.setStyleSheet("font-size: 25px;")
        layout.addWidget(self.timer_label)

        # Botões de controle do cronômetro
        self.start_button = QPushButton('Iniciar Cronômetro', self)
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Parar Cronômetro', self)
        self.stop_button.clicked.connect(self.stop_timer)
        layout.addWidget(self.stop_button)

        self.reset_button = QPushButton('Zerar Cronômetro', self)
        self.reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_button)

        # Timer para atualizar o relógio e cronômetro
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)  # Atualiza a cada segundo

        self.stopwatch_timer = QTimer(self)
        self.stopwatch_timer.timeout.connect(self.update_stopwatch)

        # Variáveis do cronômetro
        self.time_elapsed = 0
        self.is_running = False

        # Configurações da janela
        self.setLayout(layout)
        self.setWindowTitle('Relógio Digital com Calendário e Cronômetro')
        self.resize(300, 400)
        self.show()

    def update_clock(self):
        # Atualiza o relógio digital com a hora atual
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.clock_label.setText(f"Relógio: {current_time}")

    def start_timer(self):
        if not self.is_running:
            self.stopwatch_timer.start(1000)
            self.is_running = True

    def stop_timer(self):
        if self.is_running:
            self.stopwatch_timer.stop()
            self.is_running = False

    def reset_timer(self):
        self.stopwatch_timer.stop()
        self.time_elapsed = 0
        self.timer_label.setText('00:00:00')
        self.is_running = False

    def update_stopwatch(self):
        # Atualiza o cronômetro
        self.time_elapsed += 1
        hours = self.time_elapsed // 3600
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f'{hours:02}:{minutes:02}:{seconds:02}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DigitalClockApp()
    sys.exit(app.exec_())
