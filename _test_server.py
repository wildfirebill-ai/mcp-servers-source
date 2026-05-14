#!/usr/bin/env python3
"""Test MCP servers by connecting via SSE and exercising tools."""
import asyncio
import json
import os
import signal
import subprocess
import sys
import time

from mcp.client.sse import sse_client
from mcp.client.session import ClientSession

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))


async def test_server(num, name, port):
    print(f"\n{'='*60}")
    print(f"Testing {num:03d}-{name} on port {port}")
    print(f"{'='*60}")

    server_script = os.path.join(SERVER_DIR, f"{num:03d}-{name}", "server.py")
    proc = subprocess.Popen(
        [sys.executable, server_script],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)

    try:
        # Connect via SSE
        print("\n[1] Connecting via SSE...")
        async with sse_client(f"http://localhost:{port}/sse") as streams:
                async with ClientSession(streams[0], streams[1]) as session:
                    await session.initialize()
                    print("  Connection established  OK")

                    # 2. List tools
                    print("\n[2] Listing tools...")
                    tools = await session.list_tools()
                    print(f"  Found {len(tools.tools)} tools:")
                    for t in tools.tools[:6]:
                        print(f"    - {t.name}")
                    if len(tools.tools) > 6:
                        print(f"    ... and {len(tools.tools)-6} more")
                    assert len(tools.tools) >= 20, f"Expected >=20 tools, got {len(tools.tools)}"

                    # 3. Ping
                    print("\n[3] Calling ping...")
                    result = await session.call_tool("ping", {})
                    text = result.content[0].text
                    assert text == "pong", f"Expected 'pong', got '{text}'"
                    print(f"  ping -> '{text}'  PASS")

                    # 4. Echo
                    print("\n[4] Calling echo...")
                    test_text = "Hello MCP World!"
                    result = await session.call_tool("echo", {"text": test_text})
                    text = result.content[0].text
                    assert text == test_text, f"Expected '{test_text}', got '{text}'"
                    print(f"  echo -> '{text}'  PASS")

                    # 5. get_server_info
                    print("\n[5] Calling get_server_info...")
                    result = await session.call_tool("get_server_info", {})
                    info = json.loads(result.content[0].text)
                    assert info["name"] == name, f"Name mismatch: {info['name']} != {name}"
                    assert info["port"] == port, f"Port mismatch: {info['port']} != {port}"
                    print(f"  Server: {info['name']}:{info['port']}  PASS")

                    # 6. get_skills
                    print("\n[6] Calling get_skills...")
                    result = await session.call_tool("get_skills", {})
                    skills_text = result.content[0].text
                    assert len(skills_text) > 20, f"Skills too short"
                    print(f"  Skills loaded ({len(skills_text)} chars)  PASS")

                    # 7. generate_uuid
                    print("\n[7] Calling generate_uuid...")
                    result = await session.call_tool("generate_uuid", {})
                    uuid_str = result.content[0].text
                    assert len(uuid_str) == 36, f"Expected 36-char UUID, got {len(uuid_str)}"
                    print(f"  UUID: {uuid_str}  PASS")

                    # 8. calculate
                    print("\n[8] Calling calculate...")
                    result = await session.call_tool("calculate", {"expression": "2 + 3 * 4"})
                    assert result.content[0].text == "14", f"Expected 14, got {result.content[0].text}"
                    print(f"  2 + 3 * 4 = {result.content[0].text}  PASS")

                    # 9. encode_base64 / decode_base64
                    print("\n[9] Testing base64...")
                    result = await session.call_tool("encode_base64", {"text": "hello"})
                    encoded = result.content[0].text
                    result = await session.call_tool("decode_base64", {"encoded": encoded})
                    assert result.content[0].text == "hello"
                    print(f"  base64 round-trip  PASS")

                    # 10. hash_text
                    print("\n[10] Calling hash_text...")
                    result = await session.call_tool("hash_text", {"text": "test", "algorithm": "sha256"})
                    h = result.content[0].text
                    assert len(h) == 64, f"Expected 64-char SHA256, got {len(h)}"
                    print(f"  sha256('test') = {h[:16]}...  PASS")

                    # 11. validate_json
                    print("\n[11] Calling validate_json...")
                    result = await session.call_tool("validate_json", {"text": '{"a":1}'})
                    assert "Valid" in result.content[0].text
                    result = await session.call_tool("validate_json", {"text": "invalid"})
                    assert "Invalid" in result.content[0].text
                    print("  JSON validation  PASS")

                    # 12. format_json
                    print("\n[12] Calling format_json...")
                    result = await session.call_tool("format_json", {"text": '{"b":2,"a":1}'})
                    formatted = result.content[0].text
                    assert formatted.startswith("{")
                    print(f"  format_json  PASS")

                    # 13. Memory tools
                    print("\n[13] Testing memory tools...")
                    result = await session.call_tool("memory_set", {"key": "foo", "value": "bar"})
                    print(f"  memory_set -> {result.content[0].text}")

                    result = await session.call_tool("memory_get", {"key": "foo"})
                    assert result.content[0].text == "bar"
                    print(f"  memory_get -> '{result.content[0].text}'  PASS")

                    result = await session.call_tool("memory_list", {})
                    assert "foo" in result.content[0].text
                    print(f"  memory_list -> {result.content[0].text}")

                    result = await session.call_tool("memory_delete", {"key": "foo"})
                    print(f"  memory_delete -> {result.content[0].text}")

                    result = await session.call_tool("memory_stats", {})
                    stats = json.loads(result.content[0].text)
                    print(f"  memory_stats -> {stats}  PASS")

                    # 14. generate_password
                    print("\n[14] Calling generate_password...")
                    result = await session.call_tool("generate_password", {"length": 20})
                    pw = result.content[0].text
                    assert len(pw) == 20, f"Expected 20-char password, got {len(pw)}"
                    print(f"  password ({len(pw)} chars)  PASS")

                    # 15. random_number
                    print("\n[15] Calling random_number...")
                    result = await session.call_tool("random_number", {"min_val": 1, "max_val": 10})
                    rn = int(result.content[0].text)
                    assert 1 <= rn <= 10
                    print(f"  random_number = {rn}  PASS")

                    # 16. count_words
                    print("\n[16] Calling count_words...")
                    result = await session.call_tool("count_words", {"text": "one two three four"})
                    assert result.content[0].text == "4"
                    print("  count_words  PASS")

                    # 17. get_time
                    print("\n[17] Calling get_time...")
                    result = await session.call_tool("get_time", {})
                    print(f"  time -> {result.content[0].text}  PASS")

        print(f"\n  >>> {num:03d}-{name}: ALL {17} TESTS PASSED <<<")
        return True

    except Exception as e:
        print(f"\n  FAIL: {type(e).__name__}: {e}")
        return False

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def get_all_tests():
    import re
    tests = []
    for entry in os.listdir(SERVER_DIR):
        m = re.match(r"(\d{3})-([\w-]+)", entry)
        if m and os.path.isdir(os.path.join(SERVER_DIR, entry)):
            num = int(m.group(1))
            name = m.group(2)
            port = 25000 + num - 1
            tests.append((num, name, port))
    return sorted(tests)


async def main():
    tests = get_all_tests()
    print(f"Testing all {len(tests)} servers...")

    sem = asyncio.Semaphore(5)

    async def run_one(num, name, port):
        async with sem:
            return await test_server(num, name, port)

    tasks = [run_one(n, nm, p) for n, nm, p in tests]
    results = await asyncio.gather(*tasks)

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    failed_servers = [(n, nm, p) for (n, nm, p), ok in zip(tests, results) if not ok]

    print(f"\n{'='*60}")
    print(f"RESULTS: {passed} passed, {failed} failed")
    if failed_servers:
        print("Failed servers:")
        for n, nm, p in failed_servers:
            print(f"  {n:03d}-{nm} (port {p})")
    print(f"{'='*60}")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
