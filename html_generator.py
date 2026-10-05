import html
from typing import List, Dict, Any

def generate_video_html(
    title: str,
    video_id: str,
    pub_date: str,
    dur_str: str,
    channel_name: str,
    channel_url: str,
    model_signature: str,
    summary_html: str,
    tools_list: List[str],
    key_points: List[str],
    segments: List[Dict[str, Any]]
) -> str:
    """
    Génère une page HTML moderne, responsive et stylisée
    incluant la description et transcription vidéo complète intégrant les captures d'écran en timeline.
    """

    tools_badges = "".join([f'<span class="tool-tag">{html.escape(t)}</span>' for t in tools_list])
    points_items = "".join([f'<li><span class="point-bullet">✦</span><span>{html.escape(p)}</span></li>' for p in key_points])

    timeline_items = []
    for s in segments:
        idx = s.get("index", 1)
        start_str = s.get("start_str", "00:00:00")
        end_str = s.get("end_str", "00:00:00")
        verbatim = html.escape(s.get("verbatim_fr", ""))
        interface = html.escape(s.get("interface", ""))
        contenu = html.escape(s.get("contenu", ""))
        action = html.escape(s.get("action", ""))

        screenshots_list = s.get("screenshots", [])
        img_html = ""
        if screenshots_list:
            cards = []
            for sc in screenshots_list:
                img_path = html.escape(sc.get("path", ""))
                cap = html.escape(sc.get("caption", f"Démonstration @ {sc.get('timestamp', start_str)}"))
                t_str = html.escape(sc.get("timestamp", start_str))
                cards.append(f'''
                <div class="screenshot-card">
                    <div class="img-wrapper">
                        <img src="{img_path}" alt="{cap}" loading="lazy" onclick="openLightbox('{img_path}')">
                        <span class="zoom-badge">🔍 Zoom</span>
                    </div>
                    <div class="screenshot-caption">
                        <span class="caption-time">⏱️ {t_str}</span>
                        <span class="caption-text">{cap}</span>
                    </div>
                </div>
                ''')

            count_class = f"count-{min(len(screenshots_list), 4)}"
            img_html = f'''
            <div class="segment-screenshots-wrapper">
                <div class="screenshots-header">
                    <span class="media-icon">📸</span>
                    <strong>Capture(s) d'écran clé en timeline ({len(screenshots_list)}) :</strong>
                </div>
                <div class="segment-screenshots-grid {count_class}">
                    {"".join(cards)}
                </div>
            </div>
            '''

        card = f'''
        <div class="timeline-block" id="segment-{idx}">
            <div class="timeline-time">
                <span class="time-badge">⏱️ {start_str} - {end_str}</span>
                <span class="segment-idx">Segment #{idx:02d}</span>
            </div>
            <div class="timeline-content">
                <div class="verbatim-box">
                    <div class="verbatim-header">
                        <span class="speaker-icon">🔊</span>
                        <strong>Audio Verbatim (Mot pour Mot en Français) :</strong>
                    </div>
                    <blockquote class="verbatim-text">{verbatim}</blockquote>
                </div>
                <div class="visual-box">
                    <div class="visual-header">
                        <span class="eye-icon">👁️</span>
                        <strong>Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :</strong>
                    </div>
                    <div class="visual-details">
                        <p><strong>Interface & Outils :</strong> {interface}</p>
                        <p><strong>Contenu textuel & Code :</strong> {contenu}</p>
                        <p><strong>Action / Démonstration :</strong> {action}</p>
                    </div>
                </div>
                {img_html}
            </div>
        </div>
        '''
        timeline_items.append(card)

    timeline_html = "\n".join(timeline_items)

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} — Transcription Intégrale | {html.escape(channel_name)}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #0a0e17;
            --bg-card: #111827;
            --bg-card-alt: #162032;
            --border: #1f2937;
            --border-highlight: #374151;
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.25);
            --secondary: #818cf8;
            --accent: #10b981;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --text-faint: #6b7280;
            --quote-bg: rgba(17, 24, 39, 0.7);
            --visual-bg: rgba(15, 23, 42, 0.75);
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 16px;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'Fira Code', monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: var(--font-sans);
            line-height: 1.65;
            padding: 2rem 1rem 6rem;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        /* Header */
        header.hero-header {{
            background: linear-gradient(145deg, #131b2e 0%, #0c1222 100%);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 2.5rem 2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
        }}

        header.hero-header::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        }}

        .badge-channel {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(56, 189, 248, 0.12);
            color: var(--primary);
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 9999px;
            padding: 0.35rem 0.85rem;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1rem;
            text-decoration: none;
        }}

        h1.video-title {{
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            line-height: 1.25;
            color: #ffffff;
            margin-bottom: 1.2rem;
        }}

        .video-meta-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 1.2rem;
            color: var(--text-muted);
            font-size: 0.9rem;
            border-top: 1px solid var(--border);
            padding-top: 1.2rem;
        }}

        .meta-item {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .meta-item a {{
            color: var(--primary);
            text-decoration: none;
        }}

        /* Summary Section */
        .executive-summary {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 2rem;
            margin-bottom: 3rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--border);
        }}

        .tools-badges-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin: 1.2rem 0;
        }}

        .tool-tag {{
            background: var(--bg-card-alt);
            color: var(--primary);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-sm);
            padding: 0.3rem 0.75rem;
            font-size: 0.85rem;
            font-family: var(--font-mono);
            font-weight: 500;
        }}

        .key-points-list {{
            list-style: none;
            margin-top: 1.2rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}

        .key-points-list li {{
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            color: var(--text-main);
            font-size: 0.95rem;
        }}

        .point-bullet {{
            color: var(--accent);
            font-size: 1rem;
            line-height: 1.4;
        }}

        /* Timeline Blocks */
        .timeline-section {{
            position: relative;
        }}

        .timeline-block {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            margin-bottom: 2rem;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.15s ease, border-color 0.15s ease;
        }}

        .timeline-block:hover {{
            border-color: var(--border-highlight);
        }}

        .timeline-time {{
            background: var(--bg-card-alt);
            padding: 0.85rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
        }}

        .time-badge {{
            font-family: var(--font-mono);
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--primary);
            background: rgba(56, 189, 248, 0.1);
            padding: 0.25rem 0.6rem;
            border-radius: var(--radius-sm);
        }}

        .segment-idx {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-faint);
            font-weight: 700;
        }}

        .timeline-content {{
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }}

        /* Verbatim Box */
        .verbatim-box {{
            background: var(--quote-bg);
            border-left: 4px solid var(--primary);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 1.2rem;
        }}

        .verbatim-header {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.6rem;
        }}

        .verbatim-text {{
            font-size: 1rem;
            line-height: 1.7;
            color: #ffffff;
            font-weight: 400;
        }}

        /* Visual Box */
        .visual-box {{
            background: var(--visual-bg);
            border: 1px solid rgba(129, 140, 248, 0.2);
            border-radius: var(--radius-md);
            padding: 1.2rem;
        }}

        .visual-header {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            color: var(--secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.75rem;
        }}

        .visual-details p {{
            font-size: 0.92rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
        }}

        .visual-details p:last-child {{
            margin-bottom: 0;
        }}

        .visual-details strong {{
            color: var(--text-main);
        }}

        /* Screenshots Grid */
        .segment-screenshots-wrapper {{
            border-top: 1px solid var(--border);
            padding-top: 1rem;
        }}

        .screenshots-header {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            color: var(--accent);
            margin-bottom: 0.85rem;
        }}

        .segment-screenshots-grid {{
            display: grid;
            gap: 1rem;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        }}

        .screenshot-card {{
            background: var(--bg-card-alt);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-md);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .img-wrapper {{
            position: relative;
            cursor: pointer;
            overflow: hidden;
            background: #000;
            aspect-ratio: 16 / 9;
        }}

        .img-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.25s ease;
        }}

        .img-wrapper:hover img {{
            transform: scale(1.03);
        }}

        .zoom-badge {{
            position: absolute;
            bottom: 8px;
            right: 8px;
            background: rgba(0, 0, 0, 0.75);
            color: #fff;
            padding: 0.2rem 0.5rem;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
            backdrop-filter: blur(4px);
            pointer-events: none;
        }}

        .screenshot-caption {{
            padding: 0.75rem;
            font-size: 0.82rem;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}

        .caption-time {{
            font-family: var(--font-mono);
            color: var(--accent);
            font-weight: 600;
        }}

        .caption-text {{
            color: var(--text-muted);
        }}

        /* Lightbox */
        .lightbox-modal {{
            display: none;
            position: fixed;
            z-index: 99999;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(6px);
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }}

        .lightbox-modal.active {{
            display: flex;
        }}

        .lightbox-content {{
            max-width: 90vw;
            max-height: 85vh;
            border-radius: var(--radius-md);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
            border: 1px solid var(--border-highlight);
        }}

        .lightbox-close {{
            position: absolute;
            top: 25px;
            right: 35px;
            color: #fff;
            font-size: 2.5rem;
            cursor: pointer;
            user-select: none;
        }}

        footer.site-footer {{
            text-align: center;
            padding-top: 4rem;
            color: var(--text-faint);
            font-size: 0.85rem;
        }}

        @media (max-width: 768px) {{
            h1.video-title {{
                font-size: 1.6rem;
            }}
            .video-meta-bar {{
                flex-direction: column;
                gap: 0.5rem;
            }}
            .timeline-content {{
                padding: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="hero-header">
            <a href="{channel_url}" target="_blank" class="badge-channel">
                <span>📺</span>
                <span>{html.escape(channel_name)}</span>
            </a>
            <h1 class="video-title">{html.escape(title)}</h1>
            <div class="video-meta-bar">
                <div class="meta-item">
                    <span>🔗</span>
                    <a href="https://www.youtube.com/watch?v={video_id}" target="_blank">Lien YouTube (<code>{video_id}</code>)</a>
                </div>
                <div class="meta-item">
                    <span>📅</span>
                    <span>Publication : {pub_date}</span>
                </div>
                <div class="meta-item">
                    <span>⏱️</span>
                    <span>Durée : {dur_str}</span>
                </div>
                <div class="meta-item">
                    <span>🤖</span>
                    <span>Modèles : <code>{html.escape(model_signature)}</code></span>
                </div>
            </div>
        </header>

        <section class="executive-summary">
            <div class="section-header">
                <span>📌</span>
                <span>Synthèse Exécutive & Enseignements Stratégiques</span>
            </div>
            {summary_html}
            {f'<div class="tools-badges-cloud">{tools_badges}</div>' if tools_badges else ''}
            {f'<ul class="key-points-list">{points_items}</ul>' if points_items else ''}
        </section>

        <section class="timeline-section">
            <div class="section-header">
                <span>⏱️</span>
                <span>Chronologie & Transcription Complète Audio & Visuelle</span>
            </div>
            {timeline_html}
        </section>

        <footer class="site-footer">
            <p>Veille Multimodale Automatisée Antigravity sur VPS — Chaîne <strong>{html.escape(channel_name)}</strong></p>
            <p>100% Verbatim Français Audio (Whisper) & Analyse Visuelle d'Écran (Gemini)</p>
        </footer>
    </div>

    <div id="lightbox" class="lightbox-modal" onclick="closeLightbox()">
        <span class="lightbox-close">&times;</span>
        <img id="lightbox-img" class="lightbox-content" src="" alt="Capture agrandie">
    </div>

    <script>
        function openLightbox(src) {{
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox').classList.add('active');
        }}
        function closeLightbox() {{
            document.getElementById('lightbox').classList.remove('active');
        }}
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') closeLightbox();
        }});
    </script>
</body>
</html>
'''
