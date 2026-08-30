# StickerBot

Telegram bot for creating and managing sticker packs: turn images, GIFs,
videos, and existing stickers into a Telegram sticker pack, co-edit packs
with other people via a share link, and bulk-import from another Telegram
pack or a WhatsApp sticker pack export.

This bot is its own process, its own repo and its own deployment — it can
be run entirely on its own. It shares one Postgres database with the rest
of the family, but only in the sense that its tables live in their own
schema inside it (`DB_SCHEMA` in `.env`); no other bot reads or writes
them. The exception is `family.*`, where this bot posts a heartbeat and
any crash so that ParentBot can watch it — see `family_link.py`, and
ARCHITECTURE.md in the family monorepo for why it is arranged this way. Set `FAMILY_BUS=off`
to opt out of that entirely.

## Commands

- `/newpack` — start a new sticker pack
- `/addsticker` — add stickers to an existing pack
- `/mypacks` — list your packs (tap one to rename or set up co-editing)
- `/import <pack link/name>` — (while editing) bulk-copy stickers from
  another public Telegram pack, or send a WhatsApp `.zip`/`.wastickers` file
- `/done` — finish editing a pack
- `/cancel` — asks which of the things it is waiting on you for to stop,
  as one button each, and stops nothing until you pick. With nothing pending
  it says so straight away, as it always did. A pack you are three
  stickers into is no longer collateral damage of wanting out of a donation
  prompt
- `/whomade <pack link/name>` — see who created a pack (if made through this bot)
- `/donate` — chip in for hosting costs (voluntary, Telegram Stars)
- `/start` — the full instructions. The first `/start` from a brand-new
  user asks for a language before printing them, which is the one and only
  time it asks; after that it prints them in the language on record
- `/language` — the picker on demand: a short greeting in all three
  languages and one row of buttons, with a tick on the language in force.
  Choosing one (even the one already set) reprints the instructions in it
- `/en`, `/uz`, `/rus` — switch language directly, skipping the picker;
  each also reprints the instructions in the language just chosen
- `/help` — the instructions on their own
- `/convert` — a friendly redirect to @ConvertBot, which is where file
  conversion lives now; kept for anyone still typing it out of habit

Owner-only (requires `SBOT_ADMIN_ID` in `.env` — silently do nothing for
everyone else):
- `/whois <user_id>` — look up a Telegram user's name/username/bio plus any
  packs of theirs on record, e.g. to turn a `/whomade` id back into "which
  friend is this"
- `/messageas <user_id> <text>` — send a message to that user as this bot
  (only works if they've messaged the bot before — Telegram doesn't allow
  bots to cold-message anyone)
- `/dbdump` — export this bot's tables as a zip of CSVs
- `/status` — uptime, host, crashes since this process started, active users

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Requires `ffmpeg` on `PATH` (for video-sticker conversion).
2. Copy `.env.example` to `.env` and fill in `SBOT_TOKEN`/`SBOT_USERNAME`
   (from [@BotFather](https://t.me/BotFather)). Optionally set `SBOT_ADMIN_ID`
   to your own numeric user id to unlock `/whois` and `/messageas`.
3. Start the family's shared Postgres, from the monorepo root:
   ```
   docker compose up -d
   ```
   That is one database (`botfamily`) for all five bots, with a schema
   each — this one uses `DB_SCHEMA=sticker_bot`. No Docker? Install
   Postgres directly and point `DATABASE_URL` at it instead.
4. Run it:
   ```
   python bot.py
   ```

## Deploying (e.g. Railway)

The short version is below; DEPLOY.md in the family monorepo covers all five in one
pass, which is easier than doing five of these separately.

1. Point `DATABASE_URL` at the family's Postgres, and set `DB_SCHEMA` to
   `sticker_bot`. On Railway that first one is a reference variable,
   `${{Postgres.DATABASE_URL}}`, so several services can share one database.
2. Set `SBOT_TOKEN`, `SBOT_USERNAME`, and the rest of `.env` as environment
   variables on the service.
3. Deploy — `pip install -r requirements.txt` then `python bot.py`.

## Keeping a local and cloud database in sync

If you ever run this bot from both your laptop and the cloud at different
times, `db_merge.py` reconciles the two additively (never deletes or
overwrites anything):
```
python db_merge.py --from local --into cloud --dry-run   # preview first
python db_merge.py --from local --into cloud             # actually do it
```
Read the script's docstring for exactly how conflicts are handled.

## Optional: cross-promoting sibling bots

If you're running this alongside other bots (e.g. a downloader or converter
bot) and want each to mention the others in `/start`/`/help`, set
`SIBLING_BOTS` in `.env` — see the comment in `shared_features.py`. Purely
cosmetic (display text + link buttons); no database or file is shared.

## Files

- `bot.py` — handlers and the pack-editing conversation flow
- `db.py` — this bot's own Postgres schema and queries
- `family_link.py` — heartbeats, crash reporting, and the queue ParentBot
  uses to run this bot's owner-only commands (identical in every bot)
- `shared_features.py` — `/donate` (Telegram Stars) + sibling-bot cross-promotion
- `image_utils.py` / `video_sticker.py` / `emoji_utils.py` / `import_utils.py` — sticker-format conversion and pack-import logic
- `db_merge.py` — reconciles a laptop database with the cloud one, additively (see above)
