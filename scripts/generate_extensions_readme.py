import json
import os
import subprocess
from glob import glob

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(ROOT, ".."))
README_PATH = os.path.join(ROOT, "README.md")
BY_CATEGORY_PATH = os.path.join(ROOT, "EXTENSIONS_BY_CATEGORY.md")
EXT_DIR = os.path.join(ROOT, "extensions")

CATEGORY_MAP = {
    "utility": "Utilities",
    "utilities": "Utilities",
    "game": "Games",
    "games": "Games",
    "media": "Media",
    "productivity": "Productivity",
    "customization": "Customization",
    "development": "Development",
    "developer tools": "Development",
    "system": "System",
}

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_git_updated_time(path):
    try:
        # Get the last commit timestamp for the directory
        cmd = ["git", "log", "-1", "--format=%at", "--", path]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        if result.returncode == 0 and result.stdout.strip():
            return int(result.stdout.strip())
    except Exception:
        pass
    # Fallback to file modification time
    return int(os.path.getmtime(path))

def normalize_category(cat):
    if not cat:
        return "Other"
    cat_lower = cat.lower().strip()
    if cat_lower in CATEGORY_MAP:
        return CATEGORY_MAP[cat_lower]
    return cat.title()

def find_icon_path(dev, ext, icon_name):
    p1 = os.path.join(EXT_DIR, dev, ext, "assets", icon_name)
    p2 = os.path.join(EXT_DIR, dev, ext, icon_name)
    if os.path.exists(p1):
        return os.path.relpath(p1, ROOT)
    if os.path.exists(p2):
        return os.path.relpath(p2, ROOT)
    return None

def collect_extensions():
    items = []
    for dev_dir in sorted([d for d in os.listdir(EXT_DIR) if os.path.isdir(os.path.join(EXT_DIR, d))]):
        dev_meta_path = os.path.join(EXT_DIR, dev_dir, "developer.json")
        dev_name = dev_dir
        if os.path.exists(dev_meta_path):
            try:
                dev_meta = read_json(dev_meta_path)
                dev_name = dev_meta.get("name") or dev_dir
            except Exception:
                dev_name = dev_dir
        plugin_files = glob(os.path.join(EXT_DIR, dev_dir, "*", "plugin.json"))
        for pf in sorted(plugin_files):
            ext_dir = os.path.dirname(pf)
            ext_id = os.path.basename(ext_dir)
            try:
                plugin = read_json(pf)
            except Exception:
                continue
            name = plugin.get("name") or ext_id
            desc = plugin.get("description") or ""
            icon = plugin.get("icon")
            icon_path = find_icon_path(dev_dir, ext_id, icon) if isinstance(icon, str) else None
            rel_dir = os.path.relpath(ext_dir, ROOT)
            
            category = normalize_category(plugin.get("category"))
            updated_at = get_git_updated_time(ext_dir)
            
            items.append({
                "developer_dir": dev_dir,
                "developer": dev_name,
                "extension_dir": rel_dir,
                "name": name,
                "description": desc,
                "icon": icon_path,
                "category": category,
                "updated_at": updated_at
            })
    return items

def truncate_text(text, max_width=32):
    w = 0
    for i, c in enumerate(text):
        cw = 2 if ord(c) > 255 else 1
        if w + cw > max_width:
            return text[:i] + "..."
        w += cw
    return text

def render_table_grid(entries, items_per_row=5):
    html = ['<table>']
    
    # Calculate rows
    for i in range(0, len(entries), items_per_row):
        row_items = entries[i:i + items_per_row]
        html.append('<tr>')
        
        for e in row_items:
            # Prepare data
            # Use double &#10; to simulate paragraph spacing in native browser tooltips
            tooltip = f'📦 {e["name"]}&#10;👤 {e["developer"]}&#10;&#10;📝 {e["description"]}'.replace('"', '&quot;')
            icon_url = e["icon"] if e["icon"] else ""
            # iOS style: Rounded corners (approx 22%), subtle shadow, and 1px subtle border for white icon contrast
            img_tag = f'<img src="{icon_url}" alt="{e["name"]}" width="60" height="60" style="border-radius: 14px; object-fit:cover; display:block; margin: 0 auto; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);" />'
            
            truncated_name = truncate_text(e["name"])
            
            # Use align="center" for GitHub compatibility
            # Use width="120px" to simulate card width
            # Use valign="top" to ensure icons aligned at top
            # Add padding-bottom for row spacing
            cell = (
                f'<td align="center" valign="top" width="120px" style="padding: 30px 0;">'
                f'<a href="{e["extension_dir"]}" title="{tooltip}">'
                f'{img_tag}'
                f'</a>'
                f'<br/>'
                f'<a href="{e["extension_dir"]}" title="{tooltip}" style="color:inherit;">'
                f'<div style="font-size:12px;line-height:1.4;height:34px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;padding:0 8px;">{truncated_name}</div>'
                f'</a>'
                f'</td>'
            )
            html.append(cell)
            
        # Fill empty cells if last row is incomplete
        remaining = items_per_row - len(row_items)
        if remaining > 0:
            for _ in range(remaining):
                html.append('<td align="center" width="120px" style="padding-bottom: 30px;"></td>')
                
        html.append('</tr>')
        
    html.append('</table>')
    return "\n".join(html)

def get_nav_html(current_view):
    # current_view: 'author', 'category'
    
    links = []
    
    if current_view == 'author':
        links.append('**By Author**')
    else:
        links.append(f'<a href="README.md">By Author</a>')
        
    if current_view == 'category':
        links.append('**By Category**')
    else:
        links.append(f'<a href="EXTENSIONS_BY_CATEGORY.md">By Category</a>')
        
    return f'<p align="center" style="font-size:16px;margin-bottom:24px;">{" | ".join(links)}</p>\n'

def render_view(items, view_type):
    lines = []
    lines.append("## Extensions List")
    lines.append(get_nav_html(view_type))
    
    if view_type == 'author':
        # Group by Developer
        grouped = {}
        for e in items:
            grouped.setdefault(e["developer"], []).append(e)
        
        for dev_name in sorted(grouped.keys()):
            entries = grouped[dev_name]
            lines.append(f"### {dev_name}")
            lines.append(render_table_grid(entries))
            lines.append('\n')
            
    elif view_type == 'category':
        # Group by Category
        grouped = {}
        for e in items:
            grouped.setdefault(e["category"], []).append(e)
            
        for cat in sorted(grouped.keys()):
            entries = grouped[cat]
            lines.append(f"### {cat}")
            lines.append(render_table_grid(entries))
            lines.append('\n')
        
    return "\n".join(lines).strip() + "\n"

def update_file(path, content, preserve_header=False):
    header = ""
    if preserve_header and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old_content = f.read()
        parts = old_content.split("## Extensions List")
        if len(parts) > 1:
            header = parts[0].rstrip()
    
    if not header and not preserve_header:
        # Default headers for new files
        filename = os.path.basename(path)
        if filename == "EXTENSIONS_BY_CATEGORY.md":
            header = (
                "<div align='center'>\n\n"
                "# 🧩 Coco AI Extensions - By Category\n\n"
                "**Browse extensions grouped by their functionality.**\n\n"
                "[**⬅️ Back to Main README**](README.md)\n\n"
                "</div>\n\n"
                "---"
            )
            
    new_content = header + "\n\n" + content if header else content
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    items = collect_extensions()
    
    # 1. Update README.md (By Author)
    rendered_author = render_view(items, 'author')
    update_file(README_PATH, rendered_author, preserve_header=True)
    
    # 2. Update EXTENSIONS_BY_CATEGORY.md
    rendered_category = render_view(items, 'category')
    update_file(BY_CATEGORY_PATH, rendered_category, preserve_header=False)

if __name__ == "__main__":
    main()
