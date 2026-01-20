# Quick Reference Guide

## One-Line Commands

### For Linux/Mac Users (with wget):
```bash
./download-website.sh
```

### For Python Users (all platforms):
```bash
python3 download-website.py
```

### For Windows Users (with Python):
```bash
python download-website.py
```

---

## After Download

Once the download completes, commit the content:

```bash
git add website-content/
git commit -m "Add website content from punjabischoolbothell.org"
git push
```

---

## Troubleshooting Quick Fixes

### "wget: command not found"
Install wget or use the Python script instead:
```bash
python3 download-website.py
```

### "Permission denied" when running script
Make it executable:
```bash
chmod +x download-website.sh
```

### Website is down or not accessible
Use the Wayback Machine to get archived versions:
```bash
# Visit https://web.archive.org/
# Search for: punjabischoolbothell.org
# Download from a specific archived date
```

### Need more detailed instructions?
See [DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md)

---

## File Locations

| File | Purpose |
|------|---------|
| `download-website.sh` | Bash download script |
| `download-website.py` | Python download script |
| `DOWNLOAD_INSTRUCTIONS.md` | Detailed instructions |
| `IMPLEMENTATION_SUMMARY.md` | Complete overview |
| `website-content/` | Downloaded files go here |

---

## Need Help?

1. Read [DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md) for detailed guidance
2. Read [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for complete overview
3. Check if the website is accessible in your browser
4. Try the alternative download method (Python if wget fails, or vice versa)
