# PSB - Punjabi School Bothell

This repository contains the website content for Punjabi School Bothell, migrated from http://punjabischoolbothell.org.

## Downloading Website Content

Since the website content needs to be downloaded from punjabischoolbothell.org, we've provided tools to help with this process.

### Quick Start

**Option 1: Use the provided script**
```bash
./download-website.sh
```

**Option 2: Follow detailed instructions**

See [DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md) for comprehensive guide including:
- Multiple download methods (wget, HTTrack, curl)
- Troubleshooting tips
- Alternative methods using Archive.org
- Step-by-step instructions

### Prerequisites

- `wget` installed on your system (or HTTrack as an alternative)
- Access to the website (either live or archived version)
- Internet connectivity

### Directory Structure

After downloading, content will be organized as:
```
PSB/
├── website-content/         # Downloaded website files
│   └── punjabischoolbothell.org/
├── download-website.sh      # Automated download script
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
