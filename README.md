# Punjabi School Bothell Website

![Punjabi School Bothell](https://punjabischoolbothell.org/Skins/psb_v2_3/assets/images/cropp-1-1-221x221.jpg)

A modern, responsive website for Punjabi School Bothell — empowering students of all ages by teaching Punjabi, Gurmukhi, and essential life skills in Bothell, Washington.

## 🌟 Features

- **Responsive Design** - Works beautifully on desktop, tablet, and mobile devices
- **Accessibility First** - Skip links, ARIA labels, focus states, and reduced motion support
- **SEO Optimized** - Open Graph tags, meta descriptions, and semantic HTML
- **Modern UI** - Bootstrap 5, Font Awesome icons, smooth animations
- **Fast Loading** - Preconnect hints, deferred scripts, optimized assets

## 📁 Project Structure

```
PSB/
├── index.html          # Homepage
├── about.html          # About Us page
├── courses.html        # Programs & courses information
├── calendar.html       # School calendar (2025-2026)
├── resources.html      # Learning resources & materials
├── enroll.html         # Enrollment information
├── 404.html            # Custom error page
├── css/
│   └── style.css       # Custom styles
├── programs/           # PDF program documents
│   ├── Little Learners class.pdf
│   ├── FastTrack Class Program Description.pdf
│   └── ALTA Test for Punjabi.pdf
├── package.json        # npm configuration
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites

- A modern web browser
- A local web server (optional, for development)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/PSB.git
   cd PSB
   ```

2. **Open in browser:**
   - Simply open `index.html` in your browser, or
   - Use a local development server:
     ```bash
     # Using Python
     python -m http.server 8000
     
     # Using Node.js (npx)
     npx serve
     
     # Using VS Code Live Server extension
     # Right-click index.html → "Open with Live Server"
     ```

3. **View the site:**
   Open `http://localhost:8000` in your browser

## 🎨 Customization

### Color Theme

The site uses a saffron/orange theme with navy accents. Colors are defined as CSS variables in `css/style.css`:

```css
:root {
    --primary-color: #f58634;     /* Saffron Orange */
    --primary-dark: #e67524;
    --primary-light: #ffb380;
    --secondary-color: #1a365d;   /* Navy Blue */
    --accent-color: #ff9f43;
    --light-bg: #fff9f0;
    --cream-bg: #fef7ed;
}
```

### Adding New Pages

1. Copy an existing page as a template
2. Update the navigation `active` class
3. Update the `<title>` and meta tags
4. Add content within the `#main-content` section

## 📱 Pages Overview

| Page | Description |
|------|-------------|
| **Home** | Welcome section, mission, features, and CTA |
| **About** | School mission, values, and what students learn |
| **Courses** | Little Learners, Levels 1-5, FastTrack, ALTA Test |
| **Calendar** | 2025-2026 school year schedule |
| **Resources** | Learning materials and helpful links |
| **Enroll** | Enrollment options and how to register |
| **404** | Custom error page for missing pages |

## ♿ Accessibility Features

- Skip-to-content links for keyboard navigation
- ARIA labels on interactive elements
- Focus indicators for keyboard users
- Reduced motion support for vestibular disorders
- Semantic HTML structure
- Alt text on all images

## 🔧 Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Custom properties, Flexbox, Grid
- **Bootstrap 5.3** - Responsive framework
- **Font Awesome 6.5** - Icon library
- **Google Fonts** - Nunito typeface

## 📞 Contact

- **Email:** [Info@punjabischoolbothell.org](mailto:Info@punjabischoolbothell.org)
- **Phone:** +1 (425) 233-8319
- **Location:** 20412 Bothell Everett Highway, Bothell, WA 98012
- **Website:** [punjabischoolbothell.org](https://punjabischoolbothell.org)

## 📄 License

© 2026 Punjabi School Bothell. All Rights Reserved.

---

Made with ❤️ for the Punjabi School Bothell community
