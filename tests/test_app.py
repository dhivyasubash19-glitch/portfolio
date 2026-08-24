import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as c:
        yield c


def test_home_page_loads(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"S. Dhivya" in res.data


def test_home_contains_all_nav_sections(client):
    res = client.get("/")
    html = res.data.decode("utf-8")
    for section_id in ["home", "about", "skills", "experience", "projects", "education", "certifications", "contact"]:
        assert f'id="{section_id}"' in html


def test_project_detail_valid_slug(client):
    res = client.get("/projects/heart-disease-prediction")
    assert res.status_code == 200
    assert b"Heart Disease Prediction" in res.data


def test_project_detail_invalid_slug_404(client):
    res = client.get("/projects/does-not-exist")
    assert res.status_code == 404


def test_resume_download(client):
    res = client.get("/resume/download")
    assert res.status_code in (200, 404)  # 404 only if resume.pdf hasn't been placed yet


def test_contact_form_validation_errors(client):
    res = client.post("/contact", data={"name": "", "email": "not-an-email", "subject": "", "message": "short"})
    assert res.status_code == 400
    body = res.get_json()
    assert body["ok"] is False
    assert "name" in body["errors"]
    assert "email" in body["errors"]


def test_contact_form_success(client):
    res = client.post("/contact", data={
        "name": "Recruiter Test",
        "email": "recruiter@example.com",
        "subject": "Opportunity",
        "message": "This is a sufficiently long test message.",
    })
    assert res.status_code == 200
    assert res.get_json()["ok"] is True


def test_contact_form_honeypot_silently_accepted(client):
    res = client.post("/contact", data={
        "name": "Bot",
        "email": "bot@example.com",
        "subject": "spam",
        "message": "spam message here",
        "company_website": "http://spam.example",
    })
    assert res.status_code == 200
    assert res.get_json()["ok"] is True


def test_404_page(client):
    res = client.get("/this-route-does-not-exist")
    assert res.status_code == 404


def test_robots_txt(client):
    res = client.get("/robots.txt")
    assert res.status_code == 200


def test_sitemap_xml(client):
    res = client.get("/sitemap.xml")
    assert res.status_code == 200
