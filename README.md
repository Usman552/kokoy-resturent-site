# KOKOY — Restaurant · Patisserie, Multan

Website for **KOKOY**, a restaurant and patisserie at 1A/C Bosan Road, A Block, Gulgasht Colony, Multan.

**Live site:** https://usman552.github.io/kokoy-resturent-site/

The page follows one idea, "The Arch": you arrive at KOKOY's entrance at night, scroll through the arch into the lit rooms, then on to the food, the menu, dessert and the evening outside.

## Features

- Scroll-driven arch entrance that opens into the interior
- Pinned interior walk and pinned signature-dish sequence
- Interactive menu with category tabs and matching photographs
- Sideways "After dark" gallery on desktop, swipe gallery on mobile
- Reservation form with validation (concept only, see below)
- Responsive layout for phones, tablets and desktop
- Respects `prefers-reduced-motion`
- Keyboard-friendly navigation, labelled form fields, alt text on every photo

## Tech

| Area | Choice |
| --- | --- |
| Markup, styles, logic | Plain HTML, CSS and JavaScript in a single `index.html` (no build step) |
| Animation | [GSAP 3.12.5](https://gsap.com/) and ScrollTrigger, loaded from cdnjs |
| Fonts | Cormorant Garamond and Jost, from Google Fonts |
| Images | WebP files in `img/` |
| Hosting | GitHub Pages, served from the `main` branch |

## Run locally

No install needed. From the project folder:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Deploy (CD)

GitHub Pages publishes `main` automatically. Every push to `main` goes live in about a minute.

## CI

`.github/workflows/ci.yml` runs on every push and pull request. It runs `scripts/check_site.py`, which fails if:

- `index.html` references a local file that does not exist
- an image in `img/` is missing or not a valid file
- the GSAP script tags are missing

## Content still to be confirmed by KOKOY

The site does not invent restaurant information. These are placeholders until KOKOY supplies them:

- Prices (shown as `Rs —`)
- Opening hours
- Email address
- Official menu item names (current names describe the photographs)

The reservation form is a concept: it validates input and shows a confirmation, but nothing is sent anywhere yet.

## Photography

All photographs are from KOKOY. Most are about 730px wide, so the layout sizes them near their native resolution to avoid blur. Higher-resolution originals would let the photos run larger.

## Project structure

```
index.html          the whole site
img/                KOKOY photography (WebP)
scripts/            CI check script
.github/workflows/  CI
```
