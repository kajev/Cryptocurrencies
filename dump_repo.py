import os
from pathlib import Path

def dump_repo_structure(root_dir='.', output_file='repo_dump.txt', exclude_dirs=None):
    """
    Dumps entire repo structure and file contents to a single text file.
    """
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', '.idea'}
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write directory structure first
        f.write("=" * 80 + "\n")
        f.write("DIRECTORY STRUCTURE\n")
        f.write("=" * 80 + "\n\n")
        
        for root, dirs, files in os.walk(root_dir):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("FILE CONTENTS\n")
        f.write("=" * 80 + "\n\n")
        
        # Write file contents
        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, root_dir)
                
                # Skip binary files and large files
                if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.pkl', '.pyc')):
                    f.write(f"\n{'=' * 80}\n")
                    f.write(f"FILE: {relative_path}\n")
                    f.write(f"{'=' * 80}\n")
                    f.write("[Binary file - skipped]\n")
                    continue
                
                try:
                    # Check file size (skip if > 100KB)
                    if os.path.getsize(filepath) > 100000:
                        f.write(f"\n{'=' * 80}\n")
                        f.write(f"FILE: {relative_path}\n")
                        f.write(f"{'=' * 80}\n")
                        f.write("[File too large - skipped]\n")
                        continue
                    
                    with open(filepath, 'r', encoding='utf-8') as file_content:
                        f.write(f"\n{'=' * 80}\n")
                        f.write(f"FILE: {relative_path}\n")
                        f.write(f"{'=' * 80}\n")
                        f.write(file_content.read())
                        f.write("\n")
                except Exception as e:
                    f.write(f"\n{'=' * 80}\n")
                    f.write(f"FILE: {relative_path}\n")
                    f.write(f"{'=' * 80}\n")
                    f.write(f"[Error reading file: {e}]\n")
    
    print(f"Repository dumped to {output_file}")

if __name__ == "__main__":
    dump_repo_structure()