#!/usr/bin/env python3
"""Quick sequential test of key servers to diagnose failures."""
import asyncio, json, os, signal, subprocess, sys, time
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession

BASE = os.path.dirname(os.path.abspath(__file__))

async def test(num, name, port):
    folder = f"{num:03d}-{name}"
    script = os.path.join(BASE, folder, "server.py")
    proc = subprocess.Popen([sys.executable, script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    await asyncio.sleep(2)
    try:
        async with sse_client(f"http://localhost:{port}/sse") as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                tools = await session.list_tools()
                assert len(tools.tools) >= 20, f"Only {len(tools.tools)} tools"
                r = await session.call_tool("ping", {})
                assert r.content[0].text == "pong"
                r = await session.call_tool("get_server_info", {})
                info = json.loads(r.content[0].text)
                assert info["name"] == name
                assert info["port"] == port
                r = await session.call_tool("echo", {"text": "hi"})
                assert r.content[0].text == "hi"
                r = await session.call_tool("memory_set", {"key": "x", "value": "y"})
                r = await session.call_tool("memory_get", {"key": "x"})
                assert r.content[0].text == "y"
                r = await session.call_tool("memory_delete", {"key": "x"})
                print(f"  {folder}: PASS ({len(tools.tools)} tools, {info['name']}:{info['port']})")
                return True
    except Exception as e:
        print(f"  {folder}: FAIL - {type(e).__name__}: {str(e)[:120]}")
        return False
    finally:
        proc.terminate()
        try: await asyncio.wait_for(proc.wait(), 5)
        except: proc.kill()

async def main():
    import re
    passed = failed = 0
    folders = sorted([d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d)) and re.match(r'\d{3}-', d)])
    #     # full run - all folders
    for folder in folders:
        m = re.match(r"(\d{3})-([\w-]+)", folder)
        if m:
            num = int(m.group(1))
            name = m.group(2)
            port = 25000 + num - 1
            ok = await test(num, name, port)
            if ok: passed += 1
            else: failed += 1
        await asyncio.sleep(1)

    print(f"\nSequential results: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    asyncio.run(main())
