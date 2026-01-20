# PSB - Punjabi School Bothell

This repository contains the website content for Punjabi School Bothell, migrated from http://punjabischoolbothell.org.

## Downloading Website Content

Since the website content needs to be downloaded from punjabischoolbothell.org, we've provided tools to help with this process.

### Quick Start

**TL;DR:** Run one of these commands, then commit the downloaded files.

```bash
./download-website.sh        # Linux/Mac with wget
python3 download-website.py  # Any platform with Python 3
```

See [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for one-page guide.

**Detailed Options:**

**Option 1: Use the Bash script (Linux/Mac with wget)**
```bash
./download-website.sh
```

**Option 2: Use the Python script (Cross-platform)**
```bash
python3 download-website.py
```

**Option 3: Follow detailed instructions**

See [DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md) for comprehensive guide including:
- Multiple download methods (wget, HTTrack, curl)
- Troubleshooting tips
- Alternative methods using Archive.org
- Step-by-step instructions

### Prerequisites

- **For Bash script:** `wget` installed on your system
- **For Python script:** Python 3.x (usually pre-installed on Linux/Mac)
- **Alternative:** HTTrack Website Copier (GUI tool)
- Access to the website (either live or archived version)
- Internet connectivity

### Directory Structure

After downloading, content will be organized as:
```
PSB/
├── website-content/         # Downloaded website files
│   └── punjabischoolbothell.org/
├── download-website.sh      # Bash download script (wget)
├── download-website.py      # Python download script (cross-platform)
├── DOWNLOAD_INSTRUCTIONS.md # Detailed instructions
└── README.md               # This file
```

## Why Manual Download?

The automated download needs to be performed locally because:
1. The website must be accessible from your network
2. The sandboxed CI/CD environment has restricted external access
3. You may need to use archived versions if the site is no longer live

## Next Steps

1. Run the download script or follow the instructions
2. Review the downloaded content
3. Commit and push to this repository
4. The website content will be preserved in version control

## Contributing

Once the website content is downloaded and committed, you can:
- Update content by editing files directly
- Modernize the website structure
- Deploy to GitHub Pages or other hosting platforms

## License

All content is owned by Punjabi School Bothell.
