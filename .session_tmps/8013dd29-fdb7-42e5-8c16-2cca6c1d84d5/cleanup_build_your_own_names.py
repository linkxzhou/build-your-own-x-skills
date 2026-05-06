import json
from pathlib import Path

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
SKILLS = ROOT / 'skills'
PLAN = ROOT / 'plan'
MANIFEST = SKILLS / 'x-skills-manifest.json'

manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
created = manifest.get('created', [])

# Remove historical fields that still contain the old prefix.
for item in created:
    item.pop('old_name', None)
manifest.pop('rename_mapping', None)
manifest.pop('renamed_prefix_removed', None)

# Remove build-your-own fragments that are part of generated skill names, not source URLs/titles.
def clean_name(name: str) -> str:
    while 'build-your-own-' in name:
        name = name.replace('build-your-own-', '')
    while 'build-your-own' in name:
        name = name.replace('build-your-own', '')
    while '--' in name:
        name = name.replace('--', '-')
    return name.strip('-')

managed_names = [item['name'] for item in created]
unmanaged = {p.name for p in SKILLS.iterdir() if p.is_dir()} - set(managed_names)
used = set(unmanaged)
mapping = {}
for old in managed_names:
    base = clean_name(old)
    new = base
    i = 2
    while new in used:
        new = f'{base}-{i}'
        i += 1
    mapping[old] = new
    used.add(new)

# Update text in managed skill files: only generated skill names, not arbitrary source URLs.
for old, new in sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True):
    old_dir = SKILLS / old
    if not old_dir.exists() or old == new:
        continue
    for p in old_dir.rglob('*'):
        if p.is_file() and p.suffix in {'.md', '.json', '.txt'}:
            s = p.read_text(encoding='utf-8')
            s2 = s.replace(old, new)
            if s2 != s:
                p.write_text(s2, encoding='utf-8')

# Update manifest names.
for item in created:
    item['name'] = mapping[item['name']]
MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Rename directories that still changed.
tmp_pairs = []
for old, new in mapping.items():
    if old == new:
        continue
    old_path = SKILLS / old
    if old_path.exists():
        tmp = SKILLS / f'.rename2-tmp-{old}'
        old_path.rename(tmp)
        tmp_pairs.append((tmp, SKILLS / new))
for tmp, new_path in tmp_pairs:
    new_path.parent.mkdir(parents=True, exist_ok=True)
    tmp.rename(new_path)

# Update plan suggested skill names only.
for p in PLAN.glob('*.md'):
    s = p.read_text(encoding='utf-8')
    s2 = s
    # remove prefix inside suggested skill name code spans
    s2 = s2.replace('`build-your-own-', '`')
    # specific generated-name fragment cleanup
    s2 = s2.replace('misc-any-build-your-own-x-vibe-coding-vibe-coding-byo', 'misc-any-x-vibe-coding-vibe-coding-byo')
    if s2 != s:
        p.write_text(s2, encoding='utf-8')

print(json.dumps({'renamed_again': len(tmp_pairs), 'changed_names': {k:v for k,v in mapping.items() if k!=v}}, ensure_ascii=False, indent=2))
