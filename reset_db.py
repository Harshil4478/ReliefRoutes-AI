"""Reset the ReliefRoutes AI database (removes test data).

Usage (stop the Streamlit app first):
    python reset_db.py              # wipe EVERYTHING (after a backup)
    python reset_db.py --keep-centres   # keep relief centres + their stock, wipe the rest

A timestamped backup copy of relief_routes.db is made before any change.
The app recreates any missing tables automatically on next start.
"""
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

DB = Path(__file__).with_name("relief_routes.db")
ALL_TABLES = ["agent_proposals", "dispatches", "emergency_requests", "inventory", "relief_centres"]
KEEP_CENTRES_TABLES = ["agent_proposals", "dispatches", "emergency_requests"]


def main():
    if not DB.exists():
        print("No relief_routes.db found - nothing to reset.")
        return
    keep_centres = "--keep-centres" in sys.argv
    tables = KEEP_CENTRES_TABLES if keep_centres else ALL_TABLES

    print(f"This will delete all rows from: {', '.join(tables)}")
    if input("Type YES to continue: ").strip() != "YES":
        print("Cancelled.")
        return

    backup = DB.with_name(f"relief_routes_backup_{datetime.now():%Y%m%d_%H%M%S}.db")
    shutil.copy2(DB, backup)
    print(f"Backup saved: {backup.name}")

    conn = sqlite3.connect(DB)
    try:
        existing = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for table in tables:
            if table in existing:
                conn.execute(f"DELETE FROM {table}")
                conn.execute("DELETE FROM sqlite_sequence WHERE name = ?", (table,))
        conn.commit()
    finally:
        conn.close()
    print("Done. Restart the app and enter fresh, real data.")


if __name__ == "__main__":
    main()
