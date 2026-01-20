#!/bin/bash

# Script to download all content from punjabischoolbothell.org
# This script should be run locally where the website is accessible

WEBSITE_URL="http://punjabischoolbothell.org"
OUTPUT_DIR="website-content"

echo "=================================================="
echo "Punjabi School Bothell Website Downloader"
echo "=================================================="
echo ""

# Check if wget is installed
if ! command -v wget &> /dev/null; then
    echo "ERROR: wget is not installed."
    echo "Please install wget:"
    echo "  - Ubuntu/Debian: sudo apt-get install wget"
    echo "  - macOS: brew install wget"
    echo "  - Windows: Download from https://eternallybored.org/misc/wget/"
    exit 1
fi

echo "Starting download from $WEBSITE_URL..."
echo "Output directory: $OUTPUT_DIR"
echo ""

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Download the website using wget
# Options explained:
#   --recursive: Download recursively
#   --no-clobber: Don't overwrite existing files
#   --page-requisites: Get all images, CSS, JS needed to display page
#   --html-extension: Save HTML files with .html extension
#   --convert-links: Convert links for offline viewing
#   --restrict-file-names=windows: Modify filenames for Windows compatibility
#   --domains punjabischoolbothell.org: Only download from this domain
#   --no-parent: Don't ascend to parent directory
#   --wait=1: Wait 1 second between retrievals (be polite to the server)
#   --random-wait: Vary wait time between 0.5 and 1.5 times --wait value

wget --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains punjabischoolbothell.org \
     --no-parent \
     --wait=1 \
     --random-wait \
     --directory-prefix="$OUTPUT_DIR" \
     "$WEBSITE_URL"

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "Download completed successfully!"
    echo "=================================================="
    echo "Content saved to: $OUTPUT_DIR"
    echo ""
    echo "Next steps:"
    echo "1. Review the downloaded content in $OUTPUT_DIR"
    echo "2. Commit the content to git:"
    echo "   git add $OUTPUT_DIR"
    echo "   git commit -m 'Add website content from punjabischoolbothell.org'"
    echo "   git push"
else
    echo ""
    echo "=================================================="
    echo "Download failed!"
    echo "=================================================="
    echo "Please check:"
    echo "1. Is the website accessible? Try visiting $WEBSITE_URL in your browser"
    echo "2. Do you have internet connectivity?"
    echo "3. Are there any firewall restrictions?"
    exit 1
fi
