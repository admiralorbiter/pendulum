import os
import subprocess
import markdown

def compile_synthesis_report():
    html_path = "reports/research_synthesis_report.html"
    md_path = "reports/research_synthesis_report.md"
    pdf_path = "reports/research_synthesis_report.pdf"
    
    # 1. Read the existing template header from reports/research_synthesis_report.html (up to body tag)
    print("Reading HTML template...")
    header_lines = []
    with open(html_path, "r", encoding="utf-8") as f:
        for line in f:
            header_lines.append(line)
            if "<body>" in line:
                break
    header = "".join(header_lines)
    
    # 2. Read the markdown content
    print("Reading Markdown content...")
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # 3. Convert markdown to HTML
    print("Converting Markdown to HTML...")
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "md_in_html"]
    )
    
    # 4. Combine into final HTML
    print("Writing final HTML...")
    final_html = header + "\n" + html_body + "\n</body>\n</html>"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    # 5. Export to PDF using headless Chrome
    print("Exporting HTML to PDF using headless Chrome...")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    # Check if Chrome exists
    if not os.path.exists(chrome_path):
        raise FileNotFoundError(f"Chrome not found at: {chrome_path}")
        
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={os.path.abspath(pdf_path)}",
        os.path.abspath(html_path)
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("PDF export completed successfully!")
    else:
        print(f"PDF export failed with return code: {result.returncode}")
        print("Stderr:", result.stderr)
        print("Stdout:", result.stdout)

if __name__ == "__main__":
    compile_synthesis_report()
