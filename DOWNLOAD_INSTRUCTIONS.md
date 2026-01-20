# Instructions for Downloading Website Content

This document explains how to download all content from http://punjabischoolbothell.org and add it to this repository.

## Prerequisites

You need one of the following tools installed on your local machine:

### Option 1: wget (Recommended)

- **Linux/Ubuntu/Debian**: `sudo apt-get install wget`
- **macOS**: `brew install wget`
- **Windows**: Download from https://eternallybored.org/misc/wget/

### Option 2: HTTrack Website Copier

- Download from: https://www.httrack.com/
- Available for Windows, Linux, and macOS
- Provides a GUI interface for easier use

## Method 1: Using the Provided Script (wget)

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone https://github.com/msjammu/PSB.git
   cd PSB
   ```

2. **Make the download script executable**:
   ```bash
   chmod +x download-website.sh
   ```

3. **Run the download script**:
   ```bash
   ./download-website.sh
   ```

4. **Review the downloaded content**:
   ```bash
   ls -la website-content/
   ```

5. **Commit and push the downloaded content**:
   ```bash
   git add website-content/
   git commit -m "Add downloaded website content from punjabischoolbothell.org"
   git push
   ```

## Method 2: Manual wget Command

If you prefer to run wget manually with custom options:

```bash
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
     --directory-prefix=website-content \
     http://punjabischoolbothell.org
```

## Method 3: Using HTTrack (GUI)

1. **Download and install HTTrack** from https://www.httrack.com/

2. **Launch HTTrack WebSite Copier**

3. **Create a new project**:
   - Project name: "Punjabi School Bothell"
   - Base path: Select this repository directory
   - Create the project

4. **Set the website URL**:
   - Web Addresses: `http://punjabischoolbothell.org`

5. **Configure options** (recommended settings):
   - Set download limits if needed
   - Choose "Download web site(s)"
   - Modify scan rules if necessary

6. **Start the download**

7. **Commit the downloaded content**:
   ```bash
   git add website-content/
   git commit -m "Add downloaded website content from punjabischoolbothell.org"
   git push
   ```

## Method 4: Using curl (Alternative)

For a simple page download:

```bash
mkdir -p website-content
cd website-content
curl -O http://punjabischoolbothell.org/index.html
```

Note: This only downloads a single page. Use wget or HTTrack for complete site downloads.

## Method 5: Using Archive.org Wayback Machine

If the website is no longer accessible, you can retrieve archived versions:

1. **Visit the Wayback Machine**:
   - Go to https://web.archive.org/
   - Enter: `punjabischoolbothell.org`
   - Browse available snapshots

2. **Download specific snapshots**:
   ```bash
   # Replace TIMESTAMP with the actual timestamp from Wayback Machine
   wget --recursive \
        --no-clobber \
        --page-requisites \
        --html-extension \
        --convert-links \
        --directory-prefix=website-content \
        https://web.archive.org/web/TIMESTAMP/http://punjabischoolbothell.org
   ```

## Troubleshooting

### Website is not accessible
- Check if the domain is still active
- Try accessing the site in your web browser
- Check for DNS issues: `ping punjabischoolbothell.org`
- Try using HTTPS: `https://punjabischoolbothell.org`

### wget errors
- **"403 Forbidden"**: The site may block automated downloads. Try adding a user agent:
  ```bash
  wget --user-agent="Mozilla/5.0" --recursive ...
  ```
- **"Connection refused"**: Check your internet connection and firewall settings
- **"Name or service not known"**: DNS issue - the domain might be down

### Large download size
- Add `--level=2` to limit recursion depth
- Add `--exclude-directories` to skip certain paths
- Use `--reject` to exclude specific file types

## Directory Structure

After download, the content will be organized as:

```
PSB/
├── website-content/
│   └── punjabischoolbothell.org/
│       ├── index.html
│       ├── about.html
│       ├── css/
│       ├── js/
│       ├── images/
│       └── ... (other files and directories)
├── download-website.sh
├── DOWNLOAD_INSTRUCTIONS.md
└── README.md
```

## Notes

- The download script includes a 1-second delay between requests to be respectful to the server
- Downloaded links will be converted for offline viewing
- File names will be compatible with Windows systems
- Only content from the punjabischoolbothell.org domain will be downloaded (no external links followed)

## Need Help?

If you encounter issues:
1. Check that the website is accessible in your browser
2. Verify your internet connection
3. Review the troubleshooting section above
4. Check wget documentation: `man wget` or `wget --help`
