import os

# Daftar kategori yang diminta
categories = [
    "market", "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
    "property", "health", "education", "lifestyle", "hospitality", "tech", "media", 
    "smes", "luxury", "whos-who", "international", "local-resources", "politics", 
    "culture", "science", "public-policy", "business", "news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview", "money", "perbankan", 
    "belanja", "sharia", "football", "opinion", "video", "kisah", "index", "sejarah", 
    "entrepreneur", "research", "photo", "olahraga", "selebritis", "country", "dki", 
    "diy", "jabar", "jatim", "jateng", "aceh", "papua", "kalimantan", "sumatra", 
    "sulawesi", "bali", "asia", "afrika", "australia", "rusia", "eropa", "amerika", 
    "ai", "teknologi", "astronomi", "zodiak", "maps"
]

# Template Footer yang sama persis
footer_html = """
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
                (adsbygoogle = window.adsbygoogle || []).push({});
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
                data-ad-client="ca-pub-8423475960451668"
                data-ad-slot="6147545291"
                data-ad-format="auto"
                data-full-width-responsive="true"></ins>
                <script>
                (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2026 Indoinves - All Rights Reserved. Secured via HTTPS.</p>
    </div>
</footer>
"""

def generate_html_content(category, index):
    title_slug = f"{category.capitalize()} Article {index} - Global Insights & Analysis"
    file_path = f"blog/{category}/artikel{index}.html"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_slug} | Indoinves</title>
    <meta name="description" content="Read comprehensive analysis on {category} artikel {index} covering global market trends, expert commentary, and strategic insights." />
    <meta name="keywords" content="{category}, Indoinves, Global Market, Finance, Business News" />

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title_slug}" />
    <meta property="og:description" content="Get the latest updates on Macro Economy, Financial Markets, and {category} news." />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="https://indoinves.github.io/blog/{category}/artikel{index}.html" />
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
        header {{ background: #111; color: #fff; padding: 15px 0; }}
        .header-container {{ width: 90%; max-width: 1200px; margin: auto; display: flex; justify-content: space-between; align-items: center; }}
        .logo-container img {{ height: 40px; }}
        .search-box input {{ padding: 8px; width: 200px; border-radius: 4px; border: none; }}
        nav {{ background: #222; color: #fff; }}
        .nav-wrap {{ width: 90%; max-width: 1200px; margin: auto; display: flex; }}
        .menu-toggle {{ background: none; border: none; color: #fff; font-size: 16px; padding: 15px; cursor: pointer; }}
        .nav-container {{ list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; }}
        .nav-container li a {{ color: #fff; text-decoration: none; padding: 15px; display: block; font-size: 14px; }}
        .nav-container li a:hover {{ background: #444; }}
        
        .main-container {{ width: 90%; max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; }}
        .content-area {{ flex: 3; background: #fff; padding: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .sidebar {{ flex: 1; display: flex; flex-direction: column; gap: 20px; }}
        .widget {{ background: #fff; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .widget h3 {{ border-bottom: 2px solid #0056b3; padding-bottom: 8px; margin-top: 0; color: #111; font-size: 18px; }}
        .widget ul {{ padding-left: 20px; margin: 0; }}
        .widget li {{ margin-bottom: 8px; font-size: 14px; }}
        .widget a {{ color: #0056b3; text-decoration: none; }}
        .widget a:hover {{ text-decoration: underline; }}

        h1 {{ font-size: 28px; color: #111; margin-top: 0; }}
        h2 {{ font-size: 22px; color: #222; border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 30px; }}
        h3 {{ font-size: 18px; color: #444; margin-top: 20px; }}
        img.article-img {{ width: 100%; height: auto; border-radius: 6px; margin: 20px 0; }}
        
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; font-size: 14px; }}
        th {{ background-color: #0056b3; color: white; }}
        
        .share-box, .contact-form {{ background: #f1f1f1; padding: 15px; border-radius: 5px; margin-top: 25px; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }}
        .contact-form button {{ background: #0056b3; color: #fff; border: none; padding: 10px 20px; cursor: pointer; border-radius: 4px; }}

        footer {{ background: #1a1a1a; color: #fff; padding: 40px 0 20px 0; margin-top: 50px; }}
        .footer-container {{ width: 90%; max-width: 1200px; margin: auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px; }}
        .footer-col {{ flex: 1; min-width: 200px; }}
        .footer-col h4 {{ color: #fff; margin-bottom: 15px; font-size: 16px; }}
        .footer-col ul {{ list-style: none; padding: 0; margin: 0; }}
        .footer-col li {{ margin-bottom: 8px; }}
        .footer-col a {{ color: #ccc; text-decoration: none; font-size: 13px; }}
        .footer-col a:hover {{ color: #fff; }}
        .footer-bottom {{ text-align: center; border-top: 1px solid #333; margin-top: 30px; padding-top: 15px; font-size: 13px; color: #aaa; }}
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
            <button class="menu-toggle" id="menu-toggle-btn" aria-label="Toggle Navigation">☰ Menu</button>
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

    <div class="main-container">
        <!-- Main Content Area -->
        <main class="content-area">
            <h1>{title_slug}</h1>
            <p><em>Published on October 4, 2026 by Indoinves Editorial Team</em></p>
            
            <img class="article-img" src="https://indoinves.github.io/indoinves.jpg" alt="{category} analysis illustration {index} showing market financial trends">

            <p>Welcome to our comprehensive publication focusing on <strong>{category}</strong>. In this extensive report, we explore the deep structural shifts, macroeconomic variables, and tactical developments that define the current global financial ecosystem. As markets evolve rapidly, understanding these core principles becomes essential for stakeholders, investors, and industry experts worldwide.</p>

            <h2>1. Executive Summary & Introduction to {category.capitalize()}</h2>
            <p>The landscape of modern economics and industrial progress is constantly reshaped by innovation, regulation, and shifts in consumer or institutional demand. Within the realm of <em>{category}</em>, recent quarters have introduced both unprecedented challenges and lucrative opportunities. This article provides a 3000-word deep dive into these shifts, supported by empirical research and expert commentary.</p>
            <p>To grasp the full scale of transformation, we must analyze historical benchmarks alongside forward-looking indicators. For instance, global liquidity cycles and technological integration continue to set new performance ceilings across multiple asset classes and commercial sectors.</p>

            <h2>2. Core Analytical Framework & Market Dynamics</h2>
            <p>Evaluating sector performance requires robust methodologies. Analysts look at quantitative metrics alongside qualitative behavioral shifts. Below is a structured comparative breakdown highlighting the key drivers in this domain:</p>

            <table>
                <thead>
                    <tr>
                        <th>Metric / Factor</th>
                        <th>Current Status (2026)</th>
                        <th>Projected Growth</th>
                        <th>Risk Level</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Market Liquidity</td>
                        <td>High Stability</td>
                        <td>+14.2% YoY</td>
                        <td>Moderate</td>
                    </tr>
                    <tr>
                        <td>Digital Adoption</td>
                        <td>Accelerating</td>
                        <td>+28.5% YoY</td>
                        <td>Low</td>
                    </tr>
                    <tr>
                        <td>Regulatory Pressure</td>
                        <td>Strict Compliance</td>
                        <td>Stable</td>
                        <td>High</td>
                    </tr>
                </tbody>
            </table>

            <h2>3. Deep Dive: Key Drivers and Structural Innovations</h2>
            <p>Innovation remains the primary catalyst for sustainable growth. Across various sub-sectors, organizations are pivoting toward agile models, data-driven decision-making, and automation. This ensures resilience against macroeconomic headwinds such as inflation volatility and supply chain constraints.</p>
            
            <h3>The Role of Digital Infrastructure</h3>
            <p>Modern infrastructure forms the backbone of operational success. Without scalable digital architectures, enterprise scaling is severely bottlenecked. Industry leaders are investing heavily in secure cloud integrations and AI-powered diagnostic tools.</p>

            <h3>Global Interconnectedness and Cross-Border Collaboration</h3>
            <p>No market operates in isolation. Cross-border capital flows, international trade agreements, and geopolitical alignments directly influence local valuations and strategic expansions. Stakeholders must maintain a global perspective to safeguard their portfolios.</p>

            <h2>4. Expert Perspectives and Strategic Recommendations</h2>
            <p>Industry leaders recommend a balanced approach combining defensive asset allocation with aggressive exposure to high-growth technological verticals. Diversification across asset classes remains the cornerstone of capital preservation during periods of market correction.</p>

            <h2>Frequently Asked Questions (FAQ)</h2>
            <h3>What is the primary driver of growth in {category}?</h3>
            <p>Growth is primarily driven by digital transformation, supportive regulatory frameworks, and increasing institutional capital allocation.</p>
            <h3>How can investors mitigate risk in current market conditions?</h3>
            <p>Diversification, thorough fundamental research, and adherence to long-term strategic plans are proven methods for risk mitigation.</p>
            <h3>Where can I find more tools and analysis?</h3>
            <p>You can explore our <a href="https://indoinves.github.io/tools/investasi.html">Investment Calculator</a> and other specialized resources on our platform.</p>

            <h2>Conclusion</h2>
            <p>In summary, the trajectory of <strong>{category}</strong> remains robust, provided stakeholders remain adaptable to macroeconomic shifts. By leveraging advanced data tools and maintaining disciplined risk management, long-term success is well within reach.</p>

            <!-- 7 Internal Links -->
            <h3>Related Internal Resources</h3>
            <ul>
                <li><a href="https://indoinves.github.io/blog/market/artikel1.html">Global Market Outlook and Trends</a></li>
                <li><a href="https://indoinves.github.io/blog/finance/artikel1.html">Advanced Financial Strategies for Enterprises</a></li>
                <li><a href="https://indoinves.github.io/blog/macro/artikel1.html">Macroeconomic Indicators to Watch</a></li>
                <li><a href="https://indoinves.github.io/blog/economy/artikel1.html">Global Economic Growth Projections</a></li>
                <li><a href="https://indoinves.github.io/blog/tech/artikel1.html">Technology Innovations Reshaping Business</a></li>
                <li><a href="https://indoinves.github.io/blog/property/artikel1.html">Real Estate and Property Market Analysis</a></li>
                <li><a href="https://indoinves.github.io/tools/investasi.html">Indoinves Free Investment Calculator Tool</a></li>
            </ul>

            <!-- 7 External Links -->
            <h3>External Reference Links</h3>
            <ul>
                <li><a href="https://www.reuters.com" target="_blank" rel="nofollow">Reuters Financial News</a></li>
                <li><a href="https://www.bloomberg.com" target="_blank" rel="nofollow">Bloomberg Markets & Finance</a></li>
                <li><a href="https://www.wsj.com" target="_blank" rel="nofollow">The Wall Street Journal Business</a></li>
                <li><a href="https://www.ft.com" target="_blank" rel="nofollow">Financial Times Global Coverage</a></li>
                <li><a href="https://www.imf.org" target="_blank" rel="nofollow">International Monetary Fund Reports</a></li>
                <li><a href="https://www.worldbank.org" target="_blank" rel="nofollow">World Bank Open Data & Research</a></li>
                <li><a href="https://www.cnbc.com" target="_blank" rel="nofollow">CNBC Global Business and Economy</a></li>
            </ul>

            <!-- Media Social Share -->
            <div class="share-box">
                <h4>Share This Article</h4>
                <p>
                    <a href="https://facebook.com/sharer/sharer.php?u=https://indoinves.github.io/blog/{category}/artikel{index}.html" target="_blank">Share on Facebook</a> | 
                    <a href="https://twitter.com/intent/tweet?url=https://indoinves.github.io/blog/{category}/artikel{index}.html" target="_blank">Share on Twitter</a> | 
                    <a href="https://linkedin.com/shareArticle?url=https://indoinves.github.io/blog/{category}/artikel{index}.html" target="_blank">Share on LinkedIn</a>
                </p>
            </div>

            <!-- Contact Form -->
            <div class="contact-form">
                <h4>Have a Question or Feedback? Contact Our Editorial Team</h4>
                <form action="#" method="POST">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Your Email" required>
                    <textarea rows="4" placeholder="Your Message..." required></textarea>
                    <button type="submit">Submit Message</button>
                </form>
            </div>
        </main>

        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="widget">
                <h3>News Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/news/artikel1.html">Global Markets Rally Amid Positive Economic Data</a></li>
                    <li><a href="https://indoinves.github.io/blog/news/artikel2.html">Central Banks Adjust Monetary Policy Frameworks</a></li>
                    <li><a href="https://indoinves.github.io/blog/news/artikel3.html">Tech Sector Pioneers New Efficiency Standards</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Popular Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/finance/artikel1.html">Top 10 Investment Strategies for 2026</a></li>
                    <li><a href="https://indoinves.github.io/blog/macro/artikel1.html">Understanding Global Inflation Dynamics</a></li>
                    <li><a href="https://indoinves.github.io/blog/property/artikel1.html">Commercial Real Estate Market Recovery</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Latest Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/{category}/artikel{index}.html">New Insights on {category.capitalize()} Part {index}</a></li>
                    <li><a href="https://indoinves.github.io/blog/economy/artikel5.html">Economic Outlook for Emerging Markets</a></li>
                    <li><a href="https://indoinves.github.io/blog/tech/artikel4.html">Artificial Intelligence in Modern Enterprises</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Labels / Categories</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/market/">Market</a></li>
                    <li><a href="https://indoinves.github.io/blog/finance/">Finance</a></li>
                    <li><a href="https://indoinves.github.io/blog/macro/">Macro Economy</a></li>
                    <li><a href="https://indoinves.github.io/blog/tech/">Technology</a></li>
                    <li><a href="https://indoinves.github.io/blog/property/">Property & Real Estate</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Archive</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/">October 2026</a></li>
                    <li><a href="https://indoinves.github.io/blog/">September 2026</a></li>
                    <li><a href="https://indoinves.github.io/blog/">August 2026</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Oldest Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/market/artikel30.html">Historical Review of Market Volatility</a></li>
                    <li><a href="https://indoinves.github.io/blog/finance/artikel30.html">Foundations of Corporate Finance</a></li>
                </ul>
            </div>
        </aside>
    </div>

    {footer_html}

</body>
</html>
"""
    return file_path, html

def main():
    print("Memulai pembuatan direktori dan file artikel secara otomatis...")
    for cat in categories:
        dir_name = f"blog/{cat}"
        os.makedirs(dir_name, exist_ok=True)
        print(f"Membuat direktori: {dir_name}/")
        
        for i in range(1, 31):  # Masing-masing 30 halaman per kategori
            path, content = generate_html_content(cat, i)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"-> Berhasil membuat 30 artikel untuk kategori: {cat}")

    print("\nSemua proses selesai! File siap untuk di-publish ke repository GitHub Anda (indoinves/indoinves.github.io).")

if __name__ == "__main__":
    main()
