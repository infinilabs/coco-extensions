# SQL Formatter

Format and beautify SQL queries.

## Features

- **Auto-formatting** - Indentation and line breaks
- **Uppercase keywords** - Toggle keyword case
- **Minify** - Compact SQL to single line
- **Configurable indent** - 1-8 spaces

## Supported SQL

- SELECT, INSERT, UPDATE, DELETE statements
- JOINs (LEFT, RIGHT, INNER, OUTER, CROSS)
- WHERE, GROUP BY, ORDER BY, HAVING
- Subqueries and nested parentheses
- String literals (preserved)

## Options

| Option | Description |
|--------|-------------|
| Indent | Number of spaces for indentation |
| Uppercase Keywords | Convert keywords to uppercase |
| Newline Before Keywords | Add line breaks before major keywords |

## Example

**Input:**
```sql
select id, name, email from users where active = true and role = 'admin' order by name asc
```

**Output:**
```sql
SELECT
  id,
  name,
  email
FROM users
WHERE active = TRUE
AND role = 'admin'
ORDER BY name ASC
```

## Privacy

All processing happens locally.

## License

MIT License
