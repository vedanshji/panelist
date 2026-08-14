<img width="1919" height="856" alt="image" src="https://github.com/user-attachments/assets/c3fb4264-d10e-466c-a3c6-1ef6a58a9f2b" /># Panelist

> Interviews on demand. Signal on delivery.

Marketing site for **Panelist** — a marketplace of vetted expert interviewers who run first- and second-round interviews for hiring teams and deliver structured, evidence-based feedback in under 24 hours.

Live at: **https://vedanshji.github.io/panelist/** (update after deploy)

## Stack

Plain HTML + CSS + JS. No build step. No dependencies. Just drop the files on any static host.

## Structure

```
/
├── index.html          Landing page
├── companies.html      For Companies page
├── interviewers.html   Interviewer application page
├── about.html          Team / story
├── privacy.html        Privacy Policy (template — have a lawyer review)
├── terms.html          Terms of Service (template — have a lawyer review)
├── 404.html            Custom not-found page
├── styles.css          Shared design system
├── script.js           Shared JS (nav, reveal, FAQ, form)
├── favicon.svg         Browser tab icon
├── og-image.png        Social share preview (1200×630)
├── robots.txt          SEO — allow all + point to sitemap
├── sitemap.xml         SEO — list of all pages
├── CNAME               Custom domain (edit or delete)
└── DEPLOY.md           Step-by-step deployment guide
```

## Local development

Open `index.html` in your browser. Or serve with any static server:

```bash
python3 -m http.server 8000
# → open http://localhost:8000
```

## Deployment

See `DEPLOY.md` for full instructions on GitHub Pages, custom domain, forms, and analytics.

## Customization

**Change colors, fonts, spacing** → edit CSS variables at the top of `styles.css`.
**Change copy** → edit the HTML directly.
**Enable contact forms** → sign up at [formspree.io](https://formspree.io), then replace `YOUR_FORM_ID` in `index.html`, `companies.html`, and `interviewers.html`.

## License

© 2026 Panelist Inc. All rights reserved.
