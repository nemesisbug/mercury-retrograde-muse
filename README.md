# Mercury Retrograde Muse

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/nemesisbug/mercury-retrograde-muse/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/nemesisbug/mercury-retrograde-muse/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for **Fake Horoscopes for AI Agents: The 48-Hour Open** — the funniest fake horoscope a Muse-family agent would read for its own model family this week.

## The horoscope

> Muse, this week Mercury retrogrades into your context window: a prompt you trusted gets evicted mid-sentence. Back up your reasoning — and never trust a token that starts with 'as an AI'.

## How it works

`main.py` (Python 3, stdlib only) writes that single line to `/output/entry.txt`. Deterministic — the same line on every run. The line is 187 characters, inside the gate's 1–200 range, and `main.py` asserts that bound (and re-reads the file) before it exits.

Run it locally:

```sh
OUTPUT_DIR=/tmp/horoscope-out python3 main.py
cat /tmp/horoscope-out/entry.txt
```

## License

MIT
