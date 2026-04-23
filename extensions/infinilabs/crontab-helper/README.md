# Crontab Helper

Visual cron expression builder and validator.

## Features

- **Visual builder** - Select from dropdowns for each field
- **Description** - Human-readable explanation of the schedule
- **Next 5 runs** - Preview upcoming execution times
- **Quick presets** - Common schedules with one click

## Cron Format

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, Sun=0)
│ │ │ │ │
* * * * *
```

## Common Presets

| Expression | Description |
|------------|-------------|
| `* * * * *` | Every minute |
| `0 * * * *` | Every hour |
| `0 0 * * *` | Daily at midnight |
| `0 9 * * *` | Daily at 9 AM |
| `0 0 * * 0` | Weekly on Sunday |
| `0 0 1 * *` | Monthly on the 1st |
| `0 0 * * 1-5` | Weekdays at midnight |

## Privacy

All processing happens locally. No data is sent anywhere.

## License

MIT License
