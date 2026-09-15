import json
import os

# Paths
json_path = 'docs/ogden_basic_english/ogden_850.json'
output_dir = 'docs/ogden_basic_english'

# Category metadata: code -> (english_name, chinese_name, filename)
CATEGORY_META = {
    'op': ('Operations', '操作', 'operations'),
    'gt': ('General Things', '通用事物', 'general-things'),
    'pt': ('Picturable', '可图示事物', 'picturable'),
    'qg': ('Qualities General', '通用性质', 'qualities-general'),
    'qo': ('Opposites', '反义词', 'opposites'),
}


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def group_by_category(data):
    groups = {}
    for item in data:
        cat = item['category']
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(item)
    # Sort each group alphabetically by word
    for cat in groups:
        groups[cat].sort(key=lambda x: x['word'].lower())
    return groups


def format_synonyms(synonyms):
    """Format synonyms section using Rspress warning container."""
    if not synonyms:
        return ''
    lines = ['', '::: warning{title="🤔同义词"}', '']
    for syn_word, syn_info in synonyms.items():
        lines.append(f'- {syn_word}: {syn_info["definition"]} | {syn_info["contrast"]} | *{syn_info["example"]}*')
    lines.append('')
    lines.append(':::')
    return '\n'.join(lines)


def format_word_entry(item):
    """Format a single word as a Markdown section."""
    lines = [f'## {item["word"]}', '']

    # Line 1: IPA + Chinese
    lines.append(f'`{item["ipa"]}`   {item["chinese"]}')
    lines.append('')

    # Core meaning (inline with Chinese colon)
    lines.append(f'*核心意象*：{item["coreMeaning"]}')
    lines.append('')

    # English definition (inline with Chinese colon)
    lines.append(f'*英文释义*：{item["english"]}')
    lines.append('')

    # Example sentence in tip container
    lines.append('::: tip{title="🎤例句"}')
    lines.append('')
    lines.append(f'{item["example"]}（{item["exampleChinese"]}）')
    lines.append('')
    lines.append(':::')

    # Synonyms
    lines.append(format_synonyms(item.get('synonyms', {})))
    lines.append('')
    return '\n'.join(lines)


def write_category_md(groups, output_dir):
    """Write one Markdown file per category."""
    os.makedirs(output_dir, exist_ok=True)

    file_paths = {}

    for cat_code, (en_name, zh_name, filename) in CATEGORY_META.items():
        words = groups.get(cat_code, [])
        file_path = os.path.join(output_dir, f'{filename}.md')

        lines = [
            f'# {en_name} · {zh_name} · {len(words)}',
            '',
        ]

        for item in words:
            lines.append(format_word_entry(item))

        content = '\n'.join(lines)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        file_paths[cat_code] = f'{filename}.md'
        print(f'Written {file_path} ({len(words)} words)')

    return file_paths


def write_index_md(groups, file_paths, output_dir):
    """Write an index file with links to all categories."""
    lines = [
        '# Ogden\'s Basic English 850',
        '',
        'Ogden\'s Basic English 由 Charles Kay Ogden 于 1930 年提出，',
        '旨在用最少的词汇表达最广泛的意思。这 850 个核心词汇分为五大类。',
        '',
        '## 分类总览',
        '',
        '| 分类 | 英文名 | 单词数 |',
        '|------|--------|--------|',
    ]

    total = 0
    for cat_code, (en_name, zh_name, filename) in CATEGORY_META.items():
        count = len(groups.get(cat_code, []))
        total += count
        link = f'[{zh_name}（{en_name}）]({filename}.md)'
        lines.append(f'| {link} | {en_name} | {count} |')

    lines.append(f'| **合计** | | **{total}** |')
    lines.append('')

    index_path = os.path.join(output_dir, 'index.md')
    content = '\n'.join(lines)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Written {index_path}')


def main():
    print('Loading JSON...')
    data = load_json(json_path)
    print(f'Loaded {len(data)} words')

    groups = group_by_category(data)

    print('\nWriting category files...')
    file_paths = write_category_md(groups, output_dir)

    print('\nWriting index file...')
    write_index_md(groups, file_paths, output_dir)

    print('\nDone!')


if __name__ == '__main__':
    main()
