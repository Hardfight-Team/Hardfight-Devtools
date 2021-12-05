# External imports
from typing import Optional
import platform
import fnmatch
import ctypes
import struct


# Platform names table
PLATFORMS_TABLE = (
    ('windows', ('windows', 'cygwin-*')),
    ('macos', ('darwin',)),
    ('ios', ('ios',)),
    ('linux', ('linux*',)),
    ('freebsd', ('freebsd*', 'openbsd*', 'isilon onefs')),
    ('poky', ('poky',)),
)

# Architecture table
ARCH_TABLE = (
    ('x86', ('i?86', )),
    ('x86_64', ('x64', 'x86_64', 'amd64', 'intel')),
    ('arm', ('armv5',)),
    ('armv6', ('armv6l',)),
    ('armv7', ('armv7l',)),
    ('ppc64', ('ppc64le',)),
    ('mips32', ('mips',)),
    ('aarch32', ('aarch32',)),
    ('aarch64', ('aarch64', 'arm64'))
)


def get_arch_name() -> str:
    """Gets current python arch name ({os}.{arch})

    :return:    Current python arch name
    :rtype:     str
    """
    plat = platform.system().lower()
    mach = platform.machine().lower()

    # Platform
    for alias, platlist in PLATFORMS_TABLE:
        if _match_features(platlist, plat):
            plat = alias
            break

    # Platform more accurate than 'linux' via libc
    if plat == 'linux':
        cname, _ = platform.libc_ver()
        if cname == 'musl':
            plat = 'musl'
        elif cname == 'libc':
            plat = 'android'
        elif cname == 'glibc':
            v = _gnu_get_libc_version()
            if v and len(v) >= 2 and (int(v[0]) * 100 + int(v[1])) < 214:
                plat = 'centos6'

    # Architecture
    for alias, archlist in ARCH_TABLE:
        if _match_features(archlist, mach):
            mach = alias
            break

    # Platform
    if plat == 'windows' and mach == 'x86_64':
        bitness = struct.calcsize('P'.encode()) * 8
        if bitness == 32:
            mach = 'x86'

    # Return 'platform.architecture'
    return (f'{plat}.{mach}')


def _match_features(patterns, str_value) -> bool:
    """Utility function to match tables with string"""
    for pat in patterns:
        if fnmatch.fnmatch(str_value, pat):
            return (True)
    return (False)


def _gnu_get_libc_version() -> Optional[str]:
    """Gets the current GNU libc library version

    :return:    GNU libc version
    :rtype:     str
    """
    try:
        prototype = ctypes.CFUNCTYPE(ctypes.c_char_p)
        ver = prototype(
            ('gnu_get_libc_version', ctypes.cdll.LoadLibrary(''))
        )()
        return (ver.decode().split('.'))
    except Exception:
        return (None)


# Script version of the function
if __name__ == '__main__':
    arch = get_arch_name()
    print(arch)
