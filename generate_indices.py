import os

subjects = ["Algorithms", "Artificial Intelligence", "Calculas and Optimization", "Data Structure through Python", "Data Structurer and Algorithm", "Database Management System", "General Aptitude", "Linear Algebra", "Machine Learning", "Probability and Statics", "Python for Data Science", "Verbal Aptitude", "Warehousing"]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PW-GATE PRO</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: oklch(8% 0.01 250);
            --bg-card: oklch(18% 0.02 250 / 0.7);
            --accent: oklch(70% 0.2 250);
            --text: oklch(98% 0.01 250);
            --text-dim: oklch(70% 0.02 250);
        }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }}
        .container {{
            max-width: 900px;
            width: 100%;
        }}
        header {{
            margin-bottom: 60px;
        }}
        .back-btn {{
            color: var(--text-dim);
            text-decoration: none;
            font-size: 0.875rem;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 24px;
            transition: color 0.2s;
        }}
        .back-btn:hover {{ color: var(--accent); }}
        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 3rem;
            margin: 0;
            letter-spacing: -0.04em;
        }}
        .list {{
            display: grid;
            gap: 12px;
        }}
        .item {{
            background: var(--bg-card);
            padding: 20px 32px;
            border-radius: 16px;
            border: 1px solid oklch(100% 0 0 / 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-decoration: none;
            color: inherit;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .item:hover {{
            border-color: var(--accent);
            background: oklch(100% 0 0 / 0.05);
            transform: translateX(8px);
        }}
        .item-info {{
            display: flex;
            flex-direction: column;
        }}
        .item-name {{
            font-weight: 600;
            font-size: 1.1rem;
        }}
        .item-type {{
            font-size: 0.75rem;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 4px;
        }}
        .icon {{ font-size: 1.5rem; opacity: 0.5; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <a href="{back_link}" class="back-btn">← BACK TO DASHBOARD</a>
            <h1>{title}</h1>
        </header>
        <div class="list">
            {items}
        </div>
    </div>
</body>
</html>
"""

def generate_index(path, title, is_root=False):
    items_html = []
    
    # Sort items: directories first, then files
    try:
        entries = sorted(os.listdir(path))
    except FileNotFoundError:
        return

    for entry in entries:
        if entry.startswith('.') or entry == 'index.html':
            continue
            
        full_path = os.path.join(path, entry)
        is_dir = os.path.isdir(full_path)
        
        icon = "📁" if is_dir else "📄"
        type_label = "FOLDER" if is_dir else "DOCUMENT"
        
        # URL encode spaces for links
        link = entry.replace(" ", "%20")
        
        items_html.append(f"""
            <a href="{link}" class="item">
                <div class="item-info">
                    <div class="item-name">{entry}</div>
                    <div class="item-type">{type_label}</div>
                </div>
                <div class="icon">{icon}</div>
            </a>
        """)
    
    back_link = "/free-pw-notes-for-gate/" if is_root else "../"
    
    with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(HTML_TEMPLATE.format(
            title=title,
            items="".join(items_html),
            back_link=back_link
        ))

# Generate for all subjects and recursively for subdirectories
for subject in subjects:
    subject_path = os.path.join(os.getcwd(), subject)
    if os.path.exists(subject_path):
        generate_index(subject_path, subject, is_root=True)
        # Recursively handle subfolders (e.g. chapters)
        for root, dirs, files in os.walk(subject_path):
            for d in dirs:
                dir_path = os.path.join(root, d)
                generate_index(dir_path, d, is_root=False)

print("Index files generated successfully!")
