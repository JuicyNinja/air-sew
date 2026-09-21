/* Air Sew — motion & interaction layer
   Requires: GSAP 3 + ScrollTrigger, Lenis (loaded via CDN before this file) */
(function () {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasGsap = typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined";
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);

  /* ---------- Smooth scroll ---------- */
  let lenis = null;
  if (!reduce && typeof Lenis !== "undefined" && hasGsap) {
    lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }
  const scrollTo = (target) => {
    if (lenis) lenis.scrollTo(target, { offset: -80 });
    else target.scrollIntoView({ behavior: "smooth" });
  };
  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
      const id = a.getAttribute("href");
      if (id.length < 2) return;
      const t = $(id);
      if (t) { e.preventDefault(); scrollTo(t); }
    });
  });

  /* ---------- Split text helpers ---------- */
  function splitWords(el) {
    const text = el.textContent.trim();
    el.setAttribute("aria-label", text);
    el.innerHTML = text.split(/\s+/).map((w) => `<span class="word"><span>${w}</span></span>`).join(" ");
    return $$(".word > span", el);
  }
  function splitLines(el) {
    // Split into words, then group by rendered line
    const text = el.textContent.trim();
    el.setAttribute("aria-label", text);
    el.innerHTML = text.split(/\s+/).map((w) => `<span class="w">${w}</span>`).join(" ");
    const words = $$(".w", el);
    const lines = [];
    let curTop = null, cur = [];
    words.forEach((w) => {
      const top = w.offsetTop;
      if (curTop === null || Math.abs(top - curTop) < 4) { cur.push(w); curTop = top; }
      else { lines.push(cur); cur = [w]; curTop = top; }
    });
    if (cur.length) lines.push(cur);
    el.innerHTML = lines.map((ws) => `<span class="line"><span>${ws.map((w) => w.textContent).join(" ")}</span></span>`).join("");
    return $$(".line > span", el);
  }

  /* ---------- Preloader + hero intro ---------- */
  const pre = $(".preloader");
  const heroTitle = $(".hero__title");
  const heroWords = heroTitle ? splitWords(heroTitle) : [];
  const intro = () => {
    if (!hasGsap) { heroWords.forEach((w) => (w.style.transform = "none")); return; }
    const tl = gsap.timeline({ defaults: { ease: "power4.out" } });
    tl.to(heroWords, { y: 0, duration: 1.2, stagger: 0.06 }, 0)
      .from(".hero .eyebrow, .hero__sub, .hero__actions, .hero__scroll", { y: 30, opacity: 0, duration: 1, stagger: 0.1 }, 0.35)
      .from(".hero__stats .stat", { y: 24, opacity: 0, duration: 0.9, stagger: 0.08 }, 0.6)
      .from(".header", { y: -20, opacity: 0, duration: 0.8 }, 0.2);
    // page-hero (interior pages)
    const ph = $(".page-hero");
    if (ph) {
      gsap.from(".page-hero .crumbs, .page-hero h1, .page-hero .lead, .page-hero .hero__actions", { y: 36, opacity: 0, duration: 1.1, stagger: 0.1, ease: "power4.out", delay: 0.1 });
    }
  };

  if (pre && hasGsap && !reduce) {
    document.documentElement.classList.add("is-loading");
    if (lenis) lenis.stop();
    const tl = gsap.timeline({
      onComplete: () => { pre.remove(); if (lenis) lenis.start(); intro(); }
    });
    tl.to(".preloader__logo", { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" })
      .to(".preloader__line i", { scaleX: 1, duration: 1.1, ease: "power2.inOut" }, 0.2)
      .to(".preloader__inner", { opacity: 0, y: -14, duration: 0.5, ease: "power2.in" }, 1.35)
      .to(pre, { yPercent: -100, duration: 0.9, ease: "expo.inOut" }, 1.55);
  } else {
    if (pre) pre.remove();
    intro();
  }

  /* ---------- Header state ---------- */
  const header = $(".header");
  let lastY = 0;
  const onScroll = () => {
    const y = window.scrollY;
    header.classList.toggle("is-solid", y > 40);
    if (y > 400 && y > lastY + 6 && !document.body.classList.contains("menu-open")) header.classList.add("is-hidden");
    else if (y < lastY - 6 || y < 200) header.classList.remove("is-hidden");
    lastY = y;
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile drawer ---------- */
  const burger = $(".burger"), drawer = $(".drawer");
  if (burger && drawer) {
    burger.addEventListener("click", () => {
      const open = drawer.classList.toggle("is-open");
      burger.classList.toggle("is-open", open);
      document.body.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", open);
      if (lenis) open ? lenis.stop() : lenis.start();
    });
    $$(".drawer__item--sub > .drawer__link", drawer).forEach((btn) => {
      btn.addEventListener("click", () => btn.parentElement.classList.toggle("is-open"));
    });
  }

  /* ---------- Service card cursor glow ---------- */
  $$(".service").forEach((card) => {
    card.addEventListener("pointermove", (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty("--mx", `${e.clientX - r.left}px`);
      card.style.setProperty("--my", `${e.clientY - r.top}px`);
    });
  });

  /* ---------- Before / After ---------- */
  $$(".ba").forEach((ba) => {
    let dragging = false;
    const set = (clientX) => {
      const r = ba.getBoundingClientRect();
      const x = Math.min(Math.max((clientX - r.left) / r.width, 0.02), 0.98);
      ba.style.setProperty("--x", `${x * 100}%`);
    };
    ba.addEventListener("pointerdown", (e) => { dragging = true; ba.setPointerCapture(e.pointerId); set(e.clientX); });
    ba.addEventListener("pointermove", (e) => { if (dragging) set(e.clientX); });
    ba.addEventListener("pointerup", () => (dragging = false));
    ba.addEventListener("pointercancel", () => (dragging = false));
    if (hasGsap && !reduce) {
      gsap.fromTo(ba, { "--x": "88%" }, { "--x": "42%", duration: 2.2, ease: "power3.inOut", scrollTrigger: { trigger: ba, start: "top 75%", once: true } });
    }
  });

  /* ---------- Fleet tabs / filters ---------- */
  $$("[data-filter-group]").forEach((group) => {
    const tabs = $$("[data-filter]", group);
    const targetSel = group.dataset.filterGroup;
    const items = $$(targetSel + " [data-cat]");
    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        tabs.forEach((t) => t.classList.remove("is-active"));
        tab.classList.add("is-active");
        const f = tab.dataset.filter;
        items.forEach((it) => {
          const show = f === "all" || it.dataset.cat.split(" ").includes(f);
          it.classList.toggle("is-hidden", !show);
        });
        if (hasGsap) {
          gsap.fromTo(items.filter((i) => !i.classList.contains("is-hidden")), { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, stagger: 0.04, ease: "power3.out", overwrite: true });
          ScrollTrigger.refresh();
        }
      });
    });
  });

  /* ---------- Materials swatches ---------- */
  const tint = $(".materials__tint");
  $$(".swatch").forEach((sw) => {
    sw.addEventListener("click", () => {
      $$(".swatch").forEach((s) => s.classList.remove("is-active"));
      sw.classList.add("is-active");
      if (tint) { tint.style.background = sw.dataset.color; tint.style.opacity = sw.dataset.tint || 0.55; }
      const name = $(".material-name");
      if (name) name.textContent = sw.dataset.name;
    });
  });

  /* ---------- FAQ ---------- */
  $$(".faq__item").forEach((item) => {
    $(".faq__q", item).addEventListener("click", () => {
      const open = item.classList.contains("is-open");
      $$(".faq__item").forEach((i) => i.classList.remove("is-open"));
      if (!open) item.classList.add("is-open");
      if (hasGsap) setTimeout(() => ScrollTrigger.refresh(), 520);
    });
  });

  /* ---------- Contact form (client-side only) ---------- */
  const form = $("#project-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent(`Project inquiry — ${data.get("aircraft") || "Aircraft"} (${data.get("name")})`);
      const lines = [];
      for (const [k, v] of data.entries()) lines.push(`${k}: ${v}`);
      const body = encodeURIComponent(lines.join("\n"));
      window.location.href = `mailto:${form.dataset.to}?subject=${subject}&body=${body}`;
      const ok = $(".form__success");
      if (ok) ok.hidden = false;
    });
  }

  /* ---------- Cursor ---------- */
  const cur = $(".cursor");
  if (cur && window.matchMedia("(hover: hover)").matches) {
    let cx = 0, cy = 0, tx = 0, ty = 0;
    window.addEventListener("pointermove", (e) => { tx = e.clientX; ty = e.clientY; cur.style.opacity = 1; });
    const loop = () => { cx += (tx - cx) * 0.2; cy += (ty - cy) * 0.2; cur.style.transform = `translate(${cx}px, ${cy}px) translate(-50%,-50%)`; requestAnimationFrame(loop); };
    loop();
    document.addEventListener("pointerover", (e) => {
      const t = e.target.closest("a, button, .swatch");
      cur.classList.toggle("is-link", !!t);
      cur.classList.toggle("is-drag", !!e.target.closest(".ba"));
    });
  }

  /* ---------- Video play-when-visible ---------- */
  $$("video[data-lazy]").forEach((v) => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { if (!v.src && v.dataset.src) v.src = v.dataset.src; v.play().catch(() => {}); }
        else v.pause();
      });
    }, { rootMargin: "200px" });
    io.observe(v);
  });

  /* ---------- Counters ---------- */
  const countUp = (el) => {
    const target = parseFloat(el.dataset.count);
    const dur = 1600, t0 = performance.now();
    const fmt = (n) => Math.round(n).toLocaleString("en-US");
    const tick = (t) => {
      const p = Math.min((t - t0) / dur, 1);
      const e = 1 - Math.pow(1 - p, 4);
      el.firstChild.nodeValue = fmt(target * e);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if (!hasGsap || reduce) {
    // No motion fallbacks
    $$(".reveal, .reveal-fade").forEach((el) => { el.style.opacity = 1; el.style.transform = "none"; });
    $$("[data-count]").forEach(countUp);
    return;
  }

  /* ---------- Scroll-driven motion (GSAP) ---------- */
  window.addEventListener("load", () => {
    // Split line reveals
    $$("[data-split]").forEach((el) => {
      const spans = splitLines(el);
      gsap.to(spans, { y: 0, duration: 1.1, ease: "power4.out", stagger: 0.09, scrollTrigger: { trigger: el, start: "top 85%", once: true } });
    });

    // Word-by-word highlight statement
    $$(".big-statement").forEach((el) => {
      const text = el.textContent.trim();
      el.innerHTML = text.split(/\s+/).map((w) => `<span class="w">${w}</span>`).join(" ");
      const ws = $$(".w", el);
      ScrollTrigger.create({
        trigger: el, start: "top 80%", end: "bottom 45%", scrub: true,
        onUpdate: (self) => {
          const n = Math.floor(self.progress * ws.length);
          ws.forEach((w, i) => w.classList.toggle("on", i <= n));
        }
      });
    });

    // Generic reveals
    ScrollTrigger.batch(".reveal", {
      start: "top 88%", once: true,
      onEnter: (els) => gsap.to(els, { y: 0, opacity: 1, duration: 1.1, ease: "power4.out", stagger: 0.1, overwrite: true })
    });
    ScrollTrigger.batch(".reveal-fade", {
      start: "top 90%", once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, duration: 1.2, ease: "power2.out", stagger: 0.08, overwrite: true })
    });

    // Clip reveal for media
    $$(".media--reveal").forEach((m) => {
      gsap.to(m, { clipPath: "inset(0 0 0% 0)", duration: 1.4, ease: "expo.out", scrollTrigger: { trigger: m, start: "top 82%", once: true } });
      const img = $("img", m);
      if (img) gsap.from(img, { scale: 1.25, duration: 1.8, ease: "expo.out", scrollTrigger: { trigger: m, start: "top 82%", once: true } });
    });

    // Parallax media
    $$(".media--parallax").forEach((m) => {
      const img = $("img", m);
      if (!img) return;
      gsap.fromTo(img, { yPercent: -10 }, { yPercent: 10, ease: "none", scrollTrigger: { trigger: m, start: "top bottom", end: "bottom top", scrub: true } });
    });
    $$("[data-parallax]").forEach((el) => {
      const amt = parseFloat(el.dataset.parallax) || 60;
      gsap.fromTo(el, { y: -amt }, { y: amt, ease: "none", scrollTrigger: { trigger: el.parentElement, start: "top bottom", end: "bottom top", scrub: true } });
    });

    // Hero media parallax + fade
    const heroMedia = $(".hero__media, .page-hero__media");
    if (heroMedia) {
      gsap.to(heroMedia, { yPercent: 22, ease: "none", scrollTrigger: { trigger: heroMedia.parentElement, start: "top top", end: "bottom top", scrub: true } });
      gsap.to(".hero__content, .page-hero__content", { yPercent: -10, opacity: 0.2, ease: "none", scrollTrigger: { trigger: heroMedia.parentElement, start: "45% top", end: "bottom top", scrub: true } });
    }

    // Counters
    $$("[data-count]").forEach((el) => ScrollTrigger.create({ trigger: el, start: "top 90%", once: true, onEnter: () => countUp(el) }));

    // Process steps line
    $$(".step").forEach((s, i) => ScrollTrigger.create({ trigger: s, start: "top 80%", once: true, onEnter: () => setTimeout(() => s.classList.add("is-on"), i * 150) }));

    // Horizontal scroll section
    const hs = $(".hscroll");
    if (hs && window.matchMedia("(min-width: 901px)").matches) {
      const track = $(".hscroll__track", hs);
      const getDist = () => track.scrollWidth - window.innerWidth;
      gsap.to(track, {
        x: () => -getDist(), ease: "none",
        scrollTrigger: { trigger: hs, start: "top top", end: () => "+=" + getDist(), pin: true, scrub: 1, invalidateOnRefresh: true, anticipatePin: 1 }
      });
      $$(".hcard__img img", hs).forEach((img) => {
        gsap.fromTo(img, { xPercent: -6 }, { xPercent: 6, ease: "none", scrollTrigger: { trigger: hs, start: "top top", end: () => "+=" + getDist(), scrub: true } });
      });
    }

    // Big footer word
    const fb = $(".footer__big");
    if (fb) gsap.from(fb, { yPercent: 40, opacity: 0, ease: "power3.out", duration: 1.2, scrollTrigger: { trigger: fb, start: "top 95%", once: true } });

    // Magnetic buttons
    if (window.matchMedia("(hover: hover)").matches) {
      $$(".btn").forEach((b) => {
        b.addEventListener("pointermove", (e) => {
          const r = b.getBoundingClientRect();
          gsap.to(b, { x: (e.clientX - r.left - r.width / 2) * 0.25, y: (e.clientY - r.top - r.height / 2) * 0.35, duration: 0.5, ease: "power3.out" });
        });
        b.addEventListener("pointerleave", () => gsap.to(b, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.4)" }));
      });
    }

    ScrollTrigger.refresh();
  });
})();
