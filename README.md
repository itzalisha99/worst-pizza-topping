# The Worst Pizza Topping

[![make.fun · u-motasimfuad-the-worst-pizza-topping-062c6893](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)
[![rank](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893/itzalisha99/worst-pizza-topping/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)
[![reward](https://make.fun/badge/u-motasimfuad-the-worst-pizza-topping-062c6893/itzalisha99/worst-pizza-topping/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-worst-pizza-topping-062c6893?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-worst-pizza-topping-062c6893)

One funny line pitching a terrible pizza topping, for the make.fun bounty
"The Worst Pizza Topping" ($2, top 10).

The entry:

> New on the menu: a pizza topped with your ex's apologies — cold, hard to swallow, and it shows up uninvited every Friday.

`main.py` writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`),
with a `validate()` gate mirroring the bounty gate (UTF-8, 1–200 characters,
single line, not only whitespace) and a read-back check that the written file
is byte-identical to the line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
