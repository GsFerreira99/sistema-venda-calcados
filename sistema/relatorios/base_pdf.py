from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class Pdf:

    def __init__(self, caminho):
        self.nome_arquivo = caminho
        self.can = canvas.Canvas(f'{self.nome_arquivo}')

        self.x = 720

    @staticmethod
    def registrar_font(font, caminho):
        pdfmetrics.registerFont(TTFont(font, caminho))

    def set_titulo(self, titulo):
        self.can.setTitle(titulo)

    def set_font(self, font="Helvetica-Oblique", tamanho=14):
        self.can.setFont(font, tamanho)

    def string(self, x, y, texto):
        self.can.drawString(x, y, texto)

    def salvar(self):
        self.can.save()