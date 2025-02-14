#!/bin/bash

# Exit immediately if any command fails
set -e

# Set the working directory to the script's location
cd "$(dirname "${BASH_SOURCE[0]}")" || exit

# Define LibreOffice macro profile directory
OS="$(uname -s)"
if [ "$OS" = "Darwin" ]; then
    LIBREOFFICE_PROFILE="$HOME/Library/Application Support/LibreOffice/4/user/basic/Standard/"
else
    LIBREOFFICE_PROFILE="$HOME/.config/libreoffice/4/user/basic/Standard/"
fi

# Ensure LibreOffice macro directory exists
mkdir -p "$LIBREOFFICE_PROFILE"

# Copy the .xba macro file to LibreOffice
cp ../macros/ConvertModule.xba "$LIBREOFFICE_PROFILE/ConvertModule.xba"

# Create `script.xlb` to define the macro
cat <<EOF > "$LIBREOFFICE_PROFILE/script.xlb"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">
 <library:element library:name="ConvertModule"/>
</library:library>
EOF

# Process all .docx files in _site/
echo "Starting DOCX to PDF conversion..."
for file in $(find ../_site -type f -name "*.docx"); do
    echo "Processing $file..."
    soffice --headless --invisible --norestore "macro:///Standard.ConvertModule.UpdateTOCAndExportToPDF" "$file"
done

echo "All DOCX files have been processed successfully."


