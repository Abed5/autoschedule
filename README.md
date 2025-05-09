<<<<<<< HEAD
# autoschedule

**Automate Scheduling on Google Calendar with Python**

`autoschedule` is a Python-based tool that streamlines task scheduling directly to your Google Calendar. With just a task layout file and a few configuration options, you can create weighted tasks, randomize their order, insert breaks, and automatically publish them as events in your calendar.

---

## Features

* 🗓️ **Google Calendar Integration**
* 🧠 **Task Weighting & Grouping** (based on complexity or duration)
* 🔀 **Optional Task Randomization**
* ☕ **Automatic Break Insertion**
* 📋 **Custom Task Layout Parsing**
* 💾 **Persistent Task Output** to `tasks_list.txt`

---

## 📁 Project Structure

```
autoschedule/
├── generate_tasks.py        # Handles parsing, processing, grouping, and outputting tasks
├── schedule_tasks.py        # Handles interaction with Google Calendar API to schedule tasks
├── tasks_layout.txt         # Input file describing tasks
├── tasks_list.txt           # Output file used to schedule tasks
```

---

## 🧰 Setup

### Requirements

* Python 3.7+
* Google Calendar API credentials (OAuth 2.0)

### Install Dependencies

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

> ⚠️ You must set up your Google Calendar API access and download the credentials JSON file. Refer to the [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python).

---

## 📌 Input Format: `tasks_layout.txt`

The input should be written in the following format (after line 3):

```
1 TaskName 2
# Commented line (ignored)
4 AnotherTask 1
```

Where:

* First value = Initial weight classification (1, 2, or 4)
* Second value = Task name
* Third value = Task count (how many times it should appear)

Weights are then transformed into durations:

* 1 → 11 minutes
* 2 → 22 minutes
* 4 → 45 minutes

---

## 🚀 Usage

### Step 1: Generate & Organize Tasks

Run:

```bash
python generate_tasks.py
```

This will:

* Read `tasks_layout.txt`
* Convert and group tasks by weight
* Allow shuffling (optional)
* Write output to `tasks_list.txt`

### Step 2: Schedule Tasks to Google Calendar

Update your calendar ID and timezone in `schedule_tasks.py`. Then run:

```bash
python schedule_tasks.py
```

This will:

* Parse `tasks_list.txt`
* Automatically insert breaks
* Add events to your Google Calendar

---

## 🛠 Core Logic Summary

### `generate_tasks.py`

* Parses task layout
* Converts raw input to structured list
* Assigns weights
* Groups tasks so their combined weight doesn't exceed 4
* Supports shuffling and writes formatted results to file

### `schedule_tasks.py`

* Reads formatted tasks
* Calculates time blocks based on weight
* Inserts breaks between tasks
* Uses Google Calendar API to schedule them

---

## 📎 Notes

* Tasks are grouped to fit a 50-minute block (including breaks).
* Events are annotated with weight-based descriptions (e.g., `22-22`, `11-11`, etc.).
* Breaks are always inserted at the beginning, middle, and end of each block.

---

## 🔒 Authentication

The script uses OAuth 2.0 for Google Calendar API. Ensure your credentials file is stored safely and follows Google’s guidelines.

---

## 🙌 Contribution

Pull requests are welcome! If you find bugs or have feature requests, feel free to open an issue.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Created by Abednego Kipkirui. Reach out via kirui.abed@gmail.com or raise an issue.

---

Enjoy automated scheduling! 🎯