import os.path
import shutil

def locate_folder( path ):
    return os.path.isdir( path )

def locate_file( path ):
    if path.startswith( '~' ):
        path = os.path.expanduser( path )
    return os.path.isfile( path )

def copy_file( src, dst ):
    if src.startswith( '~' ):
        src = os.path.expanduser( src )
    if dst.startswith( '~' ):
        dst = os.path.expanduser( dst )
    shutil.copyfile( src, dst )
