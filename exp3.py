"""
Small educational example:
- Shows a disabled (pseudo) insecure pattern for illustration only.
- Provides a safe, runnable replacement that prevents SQL injection.
"""

# ---------- PSEUDO-VULNERABLE (DISABLED) ----------
def _disabled(op):
    raise RuntimeError("Disabled insecure operation: " + op)

def pseudo_vulnerable_user_lookup(request):
    # DO NOT RUN: this is intentionally disabled and non-executable.
    # It illustrates the classic unsafe pattern: concatenating user input
    # directly into a SQL statement (SQL injection risk).
    username = request.args.get("username", "")
    _disabled("sql_query_concatenation")
    # example of what NOT to do (commented out):
    # query = "SELECT id, username FROM users WHERE username = '" + username + "';"
    # db.execute(query)
    return "pseudo-vulnerable (disabled)"

# ---------- SECURE REPLACEMENT ----------
import sqlite3
import json

def safe_user_lookup(request, db_path=":memory:"):
    """
    Secure lookup using parameterized queries.
    request should have .args.get('username') similar to Flask's request.
    """
    username = request.args.get("username", "")
    if not username:
        return ("missing username", 400)

    conn = sqlite3.connect(db_path)
    try:
        # Use parameterized query to avoid SQL injection
        cur = conn.execute("SELECT id, username FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if not row:
            return ("not found", 404)
        result = {"id": row[0], "username": row[1]}
        return (json.dumps(result), 200)
    finally:
        conn.close()

# ---------- QUICK DEMO HARNESS (for local testing) ----------
class DummyRequest:
    def __init__(self, args):
        self.args = args

if __name__ == "__main__":
    # Create an in-memory DB and a sample user for demonstration
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
    conn.execute("INSERT INTO users (username) VALUES (?)", ("alice",))
    conn.commit()
    conn.close()

    # Test safe lookup
    req = DummyRequest(args={"username": "alice"})
    print(safe_user_lookup(req, db_path=":memory:"))  # likely returns not found in this simple demo
    # Note: using :memory: here means the demo DB above is a different connection;
    # for a persistent demo, use a temporary file DB.
