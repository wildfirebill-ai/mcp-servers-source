#!/usr/bin/env python3
"""api-builder MCP Server — port 25007"""

import base64 as _b64
import datetime
import functools
import hashlib
import json
import logging
import os
import random
import string
import subprocess
import uuid as _uuid
from pathlib import Path

from mcp.server.fastmcp import FastMCP

SERVER_NAME = "api-builder"
PORT = 25007
HOST = "0.0.0.0"

LOG_DIR = Path(__file__).parent / "data"
LOG_DIR.mkdir(parents=True, exist_ok=True)

_log_fh = logging.FileHandler(LOG_DIR / "server.log", encoding="utf-8", mode="a")
_log_fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
_log_sh = logging.StreamHandler()
_log_sh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(_log_fh)
root.addHandler(_log_sh)

logger = logging.getLogger(SERVER_NAME)
logger.info("Server starting — %s:%s", SERVER_NAME, PORT)


def _log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("TOOL %s args=%s", func.__name__, kwargs)
        try:
            result = func(*args, **kwargs)
            logger.info("TOOK %s OK", func.__name__)
            return result
        except Exception as e:
            logger.error("TOOL %s FAILED: %s", func.__name__, e)
            raise
    return wrapper


mcp = FastMCP(SERVER_NAME, host=HOST, port=PORT)


def _load_skills() -> str:
    p = Path(__file__).parent / "skills.md"
    return p.read_text() if p.exists() else "Skills file not found."

MEMORY_FILE = Path(__file__).parent / "data" / "memory.json"


def _read_memory() -> dict:
    if MEMORY_FILE.exists():
        try:
            return json.loads(MEMORY_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _write_memory(data: dict) -> None:
    MEMORY_FILE.write_text(json.dumps(data, indent=2))


@mcp.tool()
@_log_call
def ping() -> str:
    """Health check."""
    return "pong"


@mcp.tool()
@_log_call
def echo(text: str) -> str:
    """Echo back the input text."""
    return text


@mcp.tool()
@_log_call
def get_skills() -> str:
    """Return the skills defined for this server."""
    return _load_skills()


@mcp.tool()
@_log_call
def get_server_info() -> str:
    """Return metadata about this server."""
    return json.dumps({
        "name": SERVER_NAME,
        "port": PORT,
        "host": HOST,
        "protocol": "MCP (Model Context Protocol)",
        "transport": "SSE"
    }, indent=2)


@mcp.tool()
@_log_call
def read_file(path: str) -> str:
    """Read a file from the filesystem."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def write_file(path: str, content: str) -> str:
    """Write content to a file (creates parent dirs)."""
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return f"Wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def list_files(path: str = ".") -> str:
    """List directory contents."""
    try:
        p = Path(path)
        if not p.exists():
            return f"Path not found: {path}"
        items = []
        for e in sorted(p.iterdir()):
            kind = "<DIR>" if e.is_dir() else "<FILE>"
            items.append(f"{kind} {e.name}")
        return "\n".join(items) if items else "(empty)"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def execute_command(command: str) -> str:
    """Execute a shell command (30 s timeout)."""
    try:
        r = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        out = r.stdout or ""
        err = r.stderr or ""
        if r.returncode != 0:
            return f"exit {r.returncode}\n{err}\n{out}"
        return out or "(done)"
    except subprocess.TimeoutExpired:
        return "Error: command timed out"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def analyze_code(code: str, language: str = "python") -> str:
    """Basic code statistics."""
    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]
    return json.dumps({
        "language": language,
        "total_lines": len(lines),
        "non_empty_lines": len(non_empty),
        "characters": len(code),
        "words": len(code.split()),
    }, indent=2)


@mcp.tool()
@_log_call
def validate_json(text: str) -> str:
    """Check whether a string is valid JSON."""
    try:
        obj = json.loads(text)
        return f"Valid JSON — {type(obj).__name__}"
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"


@mcp.tool()
@_log_call
def encode_base64(text: str) -> str:
    """Encode text to base64."""
    return _b64.b64encode(text.encode()).decode()


@mcp.tool()
@_log_call
def decode_base64(encoded: str) -> str:
    """Decode base64 to text."""
    try:
        return _b64.b64decode(encoded).decode()
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def get_time() -> str:
    """Return current UTC timestamp."""
    return datetime.datetime.now(datetime.UTC).isoformat()


@mcp.tool()
@_log_call
def generate_uuid() -> str:
    """Generate a random UUID."""
    return str(_uuid.uuid4())


@mcp.tool()
@_log_call
def count_words(text: str) -> int:
    """Return word count."""
    return len(text.split())


@mcp.tool()
@_log_call
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression (digits + - * / ( ) . only)."""
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        return "Error: invalid characters"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def hash_text(text: str, algorithm: str = "sha256") -> str:
    """Hash text (md5, sha1, sha256, sha512)."""
    alg = algorithm.lower()
    h = hashlib.new(alg, text.encode())
    return h.hexdigest()


@mcp.tool()
@_log_call
def generate_password(length: int = 16) -> str:
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.SystemRandom().choice(chars) for _ in range(length))


@mcp.tool()
@_log_call
def search_files(pattern: str, path: str = ".") -> str:
    """Recursively search for a pattern in text files."""
    try:
        root = Path(path)
        matches = []
        for f in root.rglob("*"):
            if f.is_file():
                try:
                    if pattern in f.read_text(encoding="utf-8", errors="ignore"):
                        matches.append(str(f))
                except Exception:
                    pass
        return "\n".join(matches) if matches else "No matches"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
@_log_call
def random_number(min_val: int = 0, max_val: int = 100) -> int:
    """Return a random integer in [min_val, max_val]."""
    return random.randint(min_val, max_val)


@mcp.tool()
@_log_call
def format_json(text: str) -> str:
    """Pretty-print JSON text."""
    try:
        obj = json.loads(text)
        return json.dumps(obj, indent=2)
    except Exception as e:
        return f"Error: {e}"


# ── Memory (persistent key-value storage) ────────────────────────────

@mcp.tool()
@_log_call
def memory_set(key: str, value: str) -> str:
    """Store a value in persistent memory."""
    data = _read_memory()
    data[key] = value
    _write_memory(data)
    return f"Stored key '{key}' ({len(value)} chars)"


@mcp.tool()
@_log_call
def memory_get(key: str) -> str:
    """Retrieve a value from persistent memory."""
    data = _read_memory()
    if key not in data:
        return f"Key '{key}' not found"
    val = data[key]
    return val if isinstance(val, str) else json.dumps(val)


@mcp.tool()
@_log_call
def memory_delete(key: str) -> str:
    """Delete a key from persistent memory."""
    data = _read_memory()
    if key not in data:
        return f"Key '{key}' not found"
    del data[key]
    _write_memory(data)
    return f"Deleted key '{key}'"


@mcp.tool()
@_log_call
def memory_list() -> str:
    """List all keys in persistent memory."""
    data = _read_memory()
    if not data:
        return "(memory is empty)"
    keys = "\n".join(f"- {k}" for k in data)
    return f"Memory keys ({len(data)}):\n{keys}"


@mcp.tool()
@_log_call
def memory_clear() -> str:
    """Clear all data from persistent memory."""
    _write_memory({})
    return "Memory cleared"


@mcp.tool()
@_log_call
def memory_stats() -> str:
    """Show memory usage statistics."""
    data = _read_memory()
    total_chars = sum(len(v) if isinstance(v, str) else len(json.dumps(v)) for v in data.values())
    return json.dumps({
        "total_keys": len(data),
        "total_chars": total_chars,
        "file_size_bytes": MEMORY_FILE.stat().st_size if MEMORY_FILE.exists() else 0,
    }, indent=2)


if __name__ == "__main__":
    mcp.run(transport="sse")
