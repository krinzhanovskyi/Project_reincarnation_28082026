# Project Reincarnation (Folder Pockets)

**Folder Pockets** is a lightweight Windows utility that turns ordinary desktop folders into interactive widget-windows. Hovering the cursor over a folder automatically displays a pop-up "pocket" with its contents, eliminating unnecessary clicks and screen clutter from open File Explorer windows.

## Current Functionality Patch 0.8a

- **Intelligent Recognition:** The script detects when the cursor is specifically hovering over a desktop folder icon (ignoring shortcuts, files, and other windows).
- **Invisible Integration:** The window operates in `Tool` mode - it does not appear on the taskbar and does not steal input focus when opened.
- **DPI Independence:** Automatic correction of mouse coordinates during Windows screen scaling (DPI Scaling) via `ctypes`.
- **Smooth UI:** Shows the place of window in feature.

## Tech Stack

- **Python 3.10+**
- **PyQt6** — UI engine, hover delay timers, and the signals/slots system.
- **uiautomation** — reading the `explorer.exe` element tree (interacting with the `SysListView32` class).
- **ctypes & winreg** — low-level Windows API calls for DPI fixing and registry path resolution.

## Project Structure

```text
Project_reincarnation/
│
├── main.py                # Entry point, application orchestrator
├── config.py              # Global settings (timings, UI dimensions)
├── .gitignore             # Git ignore rules
├── README.md              # Documentation
│
├── backend/               # System logic ("brain")
│   ├── __init__.py        # Package initializer
│   ├── file_reader.py     # Parsing folder contents (upcoming)
│   ├── mouse_tracker.py   # Cursor tracking and timers via QTimer
│   └── win_api.py         # Parsing Windows UI elements and path validation
│
└── ui/                    # User Interface ("face")
    ├── __init__.py        # Package initializer
    ├── pocket_window.py   # Widget window configuration (FramelessWindowHint)
    └── styles.py          # UI styling (QSS/CSS, colors, paddings)
```

## Installation and Usage

1.  Ensure Python is installed and added to your `PATH`.
2.  Install the required dependencies:

    ```
    pip install PyQt6 uiautomation

    ```

3.  Run the main application file:

    ```
    python main.py
    or py main.py

    ```

## Roadmap

The project is divided into logical phases, from basic system integration to a full release as a complete desktop application.

### Phase 1: Core and System Integration (Completed)

- [x] **Cursor Tracking:** Background monitoring of mouse coordinates via built-in `PyQt` timers without blocking the main thread.
- [x] **Basic UI:** Creating a transparent widget without system borders (FramelessWindowHint) operating in stealth mode for the taskbar (`Tool`).
- [x] **Windows API System Hooks:** Intelligent parsing of `explorer.exe` (SysListView32) to accurately identify folders and ignore shortcuts, files, or empty space.
- [x] **DPI Awareness:** Automatic coordinate correction for non-standard Windows screen scaling via `ctypes`.

### Phase 2: Data and Content (Current started)

- [ ] **`file_reader.py` Module:** Parsing directory contents with smart sorting (e.g., showing recently modified files first).
- [ ] **Content Filtering:** Limiting the number of displayed items (protection against freezing on folders with 10,000 files) and hiding system files (like `desktop.ini`).
- [ ] **Dynamic UI Generation:** Rendering the file list inside the "pocket" (name, size, date).
- [ ] **Icon Extraction:** Fetching and caching native Windows system icons for each file type in the list.

### Phase 3: Interactivity and UX (Polishing)

- [ ] **Click-to-Open:** Implementing clickable elements in the "pocket" to instantly open a file with the standard Windows program (`os.startfile`).
- [ ] **Smart Positioning:** Algorithm to prevent window cropping (shifting the widget if the folder is near the edge or corner of the monitor).
- [ ] **Animations and Transitions:** Smooth fade-in and fade-out of the window when hover triggers are activated.
- [ ] **Custom Scrollbar:** Adding a stylized scrollbar for folders whose contents exceed the default window height.

### Phase 4: Release and Scaling (Future Plans)

- [ ] **System Tray:** Moving control to the system tray (near the clock) with a context menu for pause, exit, and settings.
- [ ] **Global Hotkeys:** Keyboard combinations to quickly toggle the widgets on/off (useful while gaming or working in full-screen applications).
- [ ] **`.exe` Packaging:** Compiling the project via PyInstaller into a single executable file so the program runs on any PC without needing to install Python.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/krinzhanovskyi/Project_reincarnation_28082026/blob/main/LICENSE) file for details.
