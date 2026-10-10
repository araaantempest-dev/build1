import os

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lumiere - Taste the Extraordinary</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;0,800;1,700&display=swap" rel="stylesheet">
<script type="importmap">
{ "imports": {
  "three": "https://unpkg.com/three@0.143.0/build/three.module.js",
  "three/examples/jsm/": "https://unpkg.com/three@0.143.0/examples/jsm/"
}}
</script>
<style>
:root{
  --bg:#04060f;--bg-2:#060a18;--ink:#f3f6ff;--muted:#9aa6c4;--muted-2:#6b7796;
  --line:rgba(150,175,230,.12);--line-strong:rgba(150,175,230,.22);
  --accent:#f0c45d;--accent-2:#d3922f;--accent-ink:#200e03;
  --glass:rgba(12,18,38,.55);--glass-2:rgba(16,24,48,.65);
  --radius:18px;--radius-lg:26px;--maxw:1180px;
  --shadow:0 30px 80px -30px rgba(0,0,0,.75);
  --font:'Inter',-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
  --font-serif:'Playfair Display',Georgia,serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:hidden}
a{color:inherit;text-decoration:none}
html.lenis,html.lenis body{height:auto}
.lenis.lenis-smooth{scroll-behavior:auto !important}
.lenis.lenis-smooth [data-lenis-prevent]{overscroll-behavior:contain}
.lenis.lenis-stopped{overflow:hidden}
[data-reveal]{opacity:0;transform:translateY(26px);transition:opacity .7s cubic-bezier(.22,.7,.2,1),transform .7s cubic-bezier(.22,.7,.2,1);transition-delay:var(--rd,0ms);will-change:opacity,transform}
[data-reveal].in{opacity:1;transform:none}
.planet-canvas{position:fixed;inset:0;width:100vw;height:100vh;display:block;z-index:0;pointer-events:none}
.page{position:relative;z-index:1}
.section{position:relative;z-index:1;max-width:var(--maxw);margin:0 auto;padding:clamp(80px,12vw,160px) 24px}
.eyebrow{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin-bottom:18px}
.section-head{max-width:680px;margin:0 auto clamp(48px,6vw,80px);text-align:center}
.section-head h2,.showcase-copy h2,.cta-card h2{font-size:clamp(30px,4.4vw,50px);font-weight:800;line-height:1.05;letter-spacing:-.02em;text-shadow:0 2px 40px rgba(0,0,0,.6);font-family:var(--font-serif)}
.section-head p{margin-top:18px;color:var(--muted);font-size:18px;line-height:1.65;text-shadow:0 1px 24px rgba(0,0,0,.55)}
.btn{display:inline-flex;align-items:center;gap:9px;font-size:15px;font-weight:600;padding:13px 22px;border-radius:999px;border:1px solid transparent;cursor:pointer;transition:transform .18s ease,box-shadow .25s ease,background .2s ease,border-color .2s ease;white-space:nowrap}
.btn svg{width:17px;height:17px}
.btn-primary{color:var(--accent-ink);background:linear-gradient(180deg,var(--accent),var(--accent-2));box-shadow:0 10px 30px -8px rgba(240,196,93,.55),inset 0 1px 0 rgba(255,255,255,.4)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 16px 38px -8px rgba(240,196,93,.7)}
.btn-outline{color:var(--ink);background:rgba(255,255,255,.04);border-color:var(--line-strong);backdrop-filter:blur(10px)}
.btn-outline:hover{background:rgba(255,255,255,.09);transform:translateY(-2px)}
.btn-ghost{color:var(--ink);background:rgba(255,255,255,.05);border-color:var(--line-strong);padding:9px 18px}
.btn-ghost:hover{background:rgba(255,255,255,.1)}
.hero{min-height:100vh;display:flex;flex-direction:column;background:radial-gradient(125% 62% at 50% -10%,rgba(4,6,15,.82) 0%,rgba(4,6,15,.28) 44%,transparent 68%)}
.nav{max-width:var(--maxw);margin:0 auto;padding:22px 24px;display:flex;align-items:center;justify-content:space-between;width:100%}
.brand{display:inline-flex;align-items:center;gap:9px;font-weight:800;font-size:19px;letter-spacing:.16em;font-family:var(--font-serif)}
.brand-mark{color:var(--accent);font-size:22px;transform:translateY(-1px)}
.nav-links{display:flex;gap:30px;list-style:none}
.nav-links a{font-size:14.5px;color:var(--muted);transition:color .2s}
.nav-links a:hover{color:var(--ink)}
.hero-inner{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:translateY(-10vh);padding:0 24px}
.hero-title{font-size:clamp(34px,5.2vw,62px);font-weight:800;line-height:1.04;letter-spacing:-.03em;max-width:15ch;text-shadow:0 2px 50px rgba(0,0,0,.55);font-family:var(--font-serif)}
.hero-title em{font-style:normal;background:linear-gradient(180deg,var(--accent),var(--accent-2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.hero-sub{margin-top:24px;max-width:560px;font-size:clamp(16px,2vw,19px);line-height:1.6;color:var(--muted)}
.hero-actions{margin-top:38px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.logos{text-align:center;padding:0 24px clamp(36px,6vw,64px)}
.logos-label{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted-2);margin-bottom:20px}
.logos-row{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:clamp(24px,5vw,56px)}
.logo{font-size:17px;font-weight:700;color:var(--muted-2);opacity:.8;transition:color .2s,opacity .2s;font-family:var(--font-serif);letter-spacing:.06em}
.logo:hover{color:var(--ink);opacity:1}
.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{padding:30px;border-radius:var(--radius);background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(14px);transition:transform .3s ease,border-color .3s ease,background .3s ease;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;inset:0;background:radial-gradient(120% 120% at 0% 0%,rgba(240,196,93,.08),transparent 45%);opacity:0;transition:opacity .3s ease;pointer-events:none}
.card:hover{transform:translateY(-4px);border-color:var(--line-strong);background:var(--glass-2)}
.card:hover::before{opacity:1}
.card-icon{width:46px;height:46px;border-radius:12px;color:var(--accent);background:rgba(240,196,93,.1);border:1px solid rgba(240,196,93,.18);display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.card h3{font-size:19px;font-weight:700;margin-bottom:10px;font-family:var(--font-serif)}
.card p{font-size:15px;color:var(--muted);line-height:1.6}
.showcase-grid{display:grid;grid-template-columns:1fr 1.05fr;gap:clamp(36px,6vw,72px);align-items:center}
.showcase-copy p{margin-top:18px;color:var(--muted);font-size:17px;line-height:1.65}
.showcase-copy .btn{margin-top:30px}
.dashboard{padding:24px;border-radius:var(--radius-lg);background:var(--glass-2);border:1px solid var(--line-strong);box-shadow:var(--shadow);backdrop-filter:blur(18px);position:relative;overflow:hidden}
.dashboard::after{content:'';position:absolute;inset:0;border-radius:var(--radius-lg);background:linear-gradient(160deg,rgba(240,196,93,.35),transparent 40%);pointer-events:none;mask:linear-gradient(#fff,#fff) content-box,linear-gradient(#fff,#fff);mask-composite:exclude;-webkit-mask-composite:destination-out;padding:1px}
.dash-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
.dash-top span{font-size:14px;font-weight:600;color:var(--muted);font-family:var(--font-serif)}
.dash-live{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;color:var(--accent)}
.dash-dot{width:7px;height:7px;border-radius:50%;background:var(--accent);animation:pulse-dot 1.8s infinite}
@keyframes pulse-dot{0%,100%{opacity:1}50%{opacity:.4}}
.dash-bars{display:flex;align-items:flex-end;gap:10px;height:150px;background:rgba(0,0,0,.25);border:1px solid var(--line);border-radius:14px;padding:16px 16px 0;margin-bottom:18px}
.dash-bar{flex:1;border-radius:6px 6px 3px 3px;background:linear-gradient(180deg,var(--accent),rgba(211,146,47,.25));transform-origin:bottom;animation:grow .9s cubic-bezier(.22,.7,.2,1) both}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.dash-rows{display:flex;flex-direction:column;gap:12px}
.dash-row{display:grid;grid-template-columns:130px 1fr;gap:14px;align-items:center;font-size:13.5px;color:var(--muted)}
.dash-track{height:8px;border-radius:999px;background:rgba(255,255,255,.06);overflow:hidden}
.dash-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,var(--accent-2),var(--accent));animation:fill .9s cubic-bezier(.22,.7,.2,1) .3s both}
@keyframes fill{from{width:0}to{width:var(--w)}}
.stats{margin-top:clamp(56px,8vw,96px);display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.stat{text-align:center;padding:30px 18px;border-radius:var(--radius);background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(12px)}
.stat-value{font-size:clamp(30px,4vw,44px);font-weight:800;background:linear-gradient(180deg,#fff,var(--accent));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;font-family:var(--font-serif)}
.stat-label{font-size:14px;color:var(--muted);margin-top:8px}
.cta-card{max-width:760px;margin:0 auto;padding:clamp(48px,7vw,80px) clamp(28px,5vw,64px);border-radius:var(--radius-lg);background:radial-gradient(120% 140% at 50% 0%,rgba(240,196,93,.12),transparent 55%),var(--glass-2);border:1px solid var(--line-strong);box-shadow:var(--shadow);backdrop-filter:blur(18px);text-align:center}
.cta-card p{margin-top:18px;color:var(--muted);font-size:17px;line-height:1.65}
.cta-card .hero-actions{margin-top:36px}
.footer{display:flex;justify-content:space-between;gap:48px;flex-wrap:wrap;margin-top:clamp(64px,9vw,110px);padding-top:48px;border-top:1px solid var(--line)}
.footer-brand .brand{font-size:16px;margin-bottom:12px}
.footer-brand p{font-size:14px;color:var(--muted);max-width:240px;line-height:1.6}
.footer-cols{display:flex;gap:clamp(32px,5vw,64px)}
.footer-col h5{font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted-2);margin-bottom:16px}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.footer-col a{font-size:14px;color:var(--muted);transition:color .2s}
.footer-col a:hover{color:var(--ink)}
.copyright{text-align:center;margin-top:56px;font-size:13px;color:var(--muted-2)}
@media(max-width:980px){.feature-grid{grid-template-columns:repeat(2,1fr)}.showcase-grid{grid-template-columns:1fr;text-align:center}.showcase-copy{text-align:center}.showcase-copy .btn{display:inline-flex}.stats{grid-template-columns:repeat(2,1fr)}}
@media(max-width:720px){.nav-links{display:none}.nav{padding:18px 20px}.section{padding:clamp(64px,16vw,110px) 20px}}
@media(max-width:560px){.feature-grid{grid-template-columns:1fr}.dash-row{grid-template-columns:90px 1fr}.hero-actions .btn{flex:1}.cta-card{padding:40px 22px}.footer{flex-direction:column}}
@media(max-width:380px){.stats{grid-template-columns:1fr}.logos-row{gap:16px}}
@media(prefers-reduced-motion:reduce){[data-reveal]{opacity:1!important;transform:none!important;transition:none!important}.dash-bar,.dash-fill{animation:none!important}.dash-bar{transform:scaleY(1)!important}}
</style>
</head>
<body>
<canvas class="planet-canvas" id="planetCanvas"></canvas>
<div class="page" id="top">

<header class="hero">
<nav class="nav">
<a class="brand" href="#top"><span class="brand-mark">&#10022;</span>Lumiere</a>
<ul class="nav-links">
<li><a href="#menu">Menu</a></li>
<li><a href="#experience">Experience</a></li>
<li><a href="#reservations">Reservations</a></li>
<li><a href="#private">Private Dining</a></li>
</ul>
<button class="btn btn-ghost" onclick="document.getElementById('reservations').scrollIntoView({behavior:'smooth'})">Reserve a Table</button>
</nav>
<div class="hero-inner">
<h1 class="hero-title" data-reveal style="--rd:60ms">Dine Beyond<br><em>Imagination</em></h1>
<p class="hero-sub" data-reveal style="--rd:180ms">Experience a culinary journey crafted from the world's finest ingredients, where every dish tells a story and every evening becomes an unforgettable memory.</p>
<div class="hero-actions" data-reveal style="--rd:300ms">
<button class="btn btn-primary" onclick="document.getElementById('reservations').scrollIntoView({behavior:'smooth'})">Reserve Your Table <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></button>
<button class="btn btn-outline" onclick="document.getElementById('menu').scrollIntoView({behavior:'smooth'})">Explore the Menu</button>
</div>
</div>
</header>

<div class="logos" data-reveal style="--rd:420ms">
<p class="logos-label">Celebrated by the world's finest critics</p>
<div class="logos-row">
<span class="logo">Michelin</span>
<span class="logo">Forbes</span>
<span class="logo">Bon Appetit</span>
<span class="logo">Wine Spectator</span>
<span class="logo">Saveur</span>
<span class="logo">James Beard</span>
</div>
</div>

<section class="section features" id="menu">
<div class="section-head">
<span class="eyebrow" data-reveal>A world of flavour</span>
<h2 data-reveal style="--rd:80ms">One dining destination for every extraordinary moment</h2>
<p data-reveal style="--rd:160ms">Stop settling for ordinary. Lumiere unifies ingredient provenance, culinary artistry, and atmospheric perfection into a single experience your palate will never forget.</p>
</div>
<div class="feature-grid">
<div class="card" data-reveal style="--rd:0ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg></div>
<h3>Seasonal Menu</h3>
<p>Every dish is reimagined quarterly from peak-harvest farms, paired with ingredients that nature offers only briefly.</p>
</div>
<div class="card" data-reveal style="--rd:90ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5M4 19h16"/><path d="M8 16v-4M13 16V8M18 16v-7"/></svg></div>
<h3>Live Sommelier</h3>
<p>In-house sommeliers curate wine pairings in real time, turning every glass into the perfect complement to your plate.</p>
</div>
<div class="card" data-reveal style="--rd:180ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
<h3>Private Dining</h3>
<p>Reserve our exclusive chef's table for intimate gatherings with tailored menus and dedicated staff.</p>
</div>
<div class="card" data-reveal style="--rd:270ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8Z"/></svg></div>
<h3>Instant Reservation</h3>
<p>Secure your evening in seconds. Our system confirms availability and your preferences the moment you submit.</p>
</div>
<div class="card" data-reveal style="--rd:360ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg></div>
<h3>Dietary Excellence</h3>
<p>Every allergy and dietary philosophy honored. Our kitchen adapts without compromising an ounce of artistry.</p>
</div>
<div class="card" data-reveal style="--rd:450ms">
<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20Z"/></svg></div>
<h3>Global Ingredients</h3>
<p>Truffles from Perigord, saffron from Kashmir, wagyu from Hokkaido. The world's best ingredients, on your plate tonight.</p>
</div>
</div>
</section>

<section class="section showcase" id="experience">
<div class="showcase-grid">
<div class="showcase-copy">
<span class="eyebrow" data-reveal>Built for connoisseurs</span>
<h2 data-reveal style="--rd:90ms">Taste every course unfold in perfect sequence</h2>
<p data-reveal style="--rd:180ms">Every flavour, texture, and aroma orchestrated live. Lumiere gives our chefs the altitude to sense what your palate craves and the mastery to deliver it flawlessly.</p>
<button class="btn btn-primary" data-reveal style="--rd:270ms" onclick="document.getElementById('reservations').scrollIntoView({behavior:'smooth'})">Explore the Experience <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></button>
</div>
<div class="dashboard" data-reveal style="--rd:160ms">
<div class="dash-top">
<span>Tonight's Covers - Table 12</span>
<span class="dash-live"><span class="dash-dot"></span>Live</span>
</div>
<div class="dash-bars">
<div class="dash-bar" style="height:62%;animation-delay:0ms"></div>
<div class="dash-bar" style="height:88%;animation-delay:90ms"></div>
<div class="dash-bar" style="height:47%;animation-delay:180ms"></div>
<div class="dash-bar" style="height:95%;animation-delay:270ms"></div>
<div class="dash-bar" style="height:71%;animation-delay:360ms"></div>
<div class="dash-bar" style="height:80%;animation-delay:450ms"></div>
<div class="dash-bar" style="height:58%;animation-delay:540ms"></div>
</div>
<div class="dash-rows">
<div class="dash-row"><span>Amuse-bouche</span><div class="dash-track"><div class="dash-fill" style="--w:90%"></div></div></div>
<div class="dash-row"><span>Entree</span><div class="dash-track"><div class="dash-fill" style="--w:72%"></div></div></div>
<div class="dash-row"><span>Plat principal</span><div class="dash-track"><div class="dash-fill" style="--w:48%"></div></div></div>
<div class="dash-row"><span>Dessert</span><div class="dash-track"><div class="dash-fill" style="--w:34%"></div></div></div>
</div>
</div>
</div>
<div class="stats">
<div class="stat" data-reveal style="--rd:0ms"><div class="stat-value">3 *</div><div class="stat-label">Michelin Stars awarded</div></div>
<div class="stat" data-reveal style="--rd:80ms"><div class="stat-value">98%</div><div class="stat-label">Guest satisfaction score</div></div>
<div class="stat" data-reveal style="--rd:160ms"><div class="stat-value">40+</div><div class="stat-label">Countries of ingredient origin</div></div>
<div class="stat" data-reveal style="--rd:240ms"><div class="stat-value">18yr</div><div class="stat-label">Head Chef's culinary mastery</div></div>
</div>
</section>

<section class="section cta" id="reservations">
<div class="cta-card">
<span class="eyebrow" data-reveal style="--rd:60ms">Your table awaits</span>
<h2 data-reveal style="--rd:140ms">Begin an evening you will never forget</h2>
<p data-reveal style="--rd:220ms">Reserve in minutes. Dietary preferences noted. Complimentary amuse-bouche on arrival. Join thousands of guests who made Lumiere their most treasured memory.</p>
<div class="hero-actions" data-reveal style="--rd:300ms">
<button class="btn btn-primary">Reserve Your Table <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></button>
<button class="btn btn-outline">Speak to Our Host</button>
</div>
</div>
<footer class="footer" id="private">
<div class="footer-brand">
<a class="brand" href="#top"><span class="brand-mark">&#10022;</span>Lumiere</a>
<p>The fine dining destination for those who believe every meal should be a masterpiece.</p>
</div>
<div class="footer-cols">
<div class="footer-col">
<h5>Dining</h5>
<ul>
<li><a href="#menu">Seasonal Menu</a></li>
<li><a href="#experience">Wine Cellar</a></li>
<li><a href="#private">Private Events</a></li>
</ul>
</div>
<div class="footer-col">
<h5>Lumiere</h5>
<ul>
<li><a href="#">Our Story</a></li>
<li><a href="#">The Chefs</a></li>
<li><a href="#">Press</a></li>
</ul>
</div>
<div class="footer-col">
<h5>Information</h5>
<ul>
<li><a href="#">Privacy</a></li>
<li><a href="#">Terms</a></li>
<li><a href="#">Allergens</a></li>
</ul>
</div>
</div>
</footer>
<p class="copyright">&#169; <span id="yr"></span> Lumiere, Inc. &#8212; Crafted among the stars.</p>
</section>

</div>
<script type="module">
import * as THREE from 'three';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { GammaCorrectionShader } from 'three/examples/jsm/shaders/GammaCorrectionShader.js';
import { CopyShader } from 'three/examples/jsm/shaders/CopyShader.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import Lenis from 'https://unpkg.com/lenis@1.3.23/dist/lenis.mjs';

document.getElementById('yr').textContent = new Date().getFullYear();
const PRM = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

const CONFIG = {
  rimColor:'#c1faff', rimPower:2.4, nightLights:10, terrainDepth:0.33, terrainShade:1.3,
  oceanGlint:0.45, oceanDeep:0.12, oceanFlow:3, oceanFlowSpeed:0.8, oceanFlowScale:2.1,
  glowColor:'#3a6cff', glowIntensity:3.35, planetRadius:1.95, spin:0.03, initRotation:2.07,
  tilt:0.37, autoRotate:0,
  cloud1Height:1.005, cloud1Opacity:0.6, cloud1Spin:0.06,
  cloud2Height:1.03,  cloud2Opacity:0.5, cloud2Spin:0.14,
  cloud3Height:1.075, cloud3Opacity:0.5, cloud3Spin:0.1,
  bgColor:'#040a1e', flameColor:'#3a6cff', flameColor2:'#c1faff', flameAmt:0.15,
  atmoColor:'#9fc4ff', atmoCount:320, atmoSize:22, atmoSpeed:0.8,
  starColor:'#cfe0ff', starCount:1400, starSize:1.6, starFlicker:1,
  markerColor:'#ffd27a', markerCount:60, markerSize:16, markerSpeed:0.5,
};
const LAYERS = { NONE:0, TORUS_SCENE:1, BLOOM_SCENE:2, ENTIRE_SCENE:3 };
const ASSET = 'https://api.getlayers.ai/storage/v1/object/public/public/assets/ascend-d9857ad1f2';

const Lerp = (a,b,t) => a+(b-a)*t;
const clampV = (v,lo,hi) => Math.max(lo,Math.min(hi,v));
function hexToVec3(hex){
  const r=parseInt(hex.slice(1,3),16)/255, g=parseInt(hex.slice(3,5),16)/255, b=parseInt(hex.slice(5,7),16)/255;
  return new THREE.Vector3(r,g,b);
}
function smoothstepF(t){ return t*t*(3-2*t); }
function sample(stops,p){
  for(let i=0;i<stops.length-1;i++){
    const a=stops[i], b=stops[i+1];
    if(p>=a.p && p<=b.p){ const t=(p-a.p)/(b.p-a.p); return Lerp(a.v,b.v,smoothstepF(t)); }
  }
  return stops[stops.length-1].v;
}

const SNOISE = `
vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}
float snoise(vec3 v){
  const vec2 C=vec2(1.0/6.0,1.0/3.0);const vec4 D=vec4(0.0,0.5,1.0,2.0);
  vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);
  vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.0-g;
  vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);
  vec3 x1=x0-i1+1.0*C.xxx;vec3 x2=x0-i2+2.0*C.xxx;vec3 x3=x0-1.0+3.0*C.xxx;
  i=mod(i,289.0);
  vec4 p=permute(permute(permute(i.z+vec4(0.0,i1.z,i2.z,1.0))+i.y+vec4(0.0,i1.y,i2.y,1.0))+i.x+vec4(0.0,i1.x,i2.x,1.0));
  float n_=1.0/7.0;vec3 ns=n_*D.wyz-D.xzx;
  vec4 j=p-49.0*floor(p*ns.z*ns.z);
  vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.0*x_);
  vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.0-abs(x)-abs(y);
  vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);
  vec4 s0=floor(b0)*2.0+1.0;vec4 s1=floor(b1)*2.0+1.0;vec4 sh=-step(h,vec4(0.0));
  vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
  vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);
  vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
  p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
  vec4 m=max(0.5-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);m=m*m;
  return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
}`;

const canvas = document.getElementById('planetCanvas');
let W = window.innerWidth, H = window.innerHeight;

const renderer = new THREE.WebGL1Renderer({canvas, antialias:true});
renderer.setPixelRatio(devicePixelRatio);
renderer.setSize(W,H);
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.VSMShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(40, W/H, 0.1, 200);
camera.position.set(0,0,8);
camera.layers.enable(LAYERS.TORUS_SCENE);
camera.layers.enable(LAYERS.BLOOM_SCENE);
camera.layers.enable(LAYERS.ENTIRE_SCENE);
scene.add(camera);

const ambLight = new THREE.AmbientLight(0xffffff,1.8);
ambLight.layers.set(LAYERS.ENTIRE_SCENE);
scene.add(ambLight);
const dirLight = new THREE.DirectionalLight(0xffffff,0.8);
dirLight.position.set(0,10,2);
dirLight.layers.set(LAYERS.ENTIRE_SCENE);
scene.add(dirLight);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.dampingFactor = 0.06;
controls.enablePan = false; controls.enabled = false;
controls.autoRotate = true; controls.autoRotateSpeed = CONFIG.autoRotate;
controls.minDistance = 3.5; controls.maxDistance = 16;
controls.target.set(0,0,0);

const FinalPass = {
  uniforms:{
    iTime:{value:0}, tDiffuse:{value:null}, torusTexture:{value:null},
    bloomTexture:{value:null}, haloTexture:{value:null},
    uBg:{value:hexToVec3(CONFIG.bgColor)},
    uFlameA:{value:hexToVec3(CONFIG.flameColor)},
    uFlameB:{value:hexToVec3(CONFIG.flameColor2)},
    uFlameAmt:{value:CONFIG.flameAmt},
  },
  vertexShader:`varying vec2 vUv;void main(){vUv=uv;gl_Position=vec4(position,1.0);}`,
  fragmentShader:`
    uniform float iTime;
    uniform sampler2D tDiffuse,bloomTexture,torusTexture,haloTexture;
    uniform vec3 uBg,uFlameA,uFlameB;
    uniform float uFlameAmt;
    varying vec2 vUv;
    vec3 warp3d(vec3 pos,float t){
      float curv=.8,a=1.9,b=0.7;pos*=2.;
      pos.x+=curv*sin(t+a*pos.y)+t*b;pos.y+=curv*cos(t+a*pos.x);
      pos.y+=curv*sin(t+a*pos.z)+t*b;pos.z+=curv*cos(t+a*pos.y);
      pos.z+=curv*sin(t+a*pos.x)+t*b;pos.x+=curv*cos(t+a*pos.z);
      return 0.5+0.5*cos(pos.xyz+vec3(1,2,4));
    }
    void main(){
      vec2 uv=2.*vUv-1.;
      vec3 w=pow(warp3d(vec3(uv.x,sin(uv.y),uv.y),iTime*1.5),vec3(1.5));
      vec3 flame=1.5*uFlameA*w.x;flame*=w.y;flame+=uFlameB*w.z;
      flame*=smoothstep(0.25,1.,abs(uv.y));
      float md=smoothstep(-0.7,1.,-uv.y*uv.x);flame*=md*md;
      vec3 bg=uBg*(1.0-0.4*length(uv));
      vec3 halo=texture2D(haloTexture,vUv).xyz;
      gl_FragColor=vec4(bg+flame*uFlameAmt+texture2D(bloomTexture,vUv).xyz+texture2D(torusTexture,vUv).xyz+texture2D(tDiffuse,vUv).xyz+halo,1.);
    }`,
};

const haloRT = new THREE.WebGLRenderTarget(W,H);

const torusComposer = new EffectComposer(renderer);
torusComposer.renderToScreen = false;
torusComposer.addPass(new RenderPass(scene,camera));
torusComposer.addPass(new ShaderPass(GammaCorrectionShader));
torusComposer.addPass(new UnrealBloomPass(new THREE.Vector2(W,H),0.22,0.2,0));
torusComposer.addPass(new ShaderPass(CopyShader));

const bloomComposer = new EffectComposer(renderer);
bloomComposer.renderToScreen = false;
bloomComposer.addPass(new RenderPass(scene,camera));
bloomComposer.addPass(new UnrealBloomPass(new THREE.Vector2(W,H),0.5,0.6,0));
bloomComposer.addPass(new ShaderPass(GammaCorrectionShader));

const finalPass = new ShaderPass(FinalPass);
finalPass.uniforms.haloTexture.value = haloRT.texture;
const finalComposer = new EffectComposer(renderer);
finalComposer.addPass(new RenderPass(scene,camera));
finalComposer.addPass(finalPass);

const STOPS_X=[{p:0,v:0},{p:0.32,v:-3.1},{p:0.64,v:3.2},{p:1,v:0}];
const STOPS_Y=[{p:0,v:-4.5},{p:0.32,v:0.55},{p:0.64,v:0.45},{p:1,v:0.15}];
const STOPS_S=[{p:0,v:2.15},{p:0.32,v:1.0},{p:0.64,v:0.92},{p:1,v:1.12}];

const worldGroup = new THREE.Group();
worldGroup.position.set(STOPS_X[0].v, STOPS_Y[0].v, 0);
worldGroup.scale.setScalar(STOPS_S[0].v);
scene.add(worldGroup);

const planetGroup = new THREE.Group();
planetGroup.rotation.z = CONFIG.tilt;
worldGroup.add(planetGroup);

const cloudGroup = new THREE.Group();
cloudGroup.rotation.z = CONFIG.tilt;
cloudGroup.visible = false;
worldGroup.add(cloudGroup);

const glowMat = new THREE.ShaderMaterial({
  transparent:true, side:THREE.DoubleSide, depthWrite:false, blending:THREE.AdditiveBlending,
  uniforms:{uGlow:{value:hexToVec3(CONFIG.glowColor)},uIntensity:{value:CONFIG.glowIntensity}},
  vertexShader:`varying vec2 vUv;void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`,
  fragmentShader:`uniform vec3 uGlow;uniform float uIntensity;varying vec2 vUv;
    void main(){float d=length(vUv-0.5)*2.0;float a=pow(clamp(1.0-d,0.0,1.0),2.2);gl_FragColor=vec4(uGlow*a*uIntensity,a);}`,
});
const glowMesh = new THREE.Mesh(new THREE.PlaneGeometry(2,2), glowMat);
glowMesh.scale.setScalar(CONFIG.planetRadius*2.3);
worldGroup.add(glowMesh);

let planetTime=0, cloudTime=0, starTime=0, markerTime=0;

function injectPlanetShader(mat, nightTex){
  mat.onBeforeCompile = shader => {
    shader.uniforms.time = {value:planetTime};
    shader.uniforms.noiseScale = {value:30};
    shader.uniforms.speedX = {value:1.5};
    shader.uniforms.speedY = {value:2.0};
    shader.uniforms.speedZ = {value:2.5};
    shader.uniforms.rimColor = {value:hexToVec3(CONFIG.rimColor)};
    shader.uniforms.rimPower = {value:CONFIG.rimPower};
    shader.uniforms.nightBlendTexture = {value:nightTex};
    shader.uniforms.nightLights = {value:CONFIG.nightLights};
    shader.uniforms.terrainDepth = {value:CONFIG.terrainDepth};
    shader.uniforms.terrainShade = {value:CONFIG.terrainShade};
    shader.uniforms.oceanGlint = {value:CONFIG.oceanGlint};
    shader.uniforms.oceanDeep = {value:CONFIG.oceanDeep};
    shader.uniforms.oceanFlow = {value:CONFIG.oceanFlow};
    shader.uniforms.oceanFlowSpeed = {value:CONFIG.oceanFlowSpeed};
    shader.uniforms.oceanFlowScale = {value:CONFIG.oceanFlowScale};
    mat._shaderRef = shader;
    shader.vertexShader = 'varying vec2 vCustomUv;\n' + shader.vertexShader.replace('void main(){','void main(){\nvCustomUv=uv;');
    const ub = `uniform float time,noiseScale,speedX,speedY,speedZ,rimPower,nightLights,terrainDepth,terrainShade,oceanGlint,oceanDeep,oceanFlow,oceanFlowSpeed,oceanFlowScale;
      uniform vec3 rimColor;uniform sampler2D nightBlendTexture;varying vec2 vCustomUv;${SNOISE}`;
    shader.fragmentShader = ub + shader.fragmentShader;
    shader.fragmentShader = shader.fragmentShader.replace('#include <dithering_fragment>',`
      #include <dithering_fragment>
      vec3 normalizedNormal=normalize(vNormal);
      vec3 viewDir=normalize(vViewPosition);
      float rim=1.0-max(dot(viewDir,normalizedNormal),0.0);
      rim=pow(rim,rimPower);rim=pow(rim,1.5);rim*=0.7;
      vec3 currentColor=gl_FragColor.rgb;
      float blueDom=currentColor.b-max(currentColor.r,currentColor.g);
      float waterMask=clamp(smoothstep(-0.005,0.03,blueDom),0.0,1.0);
      float shimmer=snoise(vec3(vCustomUv.x*noiseScale+time*speedX,vCustomUv.y*noiseScale-time*speedY,time*speedZ));
      gl_FragColor.rgb+=waterMask*shimmer*0.025;
      float fT=time*oceanFlowSpeed*4.0;
      float fS=4.0*oceanFlowScale;
      float warp=snoise(vec3(vCustomUv.x*fS-fT*0.5,vCustomUv.y*fS+fT*0.4,fT*0.5));
      float flow=snoise(vec3(vCustomUv.x*fS*2.0+fT*0.6+warp,vCustomUv.y*fS*2.0-fT*0.5,fT*0.7));
      flow=warp*0.6+flow*0.4;
      gl_FragColor.rgb+=waterMask*flow*0.12*oceanFlow;
      gl_FragColor.rgb=mix(gl_FragColor.rgb,vec3(0.01,0.06,0.16),waterMask*oceanDeep);
      vec3 finalColor=mix(gl_FragColor.rgb,rimColor,rim);
      gl_FragColor=vec4(finalColor,1.0);
      vec3 surfPos=-vViewPosition;
      float terrH=dot(texture2D(map,vCustomUv).rgb,vec3(0.299,0.587,0.114));
      vec3 sigX=dFdx(surfPos),sigY=dFdy(surfPos);
      vec3 vR1=cross(sigY,normalizedNormal),vR2=cross(normalizedNormal,sigX);
      float fDet=dot(sigX,vR1);
      vec3 vGrad=sign(fDet)*(dFdx(terrH)*vR1+dFdy(terrH)*vR2);
      vec3 bumpedNormal=normalize(abs(fDet)*normalizedNormal-terrainDepth*vGrad);
      vec3 shadeNormal=mix(bumpedNormal,normalizedNormal,waterMask);
      vec3 cityLights=texture2D(nightBlendTexture,vCustomUv).rgb*gl_FragColor.rgb*nightLights;
      vec3 viewSunDir=normalize(vec3(-0.9,0.18,0.4));
      float ndl=dot(normalizedNormal,viewSunDir);
      float dayAmt=smoothstep(-0.05,0.35,ndl);
      float relief=dot(shadeNormal,viewSunDir)-ndl;
      gl_FragColor.rgb*=clamp(1.0+relief*terrainShade*dayAmt,0.55,1.6);
      float nightFactor=smoothstep(0.18,-0.30,ndl);
      float lightsFactor=smoothstep(0.30,-0.35,ndl);
      gl_FragColor.rgb=mix(gl_FragColor.rgb,gl_FragColor.rgb*0.08,nightFactor);
      gl_FragColor.rgb+=cityLights*lightsFactor;
      vec3 halfDir=normalize(viewSunDir+viewDir);
      float ripple=snoise(vec3(vCustomUv*240.0,time*4.0));
      float ndh=max(dot(normalizedNormal,halfDir)+ripple*0.02,0.0);
      float glint=pow(ndh,140.0);
      gl_FragColor.rgb+=glint*waterMask*dayAmt*oceanGlint*vec3(1.0,0.97,0.88);
    `);
  };
}

const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.5/');
const gltfLoader = new GLTFLoader();
gltfLoader.setDRACOLoader(dracoLoader);
const texLoader = new THREE.TextureLoader();

let planetMesh=null, nightTex=null;

function findMesh(o){if(o.isMesh)return o;for(const c of o.children){const r=findMesh(c);if(r)return r;}return null;}

gltfLoader.load(ASSET+'/planet-lights.glb', gltf=>{
  const m = findMesh(gltf.scene);
  nightTex = m&&m.material&&m.material.map ? m.material.map : new THREE.Texture();
  loadPlanet();
}, undefined, ()=>{ nightTex = new THREE.Texture(); loadPlanet(); });

function loadPlanet(){
  gltfLoader.load(ASSET+'/planet.glb', gltf=>{
    const mesh = findMesh(gltf.scene);
    if(!mesh) return;
    mesh.geometry.computeBoundingSphere();
    const r = mesh.geometry.boundingSphere.radius;
    mesh.scale.setScalar(CONFIG.planetRadius/r);
    const mat = mesh.material.clone();
    mat.metalness=0; mat.roughness=1; mat.envMapIntensity=0;
    injectPlanetShader(mat, nightTex);
    mesh.material = mat;
    mesh.layers.set(LAYERS.ENTIRE_SCENE);
    planetGroup.add(mesh);
    planetMesh = mesh;
    loadClouds(mesh);
    startEntrance();
  }, undefined, e=>console.warn('planet err',e));
}

function loadClouds(pMesh){
  const defs=[
    {h:CONFIG.cloud1Height,o:CONFIG.cloud1Opacity,s:CONFIG.cloud1Spin,ry:0.0,phase:0.0},
    {h:CONFIG.cloud2Height,o:CONFIG.cloud2Opacity,s:CONFIG.cloud2Spin,ry:2.2,phase:13.0},
    {h:CONFIG.cloud3Height,o:CONFIG.cloud3Opacity,s:CONFIG.cloud3Spin,ry:4.3,phase:27.0},
  ];
  texLoader.load(ASSET+'/planet-clouds.png', tex=>{
    tex.wrapS=tex.wrapT=THREE.RepeatWrapping;
    tex.repeat.set(5,5);
    defs.forEach(def=>{
      const geo = new THREE.SphereGeometry(CONFIG.planetRadius*def.h,64,64);
      const mat = new THREE.MeshStandardMaterial({map:tex,transparent:true,depthWrite:false});
      mat._cloudSpin = def.s;
      mat.onBeforeCompile = shader=>{
        shader.uniforms.uTime={value:cloudTime};
        shader.uniforms.noiseScale={value:20};
        shader.uniforms.uSpeedX={value:1};
        shader.uniforms.uSpeedY={value:2};
        shader.uniforms.uSpeedZ={value:2};
        shader.uniforms.uOpacity={value:def.o};
        shader.uniforms.uPhase={value:def.phase};
        mat._cloudShaderRef = shader;
        shader.vertexShader='varying vec2 vCloudUv;\n'+shader.vertexShader.replace('void main(){','void main(){\nvCloudUv=uv;');
        shader.fragmentShader=`uniform float uTime,noiseScale,uSpeedX,uSpeedY,uSpeedZ,uOpacity,uPhase;varying vec2 vCloudUv;\n${SNOISE}\n`+shader.fragmentShader;
        shader.fragmentShader=shader.fragmentShader.replace('#include <dithering_fragment>',`
          #include <dithering_fragment>
          gl_FragColor.rgb=vec3(1.0);
          float cloudNoise=snoise(vec3(vCloudUv.x*noiseScale+uTime*uSpeedX+uPhase,vCloudUv.y*noiseScale-uTime*uSpeedY+uPhase,uTime*uSpeedZ+uPhase));
          float cloudNdv=max(dot(normalize(vNormal),normalize(vViewPosition)),0.0);
          float cloudEdge=pow(1.0-cloudNdv,3.0);
          float cloudMod=mix(cloudNoise,1.0,cloudEdge);
          float cloudNdl=dot(normalize(vNormal),normalize(vec3(-0.9,0.18,0.4)));
          float cloudDay=1.0-smoothstep(0.30,-0.30,cloudNdl)*0.9;
          gl_FragColor.a*=cloudMod*uOpacity*cloudDay;
        `);
      };
      const cMesh = new THREE.Mesh(geo,mat);
      cMesh.rotation.y=def.ry; cMesh.renderOrder=2;
      cMesh.layers.set(LAYERS.ENTIRE_SCENE);
      cloudGroup.add(cMesh);
    });
    cloudGroup.visible=true;
  });
}

(function buildStars(){
  const N=CONFIG.starCount;
  const pos=new Float32Array(N*3),seeds=new Float32Array(N),brights=new Float32Array(N);
  for(let i=0;i<N;i++){
    const th=Math.acos(2*Math.random()-1),ph=Math.random()*Math.PI*2,r=90;
    pos[i*3]=r*Math.sin(th)*Math.cos(ph);
    pos[i*3+1]=r*Math.sin(th)*Math.sin(ph);
    pos[i*3+2]=r*Math.cos(th);
    seeds[i]=Math.random()*100;
    brights[i]=0.35+Math.random()*0.65;
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('seed',new THREE.BufferAttribute(seeds,1));
  geo.setAttribute('bright',new THREE.BufferAttribute(brights,1));
  const mat=new THREE.ShaderMaterial({
    blending:THREE.AdditiveBlending,depthWrite:false,transparent:true,frustumCulled:false,
    uniforms:{uTime:{value:0},uSize:{value:CONFIG.starSize},uFlicker:{value:CONFIG.starFlicker},uColor:{value:hexToVec3(CONFIG.starColor)},uRes:{value:new THREE.Vector2(W,H)}},
    vertexShader:`attribute float seed;attribute float bright;uniform float uTime,uSize,uFlicker;uniform vec2 uRes;varying float vTw;
      void main(){vec4 mv=modelViewMatrix*vec4(position,1.0);float tw=0.6+0.4*sin(uTime*uFlicker+seed);vTw=bright*tw;
        gl_PointSize=max(uSize*uRes.y/900.0*(90.0/max(-mv.z,1.0)),1.0);gl_Position=projectionMatrix*mv;}`,
    fragmentShader:`uniform vec3 uColor;varying float vTw;
      void main(){vec2 p=gl_PointCoord-0.5;float l=length(p);if(l>0.5)discard;
        float core=smoothstep(0.5,0.0,l);gl_FragColor=vec4(uColor,core*vTw);}`,
  });
  const stars=new THREE.Points(geo,mat);
  stars.layers.set(LAYERS.ENTIRE_SCENE);
  stars.frustumCulled=false;
  scene.add(stars);
  window._starsMat=mat;
})();

(function buildMotes(){
  const N=CONFIG.atmoCount;
  const pos=new Float32Array(N*3),sizes=new Float32Array(N),seeds=new Float32Array(N);
  for(let i=0;i<N;i++){
    pos[i*3]=(Math.random()*2-1);
    pos[i*3+1]=(Math.random()*2-1);
    pos[i*3+2]=(Math.random()*2-1);
    sizes[i]=CONFIG.atmoSize*(0.4+Math.random());
    seeds[i]=Math.random()*100;
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('size',new THREE.BufferAttribute(sizes,1));
  geo.setAttribute('seed',new THREE.BufferAttribute(seeds,1));
  const mat=new THREE.ShaderMaterial({
    blending:THREE.AdditiveBlending,depthWrite:false,depthTest:false,transparent:true,
    uniforms:{uTime:{value:0},uRes:{value:new THREE.Vector2(W,H)},uColor:{value:hexToVec3(CONFIG.atmoColor)}},
    vertexShader:`attribute float size;attribute float seed;uniform float uTime;uniform vec2 uRes;varying float vA;
      vec3 warp(vec3 p,float t){float c=0.9,a=1.9,b=0.02,s=0.05;p*=2.;
        p.x+=c*sin(s*t+a*p.y)+t*b;p.y+=c*cos(s*t+a*p.x);p.y+=c*sin(s*t+a*p.z)+t*b;
        p.z+=c*cos(s*t+a*p.y);p.z+=c*sin(s*t+a*p.x)+t*b;p.x+=c*cos(s*t+a*p.z);
        return cos(p+vec3(1,2,4));}
      void main(){vec3 v=position*4.0+warp(position,uTime)*1.2;vec4 mv=modelViewMatrix*vec4(v,1.0);
        float r=length(v);float farF=1.0-smoothstep(5.0,6.5,r);float nearF=smoothstep(0.0,0.5,-mv.z);
        vA=farF*nearF;gl_PointSize=size*uRes.y/900.0/max(-mv.z,0.001);gl_PointSize=max(gl_PointSize,1.0);gl_Position=projectionMatrix*mv;}`,
    fragmentShader:`uniform vec3 uColor;varying float vA;
      void main(){vec2 p=gl_PointCoord-0.5;float l=length(p);if(l>0.5)discard;
        float tex=smoothstep(0.5,0.0,l);gl_FragColor=vec4(uColor*tex,tex*vA*0.55);}`,
  });
  const motes=new THREE.Points(geo,mat);
  motes.layers.set(LAYERS.ENTIRE_SCENE);
  motes.frustumCulled=false;
  motes.onBeforeRender=()=>{
    const t=performance.now()/1000;
    mat.uniforms.uTime.value=t*CONFIG.atmoSpeed*8;
    finalPass.uniforms.iTime.value=t;
    motes.position.copy(camera.position);
    if(window._starsMat)window._starsMat.uniforms.uTime.value=starTime;
  };
  scene.add(motes);
  window._motesMat=mat;
})();

const ENTRY_DUR=1.9, ENTRY_START_Y=-6.5;
let entryT=0, entryActive=false;
function startEntrance(){ if(!PRM){ entryActive=true; entryT=0; } }
function entryOffset(dt){
  if(!entryActive) return 0;
  entryT+=dt;
  const t=clampV(entryT/ENTRY_DUR,0,1);
  const e=1-Math.pow(1-t,3);
  const y=Lerp(ENTRY_START_Y,0,e);
  if(t>=1) entryActive=false;
  return y;
}

let curP=0, pTarget=0, curX=STOPS_X[0].v, curY=STOPS_Y[0].v, curS=STOPS_S[0].v, spinPhase=0;

if(!PRM){
  const lenis=new Lenis({duration:1.15,smoothWheel:true,touchMultiplier:1.5});
  (function rl(t){lenis.raf(t);requestAnimationFrame(rl);})(0);
}

const reveals=document.querySelectorAll('[data-reveal]');
if(PRM){ reveals.forEach(el=>el.classList.add('in')); }
else{
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');obs.unobserve(e.target);}});
  },{threshold:0.18,rootMargin:'0px 0px -8% 0px'});
  reveals.forEach(el=>obs.observe(el));
}

let last=0;
function animate(now){
  requestAnimationFrame(animate);
  const dt=clampV((now-last)/1000,0,0.05);
  last=now;

  const sh=document.body.scrollHeight, ih=window.innerHeight;
  pTarget=clampV(window.scrollY/(sh-ih)||0,0,1);
  curP+=(pTarget-curP)*Math.min(1,dt*4.5);

  const sideScale=clampV(window.innerWidth/1200,0.5,1);
  const tx=sample(STOPS_X,curP)*sideScale;
  const ty=sample(STOPS_Y,curP);
  const ts=sample(STOPS_S,curP);
  const k=Math.min(1,dt*3.2);
  curX=Lerp(curX,tx,k);
  curY=Lerp(curY,ty,k);
  curS=Lerp(curS,ts,k);

  const ey=entryOffset(dt);
  worldGroup.position.set(curX, curY+ey, 0);
  worldGroup.scale.setScalar(curS);

  spinPhase+=dt*CONFIG.spin;
  planetGroup.children.forEach(m=>{
    if(m.isMesh) m.rotation.y=CONFIG.initRotation+spinPhase+curP*Math.PI*1.6;
  });

  planetTime+=dt/12; cloudTime+=dt/20; starTime+=dt; markerTime+=dt;

  planetGroup.children.forEach(m=>{
    if(m.isMesh&&m.material&&m.material._shaderRef)
      m.material._shaderRef.uniforms.time.value=planetTime;
  });
  cloudGroup.children.forEach(cm=>{
    cm.rotation.y+=dt*cm.material._cloudSpin;
    if(cm.material._cloudShaderRef)cm.material._cloudShaderRef.uniforms.uTime.value=cloudTime;
  });
  if(window._markerMat){
    window._markerMat.uniforms.uTime.value=markerTime;
    window._markerMat.uniforms.uRes.value.set(W,H);
  }

  glowMesh.quaternion.copy(camera.quaternion);
  controls.update();

  camera.layers.set(LAYERS.TORUS_SCENE); torusComposer.render();
  finalPass.uniforms.torusTexture.value=torusComposer.renderTarget1.texture;
  camera.layers.set(LAYERS.BLOOM_SCENE); bloomComposer.render();
  finalPass.uniforms.bloomTexture.value=bloomComposer.renderTarget1.texture;
  camera.layers.set(LAYERS.ENTIRE_SCENE); finalComposer.render();
}
requestAnimationFrame(animate);

window.addEventListener('resize',()=>{
  W=window.innerWidth; H=window.innerHeight;
  camera.aspect=W/H; camera.updateProjectionMatrix();
  renderer.setSize(W,H);
  [torusComposer,bloomComposer,finalComposer].forEach(c=>{c.setSize(W,H);c.setPixelRatio(devicePixelRatio);});
  if(window._motesMat)window._motesMat.uniforms.uRes.value.set(W,H);
  if(window._starsMat)window._starsMat.uniforms.uRes.value.set(W,H);
  if(window._markerMat)window._markerMat.uniforms.uRes.value.set(W,H);
});
</script>
</body>
</html>
"""

out = r"c:\Users\Lenovo\Downloads\build_test1\index.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

import os
size = os.path.getsize(out)
print(f"Written {size} bytes to {out}")
