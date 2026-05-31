# Q7: Directory Scanning with Exception Handling
import os

# User-defined exception
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass


def scan_directory_interactive():
    """
    Interactive directory scanning with exception handling
    """
    print("\n" + "="*50)
    print("    DIRECTORY SCANNING WITH EXCEPTION HANDLING")
    print("="*50)
    
    print("\nEnter the directory path to scan.")
    print("Example: .", )
    directory_path = input("Directory path: ").strip()
    
    if not directory_path:
        directory_path = "."
    
    scan_directory(directory_path)


def scan_directory(path):
    """
    Scans directory structure with error handling
    
    Parameters:
    - path: Directory path to scan
    """
    try:
        # Check if the path exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")
        
        if not os.path.isdir(path):
            raise NotADirectoryError(f"Path is not a directory: {path}")
        
        print(f"\n" + "-"*50)
        print(f"Scanning directory: {os.path.abspath(path)}")
        print("-"*50)
        
        has_content = False
        
        # Walk through the directory structure
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 2 * level
            
            folder_name = os.path.basename(root) or root
            print(f"{indent}📁 {folder_name}/")
            
            # Check for empty folders
            if not files and not dirs and level > 0:
                try:
                    raise MissingFileOrFolderError(f"Empty folder detected: {root}")
                except MissingFileOrFolderError as e:
                    print(f"{indent}   ⚠️  {str(e)}")
            
            # Display files
            sub_indent = " " * 2 * (level + 1)
            for f in files:
                print(f"{sub_indent}📄 {f}")
                has_content = True
        
        if not has_content and os.path.isdir(path):
            print("   (Empty directory)")
        
        print("-"*50)
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except NotADirectoryError as e:
        print(f"❌ Error: {e}")
    except PermissionError as e:
        print(f"❌ Permission denied: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


def scan_project_directory(base_path):
    """
    Scans the Projects directory for student files
    """
    print("\n" + "="*50)
    print("    PROJECT DIRECTORY SCAN")
    print("="*50)
    
    projects_path = os.path.join(base_path, "Projects")
    
    if os.path.exists(projects_path):
        scan_directory(projects_path)
    else:
        print(f"\nProjects directory not found at: {projects_path}")
