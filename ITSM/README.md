# ITSM Chatbot

![Static Badge](https://img.shields.io/badge/Version_1.1-DB_Testing-yellow)

## Overview
This project focuses on developing an IT Service Management (ITSM) chatbot. 

To ensure data integrity and avoid disastrous accidental alterations to the live production database (hosted on Amazon), all active development and testing are performed on a secure, local copy of the database ("Local ITSM").

## Version History
* **v1.0:** Local database creation and data mirroring (Production -> Local).
* **v1.1:** Database connection testing and multi-table viewer implementation (supports both CLI and GUI interfaces).
* **Next Version (Planned):** Implement logic to differentiate between *Incidents* and *Service Requests*.

---

## Local Database Setup (MySQL Workbench)
If you need to set up the local development database from the exported backup file, follow these steps in MySQL Workbench:

### Step 1: Create the Blank Database
1. Open your MySQL Workbench workspace.
2. Click the **Create a new SQL tab** button in the top left (the icon looks like a small document with a plus sign).
3. Type the following exact command into the editor:
   
   ```sql
   CREATE DATABASE cerebree_itsmdb;
   ```
4. Click the yellow lightning bolt icon above the text editor to execute the command.
5. Check the "Action Output" window at the very bottom of the screen. You should see a green checkmark indicating the database was successfully created.

### Step 2: Import the Backup Data
1. In the top menu bar, click **Server**, then select **Data Import**.
2. Select the radio button for **Import from Self-Contained File**.
3. In the file path box, paste the exact location of your backup file:
`C:\Users\abhigyansen\OneDrive - virtualemployee P Ltd\Documents\itsmdb_backup.sql`
4. Under the **Default Target** Schema dropdown, select `cerebree_itsmdb` *(the blank database you created in Step 1)*.
5. Click the **Start Import** button in the bottom right corner to populate the database.

### Usage: Database Viewer (v1.1)
The project currently includes a Python script to test the database connection and view its contents.

#### Features:
- **Terminal Mode:** Automatically fetches and prints the top 5 records of every table in the database using grid formatting.
- **GUI Mode:** Launches a pop-up interactive window. Defaults to the incident table, features a "Back to Tables" navigation button, and allows double-clicking on any table to view all its records.

#### To toggle between modes:
Change the `TEST_GUI` flag at the bottom of the Python script:
- `TEST_GUI` = **False** *(Terminal Mode)*
- `TEST_GUI` = **True** *(GUI Mode)*