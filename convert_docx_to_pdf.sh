for file in $(find _site -type f -name "*.docx"); do
  echo "Processing $file"
  soffice --headless "macro:///Standard.Module2.UpdateTOCAndExportToPDF" "$file"
done
