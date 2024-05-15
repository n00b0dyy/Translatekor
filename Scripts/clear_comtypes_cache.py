import os
import shutil

def remove_directory(directory, silent):
    """
    Remove the specified directory.

    Args:
        directory (str): The path to the directory to be removed.
        silent (bool): If True, removes the directory without asking for confirmation.

    Returns:
        bool: True if the directory was successfully removed, False otherwise.
    """
    if directory:
        if not os.path.exists(directory):
            print('Error: Directory "%s" does not exist' % directory)
            return False
        
        if silent:
            try:
                _remove(directory)
                return True
            except Exception as e:
                print('Error while removing directory:', e)
                return False
        else:
            try:
                confirm = input('Remove comtypes cache directories? (y/n): ')
            except NameError:
                confirm = raw_input('Remove comtypes cache directories? (y/n): ')
                
            if confirm.lower() == 'y':
                try:
                    _remove(directory)
                    return True
                except PermissionError:
                    print('Error: Cannot remove directory "%s": Permission denied' % directory)
                    return False
                except OSError as e:
                    print('Error: Cannot remove directory "%s": %s' % (directory, e))
                    return False
            else:
                print('Directory "%s" NOT removed' % directory)
                return False
    else:
        print('Error: Invalid directory path')
        return False

def _remove(directory):
    """
    Remove the specified directory.

    Args:
        directory (str): The path to the directory to be removed.
    """
    try:
        shutil.rmtree(directory)
        print('Removed directory "%s"' % directory)
    except (PermissionError, OSError) as e:
        print('Error: Cannot remove directory "%s": %s' % (directory, e))

