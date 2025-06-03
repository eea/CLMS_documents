#!/bin/bash

#set -euo pipefail

RENDERED_DOCS_DIR="../../_site"

# Set the working directory to the script's location
cd "$(dirname "${BASH_SOURCE[0]}")" || exit

# Define LibreOffice macro profile directory
OS="$(uname -s)"
if [ "$OS" = "Darwin" ]; then
    LIBREOFFICE_PROFILE="$HOME/Library/Application Support/LibreOffice/4/user"
else
    LIBREOFFICE_PROFILE="$HOME/.config/libreoffice/4/user"
fi

# Kill any running LibreOffice instances
pkill -f soffice

# Ensure the required directories exist
mkdir -p "$LIBREOFFICE_PROFILE/config"
mkdir -p "$LIBREOFFICE_PROFILE/basic/Standard/"

# Copy the .xba macro file to LibreOffice
cp ./macros/ConvertModule.xba "$LIBREOFFICE_PROFILE/basic/Standard/ConvertModule.xba"

# Create script.xlb
cat <<EOF > "$LIBREOFFICE_PROFILE/basic/Standard/script.xlb"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">
    <library:element library:name="ConvertModule"/>
</library:library>
EOF

cat <<EOF > "$LIBREOFFICE_PROFILE/basic/script.xlc"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
    <library:library library:name="Standard" xlink:href="\$(USER)/basic/Standard/script.xlb/" xlink:type="simple" library:link="false"/>
</library:libraries>
EOF

# Make sure not other process is running or locking the soffice
rm -f "$LIBREOFFICE_PROFILE/../.lock"
rm -f "$LIBREOFFICE_PROFILE/../.~lock.*"

# Process all .docx files in _site/
echo "Starting DOCX to PDF conversion..."

first_run=true
find $RENDERED_DOCS_DIR -type f -name "*.docx" -print0 | while IFS= read -r -d '' file; do
    echo "Processing $file..."

    if [ "$first_run" = true ]; then
        soffice --headless --norestore --invisible "macro:///Standard.ConvertModule.UpdateTOCAndExportToPDF" "$file" &
        soffice_pid=$!
        sleep 5 && pkill -P $soffice_pid soffice && echo "Terminated soffice after 5 sec" &
        wait $soffice_pid 2>/dev/null
        first_run=false
    fi

    soffice --headless --norestore --invisible "macro:///Standard.ConvertModule.UpdateTOCAndExportToPDF" "$file"
done

#echo "All DOCX files have been processed successfully."