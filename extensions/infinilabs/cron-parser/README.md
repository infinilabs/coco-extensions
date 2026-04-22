# Cron Parser

Parse cron expressions and see the next scheduled run times.

## Features

- **Human-readable**: Explains what the cron expression means
- **Field breakdown**: Shows each field with its label
- **Next runs**: Calculates the next 5 scheduled executions
- **Presets**: Quick-access common schedules
- **Real-time**: Updates as you type

## Cron Format

Standard 5-field format:
```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, Sun=0)
│ │ │ │ │
* * * * *
```

## Special Characters

- `*` - Any value
- `,` - Value list separator (1,3,5)
- `-` - Range (1-5)
- `/` - Step values (*/15 = every 15)

## Examples

| Expression | Description |
|------------|-------------|
| `* * * * *` | Every minute |
| `0 * * * *` | Every hour |
| `0 0 * * *` | Daily at midnight |
| `0 9 * * 1-5` | Weekdays at 9am |
| `*/15 * * * *` | Every 15 minutes |

## Privacy

All parsing happens locally. No data is sent anywhere.

## License

MIT License
