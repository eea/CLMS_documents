import yaml
import re
import glob
from pathlib import Path
from keybert import KeyBERT
from io import StringIO
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq
from ruamel.yaml.scalarstring import DoubleQuotedScalarString


QUARTO_CONFIG="_quarto.yaml"

kw_model = KeyBERT('paraphrase-mpnet-base-v2')

def get_render_files(quarto_yml_path=QUARTO_CONFIG):
    with open(quarto_yml_path, 'r') as f:
        config = yaml.safe_load(f)

    render_list = config.get('project', {}).get('render', [])
    matched_files = []

    for pattern in render_list:
        matched = glob.glob(pattern, recursive=True)
        matched_files.extend([Path(f) for f in matched if f.endswith('.qmd')])

    # Exclude files named 'index.qmd'
    return [f for f in matched_files if f.name.lower() != 'index.qmd']

def inject_keywords(file_path: Path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return

    _, yaml_block, body = parts
    
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml_data = yaml.load(StringIO(yaml_block))

    keywords = kw_model.extract_keywords(body, 
                                         keyphrase_ngram_range=(1, 2), 
                                         stop_words='english', 
                                         use_mmr=True, 
                                         diversity=0.2,
                                         top_n=10)

    # Update keywords field
    keywords_list = CommentedSeq([DoubleQuotedScalarString(kw) for kw, _ in keywords])
    keywords_list.fa.set_flow_style() 
    yaml_data['keywords'] = keywords_list

    # Reconstruct YAML as string
    yaml_out = StringIO()
    yaml.dump(yaml_data, yaml_out)
    final_yaml = yaml_out.getvalue().strip()

    # Combine back
    updated_content = f"---\n{final_yaml}\n---\n{body}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
        

if __name__ == "__main__":
    files = get_render_files()
    for file in files:
        inject_keywords(file)
