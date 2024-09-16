#!/bin/bash

#create: nano convert.sh

#Quarto version
quarto --version

# Render the Jupyter notebook to HTML format
quarto render clms.ipynb --to html

# Render the Jupyter notebook to PDF format
quarto render clms.ipynb --to pdf

# Render the Jupyter notebook to DOCX format (Word document)
quarto render clms.ipynb --to docx

#add permission: chmod +x convert.sh