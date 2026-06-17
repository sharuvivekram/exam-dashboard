import os
import pandas as pd
from datetime import datetime

def make_rows(excel_path, sheet_name):
    if not os.path.exists(excel_path): return ""
    try:
        # This reads the specific tab from your single Excel file
        df = pd.read_excel(excel_path, sheet_name=sheet_name).fillna("-")
    except Exception:
        return "" # Returns empty if the tab name doesn't match
    
    html = ""
    for _, r in df.iterrows():
        portal = str(r.get('Portal', '-')).strip()
        url = f"https://{portal}" if not portal.startswith("http") else portal
        html += f"""<tr>
            <td><strong>{r.get('Exam Name','-')}</strong><br><small style='color:#64748B;'>{r.get('Full Form','-')}</small></td>
            <td><a href='{url}' target='_blank' class='portal-link'>{portal}</a></td>
            <td><code>{r.get('Notification Date','-')}</code></td>
            <td><span style='font-weight:600;'>{r.get('Exam Date','-')}</span></td>
            <td><span class='badge-salary'>{r.get('Salary (1st Yr)','-')}</span></td>
            <td><div class='text-pros'>▲ {r.get('Pros','-')}</div><div class='text-cons'>▼ {r.get('Cons','-')}</div></td>
        </tr>"""
    return html

with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

template = template.replace("{{SYNC_TIME}}", datetime.now().strftime("%Y-%m-%d %H:%M UTC"))

# Here we tell the engine to look inside Exams.xlsx and extract each tab name
template = template.replace("{{CENTRAL_ROWS}}", make_rows("Exams.xlsx", "Central"))
template = template.replace("{{STATE_ROWS}}", make_rows("Exams.xlsx", "State"))
template = template.replace("{{BANKING_ROWS}}", make_rows("Exams.xlsx", "Banking"))

os.makedirs("public", exist_ok=True)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(template)
