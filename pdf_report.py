
from fpdf import FPDF

class PDFReport:
    def generate(self, vulnerabilities, output_file):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Vulnerability Assessment Report", ln=True, align='C')

        pdf.set_font("Arial", size=12)
        for vuln in vulnerabilities:
            pdf.cell(200, 10, txt=f"Vulnerability: {vuln['type']}", ln=True)
            pdf.cell(200, 10, txt=f"URL: {vuln['url']}", ln=True)
            pdf.cell(200, 10, txt=f"Severity: {vuln.get('severity', 'Unknown')}", ln=True)
            pdf.cell(200, 10, txt=f"AI Reproducibility: {vuln.get('ai_confidence', 'N/A')}", ln=True)
            pdf.cell(200, 10, txt="--------------------------------------------", ln=True)

        pdf.output(output_file)
