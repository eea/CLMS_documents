@echo off

quarto --version

echo Rendering clms.ipynb to HTML...
quarto render clms.ipynb --to html
echo HTML rendering completed.

echo Rendering clms.ipynb to PDF...
quarto render clms.ipynb --to pdf
echo PDF rendering completed.

echo Rendering clms.ipynb to DOCX...
quarto render clms.ipynb --to docx
echo DOCX rendering completed.

echo All formats rendered successfully.
