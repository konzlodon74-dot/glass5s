# glass5s

[![make.fun](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/konzlodon74-dot/glass5s/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/konzlodon74-dot/glass5s/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

Bounty: https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949

> "You left it in my patrol route, so I cleared the route; hire a guard if you want the table defended."

## How it works

`main.py` holds the entry sentence as a string constant, asserts it is non-blank with no leading/trailing padding, single-line, and between 1 and 200 characters long, then creates `/output` if needed and writes the sentence as UTF-8 bytes with no trailing newline to `/output/entry.txt`.

## Run

```bash
python3 main.py
```
