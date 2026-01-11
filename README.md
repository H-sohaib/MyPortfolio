# Portfolio Website - Harraoui Sohaib

![Portfolio Screenshot](screenshot.png)

## Overview

A modern, responsive portfolio website showcasing my work as a Software Engineering student specializing in Full-Stack Development and Cybersecurity. Built with Flask and featuring a clean, professional design.

**Live Demo:** [harraouisohaib.pythonanywhere.com](https://harraouisohaib.pythonanywhere.com/)

## Features

- **Responsive Design** - Mobile-first approach with smooth animations
- **Portfolio Showcase** - Dynamic project gallery with modal popups
- **Contact Form** - Integrated email functionality using Flask-Mail
- **Skills Display** - Interactive skill bars and timeline resume
- **Downloadable CV** - Direct download of certificates and CV
- **Multiple Pages** - Home, About, Portfolio, Resume, and Contact sections

## Tech Stack

**Backend:**

- Python 3.x
- Flask
- Flask-Mail
- Flask-Minify

**Frontend:**

- HTML5, CSS3, JavaScript
- Bootstrap 5
- jQuery
- Tailwind CSS
- Font Awesome Icons

**Key Libraries:**

- Owl Carousel
- Masonry.js
- Waypoints.js
- FitVids.js

## Project Structure

```
MyPortfolio/
├── app/
│   ├── static/          # CSS, JS, images, fonts
│   ├── templates/       # HTML templates
│   ├── __init__.py      # App initialization
│   └── Views.py         # Route handlers
├── config.py            # Configuration settings
├── run.py               # Application entry point
└── requirements.txt     # Python dependencies
```

## Key Routes

- `/` - Home page with intro, about, portfolio sections
- `/works` - Additional projects showcase
- `/download/<file>` - Dynamic file download/preview endpoint

## Environment Variables

Create a `.env` file with:

```env
SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=465
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_USE_SSL=True
```

## Features Highlights

- **Dynamic Content Management** - Easy updates through template system
- **Email Integration** - Contact form submissions sent via SMTP
- **Certificate Viewer** - In-browser preview for certificates
- **Optimized Performance** - Minified HTML/CSS/JS for faster loading
- **Cross-platform** - Works on any OS (Windows, Linux, macOS)

## Credits

Design by [StyleShout](http://www.styleshout.com/)  
Customized and developed by Harraoui Sohaib

## License

This project is open source and available for personal use.

---

**Contact:** harraoui.sohaib1@gmail.com  
**LinkedIn:** [Harraoui Sohaib](https://www.linkedin.com/in/harraoui-sohaib-89849b246/)  
**GitHub:** [H-sohaib](https://github.com/H-sohaib)
