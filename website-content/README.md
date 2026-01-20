# Website Content Directory

This directory will contain the downloaded content from http://punjabischoolbothell.org.

## How to Populate This Directory

Run the download script from the repository root:

```bash
./download-website.sh
```

Or follow the instructions in [DOWNLOAD_INSTRUCTIONS.md](../DOWNLOAD_INSTRUCTIONS.md).

## Expected Structure

After running the download script, this directory will contain:

```
website-content/
└── punjabischoolbothell.org/
    ├── index.html          # Homepage
    ├── about.html          # About page
    ├── contact.html        # Contact page
    ├── css/                # Stylesheets
    ├── js/                 # JavaScript files
    ├── images/             # Image assets
    └── ...                 # Other website files
```

## Notes

- This directory is currently empty and waiting for content to be downloaded
- The download script will automatically create the subdirectory structure
- All downloaded files will preserve the original website structure
- Links will be converted for offline viewing

## Alternative: Manual Upload

If you have the website files already:

1. Copy all website files to this directory
2. Maintain the original directory structure
3. Commit the files:
   ```bash
   git add website-content/
   git commit -m "Add website content"
   git push
   ```
