"""
S. Dhivya -- Portfolio Website
Flask application entry point.
"""
import os
import re
import time
import secrets
from datetime import datetime

from flask import (
    Flask, render_template, request, redirect, url_for,
    send_from_directory, flash, jsonify, abort, session
)
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from data.portfolio_data import (
    PROFILE, NAV_LINKS, SKILLS, EXPERIENCE, PROJECTS, PROJECT_FILTERS,
    EDUCATION, CERTIFICATIONS, CURRENTLY_LEARNING, SITE_META,
)

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "static", "documents")
RESUME_FILENAME = "resume.pdf"

ALLOWED_RESUME_EXTENSIONS = {"pdf"}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB cap for uploads

# very small in-memory rate limiter for the contact endpoint {ip: [timestamps]}
_contact_hits = {}
CONTACT_WINDOW_SECONDS = 60
CONTACT_MAX_REQUESTS = 5


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(32))
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
    app.config["ADMIN_UPLOAD_TOKEN"] = os.environ.get("ADMIN_UPLOAD_TOKEN", "")

    os.makedirs(DOCS_DIR, exist_ok=True)

    # ---------------------------------------------------------------
    # Context available to every template
    # ---------------------------------------------------------------
    @app.context_processor
    def inject_globals():
        return {
            "profile": PROFILE,
            "nav_links": NAV_LINKS,
            "site_meta": SITE_META,
            "current_year": datetime.utcnow().year,
            "resume_exists": os.path.exists(os.path.join(DOCS_DIR, RESUME_FILENAME)),
        }

    # ---------------------------------------------------------------
    # Public pages
    # ---------------------------------------------------------------
    @app.route("/")
    def index():
        return render_template(
            "index.html",
            skills=SKILLS,
            experience=EXPERIENCE,
            projects=PROJECTS,
            project_filters=PROJECT_FILTERS,
            education=EDUCATION,
            certifications=CERTIFICATIONS,
            currently_learning=CURRENTLY_LEARNING,
        )

    @app.route("/projects/<slug>")
    def project_detail(slug):
        project = next((p for p in PROJECTS if p["slug"] == slug), None)
        if project is None:
            abort(404)
        return render_template("project_detail.html", project=project)

    # ---------------------------------------------------------------
    # Resume: download (public) + upload (backend-driven update)
    # ---------------------------------------------------------------
    @app.route("/resume/download")
    def resume_download():
        if not os.path.exists(os.path.join(DOCS_DIR, RESUME_FILENAME)):
            abort(404)
        return send_from_directory(
            DOCS_DIR, RESUME_FILENAME,
            as_attachment=True,
            download_name="S_Dhivya_Resume.pdf",
        )

    @app.route("/resume/upload", methods=["GET", "POST"])
    def resume_upload():
        """
        Lets Dhivya replace the live resume file without touching code.
        Protected by ADMIN_UPLOAD_TOKEN (set in .env). Without a token
        configured, uploads are disabled and the form says so.
        """
        token_configured = bool(app.config["ADMIN_UPLOAD_TOKEN"])
        authed = session.get("resume_admin") is True

        if request.method == "POST":
            if not token_configured:
                flash("Uploads are disabled until ADMIN_UPLOAD_TOKEN is set in the environment.", "error")
                return redirect(url_for("resume_upload"))

            if not authed:
                supplied = request.form.get("token", "")
                if not secrets.compare_digest(supplied, app.config["ADMIN_UPLOAD_TOKEN"]):
                    flash("Incorrect access token.", "error")
                    return redirect(url_for("resume_upload"))
                session["resume_admin"] = True
                authed = True

            file = request.files.get("resume")
            if not file or file.filename == "":
                flash("Choose a PDF file to upload.", "error")
                return redirect(url_for("resume_upload"))

            filename = secure_filename(file.filename)
            ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
            if ext not in ALLOWED_RESUME_EXTENSIONS:
                flash("Only PDF files are accepted.", "error")
                return redirect(url_for("resume_upload"))

            dest = os.path.join(DOCS_DIR, RESUME_FILENAME)
            file.save(dest)
            flash("Resume updated. The Download Resume button now serves this file.", "success")
            return redirect(url_for("resume_upload"))

        return render_template("resume_upload.html", token_configured=token_configured, authed=authed)

    # ---------------------------------------------------------------
    # Contact form
    # ---------------------------------------------------------------
    @app.route("/contact", methods=["POST"])
    def contact():
        ip = request.remote_addr or "unknown"
        now = time.time()
        hits = [t for t in _contact_hits.get(ip, []) if now - t < CONTACT_WINDOW_SECONDS]
        if len(hits) >= CONTACT_MAX_REQUESTS:
            return jsonify({"ok": False, "error": "Too many requests. Please try again in a minute."}), 429
        hits.append(now)
        _contact_hits[ip] = hits

        # honeypot field -- bots fill hidden fields, humans don't
        if request.form.get("company_website"):
            return jsonify({"ok": True})  # silently accept, do nothing

        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()
        subject = (request.form.get("subject") or "").strip()
        message = (request.form.get("message") or "").strip()

        errors = {}
        if not name or len(name) < 2:
            errors["name"] = "Enter your name."
        if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors["email"] = "Enter a valid email address."
        if not subject:
            errors["subject"] = "Enter a subject."
        if not message or len(message) < 10:
            errors["message"] = "Message should be at least 10 characters."

        if errors:
            return jsonify({"ok": False, "errors": errors}), 400

        # No email service is configured in this starter. Messages are logged
        # to instance/messages.log instead of being silently dropped.
        # See README for how to wire up real email delivery via SMTP env vars.
        os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)
        log_path = os.path.join(BASE_DIR, "instance", "messages.log")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.utcnow().isoformat()} | {name} | {email} | {subject} | "
                f"{message.replace(chr(10), ' ')}\n"
            )

        return jsonify({"ok": True})

    # ---------------------------------------------------------------
    # SEO helpers
    # ---------------------------------------------------------------
    @app.route("/robots.txt")
    def robots():
        return send_from_directory(BASE_DIR, "robots.txt") if os.path.exists(
            os.path.join(BASE_DIR, "robots.txt")
        ) else ("User-agent: *\nAllow: /\n", 200, {"Content-Type": "text/plain"})

    @app.route("/sitemap.xml")
    def sitemap():
        if os.path.exists(os.path.join(BASE_DIR, "sitemap.xml")):
            return send_from_directory(BASE_DIR, "sitemap.xml", mimetype="application/xml")
        abort(404)

    # ---------------------------------------------------------------
    # Error handlers
    # ---------------------------------------------------------------
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("500.html"), 500

    return app


app = create_app()

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=debug, port=port)
