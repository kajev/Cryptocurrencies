import os
import json

def create_compressed_summary(repo_path):
    """Create a highly compressed repository summary"""
    
    summary = {
        "structure": {},
        "key_files": {},
        "code_snippets": {},
        "stats": {}
    }
    
    # File type counters
    file_types = {}
    total_files = 0
    
    # Important files to read in full
    important_files = ['README.md', 'requirements.txt', 'package.json']
    
    # Code files to sample (first 500 chars)
    code_extensions = ['.py', '.js', '.html', '.css', '.sql', '.R']
    
    for root, dirs, files in os.walk(repo_path):
        # Skip common unnecessary folders
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.vscode']]
        
        rel_root = os.path.relpath(root, repo_path)
        if rel_root == '.':
            rel_root = 'root'
            
        summary["structure"][rel_root] = files[:10]  # Max 10 files per folder
        
        for file in files:
            total_files += 1
            ext = os.path.splitext(file)[1]
            file_types[ext] = file_types.get(ext, 0) + 1
            
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, repo_path)
            
            # Read important files completely
            if file in important_files:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        summary["key_files"][rel_path] = f.read()[:3000]  # Max 3000 chars
                except:
                    summary["key_files"][rel_path] = "Could not read"
            
            # Sample code files
            elif ext in code_extensions and len(summary["code_snippets"]) < 10:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()[:500]  # First 500 chars
                        if content.strip():  # Only if not empty
                            summary["code_snippets"][rel_path] = content
                except:
                    pass
    
    summary["stats"] = {
        "total_files": total_files,
        "file_types": file_types,
        "folders": len(summary["structure"])
    }
    
    return summary

def save_compressed(repo_path, output_file='compressed_summary.json'):
    """Save compressed summary as JSON"""
    summary = create_compressed_summary(repo_path)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Compressed summary saved to: {output_file}")
    print(f"File size: {os.path.getsize(output_file)} bytes")
    return summary

# Run this
summary = save_compressed(".")