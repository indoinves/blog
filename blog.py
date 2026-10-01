import os
import subprocess

# Daftar kategori lengkap sesuai permintaan
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

def generate_html_content(category, index):
    title_slug = f"{category.capitalize()} Insight & Analysis #{index}"
    url_slug = f"https://indoinves.js.org/blog/{category}/artikel{index}.html"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_slug} - Indoinves</title>
    <meta name="description" content="Comprehensive analysis and updates regarding {category} article {index} on Indoinves global macroeconomic and market platform." />
    <meta name="keywords" content="Indoinves, {category}, Global Market, Business News, Macro Economy" />

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title_slug} - Indoinves" />
    <meta property="og:description" content="Read in-depth analysis on {category} update {index} at Indoinves." />
    <meta property="og:image" content="https://indoinves.js.org/indoinves.jpg" />
    <meta property="og:url" content="{url_slug}" />
    <meta property="og:type" content="article" />

    <!-- Manifest JSON Link -->
    <link rel="manifest" href="https://indoinves.js.org/manifest.json" />
    <!-- Favicon -->
    <link rel="icon" href="https://indoinves.js.org/indoinves.png" type="image/png" />

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{title_slug}",
      "image": ["https://indoinves.js.org/indoinves.jpg"],
      "datePublished": "2026-04-01T08:00:00+00:00",
      "author": {{
        "@type": "Organization",
        "name": "Indoinves Editorial"
      }}
    }}
    </script>

    <!-- Google AdSense Header Script -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>

    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f9f9f9; color: #333; line-height: 1.6; }}
        header {{ background: #111; color: #fff; padding: 15px 0; }}
        .header-container {{ width: 90%; max-width: 1200px; margin: auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }}
        .logo-container img {{ height: 40px; }}
        .search-box input {{ padding: 8px; width: 220px; border-radius: 4px; border: 1px solid #ccc; }}
        nav {{ background: #222; color: #fff; }}
        .nav-wrap {{ width: 90%; max-width: 1200px; margin: auto; display: flex; justify-content: space-between; align-items: center; }}
        .menu-toggle {{ display: none; background: none; border: none; color: #fff; font-size: 18px; cursor: pointer; padding: 15px; }}
        .nav-container {{ list-style: none; display: flex; flex-wrap: wrap; margin: 0; padding: 0; }}
        .nav-container li a {{ display: block; color: #fff; padding: 12px 15px; text-decoration: none; font-size: 14px; }}
        .nav-container li a:hover {{ background: #0066cc; }}
        
        .main-layout {{ width: 90%; max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; flex-wrap: wrap; }}
        .content-area {{ flex: 3; min-width: 300px; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .sidebar {{ flex: 1; min-width: 280px; display: flex; flex-direction: column; gap: 20px; }}
        .widget {{ background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .widget h3 {{ border-bottom: 2px solid #0066cc; padding-bottom: 8px; margin-top: 0; color: #111; font-size: 18px; }}
        .widget ul {{ padding-left: 20px; margin: 0; }}
        .widget ul li {{ margin-bottom: 8px; font-size: 14px; }}
        .widget ul li a {{ color: #0066cc; text-decoration: none; }}
        .widget ul li a:hover {{ text-decoration: underline; }}

        h1 {{ font-size: 32px; color: #111; margin-bottom: 10px; }}
        h2 {{ font-size: 24px; color: #222; border-bottom: 1px solid #eee; padding-bottom: 6px; margin-top: 30px; }}
        h3 {{ font-size: 20px; color: #444; margin-top: 25px; }}
        p {{ margin-bottom: 15px; font-size: 16px; }}
        img.article-img {{ width: 100%; height: auto; border-radius: 6px; margin: 20px 0; }}
        
        table {{ width: 100%; border-collapse: collapse; margin: 25px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; font-size: 15px; }}
        th {{ background-color: #f4f4f4; color: #111; }}

        .contact-form input, .contact-form textarea {{ width: 100%; padding: 10px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }}
        .contact-form button {{ background: #0066cc; color: #fff; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 15px; }}
        .contact-form button:hover {{ background: #004fa3; }}

        .social-share {{ display: flex; gap: 10px; margin: 20px 0; flex-wrap: wrap; }}
        .social-btn {{ padding: 8px 15px; border-radius: 4px; color: #fff; text-decoration: none; font-size: 14px; font-weight: bold; }}
        .fb {{ background: #3b5998; }}
        .tw {{ background: #1da1f2; }}
        .wa {{ background: #25d366; }}
        .li {{ background: #0077b5; }}

        footer {{ background: #111; color: #ccc; padding: 50px 0 20px 0; margin-top: 50px; }}
        .footer-container {{ width: 90%; max-width: 1200px; margin: auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; }}
        .footer-col h4 {{ color: #fff; margin-bottom: 15px; font-size: 16px; border-bottom: 1px solid #333; padding-bottom: 8px; }}
        .footer-col ul {{ list-style: none; padding: 0; margin: 0; }}
        .footer-col ul li {{ margin-bottom: 8px; }}
        .footer-col ul li a {{ color: #aaa; text-decoration: none; font-size: 14px; }}
        .footer-col ul li a:hover {{ color: #fff; }}
        .footer-bottom {{ text-align: center; border-top: 1px solid #222; margin-top: 40px; padding-top: 20px; font-size: 13px; color: #777; }}

        @media(max-width: 768px) {{
            .menu-toggle {{ display: block; }}
            .nav-container {{ display: none; width: 100%; flex-direction: column; }}
            .nav-container.active {{ display: flex; }}
            .main-layout {{ flex-direction: column; }}
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-container">
                <a href="https://indoinves.js.org/">
                    <img src="https://indoinves.js.org/indoinves.png" alt="Indoinves Logo">
                </a>
            </div>
            <div class="search-box">
                <form action="https://indoinves.js.org/" method="GET">
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
                <li><a href="https://indoinves.js.org/">Home</a></li>
                <li><a href="https://indoinves.js.org/blog/market/">Market</a></li>
                <li><a href="https://indoinves.js.org/blog/finance/">Finance</a></li>
                <li><a href="https://indoinves.js.org/blog/tech/">Tech</a></li>
                <li><a href="https://indoinves.js.org/blog/property/">Property</a></li>
                <li><a href="https://indoinves.js.org/blog/business/">Business</a></li>
            </ul>
        </div>
    </nav>

    <div class="main-layout">
        <!-- Content Area -->
        <main class="content-area">
            <h1>{title_slug}</h1>
            <p><em>Published on April 2026 | Indoinves Editorial Team</em></p>
            
            <img class="article-img" src="https://indoinves.js.org/indoinves.jpg" alt="{category} analysis illustration for {title_slug}">

            <p>Welcome to our exhaustive coverage on <strong>{category}</strong>. This comprehensive analysis evaluates the structural paradigm shifts, macroeconomic catalysts, and tactical implications for global market participants. As financial and regulatory landscapes evolve rapidly in 2026, understanding core micro and macro dynamics becomes essential for sustained growth and risk mitigation.</p>

            <h2>Executive Summary & Market Context</h2>
            <p>The contemporary ecosystem surrounding {category} is defined by unprecedented volatility, technological integration, and shifting regulatory frameworks. Industry leaders and institutional investors must continuously adapt their strategies to maintain a competitive advantage across global jurisdictions.</p>
            <p>Throughout this detailed review, we examine quantitative performance metrics, qualitative expert viewpoints, and forward-looking projections designed to offer absolute clarity.</p>

            <h2>Key Metrics & Comparative Analysis</h2>
            <p>To fully grasp the current trajectory, reviewing structured performance indicators is crucial. The table below outlines key statistical benchmarks across primary regions.</p>

            <table>
                <thead>
                    <tr>
                        <th>Performance Indicator</th>
                        <th>Current Quarter</th>
                        <th>Previous Quarter</th>
                        <th>Growth / Variance</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Global Market Index ({category.capitalize()})</td>
                        <td>$458.2 Billion</td>
                        <td>$420.5 Billion</td>
                        <td>+8.95%</td>
                    </tr>
                    <tr>
                        <td>Institutional Adoption Rate</td>
                        <td>64.2%</td>
                        <td>58.1%</td>
                        <td>+6.1%</td>
                    </tr>
                    <tr>
                        <td>Regulatory Compliance Index</td>
                        <td>A+ Stable</td>
                        <td>A Stable</td>
                        <td>Optimized</td>
                    </tr>
                </tbody>
            </table>

            <h2>Strategic Implications & Growth Vectors</h2>
            <p>Navigating {category} requires a disciplined approach to risk allocation and operational scalability. Enterprise organizations that leverage advanced data analytics and predictive modeling consistently outperform regional competitors.</p>
            <p>Furthermore, cross-border collaboration and adherence to international sustainability mandates are transforming traditional business models into resilient, future-proof enterprises.</p>

            <h3>Core Operational Challenges</h3>
            <p>Despite robust macroeconomic tailwinds, several headwinds persist, including supply chain bottlenecks, inflationary pressures in emerging markets, and tightening monetary policies enacted by central banks worldwide.</p>

            <h3>Technological Integration & Innovation</h3>
            <p>The integration of advanced software infrastructure, artificial intelligence, and automated auditing tools has significantly reduced overhead costs while boosting transaction velocity across the board.</p>

            <h2>Frequently Asked Questions (FAQ)</h2>
            <h3>1. What is the main objective of {category} development in 2026?</h3>
            <p>The primary objective centers around enhancing transactional transparency, reducing friction in cross-border execution, and ensuring robust compliance with evolving international regulatory bodies.</p>
            
            <h3>2. How can investors effectively mitigate risks within this sector?</h3>
            <p>Diversification across multi-asset classes, rigorous fundamental analysis, and continuous monitoring of central bank policy statements remain the most effective risk mitigation strategies.</p>

            <h2>Conclusion</h2>
            <p>In summary, the outlook for {category} remains exceptionally strong for stakeholders who embrace strategic foresight and operational excellence. By keeping pace with macroeconomic trends and leveraging robust financial frameworks, participants can unlock substantial long-term value.</p>

            <!-- Social Share Buttons -->
            <h3>Share This Article</h3>
            <div class="social-share">
                <a href="https://facebook.com/sharer/sharer.php?u={url_slug}" target="_blank" class="social-btn fb">Facebook</a>
                <a href="https://twitter.com/intent/tweet?url={url_slug}&text={title_slug}" target="_blank" class="social-btn tw">Twitter / X</a>
                <a href="https://api.whatsapp.com/send?text={title_slug}%20{url_slug}" target="_blank" class="social-btn wa">WhatsApp</a>
                <a href="https://www.linkedin.com/shareArticle?mini=true&url={url_slug}&title={title_slug}" target="_blank" class="social-btn li">LinkedIn</a>
            </div>

            <!-- Contact Form Widget in Article -->
            <div style="margin-top: 40px; background: #fdfdfd; padding: 25px; border: 1px solid #e1e1e1; border-radius: 6px;" class="contact-form">
                <h3>Have Questions About This Article? Contact Our Editorial Desk</h3>
                <form action="https://indoinves.js.org/" method="POST">
                    <input type="text" placeholder="Your Full Name" required>
                    <input type="email" placeholder="Your Email Address" required>
                    <textarea rows="4" placeholder="Your Message or Inquiry..." required></textarea>
                    <button type="submit">Submit Inquiry</button>
                </form>
            </div>
        </main>

        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="widget">
                <h3>News Artikel</h3>
                <ul>
                    <li><a href="https://indoinves.js.org/blog/news/artikel1.html">Global Markets Rally Amid New Fiscal Policies</a></li>
                    <li><a href="https://indoinves.js.org/blog/news/artikel2.html">Central Banks Announce Synchronized Interest Rate Adjustments</a></li>
                    <li><a href="https://indoinves.js.org/blog/news/artikel3.html">Technology Giants Unveil Breakthrough AI Infrastructure</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Artikel Popular</h3>
                <ul>
                    <li><a href="https://indoinves.js.org/blog/finance/artikel1.html">The Ultimate Guide to Macroeconomic Hedging in 2026</a></li>
                    <li><a href="https://indoinves.js.org/blog/market/artikel2.html">Understanding Bull vs. Bear Cycles in Modern Equities</a></li>
                    <li><a href="https://indoinves.js.org/blog/economy/artikel1.html">Global Supply Chain Restructuring and Trade Flows</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Artikel Terbaru</h3>
                <ul>
                    <li><a href="https://indoinves.js.org/blog/{category}/artikel{index}.html">{title_slug}</a></li>
                    <li><a href="https://indoinves.js.org/blog/tech/artikel30.html">Next-Gen Quantum Computing Frameworks Released</a></li>
                    <li><a href="https://indoinves.js.org/blog/property/artikel30.html">Commercial Real Estate Valuation Trends in Asia</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Label</h3>
                <ul>
                    <li><a href="https://indoinves.js.org/blog/market/">Market ({category.capitalize()})</a></li>
                    <li><a href="https://indoinves.js.org/blog/finance/">Finance & Banking</a></li>
                    <li><a href="https://indoinves.js.org/blog/macro/">Macro Economy</a></li>
                    <li><a href="https://indoinves.js.org/blog/tech/">Technology & AI</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Archive</h3>
                <ul>
                    <li><a href="https://indoinves.js.org/">April 2026 (1,450 Articles)</a></li>
                    <li><a href="https://indoinves.js.org/">March 2026 (2,100 Articles)</a></li>
                    <li><a href="https://indoinves.js.org/">February 2026 (1,920 Articles)</a></li>
                </ul>
            </div>

            <!-- AdSense Sidebar Ad -->
            <div class="widget">
                <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                <ins class="adsbygoogle"
                     style="display:block"
                     data-ad-client="ca-pub-8423475960451668"
                     data-ad-slot="7183276396"
                     data-ad-format="auto"
                     data-full-width-responsive="true"></ins>
                <script>
                     (adsbygoogle = window.adsbygoogle || []).push({{}});
                </script>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-col">
                <img src="https://indoinves.js.org/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
                <p>Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.</p>
            </div>

            <div class="footer-col">
                <h4>Tools Free Indoinves</h4>
                <ul>
                    <li><a href="https://indoinves.js.org/tools/banklocator.html">Tools Peta & Direktori Bank Global</a></li>
                    <li><a href="https://indoinves.js.org/tools/contentblog.html">Tools Konten Blog</a></li>
                    <li><a href="https://indoinves.js.org/tools/investasi.html">Tools Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.js.org/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.js.org/tools/simulatorkripto-pro.html">Tools Simulator Kripto Pro</a></li>
                    <li><a href="https://indoinves.js.org/tools/simulatorkripto.html">Tools Simulator Kripto</a></li>
                    <li><a href="https://indoinves.js.org/tools/simulatorsaham.html">Tools Simulator Saham</a></li>
                    <li><a href="https://indoinves.js.org/tools/website.html">Tools Website / SEO Checker</a></li>
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
                    <li><a href="https://indoinves.js.org/">Home</a></li>
                    <li><a href="https://indoinves.js.org/about">About Us</a></li>
                    <li><a href="https://indoinves.js.org/contact">Contact Us</a></li>
                    <li><a href="https://indoinves.js.org/privacy">Privacy Policy</a></li>
                    <li><a href="https://indoinves.js.org/sitemap">Sitemap</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Policies & Editorial</h4>
                <ul>
                    <li><a href="https://indoinves.js.org/disclaimer">Disclaimer</a></li>
                    <li><a href="https://indoinves.js.org/terms">Terms On Conditional License</a></li>
                    <li><a href="https://indoinves.js.org/editorial">Editorial Guidelines</a></li>
                    <li><a href="https://indoinves.js.org/advertise">Advertise With Us</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Community & Careers</h4>
                <ul>
                    <li><a href="https://indoinves.js.org/join-team">Join the Team</a></li>
                    <li><a href="https://indoinves.js.org/contact-forum">Contact Forum</a></li>
                    <li><a href="https://indoinves.js.org/community">Komunitas Indoinves</a></li>
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
            if (navList.classList.contains('active')) {{
                navList.classList.remove('active');
            }} else {{
                navList.classList.add('active');
            }}
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    base_dir = "blog"
    os.makedirs(base_dir, exist_ok=True)
    
    total_files = 0
    for cat in categories:
        cat_dir = os.path.join(base_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)
        print(f"Creating directory and 30 articles for category: {cat}")
        
        for i in range(1, 31):
            file_name = f"artikel{i}.html"
            file_path = os.path.join(cat_dir, file_name)
            html_content = generate_html_content(cat, i)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            total_files += 1

    print(f"Successfully generated {total_files} files across {len(categories)} categories!")

    # Auto Git add, commit, and push
    try:
        print("Staging files with git...")
        subprocess.run(["git", "add", "blog/"], check=True)
        print("Committing files...")
        subprocess.run(["git", "commit", "-m", "Automated bulk generation of 30 articles per category with complete SEO and footer"], check=True)
        print("Pushing to GitHub repository...")
        subprocess.run(["git", "push"], check=True)
        print("Successfully published to GitHub!")
    except Exception as e:
        print(f"Git auto-publish note: {e}. (Pastikan repo sudah diinisialisasi git dan terhubung ke remote origin).")

if __name__ == "__main__":
    main()
