# Copilot has heavily helped me build this file either by giving me code to exchange my code with or by teaching me how to do something

from pypdf import PdfReader
import pymsgbox
# Read PDF That It's Path Was Passed As A Parameter
def readPDF(PDF_File_Name):
    # Try except from copilot
    try:
        reader = PdfReader(PDF_File_Name)
    except Exception as e:
        pymsgbox.alert(f"unable to open pdf \n error: {e}")
        return ""

    # Learned To Extract Full PDF Text From Copilt and copilot added the if statement
    fulltext = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            fulltext += text

    if fulltext:
        return fulltext
    else:
        pymsgbox.alert("couldn't extract text")
        # Copilot told me to return ""
        return ""