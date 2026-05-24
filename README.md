# 3 Bots – Danish Systems Suite

Samlet repo til tre Telegram/bot-projekter:

- `danish-systems-bot-FINAL.zip` – Danish Systems moderator bot
- `Maigret-Search.zip` – Maigret/search tooling
- `simple_encryption_telegram_bot(1).zip` – simple encryption Telegram bot
- `assets/bot-profile.png` – profilbillede/branding

## Struktur

```text
.
├── packages/
│   ├── danish-systems-bot-FINAL.zip
│   ├── Maigret-Search.zip
│   └── simple_encryption_telegram_bot(1).zip
├── assets/
│   └── bot-profile.png
├── render.yaml
└── README.md
```

## Deploy på Render

Upload secrets i Render/GitHub som environment variables. Læg aldrig API keys direkte i repoet.

Typiske env vars:

```env
TELEGRAM_BOT_TOKEN=
DATABASE_URL=
RENDER_API_KEY=
```

## Lokal udpakning

```bash
mkdir -p services
unzip packages/danish-systems-bot-FINAL.zip -d services/danish-systems-bot
unzip packages/Maigret-Search.zip -d services/maigret-search
unzip "packages/simple_encryption_telegram_bot(1).zip" -d services/simple-encryption-telegram-bot
```
