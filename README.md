# 🎯 Exam Preparation Strategy Dashboard

An automated tracking hub for central, state, and banking sector examination schedules. This project uses an automated background compiler to read live spreadsheet data and render a clean, responsive web interface via GitHub Pages.

---

## 🚀 Live Dashboard
Your tracking control center is deployed live. You can access the interface, switch between tracking categories, and monitor application window statuses at your custom GitHub Pages URL:
👉 **Find your link under: Repository Settings -> Pages**

---

## 📁 System Architecture & Files

The repository is built around a single data source and three helper automation scripts:

1. **`Exams.xlsx`**: The core data asset. This single spreadsheet contains three distinct sheets: `Central`, `State`, and `Banking`. All target deadlines, notification windows, and salary parameters live here.
2. **`template.html`**: The visual layer blueprint. It contains the structure, dark-blue themed layouts, interactive view buttons, and responsive table grids.
3. **`build_dashboard.py`**: The bridge engine. This script reads the rows and individual sheets inside `Exams.xlsx` and dynamically injects them directly into the HTML code layout.
4. **`.github/workflows/deploy.yaml`**: The automated worker schedule. It directs GitHub's built-in servers to wake up automatically and rebuild the layout.

---

## 🔄 Operational Cycle & Updates

### ⏱️ Weekly Automated Synchronization
The environment runs on a **weekly cron schedule** configured inside the deployment instructions. 
* **Every Sunday at 6:00 PM UTC**, GitHub automatically spins up a background runtime environment.
* It checks your spreadsheet data, recalculates status matrices, and pushes a fresh build to your public dashboard.

### ✍️ How to Manually Update the Dashboard
Whenever an exam date changes or a new notification is announced, you can update your tracker instantly:
1. Open your master **`Exams.xlsx`** file on your computer and make your text or date updates.
2. Ensure that your sheet tab names remain exactly as **`Central`**, **`State`**, and **`Banking`**.
3. Upload the new file to GitHub, overwriting the previous version.
4. **Instant Update Trigger**: Uploading a change to the main branch automatically fires the deployment process, and your webpage will update within 60 seconds!

---

## 🛠️ Requirements & Tooling
The automated background worker uses the following Python modules to open and slice spreadsheet layers:
* `pandas` — for rapid data framing and tabular mapping.
* `openpyxl` — to natively unpack multi-tab `.xlsx` binary spreadsheet components.


## click here: https://sharuvivekram.github.io/exam-dashboard/
