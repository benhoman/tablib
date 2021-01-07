""" Tablib - PDF Support.
"""
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

import tablib


class PDFFormat:
    title = 'pdf'
    extensions = ('pdf',)

    @classmethod
    def export_set(cls, dataset, pagesize=landscape(letter)):
        """Returns PDF representation of Dataset."""
        stream = BytesIO()
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(stream, pagesize=pagesize)
        data = dataset._package(dicts=False)
        t = Table(data)
        doc.build([t])

        return stream.getvalue()
