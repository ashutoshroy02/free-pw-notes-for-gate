import os
import urllib.parse

def generate_readme():
    subjects = ["Algorithms", "Artificial Intelligence", "Calculas and Optimization", "Data Structure through Python", "Data Structurer and Algorithm", "Database Management System", "General Aptitude", "Linear Algebra", "Machine Learning", "Probability and Statics", "Python for Data Science", "Verbal Aptitude", "Warehousing"]
    
    readme_content = [
        "# 📚 GATE Preparation Resource Hub",
        "",
        "A comprehensive, structured collection of class notes and practice problems for GATE aspirants. This repository is designed for quick access and structured learning.",
        "",
        "---",
        "",
        "## 📁 Subjects Overview",
        "Click on a subject to jump to its specific notes.",
        "",
    ]
    
    # Add Table of Contents badges/links
    toc_links = []
    for subject in subjects:
        if os.path.exists(subject):
            toc_links.append(f"[`{subject}`](#{subject.lower().replace(' ', '-')})")
    
    readme_content.append(" | ".join(toc_links))
    readme_content.append("")
    readme_content.append("---")
    readme_content.append("")
    
    # Process each subject
    for subject in subjects:
        if not os.path.exists(subject):
            continue
            
        readme_content.append(f"## 📘 {subject}")
        readme_content.append("")
        
        # Walk through subdirectories (Chapters)
        chapters = sorted([d for d in os.listdir(subject) if os.path.isdir(os.path.join(subject, d))])
        
        if not chapters:
            files = sorted([f for f in os.listdir(subject) if f.endswith('.pdf')])
            for f in files:
                link = urllib.parse.quote(f"{subject}/{f}")
                readme_content.append(f"- 📄 [{f}](./{link})")
        else:
            for chapter in chapters:
                chapter_path = os.path.join(subject, chapter)
                readme_content.append(f"### 📙 {chapter}")
                readme_content.append("<details>")
                readme_content.append(f"  <summary>View Notes and DPPs for {chapter}</summary>")
                readme_content.append("")
                
                # List PDF files in chapter
                files = sorted([f for f in os.listdir(chapter_path) if f.endswith('.pdf')])
                if files:
                    readme_content.append("  #### 📝 Class Notes")
                    for f in files:
                        link = urllib.parse.quote(f"{subject}/{chapter}/{f}")
                        readme_content.append(f"  - [{f}](./{link})")
                
                # Check for DPP subfolder
                dpp_path = os.path.join(chapter_path, "DPP")
                if os.path.exists(dpp_path):
                    readme_content.append("")
                    readme_content.append("  #### ✍️ Practice Sets (DPP)")
                    dpp_files = sorted([f for f in os.listdir(dpp_path) if f.endswith('.pdf')])
                    for f in dpp_files:
                        link = urllib.parse.quote(f"{subject}/{chapter}/DPP/{f}")
                        readme_content.append(f"  - [{f}](./{link})")
                
                readme_content.append("</details>")
                readme_content.append("")
        
        readme_content.append("---")
        readme_content.append("")

    readme_content.append("## 🤝 Contributing")
    readme_content.append("Contributions are welcome! If you have better notes or want to fix something, please open a PR.")
    readme_content.append("")
    readme_content.append("---")
    readme_content.append("<p align='center'><i>Happy Learning! 🚀</i></p>")

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("\n".join(readme_content))

if __name__ == "__main__":
    generate_readme()
    print("Clean & Professional README generated successfully!")
