# S. Dhivya -- Portfolio Website

A responsive Flask portfolio for an AI & Data Science student, targeting entry-level
ML / Python / Data roles. Built from a single content file (`data/portfolio_data.py`)
so nothing has to be edited inside the HTML templates to update copy.

## Tech stack
- Backend: Python 3.10+, Flask, Jinja2
- Frontend: semantic HTML5, hand-written CSS (no framework), vanilla JS
- Data: `data/portfolio_data.py` (single source of truth for all content)
- Tests: pytest + Flask test client

## Prerequisites
- Python 3.10 or newer
- pip

## Windows setup
```powershell
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

## macOS / Linux setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Then open **http://127.0.0.1:5000**.

## Running tests
```bash
pytest tests/ -v
```

## Where to add your content

| What | Where |
|---|---|
| Profile photo | `static/images/profile/profile.png` (already placed) |
| Resume PDF (initial) | `static/documents/resume.pdf` (already placed) |
| Update resume later, no redeploy | Visit `/resume/upload` (see below) |
| GitHub URL | `data/portfolio_data.py` -> `PROFILE["github_url"]` (already filled: your GitHub) |
| LinkedIn URL | `data/portfolio_data.py` -> `PROFILE["linkedin_url"]` (already filled: your LinkedIn) |
| Project repo / demo links | `data/portfolio_data.py` -> each project's `github_url` / `demo_url` |
| Project screenshots | `static/images/projects/` -- then reference them in the case-study template |
| Certificate images / verification links | `data/portfolio_data.py` -> `CERTIFICATIONS` list |
| Canonical domain (SEO) | `data/portfolio_data.py` -> `SITE_META["canonical_url"]`, plus `sitemap.xml` |
| All other text (headline, about, skills, experience) | `data/portfolio_data.py` |

Everything on the page pulls from `data/portfolio_data.py` -- you should almost never
need to touch a file in `templates/` to update content.

## Resume: download + backend-driven upload

- **Download**: the "Download Resume" button always calls `/resume/download`, which
  serves whatever PDF currently sits at `static/documents/resume.pdf`.
- **Upload (replace without redeploying)**: visit `/resume/upload`. This route is
  protected by an access token:
  1. Set `ADMIN_UPLOAD_TOKEN` in your `.env` file to a password only you know.
  2. Restart the app.
  3. Go to `/resume/upload`, enter the token once (stored in your session), and
     upload a new PDF. It immediately replaces the live file.
  - If `ADMIN_UPLOAD_TOKEN` is left blank, the upload form is disabled and says so --
    the download button keeps working with whatever file is already in place.

## Contact form

- Client-side + server-side validation (name, email format, subject, message length).
- Honeypot field (`company_website`) silently discards bot submissions.
- Basic per-IP rate limiting (5 requests / 60 seconds) on `/contact`.
- **No email service is wired up by default.** Submitted messages are appended to
  `instance/messages.log` so nothing is silently lost. To send real emails instead,
  fill in the `SMTP_*` variables in `.env` and add your own `smtplib` call in the
  `contact()` view in `app.py` (kept simple on purpose so you can wire up whichever
  provider -- Gmail SMTP, SendGrid, etc. -- you prefer).

## Deployment

### Render / Railway (recommended, both support Flask out of the box)
1. Push this project to a GitHub repository.
2. Create a new **Web Service** from that repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app` (add `gunicorn` to `requirements.txt` first: `pip install gunicorn` then re-freeze, or just add the line manually).
5. Add environment variables from `.env.example` in the host's dashboard (never commit `.env`).
6. Once live, update `SITE_META["canonical_url"]` in `data/portfolio_data.py` and the
   URLs in `sitemap.xml` to your real domain.

### PythonAnywhere
1. Upload the project (or `git clone` it) into your PythonAnywhere account.
2. Create a virtualenv and `pip install -r requirements.txt` inside it.
3. In the **Web** tab, create a new Flask web app pointing at `app.py` / the `app`
   object, and set the virtualenv path.
4. Set environment variables under the WSGI configuration file (`os.environ[...] = ...`)
   or a `.env` file loaded by `python-dotenv`.
5. Reload the web app.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Activate your virtualenv, then `pip install -r requirements.txt`. |
| `Address already in use` / port 5000 busy | Set `PORT=5050` (or any free port) in `.env`, or run `python app.py` after stopping the other process. |
| Resume download returns 404 | Make sure a file exists at `static/documents/resume.pdf`. |
| Resume upload says "disabled" | Set `ADMIN_UPLOAD_TOKEN` in `.env` and restart the app. |
| Contact form always fails | Check the browser console/network tab; confirm `/contact` returns JSON, not an HTML error page (usually means an exception -- check the Flask console). |
| Styles look unstyled / broken | Hard-refresh (Ctrl/Cmd+Shift+R) -- browsers aggressively cache `style.css`. |
| Blank profile photo / broken image | Confirm the file really is at `static/images/profile/profile.png`. |

## Final checklist -- placeholders still to replace

- [ ] Add per-project **GitHub repository URLs** in `data/portfolio_data.py` (each project's `github_url`) so the "Code" button appears on project cards and case studies.
- [ ] Add **live demo URLs** for any project that has a deployed version (`demo_url`).
- [ ] Add **certificate verification links / images** in the `CERTIFICATIONS` list.
- [ ] Add **dataset sources, preprocessing notes, evaluation evidence, and screenshots** for each project case study (marked with `[ADD ...]` placeholders on each case-study page).
- [ ] Set the **canonical domain** in `SITE_META["canonical_url"]` and in `sitemap.xml` once deployed.
- [ ] Decide on real **email delivery** for the contact form (currently logs to `instance/messages.log`), or keep checking the log periodically.
- [ ] Set a real `SECRET_KEY` and (optionally) `ADMIN_UPLOAD_TOKEN` in your production `.env`.

Already filled in from your details: name, email, phone, location, education, CGPA,
internships, certifications (titles/issuers), core project descriptions, GitHub
profile (`https://github.com/dhivyasubash19-glitch`), and LinkedIn profile
(`https://www.linkedin.com/in/dhivya-subash-7a997b383`).
