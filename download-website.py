#!/usr/bin/env python3
"""
Download all content from punjabischoolbothell.org

This script provides an alternative to the bash/wget approach.
It can be run on any system with Python 3 installed.
"""

import os
import sys
import urllib.request
import urllib.error
from urllib.parse import urljoin, urlparse
import time
import re

# Configuration
WEBSITE_URL = "http://punjabischoolbothell.org"
OUTPUT_DIR = "website-content"
MAX_DEPTH = 5
DELAY_SECONDS = 1  # Be polite to the server

# Track visited URLs to avoid duplicates
visited_urls = set()
downloaded_files = set()


def print_header():
    """Print script header"""
    print("=" * 60)
    print("Punjabi School Bothell Website Downloader (Python)")
    print("=" * 60)
    print()


def check_dependencies():
    """Check if required Python modules are available"""
    try:
        import urllib.request
        return True
    except ImportError:
        print("ERROR: Required Python modules not found.")
        print("This script requires Python 3.x")
        return False


def sanitize_filename(url):
    """Convert URL to safe filename"""
    # Remove protocol
    path = url.replace("http://", "").replace("https://", "")
    
    # Replace invalid filename characters
    path = re.sub(r'[<>:"|?*]', '_', path)
    
    # Handle directories - add index.html if path ends with /
    if path.endswith('/'):
        path += 'index.html'
    
    # If no extension, assume it's HTML
    if '.' not in os.path.basename(path):
        path += '.html'
    
    return path


def download_file(url, output_path):
    """Download a single file from URL to output_path"""
    try:
        # Create directory if needed
        dir_path = os.path.dirname(output_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        
        # Download file
        print(f"Downloading: {url}")
        
        # Set a user agent to avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()
            
            with open(output_path, 'wb') as f:
                f.write(content)
        
        print(f"  → Saved to: {output_path}")
        downloaded_files.add(output_path)
        return True
        
    except urllib.error.URLError as e:
        print(f"  ✗ Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Unexpected error: {e}")
        return False


def extract_links(html_content, base_url):
    """Extract links from HTML content"""
    links = set()
    
    # Simple regex patterns for finding links
    # This is a basic implementation - a proper HTML parser would be better
    patterns = [
        r'href=["\']([^"\']+)["\']',  # href links
        r'src=["\']([^"\']+)["\']',   # src attributes (images, scripts, etc)
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, str(html_content))
        for match in matches:
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, match)
            
            # Only include URLs from the same domain
            if urlparse(absolute_url).netloc == urlparse(base_url).netloc:
                links.add(absolute_url)
    
    return links


def crawl(url, depth=0):
    """Recursively crawl and download website"""
    if depth > MAX_DEPTH:
        return
    
    if url in visited_urls:
        return
    
    visited_urls.add(url)
    
    # Create output path
    filename = sanitize_filename(url)
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    # Skip if already downloaded
    if output_path in downloaded_files:
        return
    
    # Download the file
    if download_file(url, output_path):
        # If it's an HTML file, extract and follow links
        if output_path.endswith('.html') or output_path.endswith('.htm'):
            try:
                with open(output_path, 'rb') as f:
                    content = f.read()
                    links = extract_links(content, url)
                    
                    # Recursively download linked files
                    for link in links:
                        time.sleep(DELAY_SECONDS)  # Be polite
                        crawl(link, depth + 1)
            except Exception as e:
                print(f"  ! Could not parse links from {output_path}: {e}")
    
    time.sleep(DELAY_SECONDS)  # Be polite to the server


def main():
    """Main function"""
    print_header()
    
    if not check_dependencies():
        sys.exit(1)
    
    print(f"Starting download from: {WEBSITE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Max depth: {MAX_DEPTH}")
    print()
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    try:
        # Start crawling from the homepage
        crawl(WEBSITE_URL)
        
        print()
        print("=" * 60)
        print("Download completed!")
        print("=" * 60)
        print(f"Files downloaded: {len(downloaded_files)}")
        print(f"Saved to: {OUTPUT_DIR}")
        print()
        print("Next steps:")
        print("1. Review the downloaded content")
        print("2. Commit to git:")
        print(f"   git add {OUTPUT_DIR}")
        print("   git commit -m 'Add website content'")
        print("   git push")
        
    except KeyboardInterrupt:
        print()
        print("Download interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print()
        print("=" * 60)
        print("Download failed!")
        print("=" * 60)
        print(f"Error: {e}")
        print()
        print("Please check:")
        print(f"1. Is the website accessible? Try visiting {WEBSITE_URL}")
        print("2. Do you have internet connectivity?")
        print("3. Are there any firewall restrictions?")
        sys.exit(1)


if __name__ == "__main__":
    main()
