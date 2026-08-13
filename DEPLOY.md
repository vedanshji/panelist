# Deployment Guide — Panelist

Everything you need to take this from your PC to a live, professional-looking website.

---

## 1. Upload to your GitHub repo

Since you already deployed with GitHub Pages, just upload the **new files** to the same repo:

1. Go to your repo on github.com
2. Click **"Add file" → "Upload files"**
3. Drag ALL of these files into the upload area:
   - `index.html` (replaces existing)
   - `companies.html`
   - `interviewers.html`
   - `about.html`
   - `privacy.html`
   - `terms.html`
   - `404.html`
   - `styles.css`
   - `script.js`
   - `favicon.svg`
   - `og-image.png`
   - `robots.txt`
   - `sitemap.xml`
   - `README.md`
4. Scroll down, write commit message like *"Add full site"*, click **Commit changes**
5. Wait 1–2 minutes. GitHub Pages will redeploy automatically.

**Do NOT upload `CNAME`, `DEPLOY.md`, or `gen_og.py` yet** — see below.

---

## 2. Get contact forms working (Formspree)

Right now the forms have a placeholder action URL. To make them actually deliver emails to your inbox:

1. Sign up free at **https://formspree.io** (50 submissions/month free)
2. Click **"New form"** → pick your email
3. Formspree gives you an endpoint like `https://formspree.io/f/xyzabc123`
4. In your local `index.html`, `companies.html`, and `interviewers.html`, find:
   ```
   action="https://formspree.io/f/YOUR_FORM_ID"
   ```
   Replace `YOUR_FORM_ID` with `xyzabc123` (whatever Formspree gave you)
5. Re-upload the three files to your GitHub repo
6. Test — submit a form, check your inbox. Done.

You can create separate forms for each page (companies vs interviewer applications) so submissions come in tagged.

---

## 3. Fix SEO files (robots.txt & sitemap.xml)

Open both files and replace `YOUR-DOMAIN.com` with your actual URL:
- If using GitHub Pages default: `YOUR-USERNAME.github.io/panelist`
- If using custom domain: `panelist.io` (or whatever you buy)

Re-upload to the repo.

Then submit your sitemap to Google:
1. Go to **https://search.google.com/search-console**
2. Add your property (URL)
3. Verify ownership (GitHub Pages users: pick "HTML file" method, upload the verification file)
4. Sitemaps tab → submit `sitemap.xml`

Google will start indexing you within a few days.

---

## 4. Custom domain (optional, ~$12/year)

1. Buy a domain at **Namecheap**, **Porkbun**, or **Cloudflare Registrar**. Good options:
   - `panelist.io` — expensive (~$40) but on-brand
   - `panelist.co` — cheaper, still solid
   - `getpanelist.com` — cheapest, clear
2. In your domain registrar's DNS settings, add these records:
   ```
   Type: A     Name: @    Value: 185.199.108.153
   Type: A     Name: @    Value: 185.199.109.153
   Type: A     Name: @    Value: 185.199.110.153
   Type: A     Name: @    Value: 185.199.111.153
   Type: CNAME Name: www  Value: YOUR-USERNAME.github.io
   ```
3. Edit the `CNAME` file (already provided) so it contains just your domain, e.g. `panelist.io`
4. Upload `CNAME` to your GitHub repo (no file extension — must be exactly `CNAME`)
5. In your repo: **Settings → Pages → Custom domain** → enter your domain → save
6. Wait 15–60 minutes for DNS to propagate. Enable **"Enforce HTTPS"** once available.

---

## 5. Analytics (free, privacy-friendly)

Add before `</body>` in each HTML file:

**Option A — Plausible** (paid, cleanest): sign up at plausible.io
```html
<script defer data-domain="YOUR-DOMAIN.com" src="https://plausible.io/js/script.js"></script>
```

**Option B — Google Analytics 4** (free): sign up at analytics.google.com, they give you the snippet.

**Option C — Simple Analytics or PostHog**: also great alternatives.

---

## 6. Social share preview

The `og-image.png` is what appears when someone shares your link on WhatsApp, LinkedIn, Twitter, Slack. It's already wired into the meta tags — just make sure the file is uploaded to your repo root.

Test it at **https://opengraph.xyz** — paste your live URL, see how it renders.

---

## 7. What to update BEFORE launching to real users

- [ ] Formspree endpoint on all 3 forms
- [ ] `YOUR-DOMAIN.com` in robots.txt & sitemap.xml
- [ ] Team names on `about.html` (currently placeholders)
- [ ] Interviewer names/photos on `index.html` (currently fake)
- [ ] Logo names in the "Trusted by" section (currently fake)
- [ ] Testimonial quotes (currently fake — replace with real ones or delete the section)
- [ ] Privacy Policy & Terms — **have a lawyer review** before serving real customers
- [ ] Update copyright year annually
- [ ] Add analytics tracking

---

## 8. File map — what does what

| File | Purpose | Edit when… |
|---|---|---|
| `index.html` | Landing page | You want to change hero copy, pricing, testimonials |
| `companies.html` | For Companies pitch page | You want to add case studies, integrations |
| `interviewers.html` | Recruiting interviewers | You change payout, requirements, application flow |
| `about.html` | Team + story | You hire team, want to tell your origin story |
| `privacy.html` | Legal | Your data practices change |
| `terms.html` | Legal | Your business model / liability terms change |
| `404.html` | Error page | Rarely — it just needs to exist |
| `styles.css` | ALL visual styling | You want to change colors, fonts, spacing site-wide |
| `script.js` | Nav, animations, forms | You add new interactive features |
| `favicon.svg` | Browser tab icon | You want a different logo mark |
| `og-image.png` | Social preview | You rebrand or want a different share image |
| `robots.txt` | SEO — crawler rules | Adding a domain or blocking a path |
| `sitemap.xml` | SEO — page index | Adding a new page |
| `CNAME` | Custom domain | You attach a domain |

---

## 9. Adding a new page later

1. Copy `about.html` as a starting template
2. Change the `<title>`, `<meta name="description">`, and content
3. Update the nav bar and footer links across ALL pages to include your new page
4. Add its URL to `sitemap.xml`

That's it. Ship it.

---

## Questions?

Everything on this site is standard HTML/CSS/JS — any developer or ChatGPT/Claude can help you extend it.
