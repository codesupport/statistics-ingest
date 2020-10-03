# Statistics Ingest

## About
This repository contains the code for the CodeSupport statistics ingest bot. The project is written in Python using the Discord.py module for interaction with the Discord API.

It is ran every night by a GitHub action.

## Dependencies

### Production
- [Discord.py](https://pypi.org/project/discord.py/)
- [Gspread](https://pypi.org/project/gspread/)
- [TOML](https://pypi.org/project/toml/)

## Setup
1. Navigate into the repository on your computer and run `python3 -m pip install -r requirements.txt`
2. Create a Google APIs service account and include it in the folder as `service-account.json`
    - The `generate_service_account.py` script is purely used for CI
3. Start the Discord bot with `python3 main.py`
   - You will need to supply the `DISCORD_TOKEN` environment variable
   - You will need to supply the `SHEET_ID` environment variable