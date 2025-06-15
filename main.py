# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import asyncio
from shared_client import start_client
import importlib
import os
import sys
from pyrogram.types import User, Chat

async def load_and_run_plugins():
    # Start the shared client
    client, app, userbot = await start_client()
    
    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            await getattr(module, f"run_{plugin}_plugin")()

async def main():
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
    print("Starting clients ...")
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        loop.close()
