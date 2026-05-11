import os
import urllib.parse

def generate_readme():
    subjects = ["Algorithms", "Artificial Intelligence", "Calculas and Optimization", "Data Structure through Python", "Data Structurer and Algorithm", "Database Management System", "General Aptitude", "Linear Algebra", "Machine Learning", "Probability and Statics", "Python for Data Science", "Verbal Aptitude", "Warehousing"]
    
    readme_content = [
        "<div align='center'>",
        "  <img src='./banner.png' width='100%' />",
        "  <h1>🚀 GATE PRO NOTES</h1>",
        "  <p><i>The ultimate curated repository for GATE (DA & IT) preparation.</i></p>",
        "  <p>",
        "    <img src='https://img.shields.io/badge/Status-Complete-success?style=for-the-badge' />",
        "    <img src='https://img.shields.io/badge/Format-PDF-red?style=for-the-badge' />",
        "    <img src='https://img.shields.io/badge/Source-PW%20Class-blue?style=for-the-badge' />",
        "  </p>",
        "</div>",
        "",
        "> [!IMPORTANT]",
        "> **PDF PREVIEW TIP:** If GitHub says a file is \"too large to display\", click the link to open it directly in your browser's viewer, or click the **Download** button on the file page.",
        "",
        "---",
        "",
        "## 📑 Table of Contents",
    ]
    
    # Add Table of Contents links
    for subject in subjects:
        if os.path.exists(subject):
            readme_content.append(f"- [{subject}](#{subject.lower().replace(' ', '-')})")
    
    readme_content.append("")
    readme_content.append("---")
    readme_content.append("")
    
    # Process each subject
    for subject in subjects:
        if not os.path.exists(subject):
            continue
            
        readme_content.append(f"## {subject}")
        readme_content.append("")
        
        # Walk through subdirectories (Chapters)
        chapters = sorted([d for d in os.listdir(subject) if os.path.isdir(os.path.join(subject, d))])
        
        if not chapters:
            # Handle files directly in the subject folder if any
            files = sorted([f for f in os.listdir(subject) if f.endswith('.pdf')])
            for f in files:
                # Add ?raw=true to force native browser preview
                link = urllib.parse.quote(f"{subject}/{f}") + "?raw=true"
                readme_content.append(f"- 📄 [{f}](./{link})")
        else:
            for chapter in chapters:
                chapter_path = os.path.join(subject, chapter)
                readme_content.append(f"### 📂 {chapter}")
                readme_content.append("<details>")
                readme_content.append("  <summary><b>📖 Click to expand notes & DPPs</b></summary>")
                readme_content.append("")
                
                # List PDF files in chapter
                files = sorted([f for f in os.listdir(chapter_path) if f.endswith('.pdf')])
                for f in files:
                    link = urllib.parse.quote(f"{subject}/{chapter}/{f}") + "?raw=true"
                    readme_content.append(f"  - 📄 **Notes:** [{f}](./{link})")
                
                # Check for DPP subfolder
                dpp_path = os.path.join(chapter_path, "DPP")
                if os.path.exists(dpp_path):
                    readme_content.append("")
                    readme_content.append("  > [!TIP]")
                    readme_content.append("  > **Daily Practice Problems (DPP) available below:**")
                    readme_content.append("")
                    dpp_files = sorted([f for f in os.listdir(dpp_path) if f.endswith('.pdf')])
                    for f in dpp_files:
                        link = urllib.parse.quote(f"{subject}/{chapter}/DPP/{f}") + "?raw=true"
                        readme_content.append(f"  - ✍️ **DPP:** [{f}](./{link})")
                
                readme_content.append("</details>")
                readme_content.append("")
        
        readme_content.append("---")
        readme_content.append("")

    readme_content.append("## ❤️ How to Contribute")
    readme_content.append("Found something missing or want to add your own notes? Simply **Fork** the repo and submit a **Pull Request**!")
    readme_content.append("")
    readme_content.append("---")
    readme_content.append("<div align='center'>")
    readme_content.append("  <i>Generated with ❤️ for GATE aspirants. Keep Grinding!</i>")
    readme_content.append("</div>")

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("\n".join(readme_content))

if __name__ == "__main__":
    generate_readme()
    print("PDF-optimized README generated successfully!")
