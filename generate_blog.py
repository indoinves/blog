import os
import subprocess

# Daftar kategori lengkap sesuai permintaan
CATEGORIES = [
    "market", "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
    "property", "health", "education", "lifestyle", "hospitality", "tech", "media", 
    "smes", "luxury", "whos-who", "international", "local-resources", "politics", 
    "culture", "science", "public-policy", "business", "news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview", "money", "perbankan", 
    "belanja", "sharia", "football", "opinion", "video", "kisah", "index", 
    "sejarah", "entrepreneur", "research", "photo", "olahraga", "selebritis", 
    "country", "dki", "diy", "jabar", "jatim", "jateng", "aceh", "papua", 
    "kalimantan", "sumatra", "sulawesi", "bali", "asia", "afrika", "australia", 
    "rusia", "eropa", "amerika", "ai", "teknologi", "astronomi", "zodiak", "maps"
]

TOTAL_ARTICLES_PER_CATEGORY = 30

def generate_html_content(category, article_num):
    cat_title = category.replace("-", " ").title()
    title = f"{cat_title} Comprehensive Analysis & Strategic Insights #{article_num} - Indoinves"
    slug = f"artikel{article_num}"
    canonical_url = f"https://indoinves.github.io/blog/{category}/{slug}.html"
    
    # Template HTML lengkap dengan Meta, AdSense, Header, Nav, Konten SEO 3000 kata (simulasi terstruktur), Tabel, FAQ, Kesimpulan, Link Internal/Eksternal, Widget Sidebars, dan Footer
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Indoinves delivers authoritative insights on {cat_title}, Market & Finance, Macro Economy, Business News, Technology, Real Estate, and Global Politics." />
    <meta name="keywords" content="Indoinves, {cat_title}, Business News, Macro Economy, Market & Finance, Tech, Global Economy" />

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="Get the latest updates on {cat_title}, Financial Markets, Technology, and Business News worldwide." />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:type" content="article" />

    <!-- Manifest JSON Link -->
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />

    <!-- Favicon -->
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsMediaOrganization",
      "name": "Indoinves",
      "url": "https://indoinves.github.io/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://indoinves.github.io/indoinves.png"
      }},
      "sameAs": [
        "https://facebook.com/indoinves",
        "https://twitter.com/indoinves",
        "https://linkedin.com/company/indoinves"
      ]
    }}
    </script>

    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; color: #333; line-height: 1.6; }}
        header {{ background: #111; color: #fff; padding: 15px 0; border-bottom: 3px solid #d4af37; }}
        .header-container {{ display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .logo-container img {{ height: 40px; }}
        .search-box input {{ padding: 8px 12px; width: 250px; border-radius: 4px; border: 1px solid #ccc; }}
        nav {{ background: #222; color: #fff; position: relative; }}
        .nav-wrap {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }}
        .menu-toggle {{ background: none; border: none; color: #fff; font-size: 18px; cursor: pointer; padding: 15px; display: none; }}
        .nav-container {{ list-style: none; display: flex; flex-wrap: wrap; margin: 0; padding: 0; }}
        .nav-container li a {{ display: block; color: #fff; padding: 15px 15px; text-decoration: none; font-size: 14px; transition: background 0.3s; }}
        .nav-container li a:hover {{ background: #d4af37; color: #111; }}
        
        .main-layout {{ max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; padding: 0 20px; }}
        .content-area {{ flex: 3; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .sidebar-area {{ flex: 1; display: flex; flex-direction: column; gap: 20px; }}
        
        .article-img {{ width: 100%; height: auto; border-radius: 6px; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 25px 0; }}
        table, th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f4f4f4; }}
        
        .widget {{ background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .widget h3 {{ margin-top: 0; font-size: 18px; border-bottom: 2px solid #d4af37; padding-bottom: 8px; }}
        .widget ul {{ padding-left: 20px; margin: 0; }}
        .widget ul li {{ margin-bottom: 10px; }}
        .widget ul li a {{ color: #0066cc; text-decoration: none; }}
        .widget ul li a:hover {{ text-decoration: underline; }}
        
        footer {{ background: #111; color: #fff; padding: 50px 0 20px 0; margin-top: 50px; }}
        .footer-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; padding: 0 20px; }}
        .footer-col h4 {{ color: #d4af37; font-size: 16px; margin-bottom: 15px; }}
        .footer-col ul {{ list-style: none; padding: 0; margin: 0; }}
        .footer-col ul li {{ margin-bottom: 8px; }}
        .footer-col ul li a {{ color: #ccc; text-decoration: none; font-size: 14px; }}
        .footer-col ul li a:hover {{ color: #fff; }}
        .footer-col p {{ color: #aaa; font-size: 14px; line-height: 1.5; }}
        .footer-bottom {{ text-align: center; border-top: 1px solid #333; margin-top: 40px; padding-top: 20px; font-size: 13px; color: #888; }}
        
        @media(max-width: 768px) {{
            .main-layout {{ flex-direction: column; }}
            .nav-container {{ display: none; width: 100%; flex-direction: column; }}
            .nav-container.active {{ display: flex; }}
            .menu-toggle {{ display: block; }}
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-container">
                <a href="https://indoinves.github.io/">
                    <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
                </a>
            </div>
            <div class="search-box">
                <form action="https://indoinves.github.io/" method="GET">
                    <input type="text" placeholder="Search news, markets..." />
                </form>
            </div>
        </div>
    </header>

    <!-- Navigasi Dropdown Label Lengkap & Responsif -->
    <nav>
        <div class="nav-wrap">
            <button class="menu-toggle" id="menu-toggle-btn" aria-label="Toggle Navigation">â˜° Menu</button>
            <ul class="nav-container" id="main-nav-list">
                <li><a href="https://indoinves.github.io/">Home</a></li>
                <li><a href="https://indoinves.github.io/blog/market/">Market</a></li>
                <li><a href="https://indoinves.github.io/blog/finance/">Finance</a></li>
                <li><a href="https://indoinves.github.io/blog/macro/">Macro</a></li>
                <li><a href="https://indoinves.github.io/blog/economy/">Economy</a></li>
                <li><a href="https://indoinves.github.io/blog/tech/">Tech</a></li>
                <li><a href="https://indoinves.github.io/blog/property/">Property</a></li>
            </ul>
        </div>
    </nav>

    <div class="main-layout">
        <!-- Main Content Area -->
        <main class="content-area">
            <h1>{title}</h1>
            <p><em>Published by Indoinves Editorial Desk | Updated for Comprehensive Analysis</em></p>
            
            <img src="https://indoinves.github.io/indoinves.jpg" alt="{cat_title} comprehensive market trends illustration and strategic global overview" class="article-img">

            <h2>Table of Contents</h2>
            <ul>
                <li><a href="#introduction">1. Executive Summary & Introduction</a></li>
                <li><a href="#macro-overview">2. Macroeconomic Framework & Structural Shifts</a></li>
                <li><a href="#data-analysis">3. Comparative Data & Market Dynamics</a></li>
                <li><a href="#expert-perspective">4. Expert Perspectives & Case Studies</a></li>
                <li><a href="#faq">5. Frequently Asked Questions (FAQ)</a></li>
                <li><a href="#conclusion">6. Conclusion & Strategic Outlook</a></li>
            </ul>

            <h2 id="introduction">1. Executive Summary & Introduction</h2>
            <p>Welcome to this comprehensive special report regarding {cat_title}. In an era defined by rapid financial transformations, geopolitical shifts, and technological disruptions, understanding the core dynamics of {cat_title} is paramount for investors, policy makers, and enterprise leaders worldwide. This exhaustive overview synthesizes extensive empirical observations, historical records, and forward-looking economic indicators.</p>
            <p>Throughout this detailed analysis, we explore structural mechanics, regulatory evolutions, and market adaptations that shape modern outcomes. For further context on general financial frameworks, check out our report on <a href="https://indoinves.github.io/blog/finance/artikel1.html">global financial liquidity</a> and institutional structures as detailed by international monetary agencies like the <a href="https://www.imf.org" target="_blank" rel="nofollow">International Monetary Fund (IMF)</a>.</p>
            <p>Furthermore, digital transformation has accelerated information access across sector domains. Industry monitors frequently reference studies from the <a href="https://www.worldbank.org" target="_blank" rel="nofollow">World Bank</a> and academic consortiums such as <a href="https://www.mit.edu" target="_blank" rel="nofollow">MIT Technology Review</a> to track structural efficiencies. Cross-border integrations continue to influence localized valuations, mirroring shifts seen in our companion studies on <a href="https://indoinves.github.io/blog/macro/artikel1.html">macroeconomic resilience</a> and <a href="https://indoinves.github.io/blog/economy/artikel1.html">global growth trajectories</a>.</p>

            <h2 id="macro-overview">2. Macroeconomic Framework & Structural Shifts</h2>
            <p>The foundational ecosystem of {cat_title} relies heavily on robust infrastructure and adaptability. Modern asset classes and institutional frameworks undergo constant stress-testing against inflation volatility and fiscal tightening cycles. Analysts note that traditional models must now incorporate AI-driven risk modeling and automated compliance checks, aligning with insights published by the <a href="https://www.reuters.com" target="_blank" rel="nofollow">Reuters Financial Desk</a> and <a href="https://www.bloomberg.com" target="_blank" rel="nofollow">Bloomberg Markets</a>.</p>
            <p>When observing regional developments, stakeholders frequently compare local adaptations against international benchmarks. Additional reading on regulatory standards can be found through resources provided by the <a href="https://www.ft.com" target="_blank" rel="nofollow">Financial Times</a> and our internal directory on <a href="https://indoinves.github.io/blog/business/artikel1.html">business governance models</a>.</p>

            <h2 id="data-analysis">3. Comparative Data & Market Dynamics</h2>
            <p>To provide quantitative clarity, the table below outlines core metrics, growth velocities, and projected impact indices across key operational vectors:</p>
            <table>
                <thead>
                    <tr>
                        <th>Performance Metric</th>
                        <th>Current Quarter</th>
                        <th>Projected Outlook</th>
                        <th>Variance (%)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Market Liquidity Index</td>
                        <td>$4.2 Trillion</td>
                        <td>$4.8 Trillion</td>
                        <td>+14.2%</td>
                    </tr>
                    <tr>
                        <td>Institutional Adoption</td>
                        <td>68.4%</td>
                        <td>81.2%</td>
                        <td>+18.7%</td>
                    </tr>
                    <tr>
                        <td>Regulatory Compliance Score</td>
                        <td>94.1/100</td>
                        <td>98.5/100</td>
                        <td>+4.6%</td>
                    </tr>
                </tbody>
            </table>
            <p>This quantitative matrix underscores steady positive expansion, reinforced by structural updates highlighted in our reports on <a href="https://indoinves.github.io/blog/market/artikel1.html">capital market performance</a> and <a href="https://indoinves.github.io/blog/tech/artikel1.html">technological integration pipelines</a>.</p>

            <h2 id="expert-perspective">4. Expert Perspectives & Case Studies</h2>
            <p>Leading authorities emphasize that long-term viability requires diversification and rigorous risk mitigation. Case studies from emerging markets demonstrate that early adopters of automation secure higher operational yields. For supplementary research, industry professionals often consult publications by the <a href="https://www.wsj.com" target="_blank" rel="nofollow">Wall Street Journal</a>.</p>

            <h2 id="faq">5. Frequently Asked Questions (FAQ)</h2>
            <h3>What are the primary drivers of growth within {cat_title}?</h3>
            <p>Growth is primarily propelled by technological integration, expanding consumer demand, and adaptive regulatory frameworks designed to enhance market transparency.</p>
            <h3>How can investors mitigate risk in volatile cycles?</h3>
            <p>Diversification across asset classes, maintaining adequate liquidity reserves, and continuous portfolio rebalancing remain the most effective risk mitigation strategies.</p>
            <h3>Where can I access further technical documentation?</h3>
            <p>You can explore our extensive archives or visit specialized tools such as the <a href="https://indoinves.github.io/tools/contentblog.html">Indoinves Content Blog Tool</a> for automated research synthesis.</p>

            <h2 id="conclusion">6. Conclusion & Strategic Outlook</h2>
            <p>In summary, {cat_title} continues to present formidable opportunities alongside distinct structural challenges. Stakeholders who prioritize data-driven decision-making, rigorous compliance, and technological agility will be best positioned to capture sustainable long-term value. We invite you to continue exploring our continuous coverage across all Indoinves editorial channels.</p>

            <!-- Media Social Share & Contact Form Section -->
            <div style="margin-top: 40px; padding: 20px; background: #f4f4f4; border-radius: 6px;">
                <h3>Share This Article & Join the Conversation</h3>
                <p>Share this report across your professional networks:</p>
                <p>
                    <a href="https://facebook.com/sharer/sharer.php?u={canonical_url}" target="_blank" style="margin-right: 15px; color: #1877f2; text-decoration: none; font-weight: bold;">Facebook</a>
                    <a href="https://twitter.com/intent/tweet?url={canonical_url}&text={title}" target="_blank" style="margin-right: 15px; color: #1da1f2; text-decoration: none; font-weight: bold;">Twitter / X</a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url={canonical_url}&title={title}" target="_blank" style="color: #0a66c2; text-decoration: none; font-weight: bold;">LinkedIn</a>
                </p>
                <hr style="border: 0; border-top: 1px solid #ddd; margin: 20px 0;">
                <h4>Have an Inquiry or Press Tip? Contact Our Editorial Desk</h4>
                <form action="#" method="POST" style="display: flex; flex-direction: column; gap: 10px; max-width: 500px;">
                    <input type="text" name="name" placeholder="Your Name" required style="padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
                    <input type="email" name="email" placeholder="Your Email Address" required style="padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
                    <textarea name="message" rows="4" placeholder="Your Message or Inquiry..." required style="padding: 8px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
                    <button type="submit" style="padding: 10px; background: #111; color: #fff; border: none; border-radius: 4px; cursor: pointer; font-weight: bold;">Send Message</button>
                </form>
            </div>
        </main>

        <!-- Sidebar Area -->
        <aside class="sidebar-area">
            <div class="widget">
                <h3>News Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/news/artikel1.html">Global Markets Rally Amid New Economic Policy Shifts</a></li>
                    <li><a href="https://indoinves.github.io/blog/economy/artikel1.html">Central Banks Announce Synchronized Liquidity Frameworks</a></li>
                    <li><a href="https://indoinves.github.io/blog/tech/artikel1.html">AI Governance Protocols Approved by International Coalition</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Artikel Popular</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/market/artikel1.html">Mastering Equity Valuations in High-Inflation Eras</a></li>
                    <li><a href="https://indoinves.github.io/blog/property/artikel1.html">Real Estate Investment Trusts: 2026 Strategic Playbook</a></li>
                    <li><a href="https://indoinves.github.io/blog/finance/artikel1.html">Digital Currencies and the Future of Central Banking</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Artikel Terbaru</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/{category}/artikel30.html">Advanced Tactical Analysis in {cat_title} Sector</a></li>
                    <li><a href="https://indoinves.github.io/blog/{category}/artikel29.html">Regulatory Compliance Updates for {cat_title} Leaders</a></li>
                    <li><a href="https://indoinves.github.io/blog/{category}/artikel28.html">Emerging Trends and Disruptions in {cat_title}</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Label</h3>
                <p>
                    <a href="https://indoinves.github.io/blog/market/" style="display:inline-block; background:#eee; padding:5px 10px; margin:3px; border-radius:3px; font-size:12px; text-decoration:none; color:#333;">Market</a>
                    <a href="https://indoinves.github.io/blog/finance/" style="display:inline-block; background:#eee; padding:5px 10px; margin:3px; border-radius:3px; font-size:12px; text-decoration:none; color:#333;">Finance</a>
                    <a href="https://indoinves.github.io/blog/macro/" style="display:inline-block; background:#eee; padding:5px 10px; margin:3px; border-radius:3px; font-size:12px; text-decoration:none; color:#333;">Macro</a>
                    <a href="https://indoinves.github.io/blog/tech/" style="display:inline-block; background:#eee; padding:5px 10px; margin:3px; border-radius:3px; font-size:12px; text-decoration:none; color:#333;">Tech</a>
                </p>
            </div>

            <div class="widget">
                <h3>Archive</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/{category}/">January 2026 Reports</a></li>
                    <li><a href="https://indoinves.github.io/blog/{category}/">December 2025 Archive</a></li>
                    <li><a href="https://indoinves.github.io/blog/{category}/">November 2025 Archive</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Artikel Terlama</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/{category}/artikel1.html">Foundational Principles of {cat_title} Volume I</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-col">
                <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
                <p>Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.</p>
            </div>

            <div class="footer-col">
                <h4>Tools Free Indoinves</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/tools/banklocator.html">Tools Peta & Direktori Bank Global</a></li>
                    <li><a href="https://indoinves.github.io/tools/contentblog.html">Tools Konten Blog</a></li>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">Tools Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.github.io/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto-pro.html">Tools Simulator Kripto Pro</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto.html">Tools Simulator Kripto</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorsaham.html">Tools Simulator Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/website.html">Tools Website / SEO Checker</a></li>
                </ul>
                
                <!-- Unit Iklan Autorelaxed AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-format="autorelaxed"
                    data-ad-client="ca-pub-8423475960451668"
                    data-ad-slot="7183276396"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>
            </div>

            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/">Home</a></li>
                    <li><a href="https://indoinves.github.io/about">About Us</a></li>
                    <li><a href="https://indoinves.github.io/contact">Contact Us</a></li>
                    <li><a href="https://indoinves.github.io/privacy">Privacy Policy</a></li>
                    <li><a href="https://indoinves.github.io/sitemap">Sitemap</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Policies & Editorial</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/disclaimer">Disclaimer</a></li>
                    <li><a href="https://indoinves.github.io/terms">Terms On Conditional License</a></li>
                    <li><a href="https://indoinves.github.io/editorial">Editorial Guidelines</a></li>
                    <li><a href="https://indoinves.github.io/advertise">Advertise With Us</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Community & Careers</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/join-team">Join the Team</a></li>
                    <li><a href="https://indoinves.github.io/contact-forum">Contact Forum</a></li>
                    <li><a href="https://indoinves.github.io/community">Komunitas Indoinves</a></li>
                </ul>
                
                <!-- Unit Iklan Banner AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-client="ca-pub-8423475960451668"
                    data-ad-slot="6147545291"
                    data-ad-format="auto"
                    data-full-width-responsive="true"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Indoinves - All Rights Reserved. Secured via HTTPS.</p>
        </div>
    </footer>

    <script>
        document.getElementById('menu-toggle-btn').addEventListener('click', function() {{
            var navList = document.getElementById('main-nav-list');
            navList.classList.toggle('active');
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    base_dir = "blog"
    os.makedirs(base_dir, exist_ok=True)
    
    print(f"Starting generation of {len(CATEGORIES)} categories with {TOTAL_ARTICLES_PER_CATEGORY} articles each...")
    
    for category in CATEGORIES:
        cat_path = os.path.join(base_dir, category)
        os.makedirs(cat_path, exist_ok=True)
        print(f"Processing category directory: {category}")
        
        for i in range(1, TOTAL_ARTICLES_PER_CATEGORY + 1):
            filename = f"artikel{i}.html"
            filepath = os.path.join(cat_path, filename)
            content = generate_html_content(category, i)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
    print("All HTML files generated successfully locally.")
    
    # Auto-git publish commands
    print("Staging files for Git commit...")
    subprocess.run(["git", "add", "blog/"], check=True)
    
    print("Committing changes...")
    subprocess.run(["git", "commit", "-m", "Auto-publish comprehensive SEO blog articles across all categories"], check=True)
    
    print("Pushing to GitHub repository...")
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Deployment completed successfully!")

if __name__ == "__main__":
    main()
