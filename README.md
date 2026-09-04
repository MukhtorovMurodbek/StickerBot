# StickerBot

A Telegram bot for creating and managing sticker packs. It turns images,
GIFs, videos and existing stickers into a Telegram sticker pack, lets a pack
be co-edited by several people through a share link, and can bulk-import
from another public Telegram pack or from a WhatsApp sticker export.

Runs as its own process, its own repository and its own deployment, and can
be run entirely standalone. It shares a Postgres database with four sibling
bots only in the sense that its tables live in a schema of their own inside
it (`DB_SCHEMA`); no other bot reads or writes them. The one shared area is
`family.*`, where the bot posts a heartbeat and any crash so a monitoring bot
can watch it — `FAMILY_BUS=off` disables that entirely.

---

## Commands

| command | what it does |
|---|---|
| `/newpack` | Start a new sticker pack. |
| `/addsticker` | Add stickers to an existing pack. |
| `/mypacks` | List the user's packs; tapping one offers rename and co-editing. |
| `/import <pack link or name>` | While editing, bulk-copy stickers from another public pack. Also accepts a WhatsApp `.zip` or `.wastickers` export sent as a file. |
| `/done` | Finish editing. |
| `/whomade <pack link or name>` | Who created a pack, if it was made through this bot. |
| `/cancel` | Asks which of the things the bot is waiting on should stop, one button each, and stops nothing until one is chosen. |
| `/donate` | Voluntary contribution towards hosting, paid in Telegram Stars. |
| `/start` | Instructions. The first `/start` from a new user asks which language to use, once. |
| `/language`, `/en`, `/uz`, `/rus` | Switch language. Each reprints the instructions in the language chosen. |
| `/help` | The instructions on their own. |

Restricted to the account ids in `SBOT_ADMIN_ID`, and answering everyone else
exactly as a misspelt command does, so their existence is not disclosed:
`/whois <user_id>` (a user's name, username and bio, plus any packs of theirs
on record), `/messageas <user_id> <text>`, `/dbdump`, `/status` and
`/crashtest`.

Telegram does not allow a bot to message someone who has never messaged it,
so `/messageas` only reaches people who have used the bot before.

---

## How it works

**Encoding.** Video stickers have to fit inside Telegram's 256 KB ceiling as
WebM/VP9. The encoder measures rather than laddering blindly: it estimates a
bitrate from the clip's length and dimensions, encodes once, and only retries
if the result missed. Static stickers are resized to Telegram's 512-pixel
box with transparency preserved.

**Co-editing.** A pack has one creator and any number of editors, added by
share link. Editors can add and remove stickers; only the creator can rename
or hand the pack on.

**Importing.** A Telegram pack is copied by file id, so nothing is
re-encoded. A WhatsApp export is a zip of WebP images, which are converted.

**Limits.** A ceiling on updates per minute applies per account, before any
handler runs, so a script cannot hold the process busy. It is configurable;
see `.env.example`.

---

## Running it

```bash
pip install -r requirements.txt
cp .env.example .env          # fill in SBOT_TOKEN and SBOT_USERNAME
python bot.py
```

`SBOT_TOKEN` and `SBOT_USERNAME` come from
[@BotFather](https://t.me/BotFather). `SBOT_ADMIN_ID` is optional and takes
one or more numeric account ids.

The bot needs a Postgres database (`DATABASE_URL`, with `DB_SCHEMA`
defaulting to `sticker_bot`) and `ffmpeg` on `PATH` for video stickers. The
schema and its tables are created on first run.

### Deploying

Set the same values as environment variables on the host and run
`python bot.py`. `railway.json` and `nixpacks.toml` configure a Railway
deployment; neither is required elsewhere.

A deployment replaces the running container, and the bot is built so that
costs nothing visible. The new process waits on a Postgres advisory lock
until the old one has stopped polling, so Telegram never sees two consumers
of one token. A pack half-built survives, restored from a `runtime_state`
table. Anything mid-encode is announced rather than left silent. Updates sent
during the gap are held by Telegram and delivered on the first poll — nothing
is lost. `DEPLOY_SAFETY=off` disables all of it.

### Keeping two databases in sync

`db_merge.py` reconciles a local database with a remote one additively — it
never deletes or overwrites.

```bash
python db_merge.py --from local --into cloud --dry-run
python db_merge.py --from local --into cloud
```

---

## Files

| file | |
|---|---|
| `bot.py` | Handlers and the pack-editing conversation |
| `image_utils.py`, `video_sticker.py` | Resizing, and WebM/VP9 encoding to fit Telegram's limit |
| `emoji_utils.py`, `import_utils.py` | Emoji handling; Telegram and WhatsApp imports |
| `db.py` | This bot's schema, queries and connection pool |
| `i18n.py` | English, Uzbek and Russian strings |
| `family_link.py` | Heartbeats, crash reporting, and the command queue a monitoring bot uses |
| `lifecycle.py` | Surviving a redeploy: one poller at a time, state in Postgres |
| `live_message.py` | When a bot message may keep evolving in place |
| `shared_features.py` | Donations, logging, activity tracking, flood control |
| `db_merge.py` | Reconciles two databases, additively |

`family_link.py`, `lifecycle.py`, `live_message.py` and `shared_features.py`
are shared with the sibling bots by being copied rather than imported: each
bot is a separate deployment, so nothing crosses a repository boundary.

## Requirements

Python 3.11 or newer, Postgres 16 or newer, and `ffmpeg`.
