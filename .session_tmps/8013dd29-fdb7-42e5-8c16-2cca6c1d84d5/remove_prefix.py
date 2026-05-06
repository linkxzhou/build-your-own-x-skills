import json
import os
import re
from pathlib import Path

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
SKILLS = ROOT / 'skills'
PLAN = ROOT / 'plan'
MANIFEST = SKILLS / 'build-your-own-x-skills-manifest.json'
PREFIX = 'build-your-own-'

manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
created = manifest.get('created', [])
old_names = [x['name'] for x in created]

existing_dirs = {p.name for p in SKILLS.iterdir() if p.is_dir()}
managed = set(old_names)
unmanaged = existing_dirs - managed

mapping = {}
used = set(unmanaged)
for old in old_names:
    if old.startswith(PREFIX):
        base = old[len(PREFIX):]
    else:
        base = old
    new = base
    i = 2
    while new in used:
        new = f'{base}-{i}'
        i += 1
    mapping[old] = new
    used.add(new)

# Replace content first while old directories still exist.
text_files = []
for old in old_names:
    d = SKILLS / old
    if d.exists():
        for p in d.rglob('*'):
            if p.is_file() and p.suffix in {'.md', '.json', '.txt'}:
                text_files.append(p)

for p in text_files:
    s = p.read_text(encoding='utf-8')
    original = s
    # Longer names first avoids partial replacement surprises.
    for old, new in sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True):
        s = s.replace(old, new)
    if s != original:
        p.write_text(s, encoding='utf-8')

# Update manifest names and add rename mapping.
for item in created:
    item['old_name'] = item['name']
    item['name'] = mapping[item['name']]
manifest['renamed_prefix_removed'] = True
manifest['rename_mapping'] = mapping
MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Update plan suggested skill names.
plan_files = [p for p in PLAN.glob('*.md') if p.name != 'README.md']
for p in plan_files:
    s = p.read_text(encoding='utf-8')
    original = s
    # Exact suggested names generated before were sometimes duplicates and may not match final mapping,
    # so remove the prefix from all suggested skill name code spans.
    s = s.replace('`build-your-own-', '`')
    # Also remove English trigger phrase prefix where it appears inside generated descriptions.
    s = s.replace('“build your own ', '“')
    if s != original:
        p.write_text(s, encoding='utf-8')

# Rename directories via two-phase rename to avoid collisions on case-insensitive filesystems.
tmp_pairs = []
for old, new in mapping.items():
    old_path = SKILLS / old
    if not old_path.exists():
        continue
    tmp_path = SKILLS / f'.rename-tmp-{old}'
    old_path.rename(tmp_path)
    tmp_pairs.append((tmp_path, SKILLS / new))

for tmp_path, new_path in tmp_pairs:
    tmp_path.rename(new_path)

# Rename manifest file itself.
new_manifest = SKILLS / 'x-skills-manifest.json'
if new_manifest.exists():
    new_manifest.unlink()
MANIFEST.rename(new_manifest)

print(json.dumps({
    'renamed': len(tmp_pairs),
    'unmanaged_kept': sorted(unmanaged),
    'manifest': str(new_manifest),
    'sample': list(mapping.items())[:5],
}, ensure_ascii=False, indent=2))
