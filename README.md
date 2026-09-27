# Discord Export Cleaner

Two small Python utilities that transform JSON exports from [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) into analysis-friendly text files.

> **Status:** Historical utility. The scripts work from a locally configured export directory and should be updated to accept command-line paths before general reuse.

## What it produces

### `messageParser.py`

Reads every JSON export in a directory and writes one delimited row per message containing:

- Timestamp
- Channel name
- Message ID
- Author name
- Message content

### `emojiParser.py`

Extracts reaction activity into a CSV-style file containing:

- Message timestamp and content
- Author
- Emoji name and image URL
- Reaction count

## Usage notes

The input and output paths are currently hard-coded near the top of each script. To use the utilities with another export, change `directory` and the output path before running:

```powershell
python messageParser.py
python emojiParser.py
```

The scripts use only Python's standard library.
