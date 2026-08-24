(function () {
  "use strict";

  /* ---------------- Theme toggle ---------------- */
  var root = document.documentElement;
  var themeToggle = document.getElementById("theme-toggle");
  function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem("dhivya-theme", theme);
    if (themeToggle) themeToggle.setAttribute("aria-pressed", theme === "light" ? "true" : "false");
  }
  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      var current = root.getAttribute("data-theme") || "dark";
      setTheme(current === "dark" ? "light" : "dark");
    });
  }

  /* ---------------- Mobile nav ---------------- */
  var menuToggle = document.getElementById("menu-toggle");
  var primaryNav = document.getElementById("primary-nav");
  var navScrim = document.getElementById("nav-scrim");

  function openMenu() {
    primaryNav.classList.add("is-open");
    navScrim.classList.add("is-visible");
    menuToggle.setAttribute("aria-expanded", "true");
    menuToggle.setAttribute("aria-label", "Close menu");
    document.body.style.overflow = "hidden";
  }
  function closeMenu() {
    primaryNav.classList.remove("is-open");
    navScrim.classList.remove("is-visible");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open menu");
    document.body.style.overflow = "";
  }
  if (menuToggle && primaryNav && navScrim) {
    menuToggle.addEventListener("click", function () {
      var expanded = menuToggle.getAttribute("aria-expanded") === "true";
      expanded ? closeMenu() : openMenu();
    });
    navScrim.addEventListener("click", closeMenu);
    primaryNav.querySelectorAll(".nav-link").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeMenu();
    });
  }

  /* ---------------- Active-section highlighting ---------------- */
  var sections = Array.prototype.slice.call(document.querySelectorAll("main [id]"));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".nav-link"));
  if (sections.length && navLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    navLinks.forEach(function (link) { byId[link.dataset.section] = link; });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = byId[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("is-active"); });
            link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-40% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach(function (s) { observer.observe(s); });
  }

  /* ---------------- Back to top ---------------- */
  var backToTop = document.getElementById("back-to-top");
  if (backToTop) {
    backToTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------- Scroll reveal ---------------- */
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (reveals.length && "IntersectionObserver" in window) {
    var revealObserver = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    reveals.forEach(function (el) { revealObserver.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------------- Project filters ---------------- */
  var filterButtons = Array.prototype.slice.call(document.querySelectorAll(".filter-btn"));
  var projectCards = Array.prototype.slice.call(document.querySelectorAll(".project-card"));
  if (filterButtons.length && projectCards.length) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterButtons.forEach(function (b) { b.classList.remove("is-active"); b.setAttribute("aria-pressed", "false"); });
        btn.classList.add("is-active");
        btn.setAttribute("aria-pressed", "true");
        var filter = btn.dataset.filter;
        projectCards.forEach(function (card) {
          var match = filter === "All" || card.dataset.category === filter;
          card.style.display = match ? "" : "none";
        });
      });
    });
  }

  /* ---------------- Contact form (AJAX, no page reload) ---------------- */
  var form = document.getElementById("contact-form");
  if (form) {
    var statusBox = document.getElementById("form-status");
    var submitBtn = form.querySelector('button[type="submit"]');

    function clearErrors() {
      form.querySelectorAll(".field").forEach(function (f) {
        f.classList.remove("has-error");
        var err = f.querySelector(".field-error");
        if (err) err.textContent = "";
      });
    }

    function showErrors(errors) {
      Object.keys(errors).forEach(function (key) {
        var field = form.querySelector('[data-field="' + key + '"]');
        if (!field) return;
        field.classList.add("has-error");
        var err = field.querySelector(".field-error");
        if (err) err.textContent = errors[key];
      });
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      clearErrors();
      statusBox.className = "form-status";
      statusBox.textContent = "";

      var formData = new FormData(form);
      submitBtn.disabled = true;
      var originalLabel = submitBtn.textContent;
      submitBtn.textContent = "Sending...";

      fetch(form.action, { method: "POST", body: formData, headers: { "X-Requested-With": "XMLHttpRequest" } })
        .then(function (res) { return res.json().then(function (data) { return { status: res.status, data: data }; }); })
        .then(function (result) {
          if (result.data.ok) {
            form.reset();
            statusBox.classList.add("is-success");
            statusBox.textContent = "Thanks for reaching out! Your message has been sent -- I'll get back to you soon.";
          } else if (result.data.errors) {
            showErrors(result.data.errors);
            statusBox.classList.add("is-error");
            statusBox.textContent = "Please fix the highlighted fields and try again.";
          } else {
            statusBox.classList.add("is-error");
            statusBox.textContent = result.data.error || "Something went wrong. Please try again in a moment.";
          }
        })
        .catch(function () {
          statusBox.classList.add("is-error");
          statusBox.textContent = "Network error -- please try again, or email me directly.";
        })
        .finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = originalLabel;
        });
    });
  }
})();
